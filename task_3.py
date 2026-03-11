import requests
import json
import os

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
SAVE_FILE = 'resource/save.json'


def get_exchange_rates():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data['Valute']
    else:
        print("Ошибка при получении данных.")
        return {}


def show_all_currencies(currencies):
    print("\nТекущие обменные курсы всех валют:")
    for code, currency in currencies.items():
        print(f"{code}: {currency['Name']} - {currency['Value']} RUB")


def view_currency(currencies, code):
    currency = currencies.get(code)
    if currency:
        print(f"{code}: {currency['Name']} - {currency['Value']} RUB")
    else:
        print("Валюта с этим кодом не найдена.")


def load_groups():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_groups(groups):
    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(groups, f, ensure_ascii=False, indent=2)


def create_group(groups):
    name = input("Введите название новой группы: ")
    if name in groups:
        print("Эта группа уже существует.")
        return
    groups[name] = []
    print(f"Группа '{name}' создана.")


def show_groups(groups):
    if not groups:
        print("Группы пока не созданы.")
        return
    for name, currencies in groups.items():
        print(f"\nГруппа: {name}")
        for code in currencies:
            print(f"  - {code}")


def add_currency_to_group(groups, currencies):
    name = input("Введите название группы: ")
    if name not in groups:
        print("Нет такой группы.")
        return
    code = input("Введите код валюты для добавления: ")
    if code not in currencies:
        print("Неверный код валюты.")
        return
    if code in groups[name]:
        print("Эта валюта уже входит в группу.")
        return
    groups[name].append(code)
    print(f"Валюта {code} добавлена в группу '{name}'.")


def remove_currency_from_group(groups):
    name = input("Введите название группы: ")
    if name not in groups:
        print("Нет такой группы.")
        return
    code = input("Введите код валюты для удаления: ")
    if code in groups[name]:
        groups[name].remove(code)
        print(f"Валюта {code} удалена из группы '{name}'.")
    else:
        print("Данная валюта не входит в эту группу.")


def menu():
    currencies = get_exchange_rates()
    groups = load_groups()

    while True:
        print("\nВыберите действие:")
        print("1.Посмотреть все валюты")
        print("2.Просмотреть валюту по коду")
        print("3.Создать группу валют")
        print("4.Посмотреть все группы")
        print("5.Добавить валюту в группу")
        print("6.Удалить валюту из группы")
        print("7.Выйти")
        choice = input("Введите число: ")

        match choice:
            case '1':
                show_all_currencies(currencies)
            case '2':
                code = input("Введите код валюты: ")
                view_currency(currencies, code)
            case '3':
                create_group(groups)
                save_groups(groups)
            case '4':
                show_groups(groups)
            case '5':
                add_currency_to_group(groups, currencies)
                save_groups(groups)
            case '6':
                remove_currency_from_group(groups)
                save_groups(groups)
            case '7':
                break
            case _:
                print("Попробуйте снова.")
menu()
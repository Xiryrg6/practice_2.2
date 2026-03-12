import requests
import os

login = input("Введите логин: ")
os.system('cls')
response = requests.get(f"https://api.github.com/users/{login}")


def profile(user_data):
    print("|----------------------------------------|\n" \
         f"|Логин: {user_data["login"]}\n" \
         f"|Имя: {user_data["name"]}\n" \
         f"|Репозиториев: {user_data["public_repos"]}\n" \
         f"|Обсуждений: {user_data["public_gists"]}\n" \
         f"|Подписчиков: {user_data["following"]}\n" \
         f"|Подписок: {user_data["followers"]}\n" \
         f"|Профиль: {user_data["html_url"]}\n" \
          "|----------------------------------------|")
    input("\nНажмите Enter, что бы вернуться.")
    os.system('cls')


def repos(login, flag1):
    flag2 = False
    response = requests.get(f"https://api.github.com/users/{login}/repos")
    if response.status_code == 200:
        repos_data = response.json()
        if flag1:
            flag2 = True
            search = input("Введите название репозитория: ")
        found = False
        for repos in repos_data:
            if flag2:
                if repos["name"].lower() != search.lower(): continue
            found = True
            print("\n|------------------------------------------------|\n" \
                   f"|Название: {repos['name']}\n" \
                   f"|Просмотров: {repos['watchers_count']}\n" \
                   f"|Язык: {repos['language']}\n" \
                   f"|Видимость: {repos['visibility']}\n" \
                   f"|Ветка по умолчанию: {repos['default_branch']}\n" \
                   f"|Ссылка: {repos['html_url']}\n" \
                    "|------------------------------------------------|")
            if flag2: break
        if not found:
            print("\nНичего не найдено.")
        input("\nНажмите Enter, что бы вернуться")
        os.system('cls')


def menu():
    if response.status_code == 200:
        user_data = response.json()
        while True:
            print("|----------------------------|\n" \
                  "|Выберите действие:          |\n" \
                  "|1.Просмотр профиля          |\n" \
                  "|2.Просмотр всех репозиториев|\n" \
                  "|3.Поиск репозитория         |\n" \
                  "|4.Выход                     |\n" \
                  "|----------------------------|\n")
            choice = input("Введите число: ")

            match choice:
                case '1':
                    os.system('cls')
                    profile(user_data)
                case '2':
                    os.system('cls')
                    flag = False
                    repos(login, flag)
                case '3':
                    os.system('cls')
                    flag = True
                    repos(login, flag)
                case '4':
                    os.system('cls')
                    break
                case _:
                    os.system('cls')
                    print("Попробуйте снова.")
    elif response.status_code == 404:
        print("Пользователь не найден.")
    else:
        print(f"Ошибка: {response.status_code}")
    input("\nНажмите Enter, что бы выйти.")
menu()
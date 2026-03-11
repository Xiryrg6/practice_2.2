import requests

urls = ["https://github.com/", 
       "https://www.binance.com/en", 
       "https://tomtit.tomsk.ru/",
       "https://jsonplaceholder.typicode.com/",
       "https://moodle.tomtit-tomsk.ru/"]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        code = response.status_code
        match code:
            case 200:
                status = "-OK-200"
            case 202:
                status = "-Accepted-202"
            case 204:
                status = "-No_Content-204"
            case 403:
                status = "-Forbidden-403"
            case 404:
                status = "-Not_Found-404"
            case 500:
                status = "-Internal_Server-Error-500"
            case 503:
                status = "-Service_Unavailable-503"
            case 504:
                status = "-Gateway_Timeout-504"
            case _:
                status = code
        print(url, status)
    except:
        print("Ошибка запроса")
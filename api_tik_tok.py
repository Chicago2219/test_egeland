import requests
import time
from concurrent.futures import ThreadPoolExecutor


def get_tiktok_user_data(username):
    url = f"https://api.tiktok.com/v1/users/{username}/info"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    response = requests.get(url, headers=headers)

    if response.status_code == 429:
        time.sleep(60)  # Ожидание при превышении лимита запросов
        return get_tiktok_user_data(username)

    return response.json()


tiktok_users = ["obschestvoznaika_el",
                "himichka_el",
                "anglichanka_el",
                "fizik_el",
                "katya_matematichka"]


with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(get_tiktok_user_data, tiktok_users))


for result in results:
    try:
        save_to_db(result)  # Функция для сохранения данных куда-нибудь :)
    except NameError as e:
        print(e)

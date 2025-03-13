import requests
import time
from concurrent.futures import ThreadPoolExecutor


def get_instagram_user_data(username):
    url = f"https://graph.instagram.com/v12.0/{username}/media"
    params = {
        "access_token": "YOUR_ACCESS_TOKEN",
        "fields": "id,caption,media_type,media_url,permalink,timestamp"
    }
    response = requests.get(url, params=params)

    if response.status_code == 429:
        time.sleep(60)
        return get_instagram_user_data(username)

    return response.json()


instagram_users = ["russichka_el",
                   "anglichanka_kiko",
                   "olya_historyachka",
                   "obschestvoznaikaa_oge",
                   "russichka_oge"]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(get_instagram_user_data, instagram_users))

for result in results:
    try:
        save_to_db(result)  # Функция для сохранения данных куда-нибудь :)
    except NameError as e:
        print(e)
import requests
import config
from requests.structures import CaseInsensitiveDict


def reset_tokens_api():
    url = config.ariba_url + "tenders/reset_tokens/?user_type=TELEGRAM&username="+config.username
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"user_type": "TELEGRAM", "username": '+config.username+'}'
    resp = requests.post(url, headers=headers, data=data, verify=False)
    print()
    print(resp.text)
    print(resp.status_code)


def clear_categories():
    url = config.ariba_url + "tenders/clear_categories_and_watched_tenders_for_user/?username="+config.username+ \
                             "&user_type=TELEGRAM"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    data = "username=Serzhioo&user_type=TELEGRAM"

    resp = requests.post(url, headers=headers, data=data, verify=False)
    print()
    print(resp.text)
    print(resp.status_code)


def reset_history():
    try:

        headers = {
            "Content-Type": "application/json",
        }
        url = config.ariba_url + "tenders/reset_user_history/?username="+config.username+"&user_type=TELEGRAM"
        data = '{"user_type": "TELEGRAM", "username": "Serzhioo"}'
        resp = requests.post(url, headers=headers, data=data, verify=False)
        print()
        print(resp.text)
        print(resp.status_code)
    except Exception as e:
        print("error", e)


# reset_tokens_api()
reset_history()
# clear_categories()

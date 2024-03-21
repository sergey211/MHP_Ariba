import requests
from requests.structures import CaseInsensitiveDict

import config

url = config.ariba_url+"tenders/add_categories_to_tg_user/?username=Serzhioo"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = '["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", ' \
       '"28", "29"]'


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
print(resp.text)


import requests
import json

url = "https://checkout.pci.shopifyinc.com/sessions"

payload = {
  "credit_card": {
    "number": "5122 3026 4543 2875",
    "month": 8,
    "year": 2029,
    "verification_value": "364",
    "start_month": None,
    "start_year": None,
    "issue_number": "",
    "name": "Tete Yaya"
  },
  "payment_session_scope": "thebodyshop.com"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json",
  'Content-Type': "application/json",
  'sec-ch-ua': "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://checkout.pci.shopifyinc.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://checkout.pci.shopifyinc.com/build/739af4d/number-ltr.html?identifier=&locationURL=",
  'accept-language': "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)
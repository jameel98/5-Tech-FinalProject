import requests

# Define the URL and headers
url = "https://www.foxhome.co.il/checkout/cart/add/product/19798"
headers = {
    "authority": "www.foxhome.co.il",
    "method": "POST",
    "path": "/checkout/cart/add/product/19798",
    "scheme": "https",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-length": "63",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "userStage=3; _gcl_au=1.1.346657170.1715251747; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%223q6JFKbXctusCDUbQkur%22%7D; _fbp=fb.2.1715251748318.253580735; _ym_uid=1715251749317817048; _ym_d=1715251749; glassix-visitor-id-v2-49edd63d-cb0e-4de3-aaae-560018f743d7=8080a99b-0cd2-4594-a38a-6f363552d956; skid=c91aa8f2-4291-4744-8deb-082ce9612501; store=default; store_id=1; _hjSessionUser_1639715=eyJpZCI6ImU0NmE1MzkwLTExZmItNWRiYS1iY2NiLTA3ZDBlZjY5OTI1MSIsImNyZWF0ZWQiOjE3MTUyNTE3NDg1NTgsImV4aXN0aW5nIjp0cnVlfQ==; minicart_init=1; _gid=GA1.3.922489892.1722718744; mage-messages=; _rm_sessionId=eyJlbWFpbCI6ImphbWVlbHRlc3Rpbmc5OEBnbWFpbC5jb20iLCJpZGVudGl0eUdVSUQiOiIyM2IyZWM4MC01MjI5LTExZWYtYTMyNS0zZmNhMjhhZTJjZTQiLCJ0cmFja2luZ0lkIjpudWxsLCJpZCI6bnVsbH0%3D; mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; _za_utm_params=%7B%22utm_term%22%3A%22fox%2520home%22%2C%22utm_content%22%3A%22%257badgroup%257d_91723844572%257d%22%2C%22utm_campaign%22%3A%22%257b%257bcampaign.name%257d%257d%22%7D; _gac_UA-22580522-6=1.1722838573.Cj0KCQjw6PGxBhCVARIsAIumnWbH3svHTk8K74bJP4QyiIkAElSEuxb9cNXxMTAPAUMOW5UBT-RPxVsaAnkIEALw_wcB; _gac_UA-22580522-2=1.1722838585.Cj0KCQjw6PGxBhCVARIsAIumnWbH3svHTk8K74bJP4QyiIkAElSEuxb9cNXxMTAPAUMOW5UBT-RPxVsaAnkIEALw_wcB; _gcl_aw=GCL.1722838853.Cj0KCQjw6PGxBhCVARIsAIumnWbH3svHTk8K74bJP4QyiIkAElSEuxb9cNXxMTAPAUMOW5UBT-RPxVsaAnkIEALw_wcB; _gcl_gs=2.1.k1$i1722838852; userStage=3; _hjSession_1639715=eyJpZCI6Ijc3MTUzZGY0LWJkYTEtNDI1Yy04OTZlLWM1YjY5ZmM1NWIzYyIsImMiOjE3MjI5MjQ1NTk4MTAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ym_isad=2; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _ym_visorc=w; form_key=UlWwIhWujsCAak55; PHPSESSID=eq26vmc1143pmt24j32tj63c6f; X-Magento-Vary=20b556236a9f73d55ee9ffb5a21ffc45a5f6d878; private_content_version=227aea566e73d6efaa0a29e8f3b81d1e; form_key=UlWwIhWujsCAak55; idus_mylist_init=274456; __za_cds_19763407=%7B%22data_for_campaign%22%3A%7B%22country%22%3A%22IL%22%2C%22language%22%3A%22EN%22%2C%22ip%22%3A%2277.137.25.18%22%2C%22start_time%22%3A1722838567000%2C%22session_groups%22%3A%7B%223652%22%3A%7B%22campaign_Id%22%3A%2292312%22%7D%7D%2C%22session_campaigns%22%3A%7B%2265692%22%3A%7B%22type%22%3A%22popup%22%2C%22occur%22%3A1%7D%2C%2287398%22%3A%7B%22type%22%3A%22bubble%22%2C%22occur%22%3A1%7D%2C%2289677%22%3A%7B%22type%22%3A%22bubble%22%2C%22occur%22%3A1%7D%2C%2292312%22%3A%7B%22type%22%3A%22popup%22%2C%22occur%22%3A1%7D%7D%7D%7D; __za_19763407=%7B%22sId%22%3A13119766%2C%22dbwId%22%3A%221%22%2C%22sCode%22%3A%2236191410d84edbeee31a23f4af451e96%22%2C%22sInt%22%3A5000%2C%22na%22%3A9%2C%22td%22%3A2%2C%22ca%22%3A%221%22%7D; _ga=GA1.3.349965804.1715251747; cto_bundle=xQA0ll9ESEVldEowJTJCanBwenNOd2NZdnpiZ25zTERWWiUyQkJ2RUZzb3VFdnM1a3djbFJ6U2JGOVVaMVFiVzhQTEVJakluVnozNDBpSzVvdTRwM0g5eFZaZTNPMGc5czZTcnB2Zk15ZUtmV1RuZGZiNjB3JTJGdkpJT1Z6bWJVMFlCMjd4VnR3TUpvY0ljcTI1WER2QUowNnVtZm1aaE9GT0VxaGNDTjlhQWphZGMlMkZLJTJGSndjJTNE; __za_cd_19763407=%7B%22visits%22%3A%22%5B1722838570%2C1722752119%2C1722718745%2C1722499936%2C1715251750%5D%22%2C%22campaigns_status%22%3A%7B%2265692%22%3A1722930886%2C%2272289%22%3A1722930589%2C%2278744%22%3A1722930897%2C%2287398%22%3A1722843856%2C%2289677%22%3A1722843857%2C%2292312%22%3A1722843623%7D%2C%22historical_goals%22%3A%7B%221427.1428%22%3A1%7D%7D; _ga_F9XGGY00GP=GS1.3.1722930530.18.1.1722930900.0.0.0; _ga_0HZKGMPTJC=GS1.1.1722930519.23.1.1722931386.59.0.0",
    "origin": "https://www.foxhome.co.il",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.foxhome.co.il/last-chance",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# Define the data
data = {
    "product_layout": "category",
    "product": "19798",
    "form_key": "UlWwIhWujsCAak55"
}

# Make the POST request
response = requests.post(url, headers=headers, data=data)

# Print the status code and response text
print("Status Code:", response.status_code)
print("Response Text:", response.text)

# Optional: check if response is in JSON format
try:
    json_response = response.json()
    print("JSON Response:", json_response)
except ValueError:
    print("Response is not in JSON format.")

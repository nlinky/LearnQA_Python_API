from json.decoder import JSONDecodeError
import requests

# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

# response = requests.get('https://playground.learnqa.ru/api/hello')
# print(response.text)
#
# response = requests.get('https://playground.learnqa.ru/api/get_text')
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")

'''
get = params
post = data
'''
# response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
# print(response.text)
#
# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/check_type")
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(first_response.url)
# print(second_response.url)

# headers = {"some_header":"123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
# print(response.text) # заголовки запроса
# print(response.headers) # заголоки ответа сервера

paylaod = {"login":"secret_login", "password":"secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=paylaod)

cookie_value = response1.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)
import requests, os

PROXY_POOL_URL = 'http://localhost:5000/weibo/random'

def get_cookies():
    t = 0
    try:
        while t < 20:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                cookies =response.text
                t += 1
                yield cookies

    except ConnectionError:
        return None

# 可以写入本地, 如调用接口方法不用写了
# def write_cookies(cookies):
#     t = 0
#     cookies_list = []
#     for each_cookies in cookies:
#         if not each_cookies in cookies_list:
#             print(each_cookies)
#             return each_cookies
#         else:
#             pass


if __name__ == '__main__':
    text = get_cookies()
    # write_cookies(text)

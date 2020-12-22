import requests
import json
import time
import random

# 加入随机延时
time.sleep(random.randint(1,3))

fromdata = {}
if fromdata == {}:
    fromdata = eval(input().strip())
print(fromdata)
print(type(fromdata))

def main():
    s = requests.session()
    s.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    url0 = f'https://forever.ypork.com/auth/login'
    r = requests.get(url0, timeout=15)

    headers0 = {
        'origin': 'https://forever.ypork.com',
        'referer' : 'https://forever.ypork.com/auth/login'
    }
    r0 = s.post(url0, data=fromdata, headers=headers0, timeout=15)
    if r0.status_code == 200:
        t = json.loads(r0.text)
        print(t['msg'])

    url2 = f"https://forever.ypork.com/user/checkin"

    r2 = s.post(url2, timeout=15)
    r2.raise_for_status()
    t = json.loads(r2.text)
    if t["msg"]:
        print(t["msg"])
    else:
        print("Error")
        exit(100)

# if __name__ == "__main__":
#     main()
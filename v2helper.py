import requests
import json
import time
import random

# 加入随机延时
time.sleep(random.randint(1,30))

fromdata = {}
if fromdata == {}:
    fromdata['email'], fromdata["passwd"], sckey = input().strip().split(",")

# 微信推送
def send_wechat(content):
    # title and content must be string.
    title = "v2流量签到通知"                                   
    url = 'https://sc.ftqq.com/' + sckey + '.send'
    data = {'text':title,'desp':content}
    result = requests.post(url,data)
    return(result) 

def main():
    s = requests.session()
    s.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    url0 = f'https://forever.pork16.com/auth/login'
    try:
        r = requests.get(url0, timeout=15)
    except requests.exceptions.RequestException as e:
        print("响应失败")
        send_wechat("网站响应失败")
        return

    headers0 = {
        'origin': 'https://forever.pork16.com',
        # 'referer' : 'https://forever.ypork.com/auth/login'
        'referer' : 'https://forever.pork16.com/auth/login' 
    }
    try:
        r0 = s.post(url0, data=fromdata, headers=headers0, timeout=15)
    except requests.exceptions.RequestException as e:
        print(e)
        send_wechat("r0失败" + e)
        return
    if r0.status_code == 200:
        t = json.loads(r0.text)
        print(t['msg'])
    else:
        send_wechat("登录失败")

    url2 = f"https://forever.pork16.com/user/checkin"

    r2 = s.post(url2, timeout=15)
    r2.raise_for_status()
    t = json.loads(r2.text)
    if t["msg"]:
        print(t["msg"])
    else:
        print("Error")
        send_wechat("发生错误")
        exit(100)

if __name__ == "__main__":
    main()

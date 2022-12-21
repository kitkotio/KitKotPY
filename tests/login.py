from kitkot import KitKot
import time

kitkot = KitKot(api_key="my-api-key")

params = {
    "username": "my-tiktok-username",
    "password": "my-tiktok-password"
}
res = kitkot.account.login(params=params)

session_key = res["session_key"]
session_created = kitkot.get_session(params={'session_key': session_key})

attempts = 0
while True:
    if attempts > 8:
        exit()
    session_created = kitkot.get_session(params={'session_key': session_key})
    if session_created["code"] == 200:
        print(session_created)
        exit()
    print(session_created)
    time.sleep(15)

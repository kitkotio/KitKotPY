from KitKot import KitKot


kitkot = KitKot(api_key="my-api-key")

params = {
    "id": "tiktok"
}
user_ids = kitkot.user.get_user_ids(params=params)
print(user_ids)
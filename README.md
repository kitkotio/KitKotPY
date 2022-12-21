<p align="center"><img src="https://kitkot.io/img/logo.png?width=128&height=128" alt="kitkot_image"/></p>

---
<h3 align="center">
	<p>
	Python Package For The <a url="https://kitkot.io">KitKot</a> API
	</p>
</h3>

`pip install kitkot`

📘 For more examples please check the tests folder [here](https://github.com/kitkotio/KitKotPY/tree/main/tests), documentation can also be found [here](https://docs.kitkot.io/)
```python
from KitKot import KitKot

kitkot  =  KitKot(api_key="my-api-key")
params  =  {
	"id":  "tiktok"
}
user_ids  =  kitkot.user.get_user_ids(params=params)
print(user_ids)
```
---
<h3 align="center">
	<p>
		⚙️ Library Methods
	</p>
</h3>

- [x] Follow Users
- [x] Like Videos
- [x] Post Comments
- [x] Scrape Information (User, Video, etc)
- [x] Join lives & talk/fetch live messages

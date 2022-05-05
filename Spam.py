import requests
import json
import random

s = requests.Session()

username = input("Username : ")
password = input("Password : ")

headers = {
	"Host": "test.pluem.host",
	"content-length": "37",
	"accept": "application/json, text/javascript, */*; q = 0.01",
	"content-type": "application/x-www-form-urlencoded; charset = UTF-8",
	"x-requested-with": "XMLHttpRequest",
	"sec-ch-ua-mobile": "?0",
	"user-agent": "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
	"sec-ch-ua-platform": "Android",
	"origin": "https://test.pluem.host",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": "https://test.pluem.host/"
}

data = {
	"username":username,
	"password":password
}

login = s.post("https://test.pluem.host/api/login.php",data = data, headers = headers)
check_login = json.loads(login.text)
if (check_login['status'] == "success"):
	print("เข้าสู่ระบบสำเร็จ!!")
else :
	print("ชื่อหรือรหัสผ่านผิด!!")
	exit()
	
message = input("Message? : ")
amount = int(input("Amount? : "))

header = {
	"Host": "test.pluem.host",
	"content-length": "16",
	"accept": "application/json, text/javascript, */*; q = 0.01",
	"content-type": "application/x-www-form-urlencoded; charset = UTF-8",
	"x-requested-with": "XMLHttpRequest",
	"sec-ch-ua-mobile": "?0",
	"user-agent": "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
	"sec-ch-ua-platform": "Android",
	"origin": "https://test.pluem.host",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": "https://test.pluem.host/post"
}

payload = {
	"details_post":message
}

for i in range(amount):
	post_auto = s.post("https://test.pluem.host/api/post.php",data=payload, headers=header)
	check_post = json.loads(post_auto.text)
	if (check_post['status'] == "success"):
		print("Success!! -> " + str(random.randint(1,100)))
	else:
		print("Failed!!")
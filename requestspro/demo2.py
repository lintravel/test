import requests

url="http://132.232.44.158:5000/userLogin/"
d={"username":"test", "password":"123456", "captcha":"123456"}
res=requests.post(url=url,json=d)

assert res.status_code==200

re=res.json()
assert re.get("code")==200

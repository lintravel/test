import requests
'''
get方法
'''
def test_01_get():
    res=requests.get("http://132.232.44.158:8080/morning/getAllGoods")
    print("text=",res.text)
    print("header=",res.headers)
    print("status=",res.status_code)
    print("cookies=",res.cookies)
'''
post方法：form-data格式传参
'''
def test_02_post_formdata():
    url = "http://132.232.44.158:8080/morning/user/userLogin"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginName\"\r\n\r\n143@qq.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginPassword\"\r\n\r\na123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Cache-Control': "no-cache",
        'Postman-Token': "7d856ab5-4707-d805-65c8-384fb008ecb2"
        }
    res = requests.post(url=url, data=payload, headers=headers)
    print(res.text)

def test_02_post_formdata1():
    url = "http://132.232.44.158:8080/morning/user/userLogin"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginName\"\r\n\r\n143@qq.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginPassword\"\r\n\r\na12345689\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Cache-Control': "no-cache",
        'Postman-Token': "9ee07c8a-1364-95b9-4177-c6e1964ddc1f"
        }
    response = requests.post(url=url, data=payload, headers=headers)
    print(response.text)

'''
post方法：json格式传参
'''
def test_03_json():
    url="http://132.232.44.158:5000/userLogin/"
    d={"username":"test", "password":"123456", "captcha":"123456"}
    res=requests.post(url=url,json=d)
    print("json格式传参：",res.text)

if __name__=="__main__":
    test_01_get()
    test_02_post_formdata()
    test_02_post_formdata1()
    test_03_json()
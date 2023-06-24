import requests

cookie = {'visit-month':'February'}
response = requests.get('http://rahulshettyacademy.com',allow_redirects=False,cookies=cookie,timeout=1)
print(response.history)
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month':'march'})

res = se.get("https://httpbin.org/cookies",cookies={'visit-year':'2023'})
print(res.text)

#attachment

url = "https://petstore.swagger.io/v2/pet/984327/uploadImage"
files = {'file': open('C:/Users/Abhishek Singh/Downloads/download.jpg','rb')}
r= requests.post(url,files=files)
print(r.status_code)
print(r.text)

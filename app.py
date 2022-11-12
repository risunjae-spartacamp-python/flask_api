import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")

# print(res)
# print(res.text["status"])
# print(type(res.text))
# print(res.json())
# print(type(res.json()))
# print(res.json()["status"])
# print(res.json()["results"])
json = res.json()
# print(res.json()["results"][0]["prefcode"])
# print(res.json()["results"][0]["address1"])
# print(res.json()["results"][0]["address2"])
# print(res.json()["results"][0]["address3"])

print(json()["results"][0]["prefcode"])
print(json()["results"][0]["address1"])
print(json()["results"][0]["address2"])
print(json()["results"][0]["address3"])



import requests

url = "https://zip-cloud.appspot.com/api/search"
while True:
  z = input("7桁の郵便番号を入力してください(ハイフンは含まない): ")
  if not z:
    break
  print(z)
  param = {"zipcode": z}
  data = requests.get(url, param).json()
  address = data["results"][0]
  print(address["address1"] + address["address2"] + address["address3"])
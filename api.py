import requests

class api():
  # 住所検索関数
  def jusyo(self):
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

  def weather(self):
    # 270000.jsonは大阪の都道府県コード
    url = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/270000.json"
    data = requests.get(url).json()
    print(data['headlineText'])
    print(data['text'])

# メインメソッド
if __name__ == '__main__':
    api().jusyo() #住所検索
    # api().weather() #天気予報
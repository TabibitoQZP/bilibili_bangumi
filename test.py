import requests
import json

if __name__ == "__main__":
    url = "http://api.bilibili.com/pgc/view/web/season?season_id=39433"
    res = requests.get(url)
    dic = json.loads(res.text)
#    f = open("test.json", "w", encoding="utf-8")
#    json.dump(dic, f, ensure_ascii=False, indent=4)
#    f.close()
    print(dic["code"]) # 0 is successful
    print(dic["result"]["stat"])
    print(dic["result"]["publish"])
    print(dic["result"]["rating"])
    print(dic["result"]["type"])

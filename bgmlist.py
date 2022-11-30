import pandas as pd
import datetime
import requests
import json

def save_data():
    url = "https://bgmlist.com/api/v1/bangumi/season"
    res = requests.get(url)
    dic = json.loads(res.text)
    base = "https://bgmlist.com/api/v1/bangumi/archive/"
    total = []
    for i in dic["items"]:
        res = requests.get(base + i)
        tmp = json.loads(res.text)
        total += tmp["items"]
    print("total pieces:", len(total))
    f = open("bgmlist.json", "w", encoding="utf-8")
    json.dump({"items": total}, f, ensure_ascii=False, indent=4)
    f.close()

def process_data():
    f = open("./bgmlist.json", "r")
    dic = json.load(f)
    f.close()
    item = dic["items"]
    dfdic = {"title": [], "year": [], "month": [], "day": [], "type": []}
    for i in item:
        dfdic["title"].append(i["title"])
        ts = datetime.datetime.strptime(i["begin"], "%Y-%m-%dT%H:%M:%S.%fZ")
        dfdic["year"].append(ts.year)
        dfdic["month"].append(ts.month)
        dfdic["day"].append(ts.day)
        dfdic["type"].append("bgmlist")
    df = pd.DataFrame(dfdic)
    df.to_excel("bgmlist.xlsx")

if __name__ == "__main__":
    #save_data()
    process_data()

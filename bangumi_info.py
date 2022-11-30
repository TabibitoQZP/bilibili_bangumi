import json
import requests

def store_info(path, f_name):
    f = open(f_name, "r", encoding='utf-8')
    data = json.load(f)["data"]
    f.close()
    cnt = 0
    for i in range(len(data)):
        cnt += 1
        ssid = data[i]["season_id"]
        title = data[i]["title"]
        title = title.replace("/", "-")
        url = f"http://api.bilibili.com/pgc/view/web/season?season_id={ssid}"
        res = requests.get(url)
        dic = json.loads(res.text)
        if dic["code"] != 0:
            print(f"error in {cnt}!")
            break
        f = open(f"./{path}/{cnt}_{ssid}.json", "w", encoding= "utf-8")
        json.dump(dic, f, ensure_ascii=False, indent=4)
        f.close()

if __name__ == "__main__":
    store_info("all_bangumi", "./all_bangumi.json")

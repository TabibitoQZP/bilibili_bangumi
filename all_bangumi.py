import requests
import json

def url(pg, pgsize=1000):
    url = f"https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page={pg}&season_type=1&pagesize={pgsize}&type=1"
    return url

def dongman_url():
    url = "https://api.bilibili.com/pgc/season/index/result?season_version=-1&is_finish=-1&copyright=-1&season_status=-1&year=-1&style_id=-1&order=3&st=4&sort=0&page=1&season_type=4&pagesize=20&type=1"

def get_list(pg):
    res = requests.get(url(pg))
    #print(res.text)
    js = json.loads(res.text)
    has_next = True if js["data"]["has_next"] == 1 else False
    lst = js["data"]["list"]
    return lst, has_next

if __name__ == "__main__":
    pg = 1
    all_lst = []
    while True:
        lst, has_next = get_list(pg)
        all_lst += lst
        pg += 1
        if not has_next:
            break
    dic = {"data": all_lst}
    f = open("all_bangumi.json", "w", encoding="utf-8")
    json.dump(dic, f, indent=2, ensure_ascii=False)
    f.close()

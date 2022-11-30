import os
import json
import pandas as pd

def collect_sheet(root, output):
    lst = []
    if type(root) == list:
        for i in root:
            tmp = os.listdir(i)
            tmp = [os.path.join(i, j) for j in tmp]
            lst += tmp
    else:
        tmp = os.listdir(root)
        tmp = [os.path.join(root, j) for j in tmp]
        lst += tmp
    dics = []
    for i in lst:
        path = i
        f = open(path, "r")
        dic = json.load(f)
        f.close()
        stat = dic["result"]["stat"]
        title = dic["result"]["title"]
        publish = dic["result"]["publish"]
        try:
            rating = dic["result"]["rating"]
        except:
            rating = {"count": "", "score": ""}
        #dic["result"]["up_info"]["follower"]
        pub_time = publish["pub_time"].split(" ")[0].split("-")
        #print(publish["pub_time"])
        #print(pub_time)
        ele = {
                "title": title,
                "ssid": dic["result"]["season_id"],
                "pub_time": publish["pub_time"],
                "year": int(pub_time[0]),
                "month": int(pub_time[1]),
                "day": int(pub_time[2]),
                "epnum": len(dic["result"]["episodes"]),
              }
        ele.update(rating)
        ele.update(stat)
        dics.append(ele)
    df = {}
    for i in dics[0].keys():
        df[i] = []
    for i in dics:
        for j in dics[0].keys():
            df[j].append(i[j])
    pddf = pd.DataFrame(df)
    pddf.to_excel(output)

if __name__ == "__main__":
    collect_sheet("./bangumi_info", "./bangumi_info.xlsx")
    collect_sheet("./dongman_info", "./dongman_info.xlsx")
    collect_sheet(["./dongman_info", "./bangumi_info"], "./all_info.xlsx")

import requests
data = requests.get('https://covid19-api.org/api/status').json()
country_iq = ''
print("Made by Hiro Wu with ❤")
while country_iq != '0':
    country_iq = input("請輸入要查詢的國家代號(如:tw)，或按0來離開: ")
    for i in range(len(data)):
        if data[i]['country'] == country_iq.upper():
            print("國家：%s" %(data[i]['country']))
            print("更新時間：%s" %(data[i]['last_update'].replace("T"," ")))
            print("確診人數：%s" %(data[i]['cases']))
            print("死亡人數：%s" %(data[i]['deaths']))
            print("痊癒人數：%s" %(data[i]['recovered']))
    # -*- coding: utf8 -*-

import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree, parse, fromstring
import json


def run():
    dataDate=datetime.datetime.now()
    today=str(dataDate.year)+(("0"+str(dataDate.month)) if (dataDate.month <10) else (str(dataDate.month)))+(("0"+str(dataDate.day)) if (dataDate.day <10) else (str(dataDate.day)))

    hourNow=dataDate.hour

    #현재 시간에 따라서 base time을 정한다. (base time : 2,5,8,11,14,17,20,23)
    baseDate=[]
    for i in range(24):
        baseDate.append(datetime.datetime(dataDate.year,dataDate.month,dataDate.day,i,41))


    for i in range(len(baseDate)):
        if dataDate <= baseDate[0]:
            dataDate=dataDate-datetime.timedelta(days=1)
            today=str(dataDate.year)+(("0"+str(dataDate.month)) if (dataDate.month <10) else (str(dataDate.month)))+(("0"+str(dataDate.day)) if (dataDate.day <10) else (str(dataDate.day)))
            baseTime="2300"
            break
        elif dataDate <= baseDate[i]:
            baseTime=baseDate[i-1].hour
            if baseTime<10:
                baseTime="0"+str(baseDate[i-1].hour)+"00"
            else:
                baseTime=str(baseDate[i-1].hour)+"00"
            break
        else:
            baseTime="2300"
            break

    import urllib.request


    url="http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst?serviceKey=rkg5xtO94KPwqpaOkHwkZf0MqU2RcGbvOOXVbeCT%2BBoEbD99hnmXU7nUN9mfXfANBXKyuZ%2BZrhbzJdAtnpnkYg%3D%3D&pageNo=1&numOfRows=1000&dataType=XML&base_date="+today+"&base_time="+baseTime+"&nx=86&ny=87"

    response = urllib.request.urlopen(url)

    data = response.read().decode("utf-8")
    tree=ElementTree(fromstring(data))
    root=tree.getroot()


    xmlData=[]
    for i in root[1][1]:
        tmp_data=[]
        if i[2].text in ["T1H","REH","PTY","VEC","WSD"]:
            for ii in i:
                tmp_data.append(ii.text)


            xmlData.append(tmp_data)




    data_1={}
    data_2={}
    for i in range(len(xmlData)):
        data_1[xmlData[i][2]]=xmlData[i][5]
    data_2[0]=[data_1]



    with open('weather_now.json', 'w', encoding='utf-8') as make_file:
        json.dump(data_2, make_file, indent="\t")

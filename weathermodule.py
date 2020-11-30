    # -*- coding: utf8 -*-

import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree, parse, fromstring
import json


def run():
    dataDate=datetime.datetime.now()
    today=str(dataDate.year)+str(dataDate.month)+str(dataDate.day)

    hourNow=dataDate.hour

    #현재 시간에 따라서 base time을 정한다. (base time : 2,5,8,11,14,17,20,23)
    baseHour=[2,5,8,11,14,17,20,23]
    baseDate=[]
    for i in baseHour:
        baseDate.append(datetime.datetime(dataDate.year,dataDate.month,dataDate.day,i,15))


    for i in range(len(baseDate)):
        if dataDate <= baseDate[0]:
            dataDate=dataDate-datetime.timedelta(days=1)
            today=str(dataDate.year)+str(dataDate.month)+str(dataDate.day)
            baseTime= "2300"
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



    import urllib.request


    url="http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?serviceKey=rkg5xtO94KPwqpaOkHwkZf0MqU2RcGbvOOXVbeCT%2BBoEbD99hnmXU7nUN9mfXfANBXKyuZ%2BZrhbzJdAtnpnkYg%3D%3D&pageNo=1&numOfRows=1000&dataType=XML&base_date="+today+"&base_time="+baseTime+"&nx=86&ny=87"

    response = urllib.request.urlopen(url)

    data = response.read().decode("utf-8")
    tree=ElementTree(fromstring(data))
    root=tree.getroot()


    xmlData=[]
    for i in root[1][1]:
        tmp_data=[]
        if i[2].text in ["POP","PTY","REH","SKY","T3H","VEC","WSD"]:
            for ii in i:
                tmp_data.append(ii.text)


            xmlData.append(tmp_data)



    count=0
    count2=0
    data_1={}
    data_2={}
    for i in range(len(xmlData)):
        if count>=7:
            data_1["date"]=xmlData[i-1][3]
            data_1["time"]=xmlData[i-1][4]
            data_2[str(count2)]=[data_1]
            data_1={}
            count=0
            count2+=1
        data_1[xmlData[i][2]]=xmlData[i][5]
        count+=1



    with open('weather.json', 'w', encoding='utf-8') as make_file:
        json.dump(data_2, make_file, indent="\t")


'''
동네예보 코
	POP	강수확률	%	8
	PTY	강수형태	코드값	4
	R06	6시간 강수량	범주 (1 mm)	8
	REH	습도	%	8
	S06	6시간 신적설	범주(1 cm)	8
	SKY	하늘상태	코드값	4
	T3H	3시간 기온	℃	10
	TMN	아침 최저기온	℃	10
	TMX	낮 최고기온	℃	10
	UUU	풍속(동서성분)	m/s	12
	VVV	풍속(남북성분)	m/s	12
	WAV	파고	M	8
	VEC	풍향	m/s	10
	WSD	풍속	m/s	10
'''

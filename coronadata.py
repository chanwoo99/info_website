    # -*- coding: utf8 -*-

import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree, parse, fromstring
import json


def run():
    dataDate=datetime.datetime.now()
    today=str(dataDate.year)+str(dataDate.month)+str(dataDate.day-1)







    import urllib.request


    url="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=rkg5xtO94KPwqpaOkHwkZf0MqU2RcGbvOOXVbeCT%2BBoEbD99hnmXU7nUN9mfXfANBXKyuZ%2BZrhbzJdAtnpnkYg%3D%3D&pageNo=1&numOfRows=1000&startCreateDt="+today+"&endCreateDt="+today

    response = urllib.request.urlopen(url)

    data = response.read().decode("utf-8")
    tree=ElementTree(fromstring(data))
    root=tree.getroot()

    data=root[1][0]

    for i in data:
        if i[3].text=="대구":
            deagu_num=i[6].text





    return_data={"number":deagu_num,"date":str(dataDate.day)+":"+str(dataDate.hour)+":"+str(dataDate.minute)}



    with open('deagu_corona.json', 'w', encoding='utf-8') as make_file:
        json.dump(return_data, make_file, indent="\t")

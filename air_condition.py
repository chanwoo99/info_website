    # -*- coding: utf8 -*-

import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree, parse, fromstring
import json


def run():

    import urllib.request


    url="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=rkg5xtO94KPwqpaOkHwkZf0MqU2RcGbvOOXVbeCT%2BBoEbD99hnmXU7nUN9mfXfANBXKyuZ%2BZrhbzJdAtnpnkYg%3D%3D&numOfRows=100&pageNo=1&stationName=%EC%9C%A0%EA%B0%80%EC%9D%8D&dataTerm=DAILY&ver=1.7.2"
    response = urllib.request.urlopen(url)

    data = response.read().decode("utf-8")
    tree=ElementTree(fromstring(data))
    root=tree.getroot()

    if root[0][0].text == "00" or root[0][0].text == "0" :

        data1=root[1][0][0][6].text
        data2=root[1][0][0][7].text

        return_data={"value":data1,"grade":data2}







        with open('air_condition.json', 'w', encoding='utf-8') as make_file:
            json.dump(return_data, make_file, indent="\t")
    else:
        print("error")

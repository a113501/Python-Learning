#!/sur/bin/python3
# -*- coding: utf-8 -*-

import json
from urllib import request

######################################
def aqiCondi(aqi):
    if aqi<50:
        return '优',0
    elif aqi<100:
        return '良',1
    elif aqi<200:
        return '轻度污染',2
    elif aqi<300:
        return '中度污染',3
    else:
        return '重污染',4
######################################
def getInfo(cityName):
    token = '2e03b948fb4d8dc9eddffd33b66b0143649d323b'
    with request.urlopen('https://api.waqi.info/feed/%s/?token=%s'%(cityName,token)) as f:
        data=f.read()
        data_json = json.loads(data.decode('utf-8'))
    if data_json['status'] =='error':
        print(data_json['data'])
        print('请重新输入城市')
        return main()
    else:
        return analyzeInfo(data_json)
######################################
def analyzeInfo(data_json):
    condition = aqiCondi(data_json['data']['aqi'])
    return printInfo(data_json,condition)
######################################
def printInfo(data_json,condition):
    print('\n\n\n#################################################')
    print('当前城市 ： %s'% data_json['data']['city']['name'])
    print('更新时间 : %s\n' % data_json['data']['time']['s'])
    print('该时段空气污染指数为%s,空气质量状况为%s' % (data_json['data']['aqi'],condition[0]))
    try:
        print('温度 ： %.2f' % data_json['data']['iaqi']['t']['v'])
    except KeyError:
        print('当前城市无法查询温度数据')
    try:
        print('湿度 ： %.2f' % data_json['data']['iaqi']['h']['v'])
    except KeyError:
        print('当前城市无法查询湿度数据')
    try:
            print('PM2.5 ： %.2f' % data_json['data']['iaqi']['pm25']['v'])
    except KeyError:
        print('当前城市无法查询PM2.5数据')
    try:
        print('PM10 ： %.2f' % data_json['data']['iaqi']['pm10']['v'])
    except KeyError:
        print('当前城市无法查询PM10数据')
    try:
        print('露水 ： %.2f' % data_json['data']['iaqi']['d']['v'])
    except KeyError:
        print('当前城市无法查询露水数据')
    try:
        print('气压 ： %s' % data_json['data']['iaqi']['p']['v'])
    except KeyError:
        print('当前城市无法查询气压数据')
    try:
        print('臭氧含量 ： %.2f' % data_json['data']['iaqi']['o3']['v'])
    except KeyError:
        print('当前城市无法查询臭氧含量数据')
    try:
        print('一氧化碳含量 ： %.2f' % data_json['data']['iaqi']['co']['v'])
    except KeyError:
        print('当前城市无法查询一氧化碳含量数据')
    try:
        print('二氧化硫含量 ： %.2f' % data_json['data']['iaqi']['so2']['v'])
    except KeyError:
        print('当前城市无法查询二氧化硫含量数据')
    try:
        print('二氧化氮含量 ： %.2f' % data_json['data']['iaqi']['no2']['v'])
    except KeyError:
        print('当前城市无法查询二氧化氮含量数据')
    try:
        print('风力大小 ： %.2f' % data_json['data']['iaqi']['w']['v'])
    except KeyError:
        print('当前城市无法查询风力大小数据')
    try:
        print('风向 ： %s' % data_json['data']['iaqi']['wd']['v'])
    except KeyError:
        print('当前城市无法查询风向数据')
    print('#################################################')
######################################
def main():
    while True:
        cityName = input('输入城市名称（q结束)：')
        if cityName == 'q':
            break
        getInfo(cityName)
########################################
if __name__=='__main__':
    main()

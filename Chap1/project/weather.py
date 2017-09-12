# -*- coding: utf-8 -*-


with open('weather_info.txt',encoding="utf8") as file:
    list_contents = file.readlines()
weather_dic = {}

for item in list_contents:
    city = item.split(',')[0]
    weather = item.split(',')[1].rstrip('\n')
    weather_dic[city] = weather
	

history_dic = {}
while True: 
    city_name = input('输入一个城市名：')
   	
    if city_name in weather_dic.keys():
        city_weather = weather_dic[city_name]
        history_dic[city_name] = city_weather
        print('%s的天气是：%s' % (city_name,city_weather))
             
    elif (city_name == 'help') or (city_name == 'h'):
        print('输入城市名,查询该该城市的天气;')
        print('输入help,获取帮助文档;')
        print('输入history,获取查询历史;')
        print('输入quit,退出天气查询系统.')
		
    elif city_name == 'history':    
        for city_name in history_dic:
            print(city_name,history_dic[city_name])
			
    elif city_name == 'quit':
        for city_name in history_dic:
            print(city_name,history_dic[city_name])
            break	
    else:
        print('你输入的城市不存在，请重新输入。')




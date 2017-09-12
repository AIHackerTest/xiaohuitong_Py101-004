# -*- coding: utf-8

with open('weather_info.txt','r',encoding="utf8") as wea_file:
    contents = wea_file.readlines()

weather_dic = {}
for line in contents:
    lis_item = line.split(',')
    city_str = lis_item[0]
    weather_str = lis_item[1].rstrip('\n')
    weather_dic[city_str] = weather_str
#print (weather_dic)	
history = []
while True:
    user_input = input('请输入指令：')
    if user_input == 'quit' or 	user_input == 'q':
        for item in history:
            print(item)
        break
    elif user_input == 'help' or 	user_input == 'h':
        print('''
            输入城市名,查询该该城市的天气;
            输入help,获取帮助文档;
            输入history,获取查询历史;
            输入quit,退出天气查询系统.
			''')
    elif user_input in weather_dic:
        weather = weather_dic[user_input]
        history_str = user_input + ':' + weather
        history.append(history_str)
        print('%s的天气是:%s' %(user_input,weather))
    elif user_input  == 'history':
        for item in history:
            print(item)
    else:
        print('你输入的城市不存在，请重新输入')
		
        		
    
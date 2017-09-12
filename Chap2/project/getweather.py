

import requests

print('*' * 30)
print('''
    输入城市名,查询该城市的实时天气;
    输入指令,获取帮助文档;
    输入指令,获取查询历史;
    输入指令,退出天气查询系统.
    ''')
print('*' * 30)

city_history = []

while True:

    location = input('请输入一个城市名：')   
    try:    
        url = 'https://api.seniverse.com/v3/weather/daily.json'
		
        result = requests.get(
		    url, 
		    params={
                'key': 'mog6dosgivjijizh',
                'location': location,
                'language': 'zh-Hans',
                'unit': ''
            }, 
			timeout=20)  		
        result_json = result.json()
		
        result_info = result_json['results'][0]
        city_name = result_info['location']['name']
        date = result_info['daily'][0]['date']
        text_day = result_info['daily'][0]['text_day']
        text_night = result_info['daily'][0]['text_night']
        high = result_info['daily'][0]['high']
        low = result_info[0]['daily'][0]['low']
        wind_direction = result_info['daily'][0]['wind_direction']
        wind_scale = result_info['daily'][0]['wind_scale']

        weather_info = '{}：{}的天气：白天{}，夜晚{}，温度：{}~{}，{}风{}级' .format(
		    date,city_name,text_day,text_night,low,high,wind_direction,
			wind_scale)
        city_history.append(weather_info)
		
        print(weather_info)    
    except KeyError:		
        if location == 'h' or location == 'help':
            print('''
                输入城市名,查询该该城市的天气;
                输入help,获取帮助文档;
                输入history,获取查询历史;
                输入quit,退出天气查询系统.
			    ''')
        elif location == 'history':
            if city_history:
                for item in city_history:
                    print(item)
            else:
                print('你还没有查询历史。')		
        elif location == 'quit' or location == 'q':
            print('你已退出查询程序。')
            break
        else:
            print('对不起，你输入的城市不存在，请检查后重新输入。')
  
    


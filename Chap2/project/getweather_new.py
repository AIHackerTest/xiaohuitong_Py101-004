

import requests

url = 'https://api.seniverse.com/v3/weather/daily.json'

def getweather(location):
    result = requests.get(
	    url, 
		params={
            'key': 'mog6dosgivjijizh',
            'location': location,
            'language': 'zh-Hans',
            'unit': ''
        }, 
		timeout=2)
    return result.json()  
	
	
def print_weather(result_info):

    result_dic = result_info['results'][0]
    city_name = result_dic['location']['name']
    date = result_dic['daily'][0]['date']
    text_day = result_dic['daily'][0]['text_day']
    text_night = result_dic['daily'][0]['text_night']
    high = result_dic['daily'][0]['high']
    low = result_dic['daily'][0]['low']
    wind_direction = result_dic['daily'][0]['wind_direction']
    wind_scale = result_dic['daily'][0]['wind_scale']
    weather_info = '{}：{}的天气：白天{}，夜晚{}，温度：{}~{}，{}风{}级' .format(
	    date,city_name,text_day,text_night,high,low,wind_direction,
		wind_scale)
    return weather_info
	
	
history_list = []

while True:

    user_input = input('输入一个城市：')
    try:
        result_info = getweather(user_input)
        print(print_weather(result_info))
        history_list.append(print_weather(result_info))
    except KeyError:
        if user_input in ['h', 'help']:
            print('''
                输入城市名,查询该该城市的天气;
                输入help,获取帮助文档;
                输入history,获取查询历史;
                输入quit,退出天气查询系统.
			    ''')
        elif user_input == 'history':
            if not history_list:
                print('你还没有查询历史。')
            else:
                for item in history_list:
                    print(item)
        elif user_input in ['q', 'quit']:
            print('退出天气查询系统')
            break
    
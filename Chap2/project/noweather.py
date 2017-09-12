

import requests

API = 'https://api.seniverse.com/v3/weather/now.json'
unit = 'c'


def fetchweather(location, unit):

    result = requests.get(
	    API,params={
            'key':'mog6dosgivjijizh',
            'location':location,
            'language':'zh-Hans',
            'unit':unit
        },
		timeout=5)
    return result.json()

	
def print_weather(result):
    weather_dic = result_info['results'][0]
    city_name = weather_dic['location']['name']
    text = weather_dic['now']['text']
    temp = weather_dic['now']['temperature']
    last_update = weather_dic['last_update']
    weather_str = '{}的天气是{},温度是{},最后更新时间：{}'.format(city_name,text,temp, 
	                                                    last_update)
    return weather_str

	
history_list = []

while True:
    user_input = input('请输入需要查询的城市：')
    result_info = fetchweather(user_input, unit)
    try:
        print(print_weather(result_info))
        history_list.append(print_weather(result_info))
    except KeyError:
        if user_input == '1':
            unit = 'f'
        elif user_input == '0':
            unit = 'c'
        elif user_input in ['h', 'help']:
            print('''
                输入城市名,查询该该城市的天气;
                输入help,获取帮助文档;
                输入history,获取查询历史;
                输入quit,退出天气查询系统;
                输入0或1切换天气单位.
            ''')
        elif user_input in ['q', 'quit']:
            print('已退出天气查询系统！')
            break
        elif user_input == 'history':
            print('你查询的历史信息为：')
            for item in history_list:
                print(item)
        else:
            print('你输入的信息有误，请重新输入！')

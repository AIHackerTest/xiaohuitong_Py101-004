import requests

def getweather(location):
    result = requests.get(
	'https://api.seniverse.com/v3/weather/daily.json',
        params={
            'key': 'mog6dosgivjijizh',
            'location': location,
            'language': 'zh-Hans',
            'unit': ''
        },
	timeout=10)
    result_info = result.json()
    result_dic = result_info['results'][0]
    city_name = result_dic['location']['name']
    date = result_dic['daily'][0]['date']
    text_day = result_dic['daily'][0]['text_day']
    text_night = result_dic['daily'][0]['text_night']
    high = result_dic['daily'][0]['high']
    low = result_dic['daily'][0]['low']
    wind_direction = result_dic['daily'][0]['wind_direction']
    wind_scale = result_dic['daily'][0]['wind_scale']
    weather_info = '*{}* {}的天气：白天{}，夜晚{}，温度：{}~{}，{}风{}级' .format(
	    date,city_name,text_day,text_night,low,high,wind_direction,
	    wind_scale)
    return weather_info

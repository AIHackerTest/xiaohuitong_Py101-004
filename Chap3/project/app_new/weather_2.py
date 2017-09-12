
from flask import Flask, request, render_template
from weather import getweather

app = Flask(__name__)

history_list=[]
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['action'] == '查询':
            try:
                weather_str = getweather(request.form['city'])
                history_list.append(weather_str)
                return render_template('query.html', weather_str=weather_str)
            except KeyError:
                return render_template('error.html')
        elif request.form['action'] == '帮助':
            return render_template('help.html')
        elif request.form['action'] == '历史':
            return render_template('history.html', history_list=history_list)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)

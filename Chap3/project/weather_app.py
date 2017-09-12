
from flask import request,Flask,render_template
import weather

app = Flask(__name__)

history_list = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user_interface', methods=['GET', 'POST'])
def query():
    if request.args.get('query') == '查询':
        try:
            city = request.args.get('city')
            weather_str = weather.getweather(city)
            history_list.append(weather_str)
            return render_template('query.html', weather_str=weather_str)
        except KeyError:
            return render_template('error.html')
    elif request.args.get('help') == '帮助':
        return render_template('help.html')
    elif request.args.get('history') == '历史':
        return render_template('history.html', history_list=history_list)

if __name__ == "__main__":
    app.run(debug=True)

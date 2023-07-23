from flask import Flask, render_template, url_for
import requests
import pprint

authorization = "CWB-50E267C9-4312-4DCA-AB1E-760BBB2D9E62"
url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-063?locationName=信義區&elementName=Wx,T"
res = requests.get(url, {"Authorization": authorization})
resJson = res.json()
resWx = resJson['records']['locations'][0]['location'][0]['weatherElement'][1]['time']
resT = resJson['records']['locations'][0]['location'][0]['weatherElement'][0]['time']
for Wx in resWx:
    startTime = Wx['startTime']
    if (startTime[-8::] == '06:00:00'):
        elementVal = Wx['elementValue'][1]['value']
        endTime = Wx['endTime']
        print('from:' + startTime + ' to ' + endTime + ' weather stage is ' + elementVal)
for T in resT:
    startTime = T['startTime']
    if (startTime[-8::] == '06:00:00'):
        elementVal = T['elementValue'][0]['value']
        endTime = T['endTime']
        print('from:' + startTime + ' to ' + endTime + ' temperature is ' + elementVal)
# pprint.pprint(resT)
# pprint.pprint(resWx)

app = Flask(__name__)
posts = [
    {
        'author': 'Irene',
        'title': '[重要公告] 近期運輸公告',
        'content': '因近日受到物流業影響，請於兩周前提早備貨',
        'date_posted': '4月 20日, 2023'
    },
    {
        'author': 'Irene',
        'title': '[業績獎勵] 月底結算KPI',
        'content': '近日各店 項目',
        'date_posted': '7月 31, 2022'
    }
]


@app.route("/")
@app.route("/announcement")
def announcement():
    return render_template('announcement.html', title='Announcement', posts=posts)


@app.route("/inventory")
def inventory():
    return render_template('inventory.html', title='Inventory', posts=posts)


@app.route("/weather")
def home():
    return render_template('weather.html', title='Weather', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.debug = True
    app.run()

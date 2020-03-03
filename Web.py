from datetime import datetime, timedelta
import requests
import json
import eel


@eel.expose
def ten_newest_question(tag):
    url = "http://api.stackexchange.com/2.2/search?order=desc&sort=creation&tagged=" + tag + \
          "&site=stackoverflow&filter=withbody&pagesize=10"
    data = requests.get(url).json()

    with open('./nginx-1.17.8/html/demo/json/ten_newest_question.json', 'w') as f:
        json.dump(data, f)


@eel.expose
def ten_voted_question(tag):
    last_week = datetime.today() - timedelta(days=7)
    url = "http://api.stackexchange.com/2.2/search?order=desc&sort=votes&tagged=" + tag + \
          "&site=stackoverflow&filter=withbody&pagesize=10&fromdate="+str(int(last_week.timestamp()))
    data = requests.get(url).json()

    with open('./nginx-1.17.8/html/demo/json/ten_voted_question.json', 'w') as f:
        json.dump(data, f)


eel.init('nginx-1.17.8')
eel.start('html/demo/index.html')


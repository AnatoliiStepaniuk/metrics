import requests


def get_cards():

    body = '''
    {
        "action": "getCollectionStatsHTML",
        "version": 6,
        "params": {
            "wholeCollection": false
        }
    }
    '''

    resp = requests.post('http://localhost:8765', body)
    html = resp.json()['result']

    start_phrase = '>Total cards:</td><td><b>'
    start = html.find(start_phrase) + len(start_phrase)
    finish = html.find('</b>', start)
    total_cards = int(html[start: finish])
    return total_cards

print(get_cards())
import requests
import urllib.parse
import yaml
import arrow

HOUR_IN_MILLIS = 3600000


def get_hours():
    with open('config.yaml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)['toggl']
        api_token = data['api_token']
        email = data['email']
        workspace_id = data['workspace_id']

    email_safe = urllib.parse.quote(email)
    since = '2021-01-01'
    # until = '2021-01-01'
    until = arrow.now().format('YYYY-MM-DD')
    url = f'https://api.track.toggl.com/reports/api/v2/summary?user_agent={email_safe}&workspace_id={workspace_id}&since={since}&until={until}'

    programming_year_2020 = 2065
    resp = requests.get(url, auth=(api_token, 'api_token'))
    data = resp.json()['data']
    programming_current_year = round((get_learning(data) + get_job(data))/HOUR_IN_MILLIS)
    programming_total = programming_year_2020 + programming_current_year

    hustling_total = round(get_hustling(data)/HOUR_IN_MILLIS)
    return programming_total, hustling_total


def get_learning(data):
    return list(filter(lambda x: x['title']['project'] == 'Learning Programming', data))[0]['time']


def get_job(data):
    return list(filter(lambda x: x['title']['project'] == 'Tektelic', data))[0]['time']


def get_hustling(data):
    return list(filter(lambda x: x['title']['project'] == 'Hustling', data))[0]['time']


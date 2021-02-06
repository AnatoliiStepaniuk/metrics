import requests
import urllib.parse
import yaml
import arrow

HOUR_IN_MILLIS = 3600000


def get_hours():
    since = '2021-01-01'
    until = arrow.now().format('YYYY-MM-DD')
    return get_hours_range(since, until)


def get_hours_range(since, until):
    with open('config.yaml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)['toggl']
        api_token = data['api_token']
        email = data['email']
        workspace_id = data['workspace_id']

    email_safe = urllib.parse.quote(email)
    url = f'https://api.track.toggl.com/reports/api/v2/summary?user_agent={email_safe}&workspace_id={workspace_id}&since={since}&until={until}'

    resp = requests.get(url, auth=(api_token, 'api_token'))
    data = resp.json()['data']

    return get_learning(data), get_job(data), get_hustling(data)


def get_learning(data):
    filtered = list(filter(lambda x: x['title']['project'] == 'Learning Programming', data))
    learning_millis = filtered[0]['time'] if filtered else 0
    learning_hours = round(learning_millis/HOUR_IN_MILLIS)
    learning_2020 = 330
    return learning_2020 + learning_hours


def get_job(data):
    filtered = list(filter(lambda x: x['title']['project'] == 'Tektelic', data))
    working_millis = filtered[0]['time'] if filtered else 0
    working_hours = round(working_millis/HOUR_IN_MILLIS)
    working_2020 = 1733
    return working_hours + working_2020


def get_hustling(data):
    filtered = list(filter(lambda x: x['title']['project'] == 'Hustling', data))
    hustling_millis = filtered[0]['time'] if filtered else 0
    return round(hustling_millis/HOUR_IN_MILLIS)

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

    year_2020 = 2065
    resp = requests.get(url, auth=(api_token, 'api_token'))
    current_year = round(resp.json()['total_grand']/HOUR_IN_MILLIS)
    return year_2020 + current_year
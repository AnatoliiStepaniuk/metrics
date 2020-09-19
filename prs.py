import requests
import yaml


def add_credentials(url, user, password):
    return url.replace("https://bitbucket.org", f"https://{user}:{password}@bitbucket.org")


def get_prs():

    with open('config.yaml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)['bitbucket']
        uuid = data['uuid']
        username = data['username']
        app_password = data['app_password']

    url = f"https://bitbucket.org/api/2.0/pullrequests/%7B{uuid}%7D?state=MERGED"
    url = add_credentials(url, username, app_password)
    prs = 0
    while True:
        r = requests.get(url)
        if r.status_code != 200:
            raise RuntimeError
        data = r.json()
        values = data['values']
        for value in values:
            if value['author']['uuid'] == '{' + uuid + '}':
                prs += 1
        if 'next' in data.keys():
            url = add_credentials(data['next'], username, app_password)
        else:
            break

    return prs


print(get_prs())
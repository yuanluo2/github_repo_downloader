import requests
import os

USER_NAME = 'github_user_name'   # replace it with your target.
GITHUB_URL = 'https://api.github.com/users/{}/repos'.format(USER_NAME)
GITCLONE_URL_FORMAT = 'https://github.com/{}/{}.git'

ret = requests.get(GITHUB_URL)
name_set = set()

if ret.status_code == 200:
    json_data = ret.json()
    
    for item in json_data:
        name_set.add(item['name'])
        url = GITCLONE_URL_FORMAT.format(USER_NAME, item['name'])
        os.system('git clone {}'.format(url))
else:
    print("can't get data from {}".format(GITHUB_URL))

# git clone would fail, so check is needed.
while True:
    needDownloadAgain = False
    directories = [d for d in os.listdir('./') if os.path.isdir(os.path.join('./', d))]

    for dirName in directories:
        if dirName not in name_set:   # re-download.
            needDownloadAgain = True
            url = GITCLONE_URL_FORMAT.format(USER_NAME, dirName)
            os.system('git clone {}'.format(url))

    if not needDownloadAgain:
        break

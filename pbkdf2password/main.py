import json
from ecampus.crawling import getSBJ_ID, login


file_path = 'db.json'
with open(file_path, 'r') as f:
    datas = json.load(f)
    for data in datas:
        if data['model'] == 'auth.user':
            print(data['fields']['password'])

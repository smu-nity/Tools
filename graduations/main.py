import json
from crawling import getSBJ_ID, login


def main(year):
    subjects = []
    file_path = f'dataset/{year}.json'
    with open(file_path, 'r') as f:
        datas = json.load(f)['dsGrdtCritCdt']
        print(datas)

main(2019)

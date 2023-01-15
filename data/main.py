import json
from crawling import getSBJ_ID, login


def dataset(year, semester):
    session = login('201911019', '1q2w3e4r!')
    subjects = []
    file_path = f'dataset/{year}_{semester}.json'
    with open(file_path, 'r') as f:
        SBJS = []
        datas = json.load(f)['dsUcsLectLsnPdoc']
        for data in datas:
            SBJ_NO = data['SBJ_NO']
            if SBJ_NO not in SBJS:
                for id in getSBJ_ID(session, 2019, 10, SBJ_NO):
                    subject = {'id': SBJ_NO, 'ecampus': id, 'name': data['SBJ_NM'], 'credit': data['CDT'], 'type': data['CMP_DIV_NM'], 'year': year, 'semester': semester}
                    print(subject)
                    subjects.append(subject)
                SBJS.append(SBJ_NO)

dataset(2019, 10)

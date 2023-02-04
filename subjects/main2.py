import json


def main(year, semester):
    file_path = f'dataset/{year}_{semester}.json'
    with open(file_path, 'r') as f:
        ESTS = []
        datas = json.load(f)['dsUcsLectLsnPdoc']
        for data in datas:
            SBJ_EST = data['EST_DEPT_INFO'].split(',')[0]
            if SBJ_EST not in ESTS:
                ESTS.append(SBJ_EST)
        print(ESTS)
        print(len(ESTS))

main(2023, 10)

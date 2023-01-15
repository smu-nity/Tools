import json

from data.ecampus import getSBJ_ID, login


def dataset(year, semester):
    file_path = f'dataset/{year}_{semester}.json'
    with open(file_path, 'r') as f:
        data = json.load(f)['dsUcsLectLsnPdoc']
        for d in data:
            print(d)


# dataset(2019, 10)
getSBJ_ID(login('201911019', '1q2w3e4r!'), 2019, 10, 'HAAE9201')
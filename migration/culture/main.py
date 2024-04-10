import os

import json


def read_json(file):
    with open(file, 'r') as file:
        return json.load(file)


def save_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)


def culture(path, domain):
    sql, insert = '', 'INSERT INTO subject_culture (sub_domain, credit, name, number)\nVALUES '
    sub_domain = domain.split('.')[0]
    datas = read_json(os.path.join(path, domain))
    for data in datas:
        name, number, credit = data['name'], data['number'], data['credit']
        sql += f"{insert}('{sub_domain}', {credit}, '{name}', '{number}');\n"
    return sql


sql = ''
dataset_path, result_file = 'json', 'sql/subject_culture.sql'
domains = datasets = os.listdir(dataset_path)

for domain in domains:
    sql += culture(dataset_path, domain)
save_file(sql, result_file)

import requests
from bs4 import BeautifulSoup as bs

import json


def read_json(file):
    with open(file, 'r') as file:
        return json.load(file)


def type2category(type):
    dic = {'1전심': 'MAJOR_ADVANCED', '1전선': 'MAJOR_OPTIONAL', '1교직': 'MAJOR_OPTIONAL'}
    if type in dic:
        return dic[type]
    else:
        return 'ETC'


def get_grade(grade):
    dic = {'1학년': 'FIRST', '2학년': 'SECOND', '3학년': 'THIRD', '4학년': 'FOURTH', '전체학년': 'ALL'}
    return dic[grade]


def get_semester(semester):
    dic = {'1학기': 'FIRST', '2학기': 'SECOND'}
    return dic[semester]


def save_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)


def major(pk, url):
    sql, insert = '', 'INSERT INTO subject_major (category, credit, grade, name, number, semester, type, department_id)\nVALUES '
    request = requests.get(url)
    source = request.text
    soup = bs(source, "html.parser")
    datas = soup.find_all('tr')[1:]
    for data in datas:
        subject = data.find_all('td')
        number, name = subject[3].text, subject[4].text.split('/')[1]
        credit, type = int(float(subject[5].text)), subject[2].text
        sql += f"{insert}('{type2category(type)}', {credit}, '{get_grade(subject[0].text)}', '{name.strip()}', '{number}', '{get_semester(subject[1].text)}', '{type}', {pk});\n"
    return sql


sql = ''
department_file, result_file = 'json/accounts_department.json', 'sql/subject_major.sql'
departments = read_json(department_file)
total = len(departments)

for i, department in enumerate(departments):
    print(f'{i + 1}/{total}')
    pk, url = department['id'], department['url']
    sql += major(pk, url)
save_file(sql, result_file)

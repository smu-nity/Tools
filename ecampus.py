import datetime
import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs


# e-campus 로그인
def login(id, password):
    user_info = {'username': id, 'password': password}
    session = requests.Session()
    request = session.post('https://ecampus.smu.ac.kr/login/index.php', data=user_info)

    # 로그인 성공
    if request.url == 'https://ecampus.smu.ac.kr/':
        return session
    return -1


# 수강한 모든 강의 이름 크롤링
def course(session, year, semester):
    url = f'https://ecampus.smu.ac.kr/local/ubion/user/?year={year}&semester={semester}'
    request = session.get(url)
    source = request.text
    soup = bs(source, 'html.parser')
    courses = soup.find_all('a', class_='coursefullname')
    courses = list(map(lambda s: name2num(s.text), courses))
    return courses


# 강의 이름을 학수번호로 변환
def name2num(course):
    return course.split('(')[-2].strip()


if __name__ == '__main__':
    load_dotenv()
    id = os.environ.get('ID')
    password = os.environ.get('PASSWORD')
    session = login(id, password)
    courses = []

    start = int(id[:4])
    end = int(datetime.datetime.today().strftime("%Y"))

    for year in range(start, end + 1):
        for semester in range(1, 3):
            for type in range(2):
                courses += course(session, year, f'{semester}{type}')
    print(courses)

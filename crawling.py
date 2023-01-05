import requests
from bs4 import BeautifulSoup as bs


# e-campus 로그인
def login(id, password):
    user_info = {"username": id, "password": password}
    session = requests.Session()
    request = session.post("https://ecampus.smu.ac.kr/login/index.php", data=user_info)

    # 로그인 성공
    if request.url == "https://ecampus.smu.ac.kr/":
        return session
    return None


# 사용자 정보 크롤링
def information(session):
    request = session.get("https://ecampus.smu.ac.kr/user/user_edit.php")
    source = request.text
    soup = bs(source, "html.parser")

    context = {
        "name": soup.find('input', id='id_firstname').get('value'),
        "department": soup.find('input', id='id_department').get('value'),
        "email": soup.find('input', id='id_email').get('value')
    }
    return context

# 학기별 과목 정보 크롤링
def subject(session, year, semester):
    url = f'https://ecampus.smu.ac.kr/local/ubion/user/?year={year}&semester={semester}0'
    request = session.get(url)
    source = request.text
    soup = bs(source, "html.parser")
    return soup.find_all('a', class_='coursefullname')

# 전체 과목 정보 크롤링
def subjects(session, start, end):
    subjects = []
    for year in range(start, end):
        for semester in range(1, 3):
            subjects += subject(session, year, semester)
    subjects = list(map(lambda x: x.text, subjects))
    return subjects


def main():
    session = login('ID', 'PASSWORD')
    data = subjects(session, 2019, 2023)
    print(data)
    print(len(data))

if __name__ == '__main__':
    main()

import requests
from django.contrib.auth.models import User
from bs4 import BeautifulSoup as bs


# 로그인
def ecampus(id, password):
    session = login(id, password)

    if session:
        return information(session)
    return None


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
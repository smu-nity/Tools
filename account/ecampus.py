import requests
from django.contrib.auth.models import User
from bs4 import BeautifulSoup as bs


# 로그인
def authenticate(id, password):
    session = login(id, password)

    if session:
        information(session)

        user = User.objects.filter(username=id)
        if user:
            return user.first()
        else:
            user = User.objects.create(username=id)
            return user
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

    print(soup.find('input', id='id_department').get('value'))
    print(soup.find('input', id='id_firstname').get('value'))
    print(soup.find('input', id='id_email').get('value'))
import requests
from bs4 import BeautifulSoup as bs


# e-campus 로그인
def login(id, password):
    user_info = {"user_id": id, "user_password": password}
    session = requests.Session()
    session.post("https://smsso.smu.ac.kr/Login.do", data=user_info)
    session.post("https://smul.smu.ac.kr/index.do")
    res = session.get("https://smul.smu.ac.kr/UsrRecMatt/list.do")
    print(res.text)
    print(res.url)

    # print(session.cookies)
    # res = session.post('https://203.237.168.35:443')
    # print(res.text)
    # print(res.url)

    # 로그인 성공
    # if request.url == "https://portal.smu.ac.kr/index.jsp":
    #     return session
    # return None


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
    url = f'https://ecampus.smu.ac.kr/local/ubion/user/?year={year}&semester={semester}'
    request = session.get(url)
    source = request.text
    soup = bs(source, "html.parser")
    return soup.find_all('a', class_='coursefullname')

# 전체 과목 정보 크롤링
def subjects(session, start, end):
    semesters = [10, 11, 20, 21]
    subjects = []
    for year in range(start, end):
        for semester in semesters:
            subjects += subject(session, year, semester)
    subjects = list(map(lambda x: changeFormat(x['href']), subjects))
    return subjects


def getSBJ_ID(session, year, semester, SBJ_NO):
    url = f'https://ecampus.smu.ac.kr/local/ubassistant/index.php?a_year={year}&a_semester={semester}&a_type=idnumber&a_keyword={SBJ_NO}'
    request = session.get(url)
    source = request.text
    soup = bs(source, "html.parser")
    return list(map(lambda x: changeFormat(x['href']), soup.find_all('a', class_='audit')))


def changeFormat(url):
    return int(url.split('id=')[1])


login('201911019', '1q2w3e4r!')

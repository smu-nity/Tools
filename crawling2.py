from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def login(id, password):
    url = "https://smsso.smu.ac.kr/svc/tk/Auth.do?ac=Y&ifa=N&id=portal&"
    driver.get(url)

    driver.find_element(By.ID, 'user_id').send_keys(id)
    driver.find_element(By.ID, 'user_password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="firstAuth"]/fieldset/ul/li[2]/button').click()
    # print(driver.page_source)

    driver.get('https://smul.smu.ac.kr/index.do')
    driver.find_elements(By.CLASS_NAME, 'cl-text')[1].click()
    driver.find_elements(By.CLASS_NAME, 'cl-text')[42].click()
    driver.find_elements(By.CLASS_NAME, 'cl-text')[43].click()

    print(driver.page_source)
    # datas = driver.find_elements(By.CLASS_NAME, 'cl-text')
    # for data in datas:
    #     print(data.text)



    # print(driver)
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    # driver.get('203.237.168.35:443')
    # driver.get('http://203.237.168.35:443/UsrRecMatt/list.do')


    while (True):
        pass

    # driver.get('https://smul.smu.ac.kr/UsrRecMatt/list.do')

if __name__ == '__main__':
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome('chromedriver')

    login("201911019", "1q2w3e4r!")


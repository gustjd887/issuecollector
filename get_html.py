# requests 모듈
import requests

# selenium 모듈
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# requests 함수
def get_requests(url, encoding=None):
    response = requests.get(url)

    # encoding을 입력으로 사용하였을 경우 respnose.encoding을 세팅
    if encoding != None:
        response.encoding = encoding
        return response.text
    # encoding 입력이 없으면 그대로 출력
    else:
        return response.text

# selenium 함수, Docker의 Selenium StandAlone 사용,
# def get_selenium(url):
#     # Headless 옵션 설정
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_argument("--no-sandbox")
#
#     # 페이지의 로딩을 끝까지 기다리지 않기 위한 옵션 설정
#     capa = DesiredCapabilities.CHROME
#     capa["pageLoadStrategy"] = "none"
#
#     driver = webdriver.Remote('http://192.168.10.2:4444/wd/hub', desired_capabilities=capa, options=options)
#     # 페이지 로딩 10초 기다림
#     wait = WebDriverWait(driver, 10)
#
#     driver.get(url)
#     # 메인 아이콘이 나올 때까지 기다렸다가 로딩 중지
#     try:
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'icon_clien')))
#         driver.execute_script("window.stop();")
#     # 로딩 중지 후 페이지 읽어옴(icon_clien이 완전히 로딩되기 전에 중지되기 때문에 에러 발생, 그래서 예외 처리에서 마무리함.)
#     except:
#         # 페이지 소스 얻기
#         html = driver.page_source
#         # selenium 사용 반환
#         driver.quit()
#         return html

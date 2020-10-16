from get_html import get_requests
from bs4 import BeautifulSoup
import datetime
from issue_postgres import IssueDB

#리눅스 os에 적용 시 주석 해제 후 코드 정렬할 것(모듈로)

url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest'  # 타겟 url, django_crontab에서 넘겨받을 갚 테스트용으로 정의해놓음
html = get_requests(url)
soup = BeautifulSoup(html, 'html.parser')
tr_area = soup.find_all('tr', {'class': 'view list_tr_humordata'})

# site = 1  # 사이트 이름 줄인 것
site = 'ou'
_url = "http://www.todayhumor.co.kr"  # 파싱하여 가져오는 url의 앞부분에 합쳐질 주소 정의

db = IssueDB()

for tr_index in tr_area:
    url = tr_index.find('td', {'class': 'subject'}).find('a')["href"]
    title = tr_index.find('td', {'class': 'subject'}).find('a').text
    reply = tr_index.find('td', {'class': 'subject'}).find('span', {'class': 'list_memo_count_span'}).text
    name = tr_index.find('td', {'class': 'name'}).find('a').text
    date = tr_index.find('td', {'class': 'date'}).text
    hit = tr_index.find('td', {'class': 'hits'}).text
    like = tr_index.find('td', {'class': 'oknok'}).text

    # DB에 맞는 형식으로 수정
    url = _url + url
    reply = reply[2:-1]
    date = "20" + date.replace('/', '-') + ":00"

    # b_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # data = (site, url, title, reply, name, date, hit, like, b_date)
    data = (site, url, title, reply, name, date, hit, like)
    db.execute(data)
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '- ou.py')
db.close()

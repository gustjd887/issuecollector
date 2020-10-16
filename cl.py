from get_html import get_requests
from bs4 import BeautifulSoup
import datetime
from issue_postgres import IssueDB

db = IssueDB()

# site = 2
site = 'cl'
url = 'https://www.clien.net/service/'  # 타겟 url, django_crontab에서 넘겨받을 갚 테스트용으로 정의해놓음
html = get_requests(url)
soup = BeautifulSoup(html, 'html.parser')

#클리앙 메인 페이지에서 각 게시판 링크를 파싱하여 리스트로 저장
url_list = []
today_links = soup.find('div', {'class': 'section_body'}).find_all('a', {'class': 'list_subject'})
for today_link in today_links:
    url_list.append('https://www.clien.net' + today_link['href'])

#클리앙 메인 페이지에서 각 게시판 링크와 reply를 파싱하여 튜플 리스트로 저장
bs4_url_list = soup.find('div', {'class': 'section_body'}).find_all('a', {'class': 'list_subject'})
bs4_reply_list = soup.find('div', {'class': 'section_body'}).find_all('span', {'class': 'rSymph05'})
bs4_url_reply_list = list(zip(bs4_url_list, bs4_reply_list))

for (url_list, reply_list) in (bs4_url_reply_list):
    try:
        url = 'https://www.clien.net' + url_list['href']
        reply = reply_list.text

        html = get_requests(url)
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h3', {'class': 'post_subject'}).find('span', {'class': None}).text
        name = soup.find('div', {'class': 'post_info'}).find('span', {'class': 'nickname'}).find('span').text
        date = soup.find('div', {'class': 'post_author'}).find('span').text[:21].strip()
        hit = soup.find('span', {'class': 'view_count'}).find('strong').text.replace(',', '')
        like = soup.find('a', {'class': 'symph_count'}).find('strong').text
        # b_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except:
        continue
    # data = (site, url, title, reply, name, date, hit, like, b_date)
    data = (site, url, title, reply, name, date, hit, like)
    db.execute(data)
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '- cl.py')
db.close()

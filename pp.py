from get_html import get_requests
from bs4 import BeautifulSoup
import datetime
from issue_postgres import IssueDB

url = 'http://ppomppu.co.kr/hot.php?category=2'  # 뽐뿌 hot 게시글 url
html = get_requests(url)
soup = BeautifulSoup(html, 'html.parser')
tr_area = soup.find_all('tr', {'class': 'line'})

db = IssueDB()

for tr_index in tr_area:
    try:
        td_subject = tr_index.find_all('a')[1]

        # site = 3
        site = 'pp'
        url = td_subject["href"]
        title = td_subject.text
        reply = tr_index.find('span', {'class': 'list_comment2'}).text
        name = tr_index.find('td', {'align': 'left'}).text
        date = tr_index.find('span', {'class': 'info_comment1'}).find_all('td')[0].text
        hit = tr_index.find('span', {'class': 'info_comment1'}).find_all('td')[2].text
        like = tr_index.find('span', {'class': 'info_comment1'}).find_all('td')[1].text

        title = title.lstrip()
        url = 'http://ppomppu.co.kr' + url
        reply = reply.lstrip()
        if date.find(':') != -1:
            date = datetime.datetime.now().strftime("%Y-%m-%d") + " " + date
        else:
            date = date.replace('/', '-')
            date = "20" + date + " " + "00:00:00"
        like = like.split(' ')[0]
        # board = Board_info(site=Site_state.objects.get(site=site), url=url, title=title, reply=reply, name=name, date=date,
        #                    hit=hit, like=like)
        # board.save()
        # b_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except:
        continue
    # data = (site, url, title, reply, name, date, hit, like, b_date)
    data = (site, url, title, reply, name, date, hit, like)
    db.execute(data)
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '- pp.py')
db.close()

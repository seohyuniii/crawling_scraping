from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd
import datetime
from datetime import timedelta


page_num=10


############################################################################### 디씨 인사이드
base_url='https://gall.dcinside.com/board/lists'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

cnt = 1
result = []
for i in range(1, page_num):
    params = {'id': 'dcbest', "page": i}
    raw = req.get(base_url, params=params, headers=headers)
    soup = bs(raw.content, 'html.parser')
    contents = soup.find('tbody').find_all('tr')
    del contents[0]

    for i in contents:
        tmp = {}
        #print('-' * 15)
        #print(cnt)
        cnt = cnt + 1
        # 제목 추출
        title_tag = i.find('a')
        title = title_tag.text
        #print("제목: ", title)

        # 날짜 추출
        date_tag = i.find('td', class_='gall_date')
        date_dict = date_tag.attrs

        if len(date_dict) == 2:
            date = date_dict['title']
            #print("날짜: ", date)
        else:
            date = date_tag.text
            #print("날짜: ", date)
            pass

        # 조회 수 추출
        # views_tag = i.find('td', class_='gall_count')
        # views = views_tag.text
        # if views == "-":
        #     views = 0
        #print("조회수: ", views)

        # 댓글수
        # comment = i.find('span', {"class": "reply_num"}).text
        # comment = comment[1:-1]
        #print("댓글수: ", comment)

        # 추천 수 추출
        recommend_tag = i.find('td', class_='gall_recommend')
        recommend = recommend_tag.text
        if recommend == "-":
            recommend = 0
        #print("추천수: ", recommend)

        tmp['제목'] = title
        tmp['날짜'] = date
        #tmp['조회수'] = views
        #tmp['댓글수'] = comment
        tmp['추천수'] = recommend

        result.append(tmp)

df = pd.DataFrame(result)
df.to_excel('data/dcinside.xlsx')
print("dc finish")
############################################################################### 클리앙

base_url='https://www.clien.net/service/board/park'
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"}

cnt = 1
result = []
for i in range(1, page_num):
    params = {'od': 'T31', "category": 0, 'po': i}
    raw = req.get(base_url, params=params, headers=headers)
    soup = bs(raw.content, 'html.parser')
    contents = soup.find('div', class_='list_content').find_all('div', class_='list_item symph_row')
    del contents[0]

    for i in contents:
        tmp = {}
        #print('-' * 15)
        #print(cnt)
        cnt = cnt + 1
        # 제목 추출
        title_tag = i.find('span', class_='subject_fixed')
        title = title_tag.text.strip()
        #print("제목: ", title)


        # 날짜 추출
        date_tag = i.find('span', class_='timestamp').text
        #print(date_tag)

        # 조회 수 추출
        views_tag = i.find('span', class_='hit')
        views = views_tag.text
        if views == "-":
            views = 0
        #print("조회수: ", views)

        # 댓글수
        if i.find('span', {"class": "rSymph05"}) != None:
            comment = i.find('span', {"class": "rSymph05"}).text
        #         comment=comment[1:-1]
        else:
            comment = str(0)
        #print("댓글수: ", comment)

        #     # 공감 수 추출
        #     recommend_tag = i.find('td', class_='gall_recommend')
        #     recommend = recommend_tag.text
        #     if recommend=="-":
        #         recommend=0
        #     print("추천수: ", recommend)

        tmp['제목'] = title
        tmp['날짜'] = date_tag
        tmp['조회수'] = views
        tmp['댓글수'] = comment
        #     tmp['추천수']=recommend

        result.append(tmp)

df = pd.DataFrame(result)
df.to_excel('data/클리앙.xlsx', encoding = 'utf-8', index = False)

print("클리앙 finish")
############################################################################### 네이트판

base_url='https://pann.nate.com/talk/c20001'
d = datetime.datetime.now()
now = d.strftime('%X')
cnt=1
result=[]
for i in range(1,page_num):
    params={'id':'dcbest',"page":i}
    raw=req.get(base_url,params=params)
    soup=bs(raw.content, 'html.parser')
    contents = soup.find_all('tr')
    del contents[0]
    href=[]
    for i in contents:
        url=i.find('td',{"class":"subject"}).find_all('a')[-1]['href']
        href.append('https://pann.nate.com'+url)
    for i in href:
        tmp={}
        #print('-'*15)
        #print(cnt)
        cnt=cnt+1

        raw=req.get(i)
        soup=bs(raw.content, 'html.parser')

        # 제목 추출
        title=soup.find('div',{"class":"post-tit-info"}).find('h4').text.strip()
        #print("제목: ", title)


        # 날짜 추출
        date=soup.find('span',{"class":"date"}).text
        if d.strftime('%d') != date[8:10]:
            date=date[:10]
        #print("날짜: ",date)

        # 조회 수 추출

        views = soup.find('span',{"class":"count"}).text.replace('조회','')
        #print("조회수: ", views)


        # 댓글 수
        comment=soup.find('span',{"class":"num"}).find('strong').text
        #print("댓글수: ", comment)

        # 추천 수 추출
        recommend = soup.find('div', class_='btnbox up').find('span',{"class":"count"}).text
        #print("추천수: ", recommend)

        tmp['제목']=title
        tmp['날짜']=date
        tmp['조회수']=views
        tmp['댓글수']=comment
        tmp['추천수']=recommend

        result.append(tmp)

df=pd.DataFrame(result)
df.to_excel('data/네이트판.xlsx')
print("네이트판 finish")

###############################################################################더쿠

dt_now = datetime.datetime.now()
today_date = dt_now.strftime('%Y.%m.%d')
base_url = 'https://theqoo.net/square?filter_mode=normal'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"}
cnt = 1
result = []
for i in range(page_num):
    params = {'mid': 'square', 'page': i + 1}
    raw = req.get(base_url, params=params, headers=headers)
    soup = bs(raw.content, 'html.parser')
    contents = soup.find('tbody', class_='hide_notice').find_all('tr')[10:]

    for i in contents:
        tmp = {}
        #print('-' * 15)
        #print(cnt)
        cnt = cnt + 1
        # 제목 추출
        title_tag = i.find('td', class_='title')
        title = title_tag.text
        #print("제목: ", title)


        # 날짜 추출 (*인벤의 경우, 전날도 '시간:분'으로 표시됨*)
        time_tag = i.find('td', class_='time')
        try:
            time = time_tag.text.split('\n')[1][:-1]
        except:
            time = time_tag.text
        if time[2] != ':':  # 시간:분 형식이 아닌경우
            time_text = time
            #print("날짜: ", dt_now.strftime('%Y.') + time_text)  # 년.월.일
        else:  # 시간:분 형식인 경우
            time_text = today_date + ' ' + time
            #print("날짜: ", today_date + ' ' + time)

        # 조회 수 추출
        views_tag = i.find('td', class_='m_no')
        views = views_tag.text
        if views_tag == None:
            views = 0
        #print("조회수: ", views)

        # 댓글수
        if i.find('a', class_='replyNum') != None:
            num_reply_tag = i.find('a', class_='replyNum')
            num_reply = int(num_reply_tag.text)
        else:
            num_reply = int(0)
        #print("댓글수: ", num_reply)

        #     # 공감 수 추출
        #     recommend_tag = i.find('td', class_='gall_recommend')
        #     recommend = recommend_tag.text
        #     if recommend=="-":
        #         recommend=0
        #     print("추천수: ", recommend)

        # 게시물 번호 추출
        num_tag = i.find('td', class_='no')
        num_text = int(num_tag.text.split('\n')[1])
        #print("게시물 번호: ", num_text)

        tmp['제목'] = title
        tmp['날짜'] = time
        #         tmp['글쓴이']= writer
        tmp['조회수'] = views
        tmp['댓글수'] = num_reply
        #     tmp['추천수']=recommend
        tmp['게시물 번호'] = num_text

        result.append(tmp)

df = pd.DataFrame(result)
df.to_excel('data/더쿠.xlsx')
print("더쿠 finish")
###############################################################################보배드림

base_url='https://www.bobaedream.co.kr/list?code=best&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&bestCode=&bestDays=&bestbbs=&vdate=&type=list&page=1'
d = datetime.datetime.now()
now = d.strftime('%X')
cnt = 1
result = []
for i in range(1, page_num):
    params = {"page": i}
    raw = req.get(base_url, params=params)
    soup = bs(raw.content, 'html.parser')
    contents = soup.find('tbody').find_all('tr')

    for i in contents:
        tmp = {}
        #print('-' * 15)
        #print(cnt)
        cnt = cnt + 1

        # 게시판 추출
        category = i.find('td', {"class": "category"}).get('title')
        #print("분야: ", category)

        # 제목 추출
        title = i.find('a', {"class": "bsubject"}).text.strip()
        #print("제목: ", title)

        # 글쓴이 추출
        writer_tag = i.find('span', {"class": "author"})
        if writer_tag is not None:  # None 값이 있으므로 조건문을 통해 회피
            writer = writer_tag.get('title')

        else:
            writer = "없음"
        #print("글쓴이: ", writer)

        # 날짜 추출
        date = i.find('td', {"class": "date"}).text
        if date.find(':') == -1:
            date = d.strftime('%Y') + '.' + date[:2] + '.' + date[3:]
        else:
            date = d.strftime('%Y.%m.%d ') + date
        #print("날짜: ", date)

        # 조회 수 추출
        views = i.find('td', {"class": "count"}).text
        #print("조회수: ", views)

        # 댓글 수
        comment = i.find('span', {"class": "Comment"})
        if comment == None:
            comment = 0
        else:
            comment = comment.find('strong', {"class": "totreply"}).text
        #print("댓글수: ", comment)

        # 추천 수 추출
        recommend = i.find('td', {"class": "recomm"}).text
        #print("추천수: ", recommend)

        tmp['분야'] = category
        tmp['제목'] = title
        tmp['글쓴이'] = writer
        tmp['날짜'] = date
        tmp['조회수'] = views
        tmp['댓글수'] = comment
        tmp['추천수'] = recommend

        result.append(tmp)
df=pd.DataFrame(result)
df.to_excel('data/보배드림_수능2.xlsx')
print("보배드림 finish")
###############################################################################불펜

base_url='http://mlbpark.donga.com/mp/b.php?p=1&m=list&b=bullpen&query=&select=&user='
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
d = datetime.datetime.now()
now = d.strftime('%X')
cnt = 1
result = []
for i in range(page_num):
    params = {"p": i * 30 + 1}
    raw = req.get(base_url, params=params, headers=headers)
    soup = bs(raw.content, 'html.parser')
    contents = soup.find('tbody').find_all('tr')
    del contents[0:5]

    for i in contents:
        tmp = {}
        #print('-' * 15)
        #print(cnt)
        cnt = cnt + 1

        # 분야 추출
        category = i.find('a', {"class": "list_word"}).text
        #print("분야: ", category)

        # 제목 추출
        title = i.find('a', {"class": "txt"}).text.strip()
        #print("제목: ", title)

        # 글쓴이 추출
        writer_tag = i.find('span', class_='nick')
        if writer_tag is not None:  # None 값이 있으므로 조건문을 통해 회피
            writer = writer_tag.text

        else:
            writer = "없음"
        #print("글쓴이: ", writer)

        #    # 유동이나 고닉이 아닌 글쓴이 옆에 있는 ip 추출
        #    ip_tag = i.find('td', class_='gall_writer ub-writer').find('span', class_='ip')
        #    if ip_tag is not None:  # None 값이 있으므로 조건문을 통해 회피
        #        ip = ip_tag.text
        #        print("ip: ", ip)

        # 날짜 추출
        date = i.find('span', {"class": "date"}).text
        if len(date) <= 8:
            if int(date[:2]) > int(now[:2]):
                # 어제 날짜 & (시간)
                a = d - timedelta(days=1)
                date = a.strftime('%Y.%m.%d ')  # +date[:-3]
            else:
                # 오늘 날짜 & 시간
                date = d.strftime('%Y.%m.%d ') + date[:-3]
        else:
            date = date[:4] + '.' + date[5:7] + '.' + date[8:]
        #print("날짜: ", date)

        # 조회 수 추출
        views = i.find('span', {"class": "viewV"}).text
        #print("조회수: ", views)

        # 댓글 수
        comment = i.find('span', {"class": "replycnt"})
        if comment == None:
            comment = 0
        else:
            comment = comment.text
            comment = comment[1:len(comment) - 1]
        #print("댓글수: ", comment)

        # 추천 수 추출
        #    recommend = i.find_all('td')[-2].text
        #    if recommend == "":
        #        recommend=0
        #    else:
        #        recommend=recommend.split('-')[0].strip()
        #    print("추천수: ", recommend)

        tmp['분야'] = category
        tmp['제목'] = title
        tmp['글쓴이'] = writer
        tmp['날짜'] = date
        tmp['조회수'] = views
        tmp['댓글수'] = comment
        #    tmp['추천수']=recommend

        result.append(tmp)
df=pd.DataFrame(result)
df.to_excel('data/bullpen.xlsx')
print("불펜 finish")
###############################################################################뽐뿌

base_url='https://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard&page=1&divpage=1426'
d = datetime.datetime.now()
now = d.strftime('%X')
cnt = 1
result = []
for i in range(1, page_num):
    params = {"page": i}
    raw = req.get(base_url, params=params)
    soup = bs(raw.content, 'html.parser')
    contents = soup.find_all('tr', {"class": ["list1", "list0"]})

    for i in contents:
        tmp = {}
        #print('-' * 15)
        #print(cnt)
        cnt = cnt + 1

        # 제목 추출
        title = i.find('font', {"class": "list_title"}).text.strip()
        #print("제목: ", title)


        # 날짜 추출
        date = i.find('nobr', {"class": "eng list_vspace"}).text
        if date.find(':') == -1:
            date = '20' + date[:2] + '.' + date[3:5] + '.' + date[6:]
        else:
            date = d.strftime('%Y.%m.%d ') + date[:-3]
        #print("날짜: ", date)

        # 조회 수 추출

        views = i.find_all('td')[-1].text
        #print("조회수: ", views)

        # 댓글 수
        comment = i.find('span', {"class": "list_comment2"})
        if comment == None:
            comment = 0
        else:
            comment = comment.text
        #print("댓글수: ", comment)

        # 추천 수 추출
        recommend = i.find_all('td')[-2].text
        if recommend == "":
            recommend = 0
        else:
            recommend = recommend.split('-')[0].strip()
        #print("추천수: ", recommend)

        tmp['제목'] = title
        tmp['날짜'] = date
        tmp['조회수'] = views
        tmp['댓글수'] = comment
        tmp['추천수'] = recommend

        result.append(tmp)
df=pd.DataFrame(result)
df.to_excel('data/뽐뿌.xlsx')
print("뽐뿌 finish")
###############################################################################인스티즈

base_url='https://www.instiz.net/pt?page=1'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
d = datetime.datetime.now()
now = d.strftime('%X')
cnt = 1
result = []
for i in range(1, page_num):
    params = {"page": i}
    raw = req.get(base_url, params=params, headers=headers)
    soup = bs(raw.content, 'html.parser')
    contents = soup.find_all('tr')
    del contents[:20]
    del contents[19:len(contents)]

    for i in contents:
        tmp = {}
        #print('-' * 15)
        #print(cnt)
        cnt = cnt + 1

        # 제목 추출
        title = i.find('span', {"id": "subject"}).text.strip()
        #print("제목: ", title)

        # 글쓴이 추출
        writer_tag = i.find('td', {"class": "minitext2 listnm"})
        if writer_tag is not None:  # None 값이 있으므로 조건문을 통해 회피
            writer = writer_tag.text

        else:
            writer = "없음"
        #print("글쓴이: ", writer)

        #     # 유동이나 고닉이 아닌 글쓴이 옆에 있는 ip 추출
        #     ip_tag = i.find('td', class_='gall_writer ub-writer').find('span', class_='ip')
        #     if ip_tag is not None:  # None 값이 있으므로 조건문을 통해 회피
        #         ip = ip_tag.text
        #         print("ip: ", ip)

        # 날짜 추출
        date = i.find('td', {"class": "listno regdate"}).text
        if len(date) <= 5:
            if len(date) <= 4:
                date = d.strftime('%Y.%m.%d ') + '0' + date
            else:
                date = d.strftime('%Y.%m.%d ') + date
        else:
            date = d.strftime('%Y') + '.' + date[:5]
        #print("날짜: ", date)

        # 조회 수 추출
        views = i.find_all('td', {"class": "listno"})[2].text
        #print("조회수: ", views)

        # 댓글 수
        comment = i.find('a', {"id": "view_cmt"})
        if comment == None:
            comment = 0
        else:
            comment = comment.text
        #print("댓글수: ", comment)

        # 추천 수 추출
        recommend = i.find_all('td', {"class": "listno"})[3].text
        #print("추천수: ", recommend)

        tmp['제목'] = title
        tmp['글쓴이'] = writer
        tmp['날짜'] = date
        tmp['조회수'] = views
        tmp['댓글수'] = comment
        tmp['추천수'] = recommend

        result.append(tmp)
df=pd.DataFrame(result)
df.to_excel('data/instiz.xlsx')
print("인스티즈 finish")

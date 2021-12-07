from bs4 import BeautifulSoup as bs
import re

course = './courses/react.html'

with open (course,encoding='utf8') as html_file:
    c = html_file.read()
    # print(c)

    soup = bs(c,'lxml')
    times = soup.find_all('span', class_='c-course-curriculum__lesson-duration')
    seconds=[]
    minutes = []
    count_s = 0
    count_m = 0
    for time in times:
        time = re.search(r'(\d+)m (\d+)s', time.text)
        second = int(time.group(2))
        minute = int(time.group(1))
        count_s += second 
        count_m += minute

total = (count_s // 60 + count_m)/60

names = soup.find_all('span', class_='c-course-curriculum__lesson-name')
name_list=[]

for name in names:
    name = name.text
    print(name)

n_classes = len(times)
print(f"Aulas^^^\nnumero de aulas: {n_classes}\ntempo total: {total} horas")


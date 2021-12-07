from bs4 import BeautifulSoup as bs
import re

# Pergunta

chapter_index = input ('Qual capítulo você quer?')

chapter_index = int(chapter_index) - 1



# Web Scraping 

with open ('react.html',encoding='utf8') as html_file:
    content = html_file.read()

    soup = bs(content,'lxml')
    chapters = soup.find_all('li', class_='c-course-curriculum__chapter')

    selected_chapter = chapters[chapter_index]

    chapter_name = selected_chapter.find('h3', class_='c-course-curriculum__chapter-name').text
    
    classes = selected_chapter.find_all('span', class_='c-course-curriculum__lesson-name')
    name_list=[]

    times = selected_chapter.find_all('span', class_='c-course-curriculum__lesson-duration')

# Cálculo de tempo

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

# Número de aulas

n_classes = len(times)

# Tempo total 

total_minutes = count_s // 60 + count_m

hours = total_minutes // 60
and_minutes = total_minutes % 60

# print condicionado

if total_minutes < 60:

    print (f"Capítulo: {chapter_name}\nTempo: {total_minutes} minutos\nNúmero de aulas: {n_classes}\nAulas:")

else: 
    print (f"Capítulo: {chapter_name}\nTempo: {hours} horas e {and_minutes} minutos\nNúmero de aulas: {n_classes}\nAulas:")

# Print de todas as aulas

for lesson in classes:
    lesson = lesson.text
    print(lesson)
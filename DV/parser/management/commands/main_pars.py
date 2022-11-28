
import requests
from bs4 import BeautifulSoup
# from pytrends.exceptions import ResponseError
# import lxml
# import  json
# import  csv
# import time
import requests
xe=[]
from django.core.management.base import BaseCommand
from parser.models import Institutes,timetable
def start1(values):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '284d116cec806918b414484c9507d383=e2dijndm69fe2mpdrdm9liks13; SL_G_WPT_TO=ru; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
        'Origin': 'https://www.dvgups.ru',
        'Referer': 'https://www.dvgups.ru/index.php?Itemid=1247&option=com_timetable&view=newtimetable',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    params = {
        'Itemid': '1247',
        'option': 'com_timetable',
        'view': 'newtimetable',
    }


    data = {
        'Time': '05.12.2022',
        'FacID': values,
    }

    response = requests.post('https://www.dvgups.ru/index.php', params=params, headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'lxml')
    find_group=soup.find_all('option')
    product_info = []
    product_info1 = []
    for option in find_group[1:]:
     g=[]
     g1 = []
     # print( option.text,option.get('value'))
     a1=option.text
     a2=option.get('value')
     try:
         p = Institutes.objects.get(id_group=a2)
         # p.number_Institute = values,
         # p.id_group = a2,
         # p.save()
     except Institutes.DoesNotExist:
      p = Institutes(
             number_Institute=values,
             group=a1[4:12],
             id_group=a2,
      ).save()
     product_info1.append(a1)
     product_info1.append(a2)

     # product_info.append(
     #     {
     #         "group": a1,
     #         "values": a2,
     #
     #     }
     # )
     # print(product_info)
     # with open(f"{values}-Instituted.csv",'a') as f:
     #     writer=csv.writer(f)
     #     writer.writerow(
     #         (
     #         a1,
     #         a2
     #     )
     # )
    # for i in product_info:
    #     print(i)
    # print(f'1-{product_info}')
    # print(product_info1)

    # b = get_GROUP(product_info1)

    return  product_info1

def get_GROUP(*v):
        print('введите группу') # БО911пми О-должна  быть  буквой ,а не ноль
        print(v)
        find_group=input().upper()
        c = find_group[2]
        #  на сайте ЕНИ -8, а вообще 9  пример:Б0921ПРИ  ('FacID': 8),
        b = ''
        if c == '9':
            b += '8'
        else:
            b+=c
        # это нужно потом
        print(v)
        misto=''
        id=''
        for group  in v:
            print(group)
            # print(len(group))
            # print(group[::2])
            for count,i in enumerate(group[::2]):
                # print(i)
                # print(count)
                if (i[4:12])==find_group:
                    # print(i[4:12])
                    misto+=str(count)
                    # print(count)

            for i ,count in enumerate(group[1::2]):
                if misto==str(i):
                    print(count)
                    id+=str(count)


        # id = parser_response(id)
        #проверка
        # try:
        #     p=Institutes.objects.get(group=find_group)
        #     p.number_Institute = b,
        #     p.id_group = id,
        #     p.save()
        # except Institutes.DoesNotExist:
        #   p=Institutes(
        #     number_Institute=b,
        #     group=find_group,
        #     id_group=id,
        #   ).save()
        # print(p)
        xe.append(id)
        return id

def parser_response(id):
    print(id)
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '284d116cec806918b414484c9507d383=e2dijndm69fe2mpdrdm9liks13; SL_G_WPT_TO=ru; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
        'Origin': 'https://www.dvgups.ru',
        'Referer': 'https://www.dvgups.ru/index.php?Itemid=1247&option=com_timetable&view=newtimetable',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    params = {
        'Itemid': '1247',
        'option': 'com_timetable',
        'view': 'newtimetable',
    }
    data = {

         'GroupID': id
    }
    response = requests.post('https://www.dvgups.ru/index.php', params=params, headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup
def parser_baza(c):
    number_weekday = []
    weekday = []
    week = c.find_all('h3')
    for i in week:
        s = i.text.split(" ")
        number_weekday.append(s[0])
        weekday.append(s[1])
    sdsd = c.findAll(class_='table table-hover table-bordered')
    m = 0
    n=0
    print(xe)
    for i in sdsd:
        paras = i.findAll(class_='d-flex')
        for y in paras:
            n+=1
    for i in sdsd:
        paras = i.findAll(class_='d-flex')
        for y in paras:
            k = y.find(class_='col-2').text
            para = (k[:8])
            time = (k[8:])
            h = y.find(class_='col-sm-2').text
            s = y.find(class_='col-4').text
            s = s.split("FreeConferenceCall")[0]
            s = s.split("Discord")[0]
            s = s.split("FCC")[0]
            s = s.split("Zoom")[0]
            s = s.split("Контакты преподавателей")[0]
            teacher = y.text.split()[-1]
            lin=Institutes.objects.get(id_group = xe[0])
            print(lin)
            try:
             hm = timetable.objects.get(idd=xe[0],day_week=weekday[m], time=time,number_week=number_weekday[m],lesson_score=para,cabinet=h,object=s,teacher=teacher)


            except timetable.DoesNotExist:
             hm = timetable(
                    number_week=number_weekday[m],
                    day_week=weekday[m],
                    lesson_score=para,
                    time=time,
                    cabinet=h,
                    object=s,
                    teacher=teacher,
                    idd=Institutes.objects.get(id_group = xe[0])
             ).save()
             print(h)
            # except timetable.MultipleObjectsReturned:
            #    print('база полная ')
            # print(p)
            # print(p)
        m += 1
        # print('ок')
        # print(m)

class Command(BaseCommand):

    def handle(self, *args, **options):
        Institute = {1: "Институт тяги и подвижного состава", 2: "Институт управления",
                     3: 'автоматизации и телекоммуникаций', 4: 'Институт экономики',
                     5: 'Институт транспортного строительства', 6: 'Факультет воздушных сообщений',
                     7: 'Социально-гуманитарный институт', 8: 'ЕНИ', 9: 'Институт международного сотрудничества'}
        for key, value in Institute.items():
            print(key, value)
        values = input()
        a = start1(values)
        b = get_GROUP(a)
        c = parser_response(b)
        parser_baza(c)

import requests
import csv
from bs4 import BeautifulSoup
import time
from datetime import datetime
from fake_useragent import UserAgent


ALL_NEED_URL_FROM_CATEGORY={
    'аренда квартир':'https://www.avito.ru/amurskaya_oblast/kvartiry/sdam-ASgBAgICAUSSA8gQ?cd=1',
    'аренда домов':'https://www.avito.ru/amurskaya_oblast/doma_dachi_kottedzhi/sdam-ASgBAgICAUSUA9IQ',
    'продажа квартир':'https://www.avito.ru/amurskaya_oblast/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1',
    'продажа домов':'https://www.avito.ru/amurskaya_oblast/doma_dachi_kottedzhi/prodam-ASgBAgICAUSUA9AQ?cd=1'
}
HEADERS={'User-Agent': UserAgent().chrome}
HOST='https://www.avito.ru'
FILE='price.csv'
Month= {'января':1,'февраля':2,'марта':3,'апреля':4,'мая':5,'июня':6,'июля':7,'августа':8,'сентября':9,'октября':10,'ноября':11,'декабря':12}
TYPES_OF_HOME=['квартира','cтудия', 'дом','коттедж','дача']
flag_break_from_url=False
DISTRICT={'Архара':'Архаринский',
          'Белогорск':'Белогорский',
          'Благовещенск':'Благовещенский',
          'Новобурейский':'Бурейский',
          'Завитинск':'Завитинский',
          'Зея':'Зейский',
          'Ивановка':'Ивановский',
          'Константиновка':'Константиновский',
          'Магдагачи':'Магдагачинский',
          'Новокиевский Увал':'Мазановский',
          'Поярково':'Михайловский',
          'Екатеринославка':'Октябрьский',
          'Ромны':'Ромненский',
          'Экимчан':'Селемджинский',
          'Серышево':'Серышевский',
          'Сковородино':'Сковородинский',
          'Тамбовка':'Тамбовский',
          'Тында':'Тындинский',
          'Шимановск':'Шимановский',
          'Свободный':'Свободненский',
          'Райчихинск':'Райчихинск', #тут кончились районы
          'Циолковский':'ЗАТО Циолковский',
          'Прогресс':'г.о. Прогресс',
          'Бурея': 'Бурейский'
          }
G_O_= {'г.о. Прогресс':'Прогресс',
       'г.о. Райчихинск':'Райчихинск',
       'г.о. Город Зея':'Зейский',
       'г.о. Благовещенск':'Благовещенский',
       'г.о. Циолковский':'Циолковский'
       }
CITY_ENG={
        'belogorsk': 'Белогорск',
        'blagoveschensk': 'Благовещенск',
        'zavitinsk': 'Завитинск',
        'zeya': 'Зея',
        'raychihinsk': 'Райчихинск',
        'svobodnyy': 'Свободный',
        'skovorodino': 'Сковородино',
        'tynda': 'Тында',
        'ciolkovskij': 'Циолковский',
        'shimanovsk': 'Шимановск',
        'arhara':'Архара',
        'progress':'Прогресс',
        'novobureyskiy':'Новобурейский',
        'tambovka':'Тамбовка',
        'ekaterinoslavka':'Екатеринославка'
}
VILLAGE_BELONGS={
    'Благовещенск':['Белогорье','Мухинка','Белогорье','Призейская','Плодопитомник','Садовое','Чигири'],
    'Белогорск':['Низинное'],
    'Зея':['Широкий','Угольное','Зельвино'],
    'Прогресс':['Кивдинский'],
    'Завитинск':['Новоалексеевка','Червоная Армия',' Тур'],
    'Архара':['Бон','Журавли'],
    'Новобурейский':['Николаевка']
}

def csv_dict_reader(path,delimiter=',',code='utf-8'): #?????? ?? csv ????a
    with open(path, encoding=code) as file_obj:
        reader = list(csv.DictReader(file_obj, delimiter=delimiter))
    return reader

def writer_str_csv(data,path,type='w'): #?????? ? csv ????
    with open(path,type, encoding='utf-8',newline='') as file:
        columns=data[0].keys()
        writer=csv.DictWriter(file,fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)
    return

def get_html(url, header=None, params=None):
    if header is None:
        header = HEADERS
    while True:
        try:
            r=requests.get(url, headers=header, params=params)
            if r.status_code!=200:
                print(r.status_code)
                time.sleep(1)
                continue
            return r
        except requests.exceptions.ConnectionError:
            print('Connection Error')

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination=soup.find_all('span', class_='pagination-item-1WyVp')
    if pagination:
        return int(pagination[-2].get_text())
    else:
        return 1

def get_last_link_ad(html):
    pass

def read_from_txt(file):
    file=open(file,'r',encoding='utf-8')
    lines=file.readlines()
    lines=[line.rstrip('\n') for line in lines]
    file.close()
    return lines

def check_type_of_home(str):
    str=str.lower()
    for type_of_home in TYPES_OF_HOME:
        if type_of_home in str:
            return type_of_home
        else:
            return 'нет'

def writer_txt(feature,file_name,type='w'): #?????? ? ?????? ? ????????? ????
    with open(file_name,type, encoding='utf-8',newline='') as file:
        file.write(str(feature)+'\n')
    return

def get_district_from_village(village):
    village=village.replace('пос.','').replace('с.','').replace('село','').strip()
    for city in VILLAGE_BELONGS.keys():
        for inner_village in VILLAGE_BELONGS[city]:
            if inner_village in village:
                return {'Район':DISTRICT[city]}

def unification_address_with_population(address):
    population=csv_dict_reader('population_data.csv')
    split_address={}
    flag_break=False
    for vilage in population:
        split_address_from_line=address.split(',')

        address_vilage=vilage['Населёный пункт'].replace('г. ','').replace('г.','').replace('пгт ','').replace('село ','').replace('поселок ','').replace('посёлок ','').replace('железнодорожная станция ','')
        address_vilage=address_vilage.replace('железнодорожный блок-пост ','').replace('железнодорожный разъезд ','').replace('железнодорожный блок-пост ','').replace('населённый пункт Блок-Пост ','')

        for address_ad in split_address_from_line:
            if address_vilage in address_ad and not address_vilage+'ий' in address_ad:

                split_address['Область']=vilage['Область']

                split_address['Район']=vilage['Регион']

                split_address['Пункт населения(Город, село и т.д.)']=vilage['Населёный пункт']

                flag_break=True
                break
        if flag_break:
            break
    return split_address

def get_split_address_from_url(url,district):
    address={'Пункт населения(Город, село и т.д.)':'нет',
             'Район':district}
    for city in CITY_ENG.keys():
        if city in url:
            address['city']=CITY_ENG[city]
            if district =='нет':
                address['Район']=DISTRICT[CITY_ENG[city]]
            return address
    return address

def get_split_address(address,url,show_d=False):
    list_address={
        'Улица':'нет',
        'Номер дома':'нет'
    }
    address=address.split(',')
    try:
        for current_address in address:
            current_address = current_address.strip().strip()
            if 'область' in current_address:
                continue
            elif ('р-н' in current_address) or ('район' in current_address) or ('р-н' in current_address):
                continue
            elif current_address in DISTRICT.keys():
                continue
            elif current_address in G_O_:
                continue
            elif ('ул.' in current_address) or ('ш.' in current_address) or ('пр-т' in current_address) or (
                            'шоссе' in current_address) or ('улица' in current_address) or (
                                 'ул ' in current_address) or (' ул' in current_address) or (
                                 'пер.' in current_address) or (' пер' in current_address) or (
                                 'б-р' in current_address) or (' лет ' in current_address):
                list_address['Улица'] = current_address
                continue
            elif ('пос.' in current_address) or ('с.' in current_address) or ('село' in current_address):
                continue

            else:
                list_address['Номер дома'] = current_address
                continue
    except:
        print(address)
    return list_address

def filling_empty_features(features):
    need_features=read_from_txt('features.txt')
    for need_feature in need_features:
        if need_feature in features.keys():
            continue
        else:
            features[need_feature]='нет'
    return features

def get_content(html,category,pages_count,page_count):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item_table-wrapper')
    count_ad = int(soup.find('span', class_='page-title-count-1oJOc').text.replace(' ', ''))
    last_viewed=read_from_txt(str(category)+'.txt')
    data=[]
    for index, item in enumerate(items):
        features={}
        if ((pages_count - 1) * page_count + index) >= count_ad:
            break
        print('Проход по объявлениям: ', index + 1, ' из ', count_ad, '(', len(items), ')')
        try:
            link = HOST + item.find('a', class_='snippet-link').get('href')
        except:
            link = 'нет'
        features['Ссылка на объявление'] = link
        if link in last_viewed:
            global flag_break_from_url
            flag_break_from_url = True
            break
        try:
            title = item.find('div', class_='snippet-title-row').find('a', class_='snippet-link').text.strip()
        except:
            title = 'нет'
        features['Название'] = title
        features['Вид объекта'] = check_type_of_home(title).title()
        try:
            online_view = item.find('div', class_='snippet-title-row').find('span', class_='snippet-tag').text.strip()
            online_view = 'Да'
        except:
            online_view = 'Нет'
        features['Возможность онлайн просмотра'] = online_view
        try:
            date_all = item.find('div', class_='snippet-date-info').get('data-tooltip').strip().split(' ')
            if date_all == ['']:
                date_all = item.find('div', class_='snippet-date-info').text.strip().split(' ')
            date = date_all[0] + '.' + str(Month[date_all[1]]) + '.' + str(datetime.now().year)
        except:
            date = 'нет'
        features['Дата размещения'] = date
        try:
            price_and_rent = item.find('div', class_='snippet-price-row').text.strip().split('₽')
            if (price_and_rent[1]) == '':
                type_ad = 'продажа'
            else:
                type_ad = price_and_rent[1].strip().split('\n')[0].strip()
            price = price_and_rent[0].strip()
        except:
            price = 'нет'
            type_ad = 'нет'
        features['Цена'] = price
        features['Вид'] = type_ad
        data.append(features)
    return data

def get_inner_content(url):
    html=get_html(url)
    soup = BeautifulSoup(html.text,'html.parser')
    try:
        views=soup.find('div', class_='title-info-metadata-views').text.rstrip().split('(+')
        views=int(views[0])+int(views[1].replace(')', ''))
        views=str(views)
    except:
        views='нет'
    try:
        id_ad=soup.find('div',class_='item-view-search-info-redesign').find('span').text.replace('№','').strip()
    except:
        id_ad='нет'
    try:
        link_seller = HOST + soup.find('div', class_='seller-info-name js-seller-info-name').find('a').get('href')
    except:
        link_seller = 'нет'
    try:
        spans_of_secondary=soup.find('div', class_='item-navigation').find('div',class_='breadcrumbs').find_all('span')
        secondary='нет'
        for span_of_secondary in spans_of_secondary:
            if 'Вторичка' in span_of_secondary.text:
                secondary='Вторичка'
            elif 'Новостройки' in span_of_secondary.text:
                secondary='Первичка'
    except:
        secondary = 'нет'
        print('Ошибка при получении свойства первичка/вторичка')
    try:
        name_seller=soup.find('div',class_='seller-info-name js-seller-info-name').text.strip()
    except:
        name_seller='нет'
    try:
        address_inner=soup.find('span',class_='item-address__string').text.strip()
        split_address=unification_address_with_population(address_inner)
        split_address.update(get_split_address(address_inner,url))
    except Exception as e:
        print(e.__class__)
        address_inner='нет'
        split_address={'Область': 'нет',
            'Район': 'нет',
            'Пункт населения(Город, село и т.д.)': 'нет',
            'Улица': 'нет',
            'Номер дома': 'нет'}
    propertys=soup.find_all('li',class_='item-params-list-item')
    features={}
    for feature in propertys:
        try:
            params=feature.text.strip().split(': ')
            name_feature=params[0].strip()
            value_feature=params[1].strip()
            if name_feature=='Площадь дома':
                name_feature='Общая площадь'
            if name_feature=='Тип дома':
                name_feature='Материал стен'
            if name_feature=='Этаж':
                value_feature=value_feature.split(' из ')
                features['Этажей в доме']=value_feature[1].strip()
                features[name_feature]=value_feature[0].strip()
                continue
            features[name_feature]=value_feature.rstrip('\xa0м²').rstrip('\xa0км').rstrip('сот.').rstrip(' м²').rstrip('\xa0сот.').rstrip('\xa0сот.').replace('.',',')

        except:
            continue
    features['Просмотров']=views
    features['id_ad']=id_ad
    features['Имя продовца']=name_seller
    features['Ссылка на прдовца']=link_seller
    features['Адрес Полный']=address_inner
    features['Первичка/Вторичка']=secondary
    features.update(split_address)
    return features

def check_from_writer(curret_ad):
    clear_data_of_ads = csv_dict_reader('unification_data.csv')
    for saved_ad in clear_data_of_ads:
        if curret_ad['Ссылка на объявление']==saved_ad['Ссылка на объявление']:
            print('проверка1')
            return False
        if curret_ad['Цена'] == saved_ad['Цена']  and curret_ad['Этажей в доме']==saved_ad['Этажей в доме'] and curret_ad['Этаж']==saved_ad['Этаж'] and curret_ad['Общая площадь'] != saved_ad['Общая площадь'] and curret_ad['Адрес Полный']==saved_ad['Адрес Полный']:
            print('проверка2')
            writer_str_csv(curret_ad,'ban_if_similar_ads.csv','a')
            return False
    return True

def parse(category):
    data=[]
    global flag_break_from_url
    flag_break_from_url = False
    url=ALL_NEED_URL_FROM_CATEGORY[category]
    html=get_html(url)
    data=[]
    if html.status_code==200:
        pages_count=get_pages_count(html.text)
        for page in range(1,pages_count+1):
            print(f'Парсинг страницы {page} из {pages_count}')
            html=get_html(url, params={'p':page})
            data+=get_content(html.text,category,pages_count,page)
            time.sleep(1)
            if  flag_break_from_url:
                break
        if data==[]:
            return
        # writer_txt('', str(category) + '.txt')
        for line in data:
            # writer_txt(line['Ссылка на объявление'], str(category) + '.txt', 'a')
            line.update(get_inner_content(line['Ссылка на объявление']))
            line = filling_empty_features(line)
            if check_from_writer(line):
                print('Чекнулась')
                writer_str_csv(line,'new_data.csv','a')
            time.sleep(1)
    else:
        print('Не удалось получить html')

if __name__ == "__main__":
    while True:
        for category in ALL_NEED_URL_FROM_CATEGORY.keys():
            print(category.upper())
            parse(category)

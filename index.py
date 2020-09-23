import re
import requests
import csv
from bs4 import BeautifulSoup
import time
from datetime import datetime
from fake_useragent import UserAgent
import pymysql
from random import randint
from time import sleep

connection = pymysql.connect(
    host="localhost",
    user="vladimir",
    password="_Lbvf_82461973",
    db="avito_db",
    database="avito_db",
    port=3306
)
ALL_NEED_URL_FROM_CATEGORY={
    'аренда домов': 'https://www.avito.ru/amurskaya_oblast/doma_dachi_kottedzhi/sdam-ASgBAgICAUSUA9IQ',

    'аренда квартир': 'https://www.avito.ru/amurskaya_oblast/kvartiry/sdam-ASgBAgICAUSSA8gQ?cd=1',

    'продажа квартир': 'https://www.avito.ru/amurskaya_oblast/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1',
    'продажа домов':'https://www.avito.ru/amurskaya_oblast/doma_dachi_kottedzhi/prodam-ASgBAgICAUSUA9AQ?cd=1'
}
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 YaBrowser/20.7.2.115 Yowser/2.5 Safari/537.36',
	'accept': '*/*'}

HOST='https://www.avito.ru'
FILE='price.csv'
Month= {'января':1,'февраля':2,'марта':3,'апреля':4,'мая':5,'июня':6,'июля':7,'августа':8,'сентября':9,'октября':10,'ноября':11,'декабря':12}
TYPES_OF_HOME=['квартира','cтудия', 'дом','коттедж','дача','студия','своб. планировка']
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
# district_read_from_db={}
# lacality_read_from_db={}
# property_read_from_db={}
# species_read_from_db={}
# material_read_from_db={}
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
                sleep(randint(3,6))
                continue
            sleep(randint(3,6))
            return r
        except requests.exceptions.ConnectionError:
            print('Connection Error')
        sleep(randint(3,6))

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
    global population
    split_address={}
    flag_break=False
    split_address_from_line = address.split(',')
    first_district = 'нет'
    second_district = 'нет'
    split_address['Область'] = 'Амурская обл.'
    for vilage in population:

        lacality=vilage['Населёный пункт'].replace('г. ','').replace('г.','').replace('пгт ','').replace('село ','').replace('поселок ','').replace('посёлок ','').replace('железнодорожная станция ','')
        lacality=lacality.replace('железнодорожный блок-пост ','').replace('железнодорожный разъезд ','').replace('железнодорожный блок-пост ','').replace('населённый пункт Блок-Пост ','').rstrip().rstrip()
        district = vilage['Регион'].replace('Городской округ пгт ', '').replace('Городской округ г.','').rstrip().rstrip()

        for address_ad in split_address_from_line:
            # if re.search(r''+lacality+'\b',address_ad):
            #     split_address['Пункт населения(Город, село и т.д.)']=vilage['Населёный пункт']

            if lacality+' ' in address_ad+' ' and\
                    not lacality+'ий' in address_ad and\
                    not 'ул.' in address_ad and\
                    not 'ш.' in address_ad and\
                    not 'переулок' in address_ad and\
                    not 'пер.' in address_ad and\
                    not 'улица' in address_ad:
            # if re.search(r''+lacality.lower()+'\b',address_ad.lower()):

                # split_address['Область']=vilage['Область']

                # split_address['Район']=vilage['Регион']
                first_district = vilage['Регион']
                split_address['Пункт населения(Город, село и т.д.)']=vilage['Населёный пункт']

            if district in address_ad:
                second_district=vilage['Регион']
                # flag_break=True
                # break
        # if flag_break:
        #     break
        if second_district=='нет':
            split_address['Район']=first_district
        elif second_district!=first_district:
            split_address['Район']=second_district
        else:
            split_address['Район']=first_district
    # print(split_address)
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

def get_content(html,pages_count,page_count,category=''):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item_table-wrapper')
    try:
        count_ad = int(soup.find('span', class_='page-title-count-1oJOc').text.replace(' ', ''))
    except:
        print('Ошибка при получение количество объявлений на странице')
        return []
    if category=='':
        last_viewed=[]
    else:
        last_viewed=read_from_txt(str(category)+'.txt')
    data=[]
    for index, item in enumerate(items):
        features={}
        if pages_count==page_count and ((pages_count - 1) * 50 + index) >= count_ad:
        # if ((pages_count - 1) * page_count + index) >= count_ad:
            print('Проверка на количество страниц сраотатла')
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
            online_view=0
            online_view = item.find('div', class_='snippet-title-row').find('span', class_='snippet-tag').text.strip()
            online_view = 1
        except:
            online_view = 0
        features['Возможность онлайн просмотра'] = online_view
        try:
            date_all = item.find('div', class_='snippet-date-info').get('data-tooltip').strip().split(' ')
            if date_all == ['']:
                date_all = item.find('div', class_='snippet-date-info').text.strip().split(' ')
            date =str(datetime.now().year) + '.' + str(Month[date_all[1]]) + '.' +  date_all[0]
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
            price = 0
            type_ad = 'нет'
        features['Цена'] = int(price.replace(" ",'').replace(" ",'').replace(" ",'').replace(" ",'').replace(" ",'').replace(" ",'').replace(" ",''))
        features['Вид'] = type_ad
        data.append(features)
    return data

def get_inner_content(url):
    html=get_html(url)
    soup = BeautifulSoup(html.text,'html.parser')
    try:
        views=soup.find('div', class_='title-info-metadata-views').text.rstrip().split('(+')
        views=int(views[0])+int(views[1].replace(')', ''))
    except:
        views=0
    try:
        id_ad=soup.find('div',class_='item-view-search-info-redesign').find('span').text.replace('№','').strip()
        id_ad=int(id_ad)
    except:
        id_ad=0
    try:
        link_seller = HOST + soup.find('div', class_='seller-info-name js-seller-info-name').find('a').get('href')
    except:
        link_seller = 'нет'

    secondary = 0
    try:
        spans_of_secondary=soup.find('div', class_='item-navigation').find('div',class_='breadcrumbs').find_all('span')
        for span_of_secondary in spans_of_secondary:
            if 'Новостройки' in span_of_secondary.text:
                secondary=1
                continue
    except:
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
        split_address = {'Область': 'нет',
                         'Район': 'нет',
                         'Пункт населения(Город, село и т.д.)': 'нет',
                         'Улица': 'нет',
                         'Номер дома': 'нет'}
        print(e.__class__)
        writer_txt(':  '+str(e.__class__)+'\n', 'log.txt', 'a')
        # writer_txt('Ошибка при чтении адреса'+datetime.now(),'log.txt','a')
        address_inner='нет'
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

def check_from_verified_ad(curret_ad):
    mycursor = connection.cursor()
    sql = 'SELECT linkAd,status,idAds,price FROM avito_db.ads where linkAd= "' + curret_ad[
        'Ссылка на объявление'] + '";'
    try:
        mycursor.execute(sql)
        query = mycursor.fetchall()
    except Exception as e:
        print(e.__class__)
        print('Ошибка: проверку на наличие в таблице ад')
        writer_txt('Ошибка: проверку на наличие в таблице ад','log.txt','a')
        writer_txt('Ошибка: проверку на наличие в таблице ад - ' + str(datetime.now()) + ' - ' + curret_ad[
            'Ссылка на объявление'], 'log.txt', 'a')
        writer_txt(e.__class__, 'log.txt', 'a')
        return False

    status_of_original=1

    if len(list(query)) != 0:
        ans = list(query[0])
        status_of_original = ans[1]
        id_of_original = ans[2]
        if ans:
            if ans[1] == 0:
                sql = "UPDATE `ads` set `status`='1',`price`='" + str(curret_ad['Цена']) + "' WHERE (`idAds` = '" + str(
                    ans[2]) + "');"
                try:
                    mycursor.execute(sql)
                    connection.commit()
                except Exception as e:
                    print(e.__class__)
                    print('Ошибка: обновление (на наличие в таблице ад)')
                    writer_txt('Ошибка: обновление (на наличие в таблице ад) - '+str(datetime.now())+' - '+curret_ad['Ссылка на объявление'],'log.txt','a')
                    writer_txt(e.__class__, 'log.txt', 'a')
                    return False
            return False

    sql = 'SELECT linkAd,status,idAds,price FROM avito_db.adsbanned where linkAd= "' + curret_ad[
        'Ссылка на объявление'] + '";'
    try:
        mycursor.execute(sql)
        query = mycursor.fetchall()
        if len(list(query)) != 0:
            ans_b = list(query[0])
            if ans_b:
                if status_of_original == 0:
                    sql = "UPDATE `ads` set `status`='1',`price`='" + str(curret_ad['Цена']) + "' WHERE (`idAds` = '" + str(ans[2]) + "');"
                    mycursor.execute(sql)
                    return False
            return False
    except Exception as e:
        print(e.__class__)
        writer_txt(e.__class__, 'log.txt', 'a')
        writer_txt('Ошибка: обновление (на наличие в таблице адбан) - ' + str(datetime.now()) + ' - ' + curret_ad[
            'Ссылка на объявление'], 'log.txt', 'a')
        return False
    return True

def check_from_writer(curret_ad):
    mycursor=connection.cursor()
    try:
        sql = 'SELECT price,`numberOfFloors`,`floor`,`totalArea`,`addressFull`,idAds FROM avito_db.ads;'
        mycursor.execute(sql)
    except:
        writer_txt('Ошибка')
    
    clear_data_of_ads = mycursor.fetchall()
    # try:
    for saved_ad in clear_data_of_ads:
        saved_ad=list(saved_ad)
        if curret_ad['Цена'] == saved_ad[0]  and curret_ad['Этажей в доме']==saved_ad[1] and curret_ad['Этаж']==saved_ad[2] and curret_ad['Общая площадь'] != saved_ad[3] and curret_ad['Адрес Полный']==saved_ad[4]:
            writer_db(curret_ad,['idOfOriginalAd'],[str(saved_ad[5])],'adsbanned')
            # if
            return False
    # except Exception as e:
    #     print('Ошибка при проверки на бан')
    #     print(e.__class__)
    #     writer_txt(e.__class__, 'log.txt', 'a')
    #     return False
    return True

def writer_db(line,fieldnames=[],values=[],table="ads"):
    try:
        global district_read_from_db
        global lacality_read_from_db
        mycursor = connection.cursor()

        sql = "INSERT INTO "+table+" (`name`,`price`,`addressFull`,`primary`,`date`,`linkAd`,`views`,`idAdInSite`,`seller`,`linkSeller`,`floor`,`numberOfFloors`,`numberOfRooms`,`livingSpace`,`totalArea`,`kithenArea`,`yearOfConstruction`,`finishing`,`developer`,`nameOfTheNewBulding`,`thePlots`,`distanseToCity`,`online`,`ownership`,`idKindOfProperty`,`species_idSpecie`,`lacality_idlacality`,`idMaterial`"
        for fieldname in fieldnames:
            sql+=", `"+fieldname+"`"

        sql+=") VALUES ("

        sql+="'"+(line['Название'])+"'"
        sql+=","+"'"+str(line['Цена'])+"'"
        sql+=","+"'"+(line['Адрес Полный'])+"'"
        sql+=","+"'"+str(line['Первичка/Вторичка'])+"'"
        sql+=","+"'"+(line['Дата размещения'])+"'"
        sql+=","+"'"+(line['Ссылка на объявление'])+"'"
        sql+=","+"'"+str(line['Просмотров'])+"'"
        sql+=","+"'"+str(line['id_ad'])+"'"
        sql+=","+"'"+(line['Имя продовца'])+"'"
        sql+=","+"'"+(line['Ссылка на прдовца'])+"'"
        sql+=","+"'"+(line['Этаж'])+"'"
        sql+=","+"'"+(line['Этажей в доме'])+"'"
        sql+=","+"'"+(line['Количество комнат'])+"'"
        sql+=","+"'"+(line['Жилая площадь'])+"'"
        sql+=","+"'"+(line['Общая площадь'])+"'"
        sql+=","+"'"+(line['Площадь кухни'])+"'"
        sql+=","+"'"+(line['Год постройки'])+"'"
        sql+=","+"'"+(line['Отделка'])+"'"
        sql+=","+"'"+(line['Официальный застройщик'])+"'"
        sql+=","+"'"+(line['Название новостройки'])+"'"
        sql+=","+"'"+(line['Площадь участка'])+"'"
        sql+=","+"'"+(line['Расстояние до города'])+"'"
        sql+=","+"'"+str(line['Возможность онлайн просмотра'])+"'"
        sql+=","+"'"+(line['Право собственности'])+"'"
        sql+=","+"'"+str(property_read_from_db[line['Вид объекта'].lower()])+"'"
        sql+=","+"'"+str(species_read_from_db[line['Вид']])+"'"
        try:
            line['Пункт населения(Город, село и т.д.)']
        except:
            print(line)
        # if 'г.' in line['Пункт населения(Город, село и т.д.)'] and not 'г. ' in line['Пункт населения(Город, село и т.д.)']:
        #     line['Пункт населения(Город, село и т.д.)']=line['Пункт населения(Город, село и т.д.)'].replace('г.','г. ')
        get_id_of_lacality='SELECT idlacality FROM avito_db.lacality inner join district on (lacality.idDistrict=district.idDistrict) inner join regions on (lacality.idRegion=regions.idRegion) where lacality.name="'+line['Пункт населения(Город, село и т.д.)']+'" and district.name = "'+line['Район']+'";'
        # print(get_id_of_lacality)
        mycursor.execute(get_id_of_lacality)
        list_of_lacality=list(mycursor.fetchall())
        # print('list: ',list_of_lacality)
        # for x in list_of_lacality:
        try:
            id_of_lacality=list(list_of_lacality[0])[0]
            # print('id: ', id_of_lacality)

        except:
            id_of_lacality=list_of_lacality
            print('Ошибка при получении id')
        sql+=","+"'"+str(id_of_lacality)+"'"
        # print(id_of_lacality)
        sql+=","+"'"+str(material_read_from_db[line["Материал стен"]])+"'"
        for value in values:
            sql+=","+"'"+str(value)+"'"
        sql+=");"
        mycursor.execute(sql)
        print('Строка записанна')

        connection.commit()
    except:
        writer_txt(sql,'write_bag.txt','a')
        writer_txt(line,'write_bag.txt','a')
        writer_txt(datetime.now(),'write_bag.txt','a')
        print("Ошибка при записи в бд: ", sql)

def parse(category):
    # data=[]
    global flag_break_from_url
    flag_break_from_url = False
    url=ALL_NEED_URL_FROM_CATEGORY[category]
    html=get_html(url)
    data=[]
    if html.status_code==200:
        try:
            pages_count=get_pages_count(html.text)
            # pages_count=1

        except:
            print('Ошибка при получении страниц')
            pages_count=1

        # pages_count=5
        for page in range(1,pages_count+1):
            print(f'Парсинг страницы {page} из {pages_count}')
            html=get_html(url, params={'p':page})
            data+=get_content(html.text,pages_count,page,category)
            if  flag_break_from_url:
                break

        if data==[]:
            print("Зашла при пустом data листе")
            return

        for index,line in enumerate(data):

            writer_txt(line['Ссылка на объявление'], str(category) + '.txt', 'a')

            # mycursor = connection.cursor()
            # sql = 'SELECT linkAd,status,idAds,price FROM avito_db.ads where linkAd= "' + line[
            #     'Ссылка на объявление'] + '";'
            # mycursor.execute(sql)
            # query = mycursor.fetchall()
            # if len(list(query)) != 0:
            #     if list(query)[1]==1:
            #         continue
            if check_from_verified_ad(line)==False:
                print('Проверка на уникальность')
                continue

            line.update(get_inner_content(line['Ссылка на объявление']))
            line = filling_empty_features(line)
            if line['Район']=='нет' :
                print('Не прошла по адресу')
                print(line)
                writer_txt(line['Ссылка на объявление'],'emtyaddress.txt','a')
                continue
            # writer_txt(line, str(category) + '.txt')
            print('ПРоверка данных для записи: ',index,' из ',len(data))
            if check_from_writer(line):
                print('Прошла')
                # writer_str_csv(line,'new_data.csv','a')
                # try:
                writer_db(line)
                continue
                # except Exception as e:
                #     print(e.__class__)
                #     writer_txt(e.__class__, 'log.txt', 'a')
            print('Строка не прошла на запись')


    else:
        print('Не удалось получить html')

def check_status_ads():
    # data=[]
    global flag_break_from_url
    for category in ALL_NEED_URL_FROM_CATEGORY.keys():
        flag_break_from_url = False
        url=ALL_NEED_URL_FROM_CATEGORY[category]
        html=get_html(url)
        data=[]
        if html.status_code==200:
            try:
                pages_count = get_pages_count(html.text)
            except:
                print('Ошибка при получении страниц')
                # pages_count = 1
            pages_count=1
            for page in range(1,pages_count+1):
                print(f'Проверка статусов: страница {page} из {pages_count}')
                html = get_html(url, params={'p': page})
                data+=get_content(html.text,pages_count,page)
                if  flag_break_from_url:
                    break
        else:
            print('Не удалось получить html')
        sleep(60)
    mycursor = connection.cursor()
    sql='SELECT linkAd,price,status FROM avito_db.ads where status=1;'
    mycursor.execute(sql)
    ads_query=mycursor.fetchall()
    ads=[ list(i) for i in ads_query]
    data_clear=[]
    for ad in ads:
        flag_status_ad=False
        # print(ad[0])
        for line in data:
            # print(line['Ссылка на объявление'])
            if line['Ссылка на объявление'] in ad[0]:
                print('ПРоверка сработала на наличие в найденом списке')
                flag_status_ad=True
                break
        if not flag_status_ad:
            sql="update ads set status=0 where linkAd='"+ad[0]+"'"
            print('Запись на обновление')
            try:
                mycursor.execute(sql)
                print('Произошло обновление')
            except:
                print('Ошибка при обновлении статуса в объявления')
                writer_txt('Ошибка при обновлении статуса в объявления'+str(datetime.now()),'log.txt','a')

    data_clear=data
    for index, line in enumerate(data_clear):
        if check_from_verified_ad(line) == False:
            print('Проверка на уникальность(статус)')
            continue
        line.update(get_inner_content(line['Ссылка на объявление']))
        line = filling_empty_features(line)
        if line['Район'] == 'нет':
            print('Не прошла по адресу')
            print(line)
            writer_txt(line['Ссылка на объявление'], 'emtyaddress.txt', 'a')
            continue
        # writer_txt(line, str(category) + '.txt')
        print('Проверка данных для записи (статус): ', index, ' из ', len(data_clear))
        if check_from_writer(line):
            # print('Прошла')
            # writer_str_csv(line,'new_data.csv','a')
            # try:
            writer_db(line)
            continue
            # except Exception as e:
            #     print(e.__class__)
            #     writer_txt(e.__class__, 'log.txt', 'a')
        print('Строка не прошла на запись')
    return

if __name__ == "__main__":
    global district_read_from_db
    global property_read_from_db
    global species_read_from_db
    global material_read_from_db
    global lacality_read_from_db
    global population
    population=csv_dict_reader('population_data.csv')


    district_read_from_db = {}
    lacality_read_from_db = {}
    property_read_from_db = {}
    species_read_from_db = {}
    material_read_from_db = {}
    try:
        with connection.cursor() as cursor:
            query = 'SELECT * FROM district'
            cursor.execute(query)

            for row in cursor:
                district_read_from_db[row[1]] = row[0]


        with connection.cursor() as cursor:
            query = 'SELECT * FROM lacality'
            cursor.execute(query)
            for row in cursor:
                lacality_read_from_db[row[1]] = row[0]

        with connection.cursor() as cursor:
            query = 'SELECT * FROM kindofpropertys'
            cursor.execute(query)
            for row in cursor:
                property_read_from_db[row[1]] = row[0]


        with connection.cursor() as cursor:
            query = 'SELECT * FROM buildingmaterials'
            cursor.execute(query)
            for row in cursor:
                material_read_from_db[row[1]] = row[0]

        with connection.cursor() as cursor:
            query = 'SELECT * FROM species'
            cursor.execute(query)
            for row in cursor:
                species_read_from_db[row[1]] = row[0]
    except:
        print('Неудача при чтении первых свойств')
        input()
    flag_check_all_close_ads=True
    while True:

        if (flag_check_all_close_ads and (datetime(1,1,1,1,1,1).time()>datetime.now().time() or (datetime(1,1,1,13,1,1).time()< datetime.now().time() and datetime(1,1,1,15,1,1).time()> datetime.now().time()))):
            print('Проверка статусов ')
            check_status_ads()
            input()
            flag_check_all_close_ads=False
        if not flag_check_all_close_ads and ((datetime(1,1,1,2,1,1).time()<datetime.now().time() and datetime(1,1,1,13,1,1).time()>datetime.now().time()) or datetime(1,1,1,15,1,1).time() < datetime.now().time()):
            flag_check_all_close_ads=True
        for category in ALL_NEED_URL_FROM_CATEGORY.keys():
            print(category.upper())
            parse(category)
            sleep(randint(2,5))
        sleep(60)




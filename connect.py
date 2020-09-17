import pymysql
from pymysql.cursors import DictCursor
import csv

connection = pymysql.connect(
  host="localhost",
  user="vladimir",
  password="_Lbvf_82461973",
  db="avito_db"
)

def csv_dict_reader(path, delimiter=',', code='utf-8'):
  with open(path, encoding=code) as file_obj:
    reader = list(csv.DictReader(file_obj, delimiter=delimiter))
  return reader

if __name__ == '__main__':
    data=csv_dict_reader('population_data.csv')
    # data=csv_dict_reader('unification_data.csv')
    # wall=[]
    # count=0
    # for line in data:
    #     if not line['Материал стен'] in wall:
    #         count+=1
    #         wall.append(line['Материал стен'])
    #         print(count,' ',line['Материал стен'])
    # val=[]
    # for line in wall:
    #     val=(line)
    #     query = 'INSERT INTO buildingmaterials (name) VALUES (%s)'
    #     with connection.cursor() as cursor:
    #         cursor.execute(query, val)
    #         connection.commit()
    # print(val)
    # val=[['name','cur'],['name','cur']]
    # val.append(['end','end2'])
    # print((val))
    # data=[]
    # for line in val:
    #     data.append(tuple(line))
    # print(data)
    #
    district={}
    mycursor=connection.cursor()
    query = 'SELECT linkAd,price FROM avito_db.ads;'
    mycursor.execute(query)
    q=mycursor.fetchall()
    # print(q)
    ads=[list(i) for i in list(q)]
    data_clear_list=[]
    for line in ads:
        if line in ads:
            # print('del')
            continue
        else:
            data_clear_list.append(line)
            print('not')
        #
    # for line in data:
    #     print(line['Регион'],'==',district[line['Регион']])
    #     with connection.cursor() as cursor:
    #         tweets = (line['Населёный пункт'],int(district[line['Регион']]),1,line['Население'])
    #         query = 'INSERT INTO lacality (name,idDistrict,idRegion,population) VALUES (%s,%s,%s,%s)'
    #         cursor.execute(query, tweets)
    #         # необходимо, т.к. по-умолчанию commit происходит только после выхода
    #         # из контекстного менеджера иначе мы бы не увидели твиттов
    #         connection.commit()
    # #
    # mycursor = connection.cursor()
    #
    # sql = "INSERT INTO kindofpropertys (name) VALUES (%s)"
    # val = [
    #     ('дачи'),
    #     ('дома'),
    #     ('квартира'),
    #     ('коттеджи'),
    #     ('таунхаусы'),
    #     ('студия'),
    # ]
    #
    # mycursor.executemany(sql, val)
    #
    # connection.commit()

    # mycursor = connection.cursor()
    #
    # sql = "INSERT INTO species (name) VALUES (%s)"
    # val = [
    #     ('продажа'),
    #     ('в месяц'),
    #     ('за сутки'),
    # ]
    #
    # mycursor.executemany(sql, val)
    #
    # connection.commit()
    # mycursor = connection.cursor()

    # sql = "INSERT INTO species (name) VALUES (%s)"
    # val = [
    #     ('продажа'),
    #     ('в месяц'),
    #     ('за сутки'),
    # ]

    # mycursor.executemany(sql, val)

    # sql='SELECT linkAd,status FROM avito_db.ads where linkAd= "https://www.avito.ru/amurskaya_oblast_blagoveschensk/kvartiry/studiya_28_m_34_et._1614484393";'
    # mycursor.execute(sql)
    # ans = list(mycursor.fetchall()[0])
    # print(ans)
    # if ans:
    #     print(ans[1])
    #     if ans[1]==0:
    #         print('Status 0')
    #     print('dd')
    # connection.commit()
    connection.close()
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
    # data=csv_dict_reader('population_data.csv')
    data=csv_dict_reader('unification_data.csv')
    wall=[]
    count=0
    for line in data:
        if not line['Материал стен'] in wall:
            count+=1
            wall.append(line['Материал стен'])
            print(count,' ',line['Материал стен'])
    val=[]
    for line in wall:
        val=(line)
        query = 'INSERT INTO buildingmaterials (name) VALUES (%s)'
        with connection.cursor() as cursor:
            cursor.execute(query, val)
            connection.commit()
    print(val)


    #
    # with connection.cursor() as cursor:
    #     query = 'SELECT * FROM district'
    #     cursor.execute(query)
    #     for row in cursor:
    #         district[row[1]]=row[0]
    # for line in data:
    #     print(line['Регион'],'==',district[line['Регион']])
    #     with connection.cursor() as cursor:
    #         tweets = (line['Населёный пункт'],int(district[line['Регион']]),1,line['Население'])
    #         query = 'INSERT INTO lacality (name,idDistrict,idRegion,population) VALUES (%s,%s,%s,%s)'
    #         cursor.execute(query, tweets)
    #         # необходимо, т.к. по-умолчанию commit происходит только после выхода
    #         # из контекстного менеджера иначе мы бы не увидели твиттов
    #         connection.commit()
    #
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
    mycursor = connection.cursor()

    sql = "INSERT INTO species (name) VALUES (%s)"
    val = [
        ('продажа'),
        ('в месяц'),
        ('за сутки'),
    ]

    mycursor.executemany(sql, val)

    connection.commit()
    connection.close()
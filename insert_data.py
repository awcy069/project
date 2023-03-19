import requests
import pymysql

try:
    connection = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="inputtuser",
        password="passwO9_rd",
        database="next_bd",
    )
    print('successfully connected...')
    try:
        with connection.cursor() as cursor:
            select_url = '''select * from url order by url desc limit 1'''
            cursor.execute(select_url)
            url = cursor.fetchall()[0][0]
            connection.commit()
            print(url)

    except Exception as ex:
        print('Connection refused...')
        print(ex)

    data_fu = requests.get(url, headers={'X-Auth-Token': 'cgbg7z39'}).json()['message']

    for i in range(len(data_fu)):
        points = data_fu[i]['points']
        print(points)
        for j in range(len(points)):

            SH = data_fu[i]['points'][j]['SH']
            distance = data_fu[i]['points'][j]['distance']

            try:
                with connection.cursor() as cursor:
                    select_n = '''select * from number'''
                    cursor.execute(select_n)
                    n = cursor.fetchall()[0][0]
                    connection.commit()
                    print(n)

            except Exception as ex:
                print('Connection refused...')
                            except Exception as ex:
                print('Connection refused...')
                print(ex)

            try:
                with connection.cursor() as cursor:
                    query = '''insert into get_data (url,number,SH,distance) values (%s,%s,%s,%s)'''
                    cursor.execute(query, (url, n, SH, distance))
                    connection.commit()

            except Exception as ex:
                print('Connection refused...')
                print(ex)


        try:
            with connection.cursor() as cursor:
                query = '''insert into number (number) values (%s)'''
                cursor.execute(query, (n + 1))
                connection.commit()

        except Exception as ex:
            print('Connection refused...')
            print(ex)
except Exception as ex:
    print('Connection refused...')
    print(ex)






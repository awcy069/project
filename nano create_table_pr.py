import pymysql

try:
        connection = pymysql.connect(
                host="127.0.0.1",
                port=3306,
                user="inputtuser",
                password="passwO9_rd",
                database="mysql",
        )
        print('successfully connected...')

    #create table

        try:
                with connection.cursor() as cursor:
                        create_table_query = "CREATE TABLE IF NOT EXISTS teplitsa_bd (time int, hum_g_1 int, hum_g_2 int, hum_g_3 int, hum_g_4 int, hum_g_5 int, hum_b_6 int, hum_air_1 int,$
        #with connection.cursor() as cursor:
                        cursor.execute(create_table_query)
                        connection.commit()
                        print('table created successfully')
        except Exception as ex:
                print('Connection refused...')
                print(ex)
except Exception as ex:
        print('Con.')
        print(ex)




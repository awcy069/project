import time as time_s
import pymysql
import requests
import datetime
from datetime import datetime
i = 0
while i < 5:

        try:
                connection = pymysql.connect(
                        host="127.0.0.1",
                        port=3306,
                        user="inputtuser",
                        password="passwO9_rd",
                        database="teplitsa_bd",
                )
                print('successfully connected...')
# data for db

                        hum_g_1 = requests.get(data_urls['sens_g_1']).json()['humidity']
                        hum_g_2 = requests.get(data_urls['sens_g_2']).json()['humidity']
                        hum_g_3 = requests.get(data_urls['sens_g_3']).json()['humidity']
                        hum_g_4 = requests.get(data_urls['sens_g_4']).json()['humidity']
                        hum_g_5 = requests.get(data_urls['sens_g_5']).json()['humidity']
                        hum_g_6 = requests.get(data_urls['sens_g_6']).json()['humidity']
                        hum_air_1 = requests.get(data_urls['sens_air_1']).json()['humidity']
                        hum_air_2 = requests.get(data_urls['sens_air_2']).json()['humidity']
                        hum_air_3 = requests.get(data_urls['sens_air_3']).json()['humidity']
                        hum_air_4 = requests.get(data_urls['sens_air_4']).json()['humidity']
                        temp_1 = requests.get(data_urls['sens_air_1']).json()['temperature']
                        temp_2 = requests.get(data_urls['sens_air_2']).json()['temperature']
                        temp_3 = requests.get(data_urls['sens_air_3']).json()['temperature']
                        temp_4 = requests.get(data_urls['sens_air_4']).json()['temperature']

                        print(i)
                        i += 1
                        with connection.cursor() as cursor:
                                insert_teplitsa_bd_query = """INSERT INTO data_urls (time, hum_g_1, hum_g_2, hum_g_3, hum_g_4, hum_g_5, hum_g_6, hum_air_1, hum_air_2, hum_air_3, hum_air_4, temp_1, temp_2, temp_3, temp_4) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                                cursor.execute(insert_teplitsa_bd_query,(time, hum_g_1, hum_g_2, hum_g_3, hum_g_4, hum_g_5, hum_g_6, hum_air_1, hum_air_2, hum_air_3, hum_air_4, temp_1,  temp_2, temp_3, temp_4))

                #       cursor.execute(insert_teplitsa_bd_query, (hum_g_1))
                #       cursor.execute(insert_teplitsa_bd_query)
                                connection.commit()
                        print('ok')
                except Exception as ex:
                        print('Connection refused...')
                        print(ex)
        except Exception as ex:
                print('Con.')
                print(ex)
        time_s.sleep(60)

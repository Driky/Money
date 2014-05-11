# -*-coding:Utf-8 -*

import sqlite3

#from Models import *

__author__ = 'Driky'


class Dao:

    def __init__(self, database):

        self.init_databas(database)

        with sqlite3.connect(database) as conn:
                cur = conn.cursor()

                cur.execute('''SELECT * FROM Account''')
                for row in cur:
                    print(row)

                conn.close()

    def init_databas(self, database):
        with sqlite3.connect(database) as conn:
            try:
                sql_file = open('./resources/initialisationSql.sql', 'r')
                sql = sql_file.read()

                cursor = conn.cursor()
                cursor.executescript(sql)

                conn.commit()

            except Exception as e:
                # Roll back any change if something goes wrong
                conn.rollback()
                raise e

            finally:
                sql_file.close()
                conn.close()

        return True
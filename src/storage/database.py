import datetime
import json
import sqlite3
from sqlite3 import Error
from network import Speedtest


class Database(object):

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = create_connection(self.db_file)
            create_table(self.conn, _sql_create_speedtests_table)

    def add_speedtest(self, speedtest: Speedtest):
        if self.conn is not None:
            create_speedtest(self.conn, speedtest.as_tuple())

    def get_all_speedtests(self):
        if self.conn is not None:
            cur = self.conn.cursor()
            cur.execute(f"SELECT * FROM {_speedtests_table}")

            rows = cur.fetchall()

            speedtests = []

            for row in rows:
                timestamp = row[1]
                download = row[2]
                upload = row[3]
                latency = row[4]

                speedtests.append(Speedtest(timestamp, download, upload, latency))

            return speedtests

    def get_speedtests(self, start: datetime, end: datetime):
        if self.conn is not None:
            cur = self.conn.cursor()

            sql = f'''SELECT * FROM {_speedtests_table} WHERE timestamp BETWEEN ? AND ?'''
            args = (start, end)
            cur.execute(sql, args)
                            
            rows = cur.fetchall()

            speedtests = []

            for row in rows:
                timestamp = row[1]
                download = row[2]
                upload = row[3]
                latency = row[4]

                speedtests.append(Speedtest(timestamp, download, upload, latency))

            return speedtests

    @classmethod
    def from_config(cls):
        with open("config.json") as json_config:
            data = json.load(json_config)
            
        return cls(data["dbLocation"])


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_speedtest(conn, speedtest):
    sql = ''' INSERT INTO speedtests(timestamp,download,upload,latency)
            VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, speedtest)
    conn.commit()

    return cur.lastrowid


_speedtests_table = "speedtests"
_sql_create_speedtests_table = f""" CREATE TABLE IF NOT EXISTS {_speedtests_table} (
                                        id integer PRIMARY KEY,
                                        timestamp timestamp NOT NULL,
                                        download integer,
                                        upload integer,
                                        latency real
                                    ); """


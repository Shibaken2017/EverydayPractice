#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import datetime
conn=sqlite3.connect("./test.db")
curs=conn.cursor()
#te=curs.execute("select count(*) from sqlite_master where type='table' and name='aaaa'")
#print te.fetchall()[0]==(0,)


d = datetime.datetime.today()
now=d.strftime("%Y-%m-%d %H:%M:%S")

#curs.execute('''CREATE TABLE practice(date TIMESTAMP,word VARCHAR(50),definition VARCHAR(50))''')

#ins = "INSERT INTO practice  (date,word,definition) VALUES (?,?,?)"

#curs.execute(ins,(now,"practice","repeated execise"))



#d = datetime.datetime.today()
#now=d.strftime("%Y-%m-%d %H:%M:%S")

#curs.execute(ins,(now,"economics","the branch of knwledge concerned with the production consumption"))

#conn.commit()
#


curs.execute(r'select * from practice where word="economics"')
test=curs.fetchall()
print test
for ele in test:
    print ele




curs.close()
conn.close()

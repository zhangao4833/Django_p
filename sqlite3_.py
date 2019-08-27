# -*- coding: utf-8 -*-
import sqlite3

# sqlite3是一个微型的数据库，主要用于浏览器、手机、平板、智能设备的应用中
# 支持标准的sql语句，不过没有特定的数据类型，可以根据开发语言的特性或类型来限定字段的类型
con = sqlite3.connect('users.sqlite3') # 当文件不存在的时候会自动创建
cursor = con.cursor()

# cursor.execute('''
# create table user(id integer primary key , name, age, phone)
# ''')
cursor.execute('''
insert into user(name, age, phone) values ('jack', 18, '123123123')
''')
cursor.execute('''
insert into user(name, age, phone) values ('tom', 19, '11111111113')
''')
# cursor.execute('''
# update user set name='tomase' where name='tom'
# ''')
cursor.execute('''
select * from user
''')

print(cursor.fetchall())

con.commit()
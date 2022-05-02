# -*- coding: utf8 -*-
from sql import SQL
db = SQL('db.db')
id = 91153
name = ""
q = []
a = '0'
#
# while a == '0':
#     id = input()
#     a = input()
#     if id not in q:
#         q.append(id)
#     else:
#         q.remove(id)
#     print(q)
print(db.get_fio(id))
print(db.get_pos(id))
print(db.get_flag(id))

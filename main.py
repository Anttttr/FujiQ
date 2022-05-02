id = 0
name = ""
q = []
a = '0'

while a == '0':
    id = input()
    a = input()
    if id not in q:
        q.append(id)
    else:
        q.remove(id)
    print(q)

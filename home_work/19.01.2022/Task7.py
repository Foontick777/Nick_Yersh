def kwar(**data):
    for key,value in data.items():
        if value%2 == 0:
            print('{}:{}'.format(key,value))
    return
kwar(a=3,b=4,c=5,d=6,e=7,f=8,i=9)

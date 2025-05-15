import mysql.connector




def analyse(data):
    l1=[]
    high = 50000
    med = 25000
    count=0
    for e in data:
        if e < med:
            count+=1
    l1.append(count)
    count=0
    for e in data:
        if e > med and e<high:
            count+=1
    l1.append(count)
    count=0
    for e in data:
        if e > high:
            count+=1
    l1.append(count)
    return l1


def analysis1(data):
    l1=[]
    depart_list=["HR","Finance","Engineering","Sales","Marketing","Other"]
    for e in depart_list:
        count=0
        for i in data:
            if e==i:
                count+=1
        l1.append(count)
    return l1


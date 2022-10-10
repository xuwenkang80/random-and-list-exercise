import random
人名 = ["初音未来","只因未来","坤哥","小黑子","ikun","徐闻康","李中大","张水健"]
_1班 = []
_2班 = []
_3班 = []
ran = 0
ran_class = 0

print(len(人名),"个人")

for x in [_1班,_2班,_3班]:
    print("还剩",len(人名),"个人")
    ran = random.randint(0,len(人名)-1)
    print(人名[ran])

    
    x.append(人名[ran])
    人名.remove(人名[ran])


while len(人名)>2:
    ran = random.randint(0,len(人名)-1)
    _1班.append(人名[ran])
    人名.remove(人名[ran])
    ran = random.randint(0,len(人名)-1)
    _2班.append(人名[ran])
    人名.remove(人名[ran])
    ran = random.randint(0,len(人名)-1)
    _3班.append(人名[ran])
    人名.remove(人名[ran])


print([_1班,_2班,_3班])

import re
mytext = "bmw google andr@gmail.com misc.yandex wewe@gmail"\
        "name@sdsd.ru 1234 Serhii "\
        "sdf  sdfsdf    werwe  1 Serhii"
print (mytext)
textlookfor=r"@"
allres= re.findall(textlookfor,mytext)
print(allres)

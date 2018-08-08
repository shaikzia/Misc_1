list1 = ['cars', 'scar', 'srac', 'ten', 'net','abcd']
# cars, scar, srac
# ten, net
# strings:
# word sort by characters
# cars - acrs, scar - acrs,
#
# Map ( key -> value )
# output = Map ( acrs -> cars, scar,
#       ent  -> ten, net
#     )
#    key = word sorted by characters.
# 0. Map = ("key"
# 1. DataStruct = Map( "key", Set(cars, srac))

from collections import Counter
def order(list):
    d = {}
    for word in list1:
        WD = Counter(word)

        k = WD.keys()
        k = sorted(k)
        k = ''.join(k)

        if k in d.keys():
            d[k].append(word)

        else:
            d[k]=[]
            d[k].append(word)

    print(d.items())
    for (key,value) in d.items():
        print(','.join(d[key]))


order(list1)


























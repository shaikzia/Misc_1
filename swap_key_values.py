# You have a k
# Map( "kabeer" -> 3
#      "faiz" -> 4
#      "zaira" -> 3
#      "sajida" -> 5
#
# output should be of the form:
#   Map( 3 -> ["kabeer", "zaira"], 4 -> faiz, 5 -> sajida)

from collections import defaultdict
dnames = {"Kabeer":3, "Faiz":4, "Zairah":3, "Sajida":5, "Saad":5}
def convert(dnames):
    d = defaultdict(list)
    print(d.keys())
    print(d.items())

    for k,v in dnames.items():
        d[v].append(k)
    print(type(d))
    print(d)

convert(dnames)

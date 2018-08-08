array = ['1','2','3','4','5']
# print(type(array))
leng = len(array)
int_list = []
lessthan_avg    = []
greaterthan_avg = []
equal_to_avg    = []

def get_sum():
    index = 0
    j = 0
    for i in array:
        x = int(array[index])
        int_list.append(x)
        index = index + 1
        j = x + j
    # return j
    avg = j / leng

    for k in int_list:
        if k < avg:
            lessthan_avg.append(k)
        elif k > avg:
            greaterthan_avg.append(k)
        elif k == avg:
            equal_to_avg.append(k)
        pass

    print(leng)
    print(avg)
    print(int_list)

    print(len(lessthan_avg), 'are less than average', lessthan_avg)
    print(len(greaterthan_avg), 'are greater than average',greaterthan_avg)
    print(len(equal_to_avg), 'equal to average', equal_to_avg)

get_sum()
x = [1,2,3,2,5,2,7,2]

def getMedian(list) :
    list.sort();
    median = 0;
    if (len(list) % 2 != 0) :
        median = list[floor(len(list) / 2)] ;
    else :
        mid1 = list[(int(len(list)/ 2) - 1)] ;
        mid2 = list[int(len(list) / 2)] ;
        median = (mid1 + mid2) / 2;
    return median ;
print(getMedian(x));

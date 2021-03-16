x = [1,2,3,2,5,2,7,2]

def getMean(list) :
    sum = 0;
    for item in list :
        sum += item;
    
    mean = sum / len(list) ;
    return mean;

print(getMean(x));

List1 = [5, -5, 10, 100, 25, 30]
    def kali5 (angka): 
        return angka * 5

    hasilMap = map(kali5, List1)
    print(hasilMap, type(hasilMap))
    hasilMapList = list(hasilMap)
    print(hasilMapList)
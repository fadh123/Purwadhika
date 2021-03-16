def main():
    # List of numbers
    listOfNum = [1,3,2,2,1,5,1,24,12,124,12,21,31,15]
    
    
    # print the List
    print("Initial List", listOfNum,  sep='\n')
        
    
    print("Sorting the List in ascending Order")
    
    # Create a sorted copy of existing list
    newList = sorted(listOfNum)
     # print the List
    print("New List", newList,  sep='\n')
     # print the List
    print("Existing List", listOfNum,  sep='\n')
    
    # Sort the List in Place
    listOfNum.sort()
    # print the List
    print("List Sorted in Ascending Order", listOfNum,  sep='\n')
    print("Sorting the List in Descending Order")
    
    # Create a sorted copy of existing list
    newList = sorted(listOfNum, reverse=True)
     # print the List
    print("New List", newList,  sep='\n')
     # print the List
    print("Existing List", listOfNum,  sep='\n')
    
    # Sort the List in Place (Descending Order)
    listOfNum.sort(reverse=True)
    # print the List
    print("List Sorted in Descending Order", listOfNum,  sep='\n')
if __name__ == "__main__":
    main()
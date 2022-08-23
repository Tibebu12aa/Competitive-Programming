def selection_sort(N,arr):
    #start an outer loop iterating for each element in the arr starting from index 0 to the one before the last
    for i in range(0,len(arr)-1):
        #first set the current minimum to the first index
        currnet_min =i
        #now start a second loop stating from the element next to the current index to the last element
        for j in range(i+1,len(arr)):
            #check if the index i is the smallest number
            if arr[j] < arr[currnet_min]:
                #if true set the value to the current_min
                currnet_min =j
        #swap the numbers
        arr[i],arr[currnet_min]=arr[currnet_min],arr[i]
    print(*arr)
if __name__ == '__main__':
    N = int(input("Enter length of array: ").strip())

    arr = list(map(int, input("Enter Array Elements: ").rstrip().split()))

    selection_sort(N, arr)


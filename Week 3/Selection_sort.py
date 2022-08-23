def selection_sort(N,arr):
    for i in range(0,len(arr)-1):
        currnet_min =i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[currnet_min]:
                currnet_min =j
        arr[i],arr[currnet_min]=arr[currnet_min],arr[i]
    print(*arr)
if __name__ == '__main__':
    N = int(input("Enter length of array: ").strip())

    arr = list(map(int, input("Enter Array Elements: ").rstrip().split()))

    selection_sort(N, arr)


def count_inversions(arr):
    count=0
    n=len(arr)
    inversions=[]

    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                count+=1
                inversions.append((arr[i],arr[j]))

    print("Total inversions:",count)
    print("Inversion pairs:",inversions)

arr=[9,8,7,6,5,4,3,2,1]
count_inversions(arr)
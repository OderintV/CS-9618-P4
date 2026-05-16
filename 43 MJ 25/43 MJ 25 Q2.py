from idlelib.editor import index2line

DataArray = [0,3,4,56,67,44,43,32,31,345,45,6,54,1]

def InsertionSort(DataArray):
    for i in range(1,len(DataArray)):
        key = DataArray[i]
        j = i -1
        while j>=0 and key < DataArray[j]:
            DataArray[j+1] = DataArray[j]
            j -= 1
        DataArray[j+1] = key
    return DataArray

def OutputArray(arr):
    line = ""
    for item in arr:
        line = line + str(item) + " "
    print(line.strip())

def Search(arr, target):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


OutputArray(DataArray)
DataArray = InsertionSort(DataArray)
OutputArray(DataArray)

index1 = Search(DataArray,0)
index2 = Search(DataArray,345)
index3 = Search(DataArray,67)
index4 = Search(DataArray,2)

def smallest(arr):
    smallestNum = arr[0]
    smallestIndex = 0
    for i in range(len(arr)):
        if arr[i] < smallestNum:
            smallestNum = arr[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(arr):
    sortedArr = []
    for i in range(len(arr)):
        smallestIndex = smallest(arr)
        sortedArr.append(arr.pop(smallestIndex))
    return sortedArr

if __name__ == "__main__":
    arr = [1,23,21,11,5]
    print(selectionSort(arr))

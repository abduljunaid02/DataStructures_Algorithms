def binary_search(arr, item):
    low = 0
    high = len(arr) -1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess < mid:
            low = mid + 1
        else:
            high = mid - 1
        return None

if __name__ == "__main__":
    arr = [1,3,5,7,9]
    item = 5
    print(binary_search(arr,item))

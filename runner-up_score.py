if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    max_score = arr[-1]
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < max_score:
            print(arr[i])
            break
    

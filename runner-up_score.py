if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    # set max score to the last item of sorted array which is the largest value
    max_score = arr[-1]

    # iterate in reverse & find the 2nd smallest value
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < max_score:
            print(arr[i])
            break
    

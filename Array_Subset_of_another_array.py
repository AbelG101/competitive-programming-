def isSubset( a1, a2, n, m):
    a1_dict = {}

    for num in a1:
        if num in a1_dict:
            a1_dict[num] += 1
        else:
            a1_dict[num] = 1
    
    for num in a2:
        if num in a1_dict and a1_dict[num] > 0:
            a1_dict[num] -= 1
        elif num not in a1_dict or a1_dict[num] <= 0:
            return "No"
    
    
    return "Yes"

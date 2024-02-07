if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command = input().split()
        operation = command[0]
      
        if "insert" in operation:
            _, pos, elt = command
            my_list.insert(int(pos), int(elt))
        elif "print" in operation:
            print(my_list)
        elif "remove" in command:
            elt = command[1]
            my_list.remove(int(elt))
        elif "append" in operation:
            elt = command[1]
            my_list.append(int(elt))
        elif "sort" in operation:
            my_list.sort()
        elif "pop" in operation:
            my_list.pop()
        elif "reverse" in operation:
            my_list.reverse()

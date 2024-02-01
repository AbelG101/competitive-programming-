def split_and_join(line):
    # write your code here
    result = ""
    for ch in line:
        if (ch == " "):
            result += "-"
        else: result += ch
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

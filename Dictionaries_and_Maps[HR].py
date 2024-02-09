from sys import stdin

number_of_friends = int(input())
phone_book = {}
names_to_be_searched = []

for i in range(number_of_friends):
    name, number = input().split()
    phone_book[name] = number


for name in stdin:
    names_to_be_searched.append(name.strip())
    
for name in names_to_be_searched:
    if name in phone_book:
        print(f'{name}={phone_book[name]}')
    else:
        print("Not found")

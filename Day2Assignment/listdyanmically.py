my_list = []

for _ in range(3):
    try:
        my_list.append(int(input('Enter a number: ')))
    except ValueError:
        print('The provided value is not an integer')


print(my_list)




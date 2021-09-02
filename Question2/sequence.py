n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_num = 1
second_num = 2
third_num = 3
for i in range(1, n+1):
    if i < 4:
        print_num = i
    else:
        print_num = first_num + second_num + third_num
        first_num = second_num
        second_num = third_num
        third_num = print_num
    print(print_num)
def max_num(numbers):
    max=numbers[0]
    for num in numbers:
        if(num>max):
            max=num
    print(max)
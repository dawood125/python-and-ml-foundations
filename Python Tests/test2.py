def calculate_average(numbers):
    if len(numbers) == 0:  
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count

def find_highest(numbers):
    return max(numbers)

def find_lowest(numbers):
    return min(numbers)


marks = [85, 92, 67, 78, 95, 88, 73]

print(f"Average marks: {calculate_average(marks)}")
print(f"Highest mark:  {find_highest(marks)}")
print(f"Lowest mark:   {find_lowest(marks)}")

new_mark = int(input("Enter a new mark: "))
marks.append(new_mark)

print(f"Updated average: {calculate_average(marks)}")
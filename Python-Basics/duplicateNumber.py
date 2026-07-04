numbers=[4,5,6,3,2,2,7,9,9];
uniques=[];
for num in numbers:
    if num not in uniques:
        uniques.append(num)


print(uniques);
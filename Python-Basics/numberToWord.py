numbers=input("phone: ")

words={
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

for number in numbers:
    for word in words:
        if number == word:
            print(words[word])
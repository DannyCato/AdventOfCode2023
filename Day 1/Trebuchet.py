import re

def read(filename):
    num1 = ""
    num2 = ""
    null = ""
    cumulative = 0
    with open(filename) as file:
        for line in file:
            num1 = ""
            line = line_sterilize(line)
            for letter in line:
                if letter.isnumeric():
                    if num1 == null:
                        num1 = letter
                    num2 = letter
            number = num1 + "" + num2
            cumulative = cumulative + int(number)
    return cumulative

def line_sterilize(str):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in words:
        if re.match(word, str):
            str = remove(str, word)

    
def remove(str, word):
    number = get_number(word)
    length = len(word)
    
    for i in range(0, len(str) - length):
        temp = str[i, i + length]
        if temp == word:
            str = str[0,i] + number + str[ i+length]

def get_number(number):
    match number:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"

def main():
    print(read("Day 1\Trebuchet.txt"))

if __name__ == "__main__":
    main()
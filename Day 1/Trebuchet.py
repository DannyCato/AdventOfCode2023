import re
import time as t

def read(filename):
    cumulative = 0
    with open(filename) as file:
        for line in file:
            new = line_sterilize(line)
            numbers = re.findall("\d", new)
            cumulative = cumulative + int(numbers[0] + numbers[len(numbers) - 1])
    return cumulative

def line_sterilize(str):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in words:
        if re.search(word, str):
            str = remove(str, word)
    return str

def remove(str, word):
    number = get_number(word)
    length = len(word)
    # print(str)

    for i in range(0, len(str) - length):
        temp = str[i:i + length]
        if temp == word:
            # print(str[:i])
            # print(str[i + length])
            str = str[:i] + number + str[i + length: ]

    return str

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
    start = t.perf_counter()
    print(read("Day 1\Trebuchet.txt"))
    end = t.perf_counter()
    print("Elpased Time: " + str(end - start))
    

if __name__ == "__main__":
    main()
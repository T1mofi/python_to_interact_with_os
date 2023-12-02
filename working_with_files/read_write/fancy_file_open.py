with open("spider.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("spider.txt", "r") as file:
    lines = file.readlines()
    lines.sort()
    print(lines)
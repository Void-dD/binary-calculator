fnum = input('First Number: ')
snum = input('Second Number: ')
add = 0
numlen = abs(len(str(fnum)) - len(str(snum)))
result = []

for i in range(len(fnum)):
    if int(fnum[i]) != 1:
        if int(fnum[i]) != 0:
            print("Please Enter In Binary! Digit: " + str(i + 1) + " of First Number Invalid!")
            exit()


for i in range(len(str(snum))):
    if snum[i] != str(1):
        if snum[i] != str(0):
            print("Please Enter In Binary! Digit: " + str(i + 1) + " of Second Number Invalid!")
            exit()


for i in range(len(str(fnum)), 0, -1):
    x = int(fnum[i - 1]) + int(snum[i - 1 + numlen]) + add
    if x == int(2):
        add = 1
        x = 0
        result.append(x)
    elif x == int(3):
        add = 1
        x = 1
        result.append(x)
    elif x != int(2):
        add = 0
        result.append(x)
if x != int(0):
    result.append(x)

result.reverse()
formatted = str(result).replace(', ', '')
print("LengthDifference: " + str(numlen))
print(formatted)
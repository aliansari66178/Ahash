import random
import time

def unhash (inp, hash, ver) :
    unhashed = []
    code = (hash.read()).split("\n")
    ascii = []
    data = (inp.read()).split("\n")
    arr = []
    code_arr = []
    for i in range (len(code)):
        ascii.append((code[i][0]))
    for o in range (len(data)):
        arr.append([])
        for i in range (int(len(data[o]) / ver)):
            arr[o].append(data[o][ver*i:ver*i+ver])
    for i in range (len(code)):
        code_arr.append(code[i][2:].split(" "))
    # for i in range (len(arr)):
    #     if arr[i] in ascii:
    #         arr[i] = random.sample((code_arr[ascii.index(arr[i])]), 1)[0]
    #     elif arr[i] != "\n": 
    #        arr[i] = arr[i] * ver
    for o in range (len(data)):
        unhashed.append("")
        for m in range (len(arr[o])):
            tmp = True
            for i in range (len(code)):
                if arr[o][m] in code_arr[i]:
                    unhashed[o] += ascii[i]
                    tmp = False
            if tmp:
                unhashed[o] += arr[o][m][0]
    # for i in range (len(arr)):
    #     hashed += arr[i]
    return unhashed


input('"Type your text in "input.txt" and Copy your hash code with name "code.hash"! Then Press Enter!')
# print('The hashed text is :')
for i in range (int(((open("ver.hash", 'r', encoding='utf-8')).read().split("\n"))[4])):
    final = (unhash((open("input.txt", 'r', encoding='utf-8')), (open("code.hash", 'r', encoding='utf-8')), (int(((open("ver.hash", 'r', encoding='utf-8')).read().split("\n"))[1]))))
    for i in range (len(final) - 1):
        final[i] += "\n"
    with open("output.txt", 'w', encoding='utf-8') as o:
        o.writelines(final)
    with open("input.txt", 'w', encoding='utf-8') as o:
        o.writelines(final)
# out = open("output.txt", 'r', encoding='utf-8')

print("10%")
time.sleep(0.5)
print("20%")
time.sleep(0.5)
print("30%")
time.sleep(0.5)
print("40%")
time.sleep(0.5)
print("50%")
time.sleep(0.5)
print("60%")
time.sleep(0.5)
print("70%")
time.sleep(0.5)
print("80%")
time.sleep(0.5)
print("90%")
time.sleep(0.5)
print("99%")
time.sleep(2)
print("unhashed successfully")
time.sleep(3)
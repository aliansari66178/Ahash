import random
import time

def hash (inp, hash) :
    hashed = ""
    code = (hash.read()).split("\n")
    ascii = []
    data = (inp.read())
    arr = []
    code_arr = []
    for i in range (len(code)):
        ascii.append((code[i][0]))
    for i in range (len(data)):
        arr.append(data[i])
    for i in range (len(code)):
        code_arr.append(code[i][2:].split(" "))
    for i in range (len(arr)):
        if arr[i] in ascii:
            arr[i] = random.sample((code_arr[ascii.index(arr[i])]), 1)[0]
        elif arr[i] != "\n": 
           arr[i] = arr[i] * 4
    for i in range (len(arr)):
        hashed += arr[i]
    return hashed


input('"Type your text in "input.txt" and Copy your hash code with name "code.hash"! Then Press Enter!')
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
print("hashed successfully")
# print('The hashed text is :')
final = (hash(open("input.txt", 'r', encoding='utf-8'), open("code.hash", 'r', encoding='utf-8')))
# out = open("output.txt", 'r', encoding='utf-8')
with open("output.txt", 'w', encoding='utf-8') as o:
  o.write(final)
time.sleep(3)
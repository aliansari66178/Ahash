import cv2
import time

def uh (map, inp):
    ver = int(map.split("\n")[0])
    map = map.split("\n")[1]
    out = ''
    # inp = inp.split(ver*"0")
    arr = []
    for i in range (int(len(inp) / ver)):
        arr.append(inp[3*i:3*i+3])
    for i in range(len(arr)):
        num = 0
        for m in range(ver):
            num += (int(arr[i][0 - m - 1]) * (6 ** m))
        if num == 000:
            arr = arr[:i]
            break
        arr[i] = map[num -1]
    num = map.find(inp[i])+1
    for i in arr:
        out += i
    return out









def ui (img):
    # print(img)
    out = ""
    for i1 in range (len(img)):
        for i2 in range (len(img[0])):
            for i3 in range (len(img[0][0])):
                out += str(img[i1][i2][i3] % 10)


    return out

img = cv2.imread('input.png')
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# k=cv2.destroyAllWindows()
with open("colors.cm", "w") as f:
    f.write(ui(img))
#   f.writelines(multiple_lines)
img = (uh(open("map.cm", "r", encoding="UTF8").read(), open("colors.cm", "r", encoding="UTF8").read()))
# img = ih(img, open("colors.cm", "r").read())
# cv2.imwrite('output.png', img)
with open("output.txt", "w", encoding="UTF8") as f:
    f.write(img)
print("unhashed successfully")
time.sleep(3)

import cv2
import time

def ha (map, inp):
    ver = int(map.split("\n")[0])
    map = map.split("\n")[1]
    out = ''
    for i in range (len(inp)):
        num = map.find(inp[i])+1
        tmp = ""
        for m in range ((ver-1), -1, -1):
            tmp += str(int(num / (6**m)))
            num -= (int(num / (6**m)) * (6**m))
        out += tmp
    return (out + "000")









def ih (img, data):
    counter = 0
    for i1 in range (len(img)):
        for i2 in range (len(img[0])):
            for i3 in range (len(img[0][0])):
                if counter < len(data):
                    img[i1][i2][i3] = (int(img[i1][i2][i3] / 10) * 10 + int(data[counter]))
                counter += 1


    return img

img = cv2.imread('input.png')
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# k=cv2.destroyAllWindows()
with open("colors.cm", "w") as f:
    f.write(ha(open("map.cm", "r", encoding="UTF8").read(), open("input.txt", "r", encoding="UTF8").read()))
#   f.writelines(multiple_lines)

img = ih(img, open("colors.cm", "r").read())
cv2.imwrite('output.png', img)
print("hashed successfully")
time.sleep(3)

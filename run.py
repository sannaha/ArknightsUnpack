from PIL import Image
import os

filepath = 'skinpack'
list = os.listdir(filepath)
print('一共有' + str(len(list) // 2) + '张立绘')

for index in range(len(list) // 2):
    imageName = list[2 * index]
    maskName = list[2 * index + 1]
    image = Image.open(filepath + '\\' + imageName)
    mask = Image.open(filepath + '\\' + maskName)
    pixdata_img = image.load()
    pixdata_mask = mask.load()
    if image.size == mask.size:
        for y in range(mask.size[1]):
            for x in range(mask.size[0]):
                pixdata_img[x,
                            y] = (pixdata_img[x, y][0], pixdata_img[x, y][1],
                                  pixdata_img[x, y][2], pixdata_mask[x, y][2])
    elif image.size[0] == 2 * mask.size[0]:
        for y in range(2 * mask.size[1]):
            for x in range(2 * mask.size[0]):
                pixdata_img[x,
                            y] = (pixdata_img[x, y][0], pixdata_img[x, y][1],
                                  pixdata_img[x, y][2], pixdata_mask[x / 2,
                                                                     y / 2][2])
    else:
        print(imageName + ' not match ' + maskName)

    image.save('mix_' + imageName)
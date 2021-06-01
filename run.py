from PIL import Image
from natsort import natsorted
from tqdm import trange
import os

choice = input(
    "1.干员角色立绘(source_charpack)\n2.干员皮肤立绘(source_skinpack)\n3.剧情角色立绘(characters)\n4.测试\n请选择合成类型："
)

inputPath = ''
outputPath = ''

if choice == '1':
    inputPath = 'F:\\Pixiv\\Arknights\\apk\\source_charpack\\new\\Texture2D'
    outputPath = 'F:\\Pixiv\\Arknights\\apk\\source_charpack\\new_mix\\'
elif choice == '2':
    inputPath = 'F:\\Pixiv\\Arknights\\apk\\source_skinpack\\new\\Texture2D'
    outputPath = 'F:\\Pixiv\\Arknights\\apk\\source_skinpack\\new_mix\\'
elif choice == '3':
    inputPath = 'F:\\Pixiv\\Arknights\\apk\\source_avg\\characters\\new\\Texture2D'
    outputPath = 'F:\\Pixiv\\Arknights\\apk\\source_avg\\characters\\new_mix\\'
else:
    print('使用测试数据进行合成！')
    inputPath = './skinpack/'
    outputPath = './mix_'

# 引入natsort对文件名进行自然排序
list = natsorted(os.listdir(inputPath))

print('一共有' + str(len(list) // 2) + '张立绘')

for index in trange(len(list) // 2):
    imageName = list[2 * index]
    maskName = list[2 * index + 1]
    image = Image.open(inputPath + '\\' + imageName)
    mask = Image.open(inputPath + '\\' + maskName)
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

    image.save(outputPath + imageName)
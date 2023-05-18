import cv2
import os
import numpy as np
def yanse_num(img):
    # 将图像转换为一维数组，每个元素表示一个像素的BGR通道值（0-255）
    pixels = img.reshape(-1, 3)

    # 查找唯一的颜色并计算数量
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
    num_colors = len(unique_colors)

    # 输出结果
    print(f"The image has approximately {num_colors} colors.")
def gaiyanse(img):




    # 将214 214 214替换为1 1 1
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j, 0] == 214 and img[i, j, 1] == 214 and img[i, j, 2] == 214:
                img[i, j, 0] = 1
                img[i, j, 1] = 1
                img[i, j, 2] = 1

    # 将255 255 255替换为0 0 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j, 0] == 255 and img[i, j, 1] == 255 and img[i, j, 2] == 255:
                img[i, j, 0] = 2
                img[i, j, 1] = 2
                img[i, j, 2] = 2




n=0
for i in os.listdir('./yuantu'):

    # 加载要拼接的两张图片
    image1 = cv2.imread('./yuantu/{}'.format(i))

    image2 = cv2.imread('./label/{}.png'.format(n))
    gaiyanse(image2)
    # 将两张图片按水平方向拼接
    result = cv2.hconcat([image1, image2])

    # 展示拼接后的结果
    cv2.imwrite('./123/{}.png'.format(n), result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    n += 1


import cv2
import os
import numpy as np

def cv_imread(filepath):
    """
    功能相当于cv2.imread
    :param filepath:读取的图片地址（包含名字），如 "C:\\待处理图片\\宝马.jpg"
    """
    cv_imr = cv2.imdecode(np.fromfile(filepath,dtype=np.uint8),cv2.IMREAD_COLOR)
    return cv_imr

def cv_imwrite(filepath,img):
    """
    功能相当于cv2.imwrite
    :param filepath: 保存的图片地址（包含名字），如 "C:\\已处理图片\\宝马.jpg"
    :param img: 要保存的图片，三维数组
    """
    cv_imw = cv2.imencode('.jpg',img)[1].tofile(filepath)
    return cv_imw
def show(a,b):
    cv2.imshow(a,b)
    cv2.waitKey(0)
def color_num(path):
    # 读取图像并获取宽高
    img = cv_imread(path)
    height, width, _ = img.shape

    # 将图像数组转换为一维数组，并统计不同颜色
    colors = np.unique(img.reshape(-1, 3), axis=0)

    # 输出不同颜色数量
    print(len(colors))
def yanse_num(img):
    # 将图像转换为一维数组，每个元素表示一个像素的BGR通道值（0-255）
    pixels = img.reshape(-1, 3)

    # 查找唯一的颜色并计算数量
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
    num_colors = len(unique_colors)

    # 输出结果
    print(f"The image has approximately {num_colors} colors.")
# n=0
# for i in os.listdir('./label'):
#     path1=os.path.join('./label',i)
#     path2=os.path.join('./yuantu',i)
#     img1=cv_imread(path1)
#     img2=cv_imread(path2)
#     cv_imwrite('./label/{}.png'.format(n),img1)
#     cv_imwrite('./yuantu/{}.png'.format(n),img2)
#     n+=1

# for i in os.listdir('./label'):
#
#
#     # 加载彩色图像
#     path=os.path.join('./label',i)
#     img = cv_imread(path)
#
#     # 转换为灰度图像
#     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # 使用阈值法进行二值化，threshold参数可以根据需要自行调整来进行二值化处理。
#     threshold = 150
#     ret, binary_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)
#
#     # 将二值化图像转化为三通道的黑白BGR图像
#     color_map = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2BGR)
#
#     yanse_num(color_map)
#     cv2.imwrite('./label_process/{}'.format(i),color_map)


# for i in os.listdir('./label_process'):
#
#
#     # 加载彩色图像
#     path=os.path.join('./label_process',i)
#     img = cv2.imread(path)
#     yanse_num(img)
#
#
#
#
#     img[img == 255] = 1
#     print('sssssss')
#     yanse_num(img)
#     print(img.max(),img.min())
#     cv2.imwrite('./label_process/{}'.format(i), img)

n=0
for i in os.listdir('./yuantu'):

    # 加载要拼接的两张图片
    image1 = cv2.imread('./yuantu/{}'.format(i))

    image2 = cv2.imread('./label_process/{}.png'.format(n))

    # 将两张图片按水平方向拼接
    result = cv2.hconcat([image1, image2])

    # 展示拼接后的结果
    cv2.imwrite('./123/{}.png'.format(n), result)

    n += 1




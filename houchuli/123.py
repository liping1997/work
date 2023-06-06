from PIL import Image

def touming():
    # 打开原始图像和语义分割图
    img = Image.open('./yuantu/0.png').convert('RGBA')
    mask = Image.open('./modified_image_B.png').convert('RGBA')
    # 为分割图设置透明度
    new_mask = []

    for pixel in mask.getdata():
        if pixel[0] == 192 and pixel[1] == 14 and pixel[2] == 235:
            new_mask.append((192, 14, 235, 133))
        elif pixel[0] == 220 and pixel[1] == 20 and pixel[2] == 60:
            new_mask.append((220, 20, 60, 136))

    mask.putdata(new_mask)
    # 将分割图覆盖到原始图像上，并保存结果
    result = Image.alpha_composite(img, mask)
    result.save("result.png")


# touming()


# from PIL import Image
# # 读取图片
# img = Image.open('./modified_image_B.png')
# # 获取宽度、高度值
# width, height = img.size
# # 去重后的像素颜色集合
# unique_colors = set()
# # 遍历所有像素，并添加到集合中
# for x in range(width):
#     for y in range(height):
#         color = img.getpixel((x,y))
#         unique_colors.add(color)
# # 实际使用的颜色数量
# actual_colors = len(unique_colors)
# print(unique_colors)
# print(f"The image has {actual_colors} actual colors.")





def change_color():
    # 打开语义分割图并获取其像素数据和模式
    img = Image.open("./label/0.png")
    # 获取像素数据
    pixels = img.load()

    # 遍历每个像素，并替换指定颜色为新的颜色
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] == (1, 1, 1):
                pixels[x, y] = (192, 14, 235)
            elif pixels[x, y] == (0, 0, 0):
                pixels[x, y] = (220, 20, 60)
    width, height = img.size
    # 去重后的像素颜色集合
    unique_colors = set()
    # 遍历所有像素，并添加到集合中
    for x in range(width):
        for y in range(height):
            color = img.getpixel((x,y))
            unique_colors.add(color)
    # 实际使用的颜色数量
    actual_colors = len(unique_colors)
    print(unique_colors)
    print(f"The image has {actual_colors} actual colors.")
    img.save("modified_image_B.png")



# change_color()



# from PIL import Image
#
# # 创建空白图像
# image = Image.newcrop("RGB", (256, 256))
#
# # 遍历每个 16x16 区域，并在该区域填充对应颜色
# for x in range(0, 256, 16):
#     for y in range(0, 256, 16):
#         color = (x, y, (x + y) % 256)  # 生成 RGB 颜色元组
#         image.paste(color, (x, y, x + 16, y + 16))  # 在当前区域填充颜色
#
# # 保存图片
# image.save("colorgrid.png")

import numpy as np
def edge(path):
    import cv2
    import os

    img_path=os.path.join('./label',path)
    # 读取语义分割图像
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 创建新的0矩阵，即边界矩阵
    height, width = img.shape[:2]
    edge_img = np.zeros((height, width), dtype=np.uint8)

    # 遍历每个像素点，找出边界点
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if img[i][j] == 0:
                continue
            # 如果当前像素点和周围八个像素点颜色都相同，则不是边界点
            if (img[i - 1][j - 1] == img[i - 1][j] == img[i - 1][j + 1] == img[i][j - 1] == img[i][j + 1] ==
                    img[i + 1][j - 1] == img[i + 1][j] == img[i + 1][j + 1]):
                continue
            else:
                # 确认为边界点，则边界矩阵对应值设为255
                edge_img[i][j] = 255

    # 保存边界图片
    aaa=path.replace('.png','_edge.png')
    out_path = os.path.join('./edge',aaa)
    cv2.imwrite(out_path, edge_img)
import os

# for i in os.listdir('./label'):
#     print(i)
#     edge(i)


import cv2
import os


def edge1(img_path,edge_path):
    # 读取语义分割图像
    img = cv2.imread(img_path)

    # 读取边界图像

    edge_img = cv2.imread(edge_path, cv2.IMREAD_GRAYSCALE)

    # 将边界图像转为BGR格式，方便和彩色图像叠加
    edge_bgr = cv2.cvtColor(edge_img, cv2.COLOR_GRAY2BGR)

    # 将边界图像拷贝到原图像中
    img[edge_img != 0] = (0, 0, 255)
    alpha = 0.1  # 设置透明度
    result = cv2.addWeighted(edge_bgr, alpha, img, 1 - alpha, 0)

    # 显示并保存结果图像

    out_path=img_path.replace('yuantu','result')
    cv2.imwrite(out_path, result)

# # 测试
# # img_path = "./yuantu/0.png"
# # edge_path='./edge/0_edge.jpg'
# # edge1(img_path,edge_path)
#
# for i in os.listdir('./yuantu'):
#     path1=os.path.join('./yuantu',i)
#     path2=os.path.join('./edge',i.replace('.png','_edge.png'))
#     edge1(path1,path2)


from PIL import Image
for i in os.listdir('./label'):
    path1=os.path.join('./yuantu',i)
    path2=os.path.join('./label',i)
    path3=os.path.join('./edge',i.replace('.png','_edge.png'))
    path4=os.path.join('./result',i)

    import cv2

    # 读取四张图片
    img_a = cv2.imread(path1)
    img_b = cv2.imread(path2)
    img_c = cv2.imread(path3)
    img_d = cv2.imread(path4)

    # 获取单张图片的高度和宽度
    height, width, _ = img_a.shape

    # 将 A、B 图片水平方向拼接
    merge_ab = cv2.hconcat([img_a, img_b])

    # 将 C、D 图片水平方向拼接
    merge_cd = cv2.hconcat([img_c, img_d])

    # 将合并后的 AB 和 CD 图片垂直方向拼接
    merge_final = cv2.vconcat([merge_ab, merge_cd])



    # 保存最终拼接结果
    cv2.imwrite('./results/{}'.format(i),merge_final)

from tkinter import messagebox

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
#     # 加载彩色图像
#     path=os.path.join('./label',i)
#     img = cv2.imread(path)
#
#     # # 转换为灰度图像
#     # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     #
#     # # 使用阈值法进行二值化，threshold参数可以根据需要自行调整来进行二值化处理。
#     # threshold = 150
#     # ret, binary_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)
#     #
#     # # 将二值化图像转化为三通道的黑白BGR图像
#     # color_map = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2BGR)
#
#     yanse_num(img)
#     # cv2.imwrite('./label_process/{}'.format(i),color_map)

# for i in os.listdir('./label'):
#
#     # 加载彩色图像
#     path=os.path.join('./label',i)
#     img = cv2.imread(path)
#     yanse_num(img)
#
#     img[img == 255] = 2
#     img[img == 220] = 1
#     img[img == 200] = 0
#     img[img <20] ==0
#     yanse_num(img)
#     print(img.max(),img.min())
#     cv2.imwrite('./label_a/{}'.format(i), img)


# for i in os.listdir('./label'):
#
#     # 加载彩色图像
#     path=os.path.join('./label',i)
#     img = cv2.imread(path)
#     yanse_num(img)
#
#     img[img == 255] = 3
#     img[img == 220] = 2
#     img[img == 200] = 1
#     img[img <20] ==0
#     yanse_num(img)
#     print(img.max(),img.min())
#     cv2.imwrite('./label_process/{}'.format(i), img)
#
# for i in os.listdir('./label_process'):
#     path=os.path.join('./label_process',i)
#     img=cv2.imread(path)
#     print(path)
#     yanse_num(img)

# for i in os.listdir('./label_a'):
#     path=os.path.join('./label_a',i)
#     img=cv2.imread(path)
#     print(path)
#     yanse_num(img)

for i in os.listdir('./yuantu'):

    # 加载要拼接的两张图片
    image1 = cv2.imread('./yuantu/{}'.format(i))
    image2 = cv2.imread('./label_a/{}'.format(i))

    # 将两张图片按水平方向拼接
    result = cv2.hconcat([image1, image2])
    print(i)
    # 展示拼接后的结果
    cv2.imwrite('./123/{}'.format(i), result)

#
# import os
# from PyQt5.QtCore import Qt, QRectF, QRect, QPoint
# from PyQt5.QtGui import QImage, QPainter, QPen, QPixmap
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QFileDialog
#
#
# class ImageCropper(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # 初始化界面
#         self.init_ui()
#
#         # 文件列表
#         self.files = []
#         self.current_file_index = -1
#
#         # 当前截图状态
#         self.dragging = False
#         self.start_drag_pos = None
#         self.end_drag_pos = None
#
#     def init_ui(self):
#         # 设置窗口标题
#         self.setWindowTitle("图片裁剪器")
#
#         # 设置菜单栏
#         menubar = self.menuBar()
#         file_menu = menubar.addMenu("文件")
#         open_action = QAction("打开文件夹", self)
#         open_action.triggered.connect(self.on_open_folder_clicked)
#         file_menu.addAction(open_action)
#
#         # 添加工具栏按钮
#         toolbar = self.addToolBar("")
#         prev_action = QAction("上一张", self)
#         prev_action.triggered.connect(self.on_prev_button_clicked)
#         next_action = QAction("下一张", self)
#         next_action.triggered.connect(self.on_next_button_clicked)
#         toolbar.addAction(prev_action)
#         toolbar.addAction(next_action)
#
#         # 显示图片区域
#         self.image_label = QLabel(self)
#         self.setCentralWidget(self.image_label)
#
#         # 设置图片区域鼠标事件
#         self.image_label.setMouseTracking(True)
#         self.image_label.mousePressEvent = self.on_mouse_press_event
#         self.image_label.mouseMoveEvent = self.on_mouse_move_event
#         self.image_label.mouseReleaseEvent = self.on_mouse_release_event
#
#     def on_open_folder_clicked(self):
#         # 选择文件夹
#         folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
#         if folder_path:
#             # 获取文件列表
#             self.files = [os.path.join(folder_path, file_name)
#                           for file_name in os.listdir(folder_path)
#                           if file_name.endswith(".jpg") or file_name.endswith(".png")]
#             print(self.files)
#             if len(self.files) > 0:
#                 # 显示第一张图片
#                 self.current_file_index = 0
#                 self.show_image()
#
#     def on_prev_button_clicked(self):
#         # 显示上一张图片
#         if self.current_file_index > 0:
#             self.current_file_index -= 1
#             self.show_image()
#
#     def on_next_button_clicked(self):
#         # 显示下一张图片
#         if self.current_file_index < len(self.files) - 1:
#             self.current_file_index += 1
#             self.show_image()
#
#     def show_image(self):
#         # 加载图片到QImage对象
#         image = QImage()
#         if image.load(self.files[self.current_file_index]):
#             # 显示图片
#             self.image_label.setPixmap(QPixmap.fromImage(image))
#             self.image_label.adjustSize()
#
#     def on_mouse_press_event(self, event):
#         if event.button() == Qt.LeftButton:
#             self.dragging = True
#             self.start_drag_pos = event.pos()
#
#     def on_mouse_move_event(self, event):
#         if self.dragging:
#             # 记录拖动结束点
#             self.end_drag_pos = event.pos()
#
#             # 刷新图片显示
#             self.show_image()
#
#             # 绘制矩形框
#             painter = QPainter(self.image_label.pixmap())
#             painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
#             rect = QRect(self.start_drag_pos.x()-1, self.start_drag_pos.y()-1,
#                          768+2,
#                          384+2)
#             painter.drawRect(rect)
#             painter.end()
#
#     def on_mouse_release_event(self, event):
#         if event.button() == Qt.LeftButton:
#             if self.dragging:
#                 # 记录拖动结束点
#
#
#
#
#
#
#
#                 # 计算裁剪区域
#                 x = self.start_drag_pos.x()
#                 y = self.start_drag_pos.y()
#                 width = 768
#                 height = 384
#
#                 # 裁剪并保存图片
#                 image = QImage(self.image_label.pixmap().toImage())
#                 cropped_image = image.copy(x, y, width, height)
#                 # save_path, _ = QFileDialog.getSaveFileName(parent=self,
#                 #                                            caption="保存文件",
#                 #                                            filter="PNG (*.png);;JPEG (*.jpg)")
#                 # if save_path != "":
#                 #     cropped_image.save(save_path)
#
#                 save_path=os.path.join(self.files[self.current_file_index].replace('A','crop2'))
#                 print(self.files[self.current_file_index],save_path)
#                 cropped_image.save(save_path)
#             # 重置状态
#             self.dragging = False
#             self.start_drag_pos = None
#             self.end_drag_pos = None
#
#
# if __name__ == '__main__':
#     app = QApplication([])
#     cropper = ImageCropper()
#     cropper.show()
#     app.exec_()

# from PIL import Image
#
# # 指定3张图片路径
# img_path_1 = './C/14.png'
# img_path_2 = './B/14.png'
# img_path_3 = './A/14.jpg'
#
# # 打开3张图片并获取宽度和高度
# img_1 = Image.open(img_path_1)
# img_2 = Image.open(img_path_2)
# img_3 = Image.open(img_path_3)
#
# new_width = img_1.width + img_2.width + img_3.width
# new_height = max(img_1.height, img_2.height, img_3.height)
#
# # 创建新图像对象，并将之前的3张图片拼接成一张新的横向的图像
# new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
# new_img.paste(img_1, (0, 0))
# new_img.paste(img_2, (img_1.width, 0))
# new_img.paste(img_3, (img_1.width+img_2.width, 0))
#
# # 将新图像保存到磁盘
# new_img.save('new_image1.jpg')







# from PIL import Image
#
# # 指定两张图片路径
# img_path_1 = './new_image.jpg'
# img_path_2 = './new_image1.jpg'
#
# # 打开两张图片并获取宽度和高度
# img_1 = Image.open(img_path_1)
# img_2 = Image.open(img_path_2)
#
# new_width = max(img_1.width, img_2.width)
# new_height = img_1.height + img_2.height
#
# # 创建新图像对象，并将之前的两张图片拼接成一张新的纵向的图像
# new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
# new_img.paste(img_1, (0, 0))
# new_img.paste(img_2, (0, img_1.height))
#
# # 将新图像保存到磁盘
# new_img.save('new_image2.jpg')

# aa=37
# for i in os.listdir('./crop2'):
#     path=os.path.join('./crop2',i)
#     img=cv2.imread(path)
#     path1=os.path.join('./crop1/','{}.png'.format(aa))
#     print(path1)
#     cv2.imwrite(path1,img)
#     aa+=1
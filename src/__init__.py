"""占位用，丢代码片段"""

# op = QGraphicsOpacityEffect()
# # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
# op.setOpacity(0.1)
# self.ui.output_box.setGraphicsEffect(op)
# self.ui.output_box.setAutoFillBackground(True)
#
# op2 = QGraphicsBlurEffect()
# op2.setBlurRadius(12)
# self.setGraphicsEffect(op2)
# #     # 设置背景色
# #     # # self.bgColor = QColor(255, 50, 50, 80)  # 可以根据个人需要调节透明度
#     self.bgColor = QColor(255, 255, 255, 50)  # 可以根据个人需要调节透明度
# #
#     # 调用api
#     hWnd = HWND(int(self.winId()))  # 直接HWND(self.winId())会报错
#     cdll.LoadLibrary(r'utils\ui_manager\Aero\aeroDll.dll').setBlur(hWnd)  # dll和脚本放在同一个目录下会报错找不到dll
#     #出自 https://www.cnblogs.com/zhiyiYo/p/14643855.html
# #
# #
# def paintEvent(self, e):
#     """ 绘制背景,添加上一层蒙版 """
#     painter = QPainter(self)
#     painter.setRenderHint(QPainter.Antialiasing)
#     painter.setPen(Qt.NoPen)
#     painter.setBrush(self.bgColor)
#     painter.drawRoundedRect(self.rect(), 20, 20)

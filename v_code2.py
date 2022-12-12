import pytesseract
from PIL import Image

image = Image.open('2.png')

#对图像做灰度处理
image = image.convert('L')

#对图像做二值化处理
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')

#打印结果
print(pytesseract.image_to_string(image))
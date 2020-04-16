from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

image = Image.open("../res/images/man.jpg")
w, h = image.size
image.thumbnail((w // 2, h // 2))
image.save("../res/images/thumbMan.jpg", 'jpeg')

image2 = image.filter(ImageFilter.BLUR)
image2.save("../res/images/blurImage.jpg", 'jpeg')


# 随机字母:
def rnd_char():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rnd_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2:
def rnd_color2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def create():
    width = 60 * 4
    height = 60
    image1 = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('../res/font/DJB-Get-Digital-1.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image1)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rnd_color())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())
    # 模糊:
    image1 = image1.filter(ImageFilter.BLUR)
    image1.save('../res/images/code.jpg', 'jpeg')


if __name__ == "__main__":
    print("ps")
    create()

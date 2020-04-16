from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create():
    image = Image.open("../res/images/animal.jpg")
    for x in range(300,500):
        for y in range(200,400):
            image.putpixel((x, y), (128, 128, 128))
    image.show()
    image.save("../res/images/pix.jpg",'jpeg')







if __name__ == "__main__":
    print("ps")
    create()

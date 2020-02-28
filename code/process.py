from random import randint
from time import time,sleep

def downLoad(filename):
    print("开始下载" +filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    downLoad("test.pdf")
    downLoad("sounfd.avi")
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == "__main__":
    main()

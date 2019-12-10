import pytesseract as pt
# import requests
from PIL import Image
import pyperclip
import keyboard

# 从PyObjC库的AppKit模块引用NSPasteboard主类，和PNG、TIFF的格式类
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF, NSPasteboardTypeString

def write_to_file(text, filepath):
    with open(filepath, 'w') as file:
        file.write(text)

def excute_ocr(filepath):
    # url = "https://china-testing.github.io/images/python_lib_ocr.PNG"
    # img = Image.open(requests.get(url, stream=True).raw)
    img = Image.open(filepath)
    text = pt.image_to_string(img)
    # write_to_file(text, '/Users/macpro/PycharmProjects/mutils/tmp/test.txt')
    # text = pt.image_to_string(img, lang='chi_sim')    #中文
    pyperclip.copy(text)


def get_paste_img_file(filepath):
    """
    将剪切板数据保存到本地文件并返回文件路径
    """
    pb = NSPasteboard.generalPasteboard()  # 获取当前系统剪切板数据
    data_type = pb.types()  # 获取剪切板数据的格式类型

    # 根据剪切板数据类型进行处理
    if NSPasteboardTypePNG in data_type:          # PNG处理
        data = pb.dataForType_(NSPasteboardTypePNG)
        # print('png: '+str(type(data)))
        # filename = 'HELLO_PNG.png'
        # filepath = 'tmp/%s' % filename            # 保存文件的路径
        ret = data.writeToFile_atomically_(filepath, False)    # 将剪切板数据保存为文件
        if ret:   # 判断文件写入是否成功
            return data
    elif NSPasteboardTypeTIFF in data_type:         #TIFF处理： 一般剪切板里都是这种
        # tiff
        data = pb.dataForType_(NSPasteboardTypeTIFF)
        # print('tiff: '+str(type(data)))
        filename = 'HELLO_TIFF.tiff'
        filepath = '/tmp/%s' % filename
        ret = data.writeToFile_atomically_(filepath, False)
        if ret:
            return data
    elif NSPasteboardTypeString in data_type:
        # string todo, recognise url of png & jpg
        pass

def clipboard_image_text_clipboard():
    filepath = '/Users/macpro/PycharmProjects/mutils/images/ocr_test.png'
    data = get_paste_img_file(filepath)
    print(str(type(data)))
    excute_ocr(filepath)

def test():
    print('test')


def init_hot_key():
    keyboard.add_hotkey('f1', clipboard_image_text_clipboard)
    # keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey')) # 已发现无法监听ctrl、command等控制按键
    keyboard.wait()


# if __name__ == '__main__':
# init_hot_key()
clipboard_image_text_clipboard()
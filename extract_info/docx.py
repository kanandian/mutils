import os
from win32com import client as wc

def save_doc_to_docx(rawpath):  # doc转docx
    '''
    :param rawpath: 传入和传出文件夹的路径
    :return: None
    '''
    word = wc.Dispatch("Word.Application")
    # 不能用相对路径，老老实实用绝对路径
    # 需要处理的文件所在文件夹目录
    filenamelist = os.listdir(rawpath)
    for i in os.listdir(rawpath):
        # 找出文件中以.doc结尾并且不以~$开头的文件（~$是为了排除临时文件的）
        if i.endswith('.doc') and not i.startswith('~$'):
            print(i)
            # try
            # 打开文件
            doc = word.Documents.Open(rawpath + '/' + i)
            # # 将文件名与后缀分割
            rename = os.path.splitext(i)
            # 将文件另存为.docx
            doc.SaveAs(rawpath + '/' + rename[0] + '.docx', 12)  # 12表示docx格式
            doc.Close()
    word.Quit()


rawpath = 'E:/mycode/python/mutils/files'
save_doc_to_docx(rawpath)
import re

from extract_info.config import all_items, selected_items, separators, folder_path

beigao = ['被告人','被告']
benyuanrenwei = ['本院认为']

separators = '|'.join(separators)

def extract_start(item, para):
    parts = re.split(separators, para[len(item):])
    for part in parts:
        if part is not None and part != '':
            if len(part)>3:
                return None
            return part
            break
    return None

def extract_first_sentence(item, para):
    parts = re.split('。', para[len(item):])
    return parts[0][len(item):]

def handle_anhao(article):
    return article[2]

def handle_beigaoren(article):
    res = list()
    for para in article:
        for item in beigao:
            if para.startswith(item):
                rr = extract_start(item, para)
                if rr == None:
                    continue
                res.append(rr)
                break
    return res

def handle_benyuanrenwei(article):
    res = list()
    for para in article:
        for item in benyuanrenwei:
            if para.startswith(item):
                res.append(extract_first_sentence(item, para))
    return res
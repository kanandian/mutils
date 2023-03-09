# s = '我 很 帅 pip install laozi   '


def isChinese(letter):
    if '\u4e00' <= letter <= '\u9fa5':
        return True
    return False


def trimChinese(text):
    text = list(text)
    removeNums = []
    for i in range(len(text)-1):
        if i == 0:
            continue
        if text[i] == ' ' and isChinese(text[i-1]) and isChinese(text[i+1]):
            removeNums.append(i)
    for i in reversed(removeNums):
        del text[i]
    text = ''.join(text).strip()

    return text

# print(trimChinese(s))
astr = '佛奥私房话'
substr = '佛奥'
print(astr[len(substr):])

import win32clipboard

win32clipboard.OpenClipboard()
text_from_clipboard = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

print(text_from_clipboard)
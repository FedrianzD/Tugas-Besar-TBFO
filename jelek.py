from html.parser import HTMLParser
import numpy as np

arr = []

accepted_tag = ['<html>', '<head>', '<body>', '<title>', '<script>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>', '<p>', '<em>', '<b>', '<abbr>', '<strong>', '<small>', '<div>', '<th>', '<td>', '<tr>', '<table>', '<img>', '<br>', '<hr>', '<a>', '<button>', '<link>', '<form>', '<input>', 'Rel', 'href', 'src', 'alt', 'type', 'action', 'method', '</html>', '</head>', '</body>', '</title>', '</script>', '</h1>', '</h2>', '</h3>', '</h4>', '</h5>', '</h6>', '</p>', '</em>', '</b>', '</abbr>', '</strong>', '</small>', '</div>', '</th>', '</td>', '</tr>', '>', '"', 'get', '/>', 'post', 'submit', 'reset', 'button', '</button>', '</form>', '</a>', '</script>', '%', 'eps', 'class', 'id', 'style', 'text' , 'password', 'email', 'number', 'checkbox', 'input', '=', 'rel']


def editArr(arr):

# Misahin "a" jadi " a "
    i = 0  
    while i < len(arr):
        if arr[i] not in accepted_tag:
            
            if arr[i][0] == '"' and arr[i][1] == '"':
                arr.pop(i)
                arr.insert(i, '"')
                arr.insert(i+1, '"')
                i += 2
            elif arr[i][0] == '"' and arr[i][-1] == '"':
                yangdinsert = arr[i][1:-1]
                arr.pop(i)
                arr.insert(i, '"')
                arr.insert(i+1, yangdinsert)
                arr.insert(i+2, '"')
                i += 3  
            elif arr[i][0] == '"':
                yangdinsert = arr[i][1:]
                arr.pop(i)
                arr.insert(i, '"')
                arr.insert(i+1, yangdinsert)
            elif arr[i][-1] == '"':
                yangdinsert = arr[i][0:-1]
                arr.pop(i)
                arr.insert(i, yangdinsert)
                arr.insert(i+1, '"')
            else:
                i += 1 
        else:
            i+=1

# Nambahin eps ke img
    for i in range(4):
        arr.append('temp')
    i = 0  
    while i < len(arr):
        if (arr[i] == 'src'):
            if (arr[i+4] != 'alt') and arr[i+2] == '%':
                arr.insert(i+4, 'eps')
            elif (arr[i+3] != 'alt') and arr[i+2] == '"':
                arr.insert(i+3, 'eps')
        i += 1 
    for i in range(4):
        arr.pop(len(arr)-1)

# Nambahin eps ke input

    arr.append('temp')
    i = 0  
    while i < len(arr)-1:
        if (arr[i] == 'input') and (arr[i+1] != 'type'):
            arr.insert(i+2, 'eps')
        i = i + 1
    arr.pop(len(arr)-1)

# Ganti random text jadi %
    i = 0
    while i < len(arr):
        if arr[i] not in accepted_tag:
            arr[i] = '%'
        i += 1

# Ganti get sama post jadi % kalo dia bukan value dari method 
    arr.insert(0, 'temp')
    arr.insert(0, 'temp')
    i = 2
    while i < len(arr):
        if arr[i] in ['get', 'post']:
            if arr[i-2] != 'method':
                arr[i] = '%'
        i += 1
    arr.pop(0)
    arr.pop(0)

# Ganti value text, password, email, number, checkbox jadi % kalo dia bukan value dari input 
    arr.append(0)
    i = 2
    while i < len(arr):
        if arr[i] in ['text', 'password', 'email', 'number', 'checkbox']:
            if arr[i-2] != 'type' and arr[i-4] != '<input>':
                arr[i] = '%'
        i += 1
    arr.pop(len(arr)-1)

# Nambahin * ke atribut global
    i = 0
    while i < len(arr):
        if arr[i] in ['class', 'id', 'style']:
            arr[i] = f"*{arr[i]}"
        i += 1

# Merge % sama %
    arr.append('temp')
    i = 1
    while i < len(arr):
        if arr[i] == '%' and arr[i-1] == '%':
            arr.pop(i)
        else:
            i += 1
    arr.pop(len(arr)-1)

# Switch = sama elemen selanjutnya. 
    # arr.append('temp')
    i = 0
    while i < len(arr) -1 :
        if arr[i] == '=':
            arr[i+1] = arr[i+1] + '='
        i += 1

    while '=' in arr:
        arr.remove('=')    
    # arr.pop(len(arr)-1)

def tanganiTeks(arr, item):
    # arr.append("ini teks ->")
    if item[0] == "\"" and item[-1] == "\"":
        if item[1:-1] in ['get', 'post', 'submit', 'reset', 'button', 'class', 'id', 'style', 'text' , 'password', 'email', 'number', 'checkbox', 'input']:
            arr.append(item) # diubah dari item[1:-1]
        else:
            # arr.append("\"")
            arr.append(f"{item}")
            # arr.append("\"")
    else:
        arr.append(f"{item}")

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # pass
        if tag in ['html', 'head', 'body', 'title', 'script', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'em', 'b', 'abbr', 'strong', 'small', 'div', 'th', 'td', 'tr', 'table', 'img', 'br', 'hr', 'a', 'button', 'link', 'form', 'input']:
            
            for item in HTMLParser.get_starttag_text(self).split(" "):
                if '=' in list(item):
                    arr.append('=')
                for item_i in item.split("="):
                    # arr.append("=")
                    # tanganiTeks(arr, item_i)
                    for item_i_j in item_i.split("/"):
                        if ">" in item_i_j:
                            # masuk sini udah pasti
                            # item_i_j mengandung closing tag
                            for item_i_j_k in item_i_j.split(">"):
                                if item_i_j_k == "":
                                    # arr.append(">")
                                    temp = arr.copy()
                                    temp.reverse()
                                    for x in temp:
                                        if x in ['<html', '<head', '<body', '<title', '<script', '<h1', '<h2', '<h3', '<h4', '<h5', '<h6', '<p', '<em', '<b', '<abbr', '<strong', '<small', '<div', '<th', '<td', '<tr', '<table', '<img', '<br', '<hr', '<a', '<button', '<link', '<form', '<input']:
                                            arr.insert(len(arr) - 1 - temp.index(x), f"{x}>")
                                            arr.remove(x)                                
                                            break
                                else:
                                   
                                    tanganiTeks(arr, item_i_j_k)    
                                    # arr.append(f"{item_i_j_k}")    
                        elif item_i_j == "":
                            arr.append("blank")
                        else:
                            
                            tanganiTeks(arr, item_i_j)


    def handle_endtag(self, tag):
        if tag in ['html', 'head', 'body', 'title', 'script', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'em', 'b', 'abbr', 'strong', 'small', 'div', 'th', 'td', 'tr', 'table', 'button', 'a', 'form', 'script', ]:
            arr.append(f"</{tag}>")

    def handle_data(self, data):
        if not data.isspace():
            arr.append('%')

    def handle_comment(self, data):
        arr.append("comment")

parser = MyHTMLParser()

pathindex = 'index.html'
pathlowerindex = 'indexlower.html'

with open(pathindex, 'r', encoding='utf-8') as file:
    htmlfile = file.read()
content_lowercase = htmlfile.lower()
with open(pathlowerindex, 'w', encoding='utf-8') as file:
    file.write(content_lowercase)
with open(pathlowerindex, 'r', encoding='utf-8') as file:
    htmlfile = file.read()

parser.feed(htmlfile)
print(arr)
editArr(arr)
print(arr)

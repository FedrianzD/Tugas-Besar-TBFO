from html.parser import HTMLParser

arr = []

accepted_tag = ['<html>', '<head>', '<body>', '<title>', '<script>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>', '<p>', '<em>', '<b>', '<abbr>', '<strong>', '<small>', '<div>', '<th>', '<td>', '<tr>', '<table>', '<img', '<br', '<hr', '<a', '<button', '<link', '<form', '<input', 'Rel', 'href', 'src', 'alt', 'type', 'action', 'method', '</html>', '</head>', '</body>', '</title>', '</script>', '</h1>', '</h2>', '</h3>', '</h4>', '</h5>', '</h6>', '</p>', '</em>', '</b>', '</abbr>', '</strong>', '</small>', '</div>', '</th>', '</td>', '</tr>', '>', '"', 'get', '/>', 'post', 'submit', 'reset', 'button', '</button>', '</form>', '</a>', '</script>']

def editArr(arr):
    for i in range(len(arr)):
        if arr[i] not in accepted_tag:
            arr[i] = 'text'
    arr.append(0)
    i = 1
    while i < len(arr):
        if arr[i] == 'text' and arr[i-1] == 'text':
            arr.pop(i)
        else:
            i += 1
    arr.pop(len(arr)-1)

def tanganiTeks(arr, item):
    # arr.append("ini teks ->")
    if item[0] == "\"" and item[-1] == "\"":
        if item[1:-1] in ['get', 'post', '"submit"', '"reset"', 'button']:
            arr.append(item[1:-1])
        else:
            arr.append("\"")
            arr.append("text")
            arr.append("\"")
    else:
        arr.append(f"{item}")

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # pass
        print("LALA",tag)
        if tag in ['html', 'head', 'body', 'button', 'title', 'script', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'em', 'b', 'abbr', 'strong', 'small', 'div', 'th', 'td', 'tr', 'table']:
            arr.append(f"<{tag}>")
            # arr.append(attrs)
        elif tag in ['img', 'br', 'hr', 'a', 'button', 'link', 'form', 'input']:
            # arr.append(f"<{tag}")
            for item in HTMLParser.get_starttag_text(self).split(" "):
                for item_i in item.split("="):
                    # tanganiTeks(arr, item_i)
                    for item_i_j in item_i.split("/"):
                        if ">" in item_i_j:
                            # masuk sini udah pasti
                            # item_i_j mengandung closing tag
                            for item_i_j_k in item_i_j.split(">"):
                                if item_i_j_k == "":
                                    arr.append("/>")
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
            arr.append('text')

    def handle_comment(self, data):
        arr.append(data)

parser = MyHTMLParser()

path = './index.html'
with open(path, 'r', encoding='utf-8') as file:
    htmlfile = file.read()

parser.feed(htmlfile)

editArr(arr)

for i in arr:
    print(i)
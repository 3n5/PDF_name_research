"""フォルダー内にあるpdfの表紙を画像検索かけて自分で名前を入力していく"""
"""出来れば重複するキーワードとかを抜き出して自動入力処理したいけどxml情報が持ってこれない"""

folder_name = 'C:/Users/USER/Desktop/test'
def pdf2jpg(_name):
    import base64
    import PyPDF2
    pdf = PyPDF2.PdfFileReader('{0}/{1}.pdf'.format(folder_name,_name))
    xObject = pdf.pages[0]['/Resources']['/XObject'].getObject()
    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            if xObject[obj]['/Filter'] == '/DCTDecode':
                _dir = "{0}/jpg/{1}.jpg".format(folder_name, _name)
                img = open(_dir, "wb")
                img.write(xObject[obj]._data)  
                img.close()
    return _dir
            
def reverse_image_search(_name):
    #ref 逆画像検索 https://stackoverrun.com/ja/q/6373770
    import requests
    filePath = _name#"{0}.jpg".format(_name)
    searchUrl = 'http://www.google.hr/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    return fetchUrl

def name_change(url_name, root_name):
    from urllib.parse import parse_qsl
    from urllib.parse import urlparse
    import urllib
    from bs4 import BeautifulSoup
    from requests import get as GET
    import re
    import os
    import sys
    import webbrowser

    print("\n"+"-"*15+root_name+"-"*15)
    webbrowser.open(url_name)
    if add_name == "a":
        pass
    else:
        after_name = root_name
        pos = after_name.find(']')
        after_name=after_name[:pos]
        os.rename("{0}/{1}{2}".format(folder_name, root_name, root_ext),
                  "{0}/{1}] {2}{3}".format(folder_name, after_name, add_name, root_ext))

if __name__ == '__main__':
    import os
    files = os.listdir(folder_name)
    for _name in files:
        root_name = os.path.splitext(_name)[0]
        root_ext = os.path.splitext(_name)[1]
        if root_ext=='.pdf':
            _path=pdf2jpg(root_name)
            _url=reverse_image_search(_path)
            name_change(_url, root_name)
        
            


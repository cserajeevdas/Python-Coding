import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("encountered comment:", data)
        pos = self.getpos()
        print("\tAt lin:", pos[0], " Position", pos[1])
    def handle_endtag(self, data):
        print("encountered end tag:", data)
        pos = self.getpos()
        print("\tAt lin:", pos[0], " Position", pos[1])    
    def handle_data(self, data):
        print("encountered data:", data)
        pos = self.getpos()
        print("\tAt lin:", pos[0], " Position", pos[1])    
    def handle_charref(self, data):
        if data.startswith('s'):
            c = chr(int(data[1:], 16))
        else:
            c = chr(int(data))
        print("Num ent  :", c)                                 

def main():
    parser = MyHTMLParser()
    f= open("D:\MyWork\python_code\HTML download link.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)
if __name__=="__main__":
    main()

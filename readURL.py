import urllib.request

def main():
    webUrl = urllib.request.urlopen("https://mail.google.com/mail/u/0/#inbox")
    print("result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)
if __name__=="__main__":
    main()

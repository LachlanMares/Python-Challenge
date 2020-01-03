import urllib.request
import re
import bz2


if __name__ == '__main__':

    url = "http://www.pythonchallenge.com/pc/def/integrity.html"
    prevCodeword = "integrity"
    source = urllib.request.urlopen(url).read()
    un = eval("b%s" % re.search(b"un: (.*?)\n", source).group(1).decode())
    pw = eval("b%s" % re.search(b"pw: (.*?)\n", source).group(1).decode())

    user_name = bz2.decompress(un).decode()
    password = bz2.decompress(pw).decode()

    print("Username:", user_name)
    print("Password:", password)

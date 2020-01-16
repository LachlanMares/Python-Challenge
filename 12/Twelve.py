import urllib.request
import shutil
import re
from PIL import Image
import numpy as np


def download_file_from_url_with_auth_manager(local_url, file_name, usr, pwd):
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, local_url, usr, pwd)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    opener.open(local_url)
    urllib.request.install_opener(opener)
    with urllib.request.urlopen(local_url) as _response, open(file_name, 'wb') as file:
        shutil.copyfileobj(_response, file)


def auth_manager(local_url, usr, pwd):
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, local_url, usr, pwd)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    opener.open(local_url)
    urllib.request.install_opener(opener)
    return urllib.request.urlopen(local_url).read()


if __name__ == '__main__':

    username, password = 'huge', 'file'
    url = "http://www.pythonchallenge.com/pc/return/evil.html"
    source = auth_manager(url, username, password)
    imageFileName = re.findall(b"[a-z]+[0-9]+[.][a-z]+", source, flags=re.DOTALL)[-1].strip().decode()

    newUrl = "http://www.pythonchallenge.com/pc/return/" + imageFileName
    download_file_from_url_with_auth_manager(newUrl, imageFileName, username, password)
    img = Image.open(imageFileName)
    img.show()

    lastFileNumber = 1
    moreEvils = True

    while moreEvils:
        lastFileNumber = lastFileNumber + 1

        try:
            imageFileName = "evil" + str(lastFileNumber) + ".jpg"
            newUrl = "http://www.pythonchallenge.com/pc/return/" + imageFileName
            download_file_from_url_with_auth_manager(newUrl, imageFileName, username, password)
            img = Image.open(imageFileName)
            img.show()

        except:
            print(auth_manager("http://www.pythonchallenge.com/pc/return/evil" + str(lastFileNumber) + ".jpg", username, password))
            print("no more evils")
            lastFileNumber = lastFileNumber + 1
            imageFileName = "evil2.gfx"
            newUrl = "http://www.pythonchallenge.com/pc/return/" + imageFileName
            moreEvils = False

    download_file_from_url_with_auth_manager(newUrl, imageFileName, username, password)

    fileName = ''
    data = open(imageFileName, "rb").read()

    for fileNum in range(0, lastFileNumber):
        fileData = data[fileNum::lastFileNumber]
        try:
            fileType = (re.findall(b"(PNG|GIF|JFIF)", fileData, flags=re.DOTALL)[-1].strip().decode())
        except:
            fileType = "None"

        if fileType == "PNG":
            fileName = 'hint{0}.png'.format(fileNum)
        elif fileType == "GIF":
            fileName = 'hint{0}.gif'.format(fileNum)
        else:
            fileName = 'hint{0}.jpg'.format(fileNum)

        open(fileName, 'wb').write(fileData)

    print("http://www.pythonchallenge.com/pc/return/disproportional.html")





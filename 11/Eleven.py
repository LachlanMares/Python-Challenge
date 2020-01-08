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
    url = "http://www.pythonchallenge.com/pc/return/5808.html"
    source = auth_manager(url, username, password)
    imageFileName = re.findall(b"[a-z]+[.][a-z]+", source, flags=re.DOTALL)[-1].strip().decode()

    newUrl = url.replace("5808.html", imageFileName)
    download_file_from_url_with_auth_manager(newUrl, imageFileName, username, password)

    img = Image.open(imageFileName)
    npImg = np.array(img)
    img.close()

    evenImg = Image.fromarray(npImg[::2, ::2, :])
    oddImg = Image.fromarray(npImg[1::2, 1::2, :])

    evenImg.show()
    oddImg.show()

    print(url.replace("5808", "evil"))
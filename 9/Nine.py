import urllib.request
import shutil
import re
import bz2
from PIL import Image


def download_file_from_url(local_url, file_name):
    with urllib.request.urlopen(local_url) as _response, open(file_name, 'wb') as file:
        shutil.copyfileobj(_response, file)

if __name__ == '__main__':

    challengeEightUrl = "http://www.pythonchallenge.com/pc/def/integrity.html"

    source = urllib.request.urlopen(challengeEightUrl).read()
    un = eval("b%s" % re.search(b"un: (.*?)\n", source).group(1).decode())
    pw = eval("b%s" % re.search(b"pw: (.*?)\n", source).group(1).decode())

    user_name = bz2.decompress(un).decode()
    password = bz2.decompress(pw).decode()

    url = "http://www.pythonchallenge.com/pc/return/good.html"

    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    password_mgr.add_password(None, url, user_name, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)

    source = urllib.request.urlopen(url).read()
    prevCodeword = "good"
    searchFor = prevCodeword + "(.[a-z]+)"
    fileType = re.search(searchFor, str(source)).group(1)
    imageFileName = prevCodeword + fileType

    firstSet = re.search(b'first:((.|\n)*)second', source).group(1).strip().decode()
    secondSet = re.search(b'second:((.|\n)*)-->', source).group(1).strip().decode()

    firstSet = firstSet.replace('\n','').split(',')
    secondSet = secondSet.replace('\n', '').split(',')
    combinedSet = firstSet + secondSet

    oriImage = Image.open(imageFileName)
    mode = oriImage.mode
    shape = oriImage.size
    oriImage.close()

    print(mode)
    img = Image.new(mode, shape)
    pixels = img.load()

    for i in range(0, len(combinedSet), 2):
        x = int(combinedSet[i])
        y = int(combinedSet[i + 1])
        # insert a white pixel
        pixels[x, y] = (255, 255, 255, 255)

    img.show()

    print(url.replace("good","bull"))
import urllib.request
import shutil
import re
from PIL import Image

def download_file_from_url(local_url, file_name):
    with urllib.request.urlopen(local_url) as _response, open(file_name, 'wb') as file:
        shutil.copyfileobj(_response, file)

if __name__ == '__main__':

    url = "http://www.pythonchallenge.com/pc/def/oxygen.html"
    prevCodeword = "oxygen"
    source = urllib.request.urlopen(url).read()
    searchFor = prevCodeword + "(.[a-z]+)"
    fileType = re.findall(searchFor, str(source), flags=re.DOTALL)[-1].strip()
    imageFileName = prevCodeword + fileType

    newUrl = url.replace(".html", fileType)
    download_file_from_url(newUrl, imageFileName)

    img = Image.open(imageFileName)

    firstGreyscaleRow = 0

    for i in range(img.height):
        firstPixel = img.getpixel((0,i))
        if firstPixel[0] == firstPixel[1] == firstPixel[2]:
            firstGreyscaleRow = i
            break

    firstGreyscaleRowValues = [img.getpixel((j, firstGreyscaleRow)) for j in range(img.width)]
    firstGreyscaleRowValues = firstGreyscaleRowValues[::7]

    pixelValues = [chr(r) for r, g, b, a in firstGreyscaleRowValues if r == g == b]
    clueString = "".join(pixelValues)
    print(clueString)

    nextClue = re.search(r'\[(.*?)\]', clueString).group(1).split(',')
    nextClueString = "".join([chr(int(c)) for c in nextClue])

    print(url.replace("oxygen", nextClueString))
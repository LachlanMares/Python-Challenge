import urllib.request
import re

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    source = urllib.request.urlopen(url).read()
    challengeText = re.findall(b"<!--(.*?)-->", source, flags=re.DOTALL)[-1].strip().decode()
    standardCharaters = re.findall('[a-z]', challengeText)
    newUrl = url.replace("ocr", ''.join(standardCharaters))
    print(newUrl)
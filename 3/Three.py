import urllib.request
import re

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/equality.html"
    source = urllib.request.urlopen(url).read()
    challengeText = re.findall(b"<!--(.*?)-->", source, flags=re.DOTALL)[-1].strip().decode()
    groupedCharaters = re.findall(r"[^A-Z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]+", challengeText)
    newUrl = url.replace("equality", ''.join(groupedCharaters))
    print(newUrl)
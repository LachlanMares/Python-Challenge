import urllib.request
import re
import pickle

if __name__ == '__main__':

    url = "http://www.pythonchallenge.com/pc/def/peak.html"
    newUrl = ""

    newSource = str(urllib.request.urlopen(url).read()).split('\n')

    for line in newSource:
        if "peakhell" in line:
            fileName = re.findall(r"[a-z]+[.][a-z]+", str(line), flags=re.DOTALL)[-1].strip()
            newUrl = url.replace("peak.html", fileName)

    bannerData = pickle.load(urllib.request.urlopen(newUrl))

    for row in bannerData:
        print("".join(char*num for char, num in row))

    print(url.replace("peak", "channel"))
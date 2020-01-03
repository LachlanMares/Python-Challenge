import urllib.request
import re


def get_the_nothing(url_local, nothing):
    _source = urllib.request.urlopen(url_local).read()

    try:
        _nothing = re.findall(b"and the next nothing is ([0-9]+)", _source)[0].decode()
        url_local = url_local.replace(nothing, _nothing)

    except:
        if _source == b"Yes. Divide by two and keep going.":
            _nothing = str(int(nothing) // 2)
            url_local = url_local.replace(nothing, _nothing)
        else:
            _nothing = re.findall(r"[a-z]+[.][a-z]+", str(_source), flags=re.DOTALL)[-1].strip()
            return "done", _nothing

    return url_local, _nothing


if __name__ == '__main__':

    url = "http://www.pythonchallenge.com/pc/def/linkedlist.html"
    source = str(urllib.request.urlopen(url).read())
    groupedCharaters = re.findall(r"[a-z]+[.][a-z]+", source, flags=re.DOTALL)[-1].strip()

    newUrl = url.replace("linkedlist.html", groupedCharaters)
    newSource = str(urllib.request.urlopen(newUrl).read()).split()
    newLink = ""

    for line in newSource:
        if groupedCharaters in line:
            newLink = line.split('"')[1]
            break

    newUrl = url.replace("linkedlist.html", newLink)
    firstNothing = newUrl.split('=')[-1]

    newUrl, prevNothing = get_the_nothing(newUrl, firstNothing)

    for i in range(0,400):

        newUrl, nextNothing = get_the_nothing(newUrl, prevNothing)

        if newUrl == "done":
            print(url.replace("linkedlist.html", nextNothing))
            break
        else:
            prevNothing = nextNothing

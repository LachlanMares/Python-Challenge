if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/0.html"
    url = url.replace("0", str(2**38))
    print(url)
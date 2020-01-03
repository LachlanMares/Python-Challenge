if __name__ == '__main__':

    challengeText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
                    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
                    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    translationTable = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")

    print(challengeText.translate(translationTable))

    url = "http://www.pythonchallenge.com/pc/def/map.html"
    translatedUrl = url.translate(translationTable).split('/')[-1]
    newUrl = url.replace("map", translatedUrl.split('.')[0])

    print(newUrl)
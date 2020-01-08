import urllib.request
import shutil
import re


def download_file_from_url(local_url, file_name):
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
    url = "http://www.pythonchallenge.com/pc/return/bull.html"
    source = auth_manager(url, username, password)
    link = re.findall(b"[a-z]+[.][a-z]+", source, flags=re.DOTALL)[-1].strip().decode()

    newUrl = url.replace("bull.html", link)
    a = auth_manager(newUrl, username, password).decode()

    for i in range(len(a)):
        if a[i].isnumeric():
            a = (a[i:]).replace(',','').strip().split()
            break

    seqLength = len(a)
    sequence = [a[0]]

    def nextSequenceMember(prevMember):
        nextMember = ""
        digitCount = 1

        for j in range(len(prevMember) - 1):
            if prevMember[j] == prevMember[j + 1]:
                digitCount = digitCount + 1
            else:
                nextMember = nextMember + "%s%s" % (digitCount, prevMember[j])
                digitCount = 1

        nextMember = nextMember + "%s%s" % (digitCount, prevMember[-1])
        return nextMember

    seqMatch = True

    for i in range(30):
        sequence.append(nextSequenceMember(sequence[-1]))
        if i < seqLength:
            if sequence[i] == a[i]:
                continue
            else:
                seqMatch = True
                break

    if seqMatch:
        print(url.replace("bull", str(len(sequence[-1]))))
    else:
        print("Sequence does not match")
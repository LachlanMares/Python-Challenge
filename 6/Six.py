import urllib.request
import re
import shutil
from zipfile import ZipFile


def download_archive_from_url(local_url, file_name):
    with urllib.request.urlopen(local_url) as _response, open(file_name, 'wb') as file:
        shutil.copyfileobj(_response, file)


def read_archived_files(archive_name, file_name):
    f = ZipFile(archive_name).open(file_name)
    _contents = f.read().decode()
    f.close()
    return _contents


def read_archived_file_comment(archive_name, file_name):
    try:
        _comment = ZipFile(archive_name).getinfo(file_name).comment.decode()
    except:
        _comment = ""

    return _comment


def read_archived_filenames(archive_name):
    f = ZipFile(archive_name)
    return f.namelist()


def get_the_nextfile(archive_name, file_name):
    _contents = read_archived_files(archive_name, file_name)
    _comment = ""

    try:
        _nextFilename = re.findall(r"Next nothing is ([0-9]+)", _contents)[0]
        _comment = read_archived_file_comment(archive_name, file_name)
        _done = False

    except:
        _nextFilename = ""
        _done = True

    return _nextFilename, _comment, _done


if __name__ == '__main__':

    url = "http://www.pythonchallenge.com/pc/def/channel.html"
    source = str(urllib.request.urlopen(url).read())
    fileType = re.findall(r"<--(.*?)-->", source, flags=re.DOTALL)[-1].strip()

    newUrl = url.replace(url.split('.')[-1], fileType)
    archiveName = newUrl.split('/')[-1]

    download_archive_from_url(newUrl, archiveName)

    nameList = read_archived_filenames(archiveName)

    startFile = ""

    for name in nameList:
        try:
            int(name.split('.')[0])
        except:
            startFile = name

    fileContents = read_archived_files(archiveName, startFile)
    fileComments = read_archived_file_comment(archiveName, startFile)

    nextFilename = re.findall(r"hint1: start from ([0-9]+)", fileContents)[0]
    done = False

    while done != True:
        nextFilename, fileComment, done = get_the_nextfile(archiveName, nextFilename+'.txt')
        fileComments = fileComments + fileComment


    print(fileComments)

    newUrl = url.replace("channel", "hockey")

    print(urllib.request.urlopen(newUrl).read().decode())

    line5String = fileComments.split("\n")[5]
    line5String = line5String.replace(" ", "").replace("*","")
    line5StringUnique = ""
    prevChar = ''

    for i in range(len(line5String)):
        if line5String[i] != prevChar:
            line5StringUnique += line5String[i]

        prevChar = line5String[i]

    newUrl = url.replace("channel", line5StringUnique.lower())
    print(newUrl)
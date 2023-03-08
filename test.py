import os.path
import re
from QuranReader import QuranReader
# opening a file
# file1 = open("last read aya.txt", 'w')
# file1.write("2,2")
# file1.close()
f = open("last read aya.txt", 'r')
content = f.read()


def isValidSuraAya():
    f = open("last read aya.txt", 'r')
    content = f.read()
    x = re.findall("\d,\d", content)
    if x:
        return True
    return False


def converSuraAyahNumber():
    if content:
        l = []
        l = content.split(',')
        sura = int(l[0])
        ayah = int(l[1])
        return sura, ayah
    return (1,1)
    
def getFirstAyah():
    quran = QuranReader()
    return quran.getAyah(1, 1)

def getAyah():
    result = converSuraAyahNumber()
    sura = int(result[0])
    ayah = int(result[1])
    quran = QuranReader()
    return quran.getAyah(sura, ayah)

if os.path.exists("last read aya.txt"):
    if isValidSuraAya():
        ayah = getAyah()
        print(ayah)
    else:
        ayah = getFirstAyah()
        print(ayah)
else:
    ayah = getFirstAyah()
    print(ayah)

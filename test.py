import xml.etree.ElementTree as et
tree = et.parse('en.ahmedali.xml')
root = tree.getroot()
# print("root info : ",root)
def printAyas(sura,i):
    for item in root.findall('./sura'):
        if(int(item.attrib['index']) == sura):
            for aya in item.iter():
                print(aya[i].attrib["text"])     
        
try:
    printAyas(1,0)
except:
    print("")
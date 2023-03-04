import xml.etree.ElementTree as et
tree = et.parse('en.ahmedali.xml')
root = tree.getroot()
# print("root info : ",root)
def printAyas(sura,i):
    for item in root.findall('./sura'):
        if(item.attrib['index'] == sura):
            for aya in item.iter():
                print(aya[i].attrib["text"])     
                break   

# root contains :
for item in root.findall('./sura'):
    sura = (item.attrib['index'])
    for aya in item.iter():
        i = int(aya.attrib['index'])
        print(i)
        printAyas(sura,i)
    

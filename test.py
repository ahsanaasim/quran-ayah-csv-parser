import xml.etree.ElementTree as et
tree = et.parse('en.ahmedali.xml')
root = tree.getroot()

def getAyah(surahIndex, ayahIndex):
    target = {
        'surahIndex': surahIndex,
        'surah': 'not-found',
        'ayahIndex': ayahIndex,
        'ayah': 'not-found',
    }
    for child in root:
        if (int(child.attrib['index']) == int(surahIndex)):
            target['surah'] = child.attrib['name']
            for ayah in child:
                if (int(ayah.attrib['index']) == int(ayahIndex)):
                    target['ayah'] = ayah.attrib['text']
                    return target
    return target
 
        
ayah = getAyah(2,66)
print(ayah)
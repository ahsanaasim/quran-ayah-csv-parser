import xml.etree.ElementTree as et
class QuranReader:
    def __init__(self):
        self.tree = et.parse('en.ahmedali.xml')
        self.root = self.tree.getroot()

    def getAyah(self, surahIndex, ayahIndex):
        target = {
            'surahIndex': surahIndex,
            'surah': 'not-found',
            'ayahIndex': ayahIndex,
            'ayah': 'not-found',
        }
        for child in self.root:
            if (int(child.attrib['index']) == int(surahIndex)):
                target['surah'] = child.attrib['name']
                for ayah in child:
                    if (int(ayah.attrib['index']) == int(ayahIndex)):
                        target['ayah'] = ayah.attrib['text']
                        return target
        return target
    
    
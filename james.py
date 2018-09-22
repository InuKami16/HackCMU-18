from music21 import converter,instrument # or import *
def convertSong():
    s = converter.parse('Disney_Themes_-_Whole_New_World.mid')
    count = 0
    for el in s.recurse():
        #print (el.classes)
        if 'Piano' in el.classes:
            el.activeSite.replace(el, instrument.ElectricGuitar())
            print (1) 
        elif  'StringInstrument' in el.classes:
            el.activeSite.replace(el, instrument.Bass())
            print (2)
        # if 'Instrument' in el.classes: # or 'Piano'
        #     el.activeSite.replace(el, instrument.ElectricGuitar())
        count += 1
    print (count)
    
    s.write('midi', 'newfilename.mid')


convertSong()
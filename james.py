from music21 import converter,instrument # or import *
def convertSong():
    s = converter.parse('Disney_Themes_-_Whole_New_World.mid')
    count = 0
    for el in s.recurse():
        try:
            lastNote = s.recurse().getElementsByClass('Note')[count]
            #print (note)
            #print (note.getContextByClass('Part'))
            print (type(lastNote.getContextByClass("Part")))
            if (note.getContextByClass("Part") == '0x107da7e48'):
                el.activeSite.replace(el, instrument.ElectricGuitar())
                print (1)
        except:
            pass
        # if 'Instrument' in el.classes: # or 'Piano'
        #     el.activeSite.replace(el, instrument.ElectricGuitar())
        count += 1
    print (count)
    
    s.write('midi', 'newfilename.mid')


convertSong()
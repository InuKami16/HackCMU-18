from music21 import midi

score = midi.translate.midiFilePathToStream('Disney_Themes_-_Whole_New_World.mid')
save = midi.translate.streamToMidiFile(score)
tracks = save.tracks

for track in tracks:
    event = track.events[1:2][0]
    
    for change in track.events:
        if change.type == 'PROGRAM_CHANGE':
            index = change.track.index
            if index == 0:
                change.data += 20

# after manipulation
save = midi.translate.midiFileToStream(save)
save.write('midi', 'new_song.mid')

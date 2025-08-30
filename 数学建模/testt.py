from midiutil import MIDIFile

degrees  = [60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65] # MIDI note number
track    = 0
channel  = 0
time     = 0   # In beats
duration = 1   # In beats
tempo    = 60  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1
tempo = 180
MyMIDI.addTempo(track,time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

tempo = 360
MyMIDI.addTempo(track,time, tempo)
degrees  = [60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65,60, 66, 54, 65]
for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

degrees  = [60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65]
tempo = 360
MyMIDI.addTempo(track,time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1
degrees  = [60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65,70,60, 66, 54, 65]
tempo = 360
MyMIDI.addTempo(track,time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

degrees  = [60, 66, 54, 65,70,75,59,60, 66, 54, 65,70,75,59,60, 66, 54, 65,70,75,59,60, 66, 54, 65,70,75,59,60, 66, 54, 65,70,75,59,60, 66, 54, 65,70,75,59,60, 66, 54, 65,70,75,59,60, 66, 54, 65,70,75,59]
tempo = 180
MyMIDI.addTempo(track,time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

degrees  = [60,59,60,59,60,59,60,59,60,59]
tempo = 30
MyMIDI.addTempo(track,time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

degrees  = [60,59,60,59,60,59,60,59,60,59]
tempo = 30
MyMIDI.addTempo(track,time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    MyMIDI.addNote(track, channel, 73, time, duration, volume)
    MyMIDI.addNote(track, channel, 76, time, duration, volume)
    MyMIDI.addNote(track, channel, 79, time, duration, volume)
    time = time + 1
with open("major.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
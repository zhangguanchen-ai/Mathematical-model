from midiutil import MIDIFile

# 创建一个MIDI文件对象，包含1个音轨
midi_file = MIDIFile(1)

# 设置音轨、 tempo (BPM)
track = 0
time = 0
midi_file.addTempo(track, time, 120)

# 添加C大三和弦（C4, E4, G4）
channel = 0
volume = 100

# 添加和弦的三个音符，它们的开始时间相同
pitch_c = 60  # MIDI音符编号60代表C4
pitch_e = 64  # MIDI音符编号64代表E4
pitch_g = 67  # MIDI音符编号67代表G4

duration = 4  # 音符持续4拍

# 依次添加三个音符，形成和弦
midi_file.addNote(track, channel, pitch_c, time, duration, volume)
midi_file.addNote(track, channel, pitch_e, time, duration, volume)
midi_file.addNote(track, channel, pitch_g, time, duration, volume)

# 将MIDI文件写入磁盘
with open("chord_example.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
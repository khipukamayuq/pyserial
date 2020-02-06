from twelve_tone.composer import Composer
from mido import Message, MidiFile, MidiTrack
from miditime.miditime import MIDITime
import numpy as np
import random
import pretty_midi


mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

midinotes = []
offset = 60
attack = 200
beats = 1


main_list = []
c = Composer()
for instance in range(0, 100):
    c.compose()
    tone_row = c.get_melody()
    random_tone_row = random.sample(tone_row, len(tone_row))
    main_list += random_tone_row
    # c.save_to_midi(filename='twelve_tone_%s.mid' % instance)

numbered_list = [s + str(random.randint(0, 8)) for s in main_list]

note_number_list = []

compo = pretty_midi.PrettyMIDI()

compo_program = pretty_midi.instrument_name_to_program('Cello')

compo_c = pretty_midi.Instrument(program=compo_program)

numbered_list = [s for s in numbered_list if not ("/" in s)]

start = 0
end = .5

for note_name in numbered_list:
    note_number = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=end)
    compo_c.notes.append(note)
    start = random.randint(0, 1000) * 0.1
    end =  random.randint(1, 20) * 0.1


compo.instruments.append(compo_c)
compo.write('compo.mid')

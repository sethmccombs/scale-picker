# Program to randomly choose a root note, and scale to play based on the modes
# Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian
# Will return whether to play the 6th or 5th string root
# Will prompt at the beginning to choose 7 or 6 string guitar
# If playing a 7 string, will return 7th, 6th, or 5th string root

import random as rand

positions = ["A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab"  ]
root_note = positions[rand.randint(0, len(positions)-1)]

# List of Modes
modes = ["ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian"]

# ionian =
# dorian =
# phrygian =
# lydian =
# mixolydian =
# aeolian =
# locrian =

# Check for voice (Ab vs G#)
# Prompt if playing 7 or 6 string

# seven_string = input("Are you playing a seven string? ")
seven_string = "no"

# Select Mode
# mode = modes[random.randint(1, len(modes)]
mode = modes[rand.randint(0, len(modes)-1)]

# Select Root Note

# Select Root String
strings = []

if seven_string.lower() == 'yes':
    strings = ["5th","6th","7th"]
elif seven_string.lower() == 'no':
    strings = ["5th","6th"]


string = strings[rand.randint(0, len(strings)-1)]


print("%s %s, starting on the %s string" % (root_note, mode, string))




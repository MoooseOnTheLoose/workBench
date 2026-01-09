# pinPointMusic_1.1_skeleton.py

from dataclasses import dataclass 

SCALE_POSITION = ["I", "II", "III", "IV", "V", "VI", "VII"]
CHORD_POSITION = ["I", "III", "V"]

MAJOR_TRIADS = ["Major", "minor", "minor", "Major", "Major", "minor", "diminished"]
MINOR_TRIADS = ["minor", "diminished", "Major", "minor", "minor", "Major", "Major"]

SCALES = {
    # Natural keys
    "c major": ["c", "d", "e", "f", "g", "a", "b"],
    "c minor": ["c", "d", "e♭", "f", "g", "a♭", "b♭"],

    "d major": ["d", "e", "f#", "g", "a", "b", "c#"],
    "d minor": ["d", "e", "f", "g", "a", "b♭", "c"],

    "e major": ["e", "f#", "g#", "a", "b", "c#", "d#"],
    "e minor": ["e", "f#", "g", "a", "b", "c", "d"],

    "f major": ["f", "g", "a", "b♭", "c", "d", "e"],
    "f minor": ["f", "g", "a♭", "b♭", "c", "d♭", "e♭"],

    "g major": ["g", "a", "b", "c", "d", "e", "f#"],
    "g minor": ["g", "a", "b♭", "c", "d", "e♭", "f"],

    "a major": ["a", "b", "c#", "d", "e", "f#", "g#"],
    "a minor": ["a", "b", "c", "d", "e", "f", "g"],

    "b major": ["b", "c#", "d#", "e", "f#", "g#", "a#"],
    "b minor": ["b", "c#", "d", "e", "f#", "g", "a"],

    # Sharp keys
    "c# major": ["c#", "d#", "e#", "f#", "g#", "a#", "b#"],
    "c# minor": ["c#", "d#", "e", "f#", "g#", "a", "b"],

    "d# major": ["d#", "e#", "f##", "g#", "a#", "b#", "c##"],
    "d# minor": ["d#", "e#", "f#", "g#", "a#", "b", "c#"],

    "e# major": ["e#", "f##", "g##", "a#", "b#", "c##", "d##"],
    "e# minor": ["e#", "f##", "g#", "a#", "b#", "c#", "d#"],

    "f# major": ["f#", "g#", "a#", "b", "c#", "d#", "e#"],
    "f# minor": ["f#", "g#", "a", "b", "c#", "d", "e"],

    "g# major": ["g#", "a#", "b#", "c#", "d#", "e#", "f##"],
    "g# minor": ["g#", "a#", "b", "c#", "d#", "e", "f#"],

    "a# major": ["a#", "b#", "c##", "d#", "e#", "f##", "g##"],
    "a# minor": ["a#", "b#", "c#", "d#", "e#", "f#", "g#"],

    "b# major": ["b#", "c##", "d##", "e#", "f##", "g##", "a##"],  # FIXED
    "b# minor": ["b#", "c##", "d#", "e#", "f##", "g#", "a#"],

    # Flat keys
    "cb major": ["c♭", "d♭", "e♭", "f♭", "g♭", "a♭", "b♭"],
    "cb minor": ["c♭", "d♭", "e♭♭", "f♭", "g♭", "a♭♭", "b♭♭"],

    "db major": ["d♭", "e♭", "f", "g♭", "a♭", "b♭", "c"],
    "db minor": ["d♭", "e♭", "f♭", "g♭", "a♭", "b♭♭", "c♭"],

    "eb major": ["e♭", "f", "g", "a♭", "b♭", "c", "d"],
    "eb minor": ["e♭", "f", "g♭", "a♭", "b♭", "c♭", "d♭"],

    "fb major": ["f♭", "g♭", "a♭", "b♭♭", "c♭", "d♭", "e♭"],
    "fb minor": ["f♭", "g♭", "a♭♭", "b♭♭", "c♭", "d♭♭", "e♭♭"],

    "gb major": ["g♭", "a♭", "b♭", "c♭", "d♭", "e♭", "f"],
    "gb minor": ["g♭", "a♭", "b♭♭", "c♭", "d♭", "e♭♭", "f♭"],

    "ab major": ["a♭", "b♭", "c", "d♭", "e♭", "f", "g"],
    "ab minor": ["a♭", "b♭", "c♭", "d♭", "e♭", "f♭", "g♭"],

    "bb major": ["b♭", "c", "d", "e♭", "f", "g", "a"],
    "bb minor": ["b♭", "c", "d♭", "e♭", "f", "g♭", "a♭"],
   
}

CHORDS = {
       # Major chords
    "c major": ["c", "e", "g"],
    "d major": ["d", "f#", "a"],
    "e major": ["e", "g#", "b"],
    "f major": ["f", "a", "c"],
    "g major": ["g", "b", "d"],
    "a major": ["a", "c#", "e"],
    "b major": ["b", "d#", "f#"],

    "c# major": ["c#", "e#", "g#"],
    "db major": ["d♭", "f", "a♭"],
    "d# major": ["d#", "f##", "a#"],
    "eb major": ["e♭", "g", "b♭"],
    "e# major": ["e#", "g##", "b#"],
    "fb major": ["f♭", "a♭", "c♭"],
    "f# major": ["f#", "a#", "c#"],
    "gb major": ["g♭", "b♭", "d♭"],
    "g# major": ["g#", "b#", "d#"],
    "ab major": ["a♭", "c", "e♭"],
    "a# major": ["a#", "c##", "e#"],
    "bb major": ["b♭", "d", "f"],
    "b# major": ["b#", "d##", "f##"],

    # Minor chords
    "c minor": ["c", "e♭", "g"],
    "d minor": ["d", "f", "a"],
    "e minor": ["e", "g", "b"],
    "f minor": ["f", "a♭", "c"],
    "g minor": ["g", "b♭", "d"],
    "a minor": ["a", "c", "e"],
    "b minor": ["b", "d", "f#"],

    "c# minor": ["c#", "e", "g#"],
    "db minor": ["d♭", "f♭", "a♭"],
    "d# minor": ["d#", "f#", "a#"],
    "eb minor": ["e♭", "g♭", "b♭"],
    "e# minor": ["e#", "g#", "b#"],
    "fb minor": ["f♭", "a♭♭", "c♭"],
    "f# minor": ["f#", "a", "c#"],
    "gb minor": ["g♭", "b♭♭", "d♭"],
    "g# minor": ["g#", "b", "d#"],
    "ab minor": ["a♭", "c♭", "e♭"],   # FIXED
    "a# minor": ["a#", "c#", "e#"],
    "bb minor": ["b♭", "d♭", "f"],
    "b# minor": ["b#", "d#", "f##"],

    # Diminished chords
    "c diminished": ["c", "e♭", "g♭"],
    "d diminished": ["d", "f", "a♭"],
    "e diminished": ["e", "g", "b♭"],
    "f diminished": ["f", "a♭", "c♭"],
    "g diminished": ["g", "b♭", "d♭"],
    "a diminished": ["a", "c", "e♭"],
    "b diminished": ["b", "d", "f"],

    "c# diminished": ["c#", "e", "g"],
    "db diminished": ["d♭", "f♭", "a♭♭"],
    "d# diminished": ["d#", "f#", "a"],
    "eb diminished": ["e♭", "g♭", "b"],
    "e# diminished": ["e#", "g#", "b"],
    "fb diminished": ["f♭", "a♭♭", "c♭♭"],
    "f# diminished": ["f#", "a", "c"],
    "gb diminished": ["g♭", "b♭♭", "d♭♭"],
    "g# diminished": ["g#", "b", "d"],
    "ab diminished": ["a♭", "c♭", "e♭♭"],
    "a# diminished": ["a#", "c#", "e"],
    "bb diminished": ["b♭", "d♭", "f♭"],
    "b# diminished": ["b#", "d#", "f#"],
}

FREQS = {
   # Octave 0
    "e0": 20.602,
    "f0": 21.827,
    "f#0": 23.125, "gb0": 23.125,
    "g0": 24.500,
    "g#0": 25.957, "ab0": 25.957,
    "a0": 27.500,
    "a#0": 29.1353, "bb0": 29.1353,
    "b0": 30.8677,

    # Octave 1
    "c1": 32.7032,
    "c#1": 34.6479, "db1": 34.6479,
    "d1": 36.7081,
    "d#1": 38.8909, "eb1": 38.8909,
    "e1": 41.2035,
    "f1": 43.6536,
    "f#1": 46.2493, "gb1": 46.2493,
    "g1": 48.9995,
    "g#1": 51.9130, "ab1": 51.9130,
    "a1": 55.0000,
    "a#1": 58.2705, "bb1": 58.2705,
    "b1": 61.7354,

    # Octave 2
    "c2": 65.4064,
    "c#2": 69.2957, "db2": 69.2957,
    "d2": 73.4162,
    "d#2": 77.7817, "eb2": 77.7817,
    "e2": 82.4069,
    "f2": 87.3071,
    "f#2": 92.4986, "gb2": 92.4986,
    "g2": 97.9989,
    "g#2": 103.826, "ab2": 103.826,
    "a2": 110.000,
    "a#2": 116.541, "bb2": 116.541,
    "b2": 123.471,

    # Octave 3
    "c3": 130.813,
    "c#3": 138.591, "db3": 138.591,
    "d3": 146.832,
    "d#3": 155.563, "eb3": 155.563,
    "e3": 164.814,
    "f3": 174.614,
    "f#3": 184.997, "gb3": 184.997,
    "g3": 195.998,
    "g#3": 207.652, "ab3": 207.652,
    "a3": 220.000,
    "a#3": 233.082, "bb3": 233.082,
    "b3": 246.942,

    # Octave 4
    "c4": 261.626,
    "c#4": 277.183, "db4": 277.183,
    "d4": 293.665,
    "d#4": 311.127, "eb4": 311.127,
    "e4": 329.628,
    "f4": 349.228,
    "f#4": 369.994, "gb4": 369.994,
    "g4": 391.995,
    "g#4": 415.305, "ab4": 415.305,
    "a4": 440.000,
    "a#4": 466.164, "bb4": 466.164,
    "b4": 493.883,

    # Octave 5
    "c5": 523.251,
    "c#5": 554.365, "db5": 554.365,
    "d5": 587.330,
    "d#5": 622.254, "eb5": 622.254,
    "e5": 659.255,
    "f5": 698.456,
    "f#5": 739.989, "gb5": 739.989,
    "g5": 783.991,
    "g#5": 830.609, "ab5": 830.609,
    "a5": 880.000,
    "a#5": 932.328, "bb5": 932.328,
    "b5": 987.767,

    # Octave 6
    "c6": 1046.50,
    "c#6": 1108.73, "db6": 1108.73,
    "d6": 1174.66,
    "d#6": 1244.51, "eb6": 1244.51,
    "e6": 1318.51,
    "f6": 1396.91,
    "f#6": 1479.98, "gb6": 1479.98,
    "g6": 1567.98,
    "g#6": 1661.22, "ab6": 1661.22,
    "a6": 1760.00,
    "a#6": 1864.66, "bb6": 1864.66,
    "b6": 1975.53,

    # Octave 7
    "c7": 2093.00,
    "c#7": 2217.46, "db7": 2217.46,
    "d7": 2349.32,
    "d#7": 2489.02, "eb7": 2489.02,
    "e7": 2637.02,
    "f7": 2793.83,
    "f#7": 2959.96, "gb7": 2959.96,
    "g7": 3135.96,
    "g#7": 3322.44, "ab7": 3322.44,
    "a7": 3520.00,
    "a#7": 3729.31, "bb7": 3729.31,
    "b7": 3951.07,

    # Octave 8
    "c8": 4186.01,
    "c#8": 4434.90, "db8": 4434.90,
    "d8": 4698.60,
    "d#8": 4978.00, "eb8": 4978.00,
    "e8": 5274.00,
    "f8": 5587.70,
    "f#8": 5919.90, "gb8": 5919.90,
    "g8": 6271.90,
    "g#8": 6644.90, "ab8": 6644.90,
    "a8": 7040.00,
    "a#8": 7458.60, "bb8": 7458.60,
    "b8": 7902.10,

    # Octave 9
    "c9": 8372.00,
    "c#9": 8869.80, "db9": 8869.80,
    "d9": 9397.30,
    "d#9": 9956.10, "eb9": 9956.10,
    "e9": 10548.0,
    "f9": 11175.0,
    "f#9": 11840.0, "gb9": 11840.0,
    "g9": 12544.0,
    "g#9": 13290.0, "ab9": 13290.0,
    "a9": 14080.0,
    "a#9": 14917.0, "bb9": 14917.0,
    "b9": 15804.0,

    # Octave 10
    "c10": 16744.0,
    "c#10": 17740.0, "db10": 17740.0,
    "d10": 18795.0,
    "d#10": 19912.0, "eb10": 19912.0,
}

# ----------------------------
# Input normalization + aliases
# ----------------------------

def normalize(s: str) -> str:
    """
    Normalize user input for matching:
    - lowercase
    - strip spaces
    - collapse internal whitespace
    - unify unicode accidentals if you want (optional)
    """
    s = s.strip().lower()
    s = " ".join(s.split())
    return s

def normalize_key_name(s: str) -> str:
    """
    Accepts inputs like:
    - "cmajor", "c major"
    - "c# major", "c sharp major", "csharpmajor"
    - "eb minor", "e flat minor"
    Produces a canonical form like "c major", "c# major", "eb minor".
    """
    s = normalize(s)

    # expand words
    s = s.replace("sharp", "#").replace("flat", "b")

    # handle no-space forms like "cmajor" -> "c major"
    for qual in ("major", "minor", "diminished"):
        if s.endswith(qual) and " " not in s:
            root = s[: -len(qual)]
            s = f"{root} {qual}".strip()
            break

    # handle things like "c#major" -> "c# major"
    for qual in ("major", "minor", "diminished"):
        if s.endswith(qual) and " " not in s:
            pass

    # if still like "c#major" with no space
    for qual in ("major", "minor", "diminished"):
        if s.endswith(qual) and (" " not in s):
            s = s.replace(qual, f" {qual}")

    s = " ".join(s.split())
    return s

def normalize_note_octave(s: str) -> str:
    """
    Accepts:
    - "c four", "c4", "c 4", "cfour"
    - "c# 4", "c sharp four"
    - "eb 4", "e flat four"
    Produces canonical like "c4", "c#4", "eb4"
    """
    s = normalize(s)
    s = s.replace("sharp", "#").replace("flat", "b")

    # word-to-digit octave (extend as needed)
    word_oct = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"
    }
    parts = s.split()

    # cases: "c four" -> ["c","four"]
    if len(parts) == 2 and parts[1] in word_oct:
        return f"{parts[0]}{word_oct[parts[1]]}"

    # cases: "c 4" -> ["c","4"]
    if len(parts) == 2 and parts[1].isdigit():
        return f"{parts[0]}{parts[1]}"

    # cases: "cfour" -> detect suffix word
    for w, d in word_oct.items():
        if s.endswith(w):
            return f"{s[:-len(w)]}{d}"

    # cases: already like "c4", "eb10"
    return s.replace(" ", "")

# ----------------------------
# Validation (catches bad lists early)
# ----------------------------

def validate():
    # scales must be length 7
    for name, notes in SCALES.items():
        if len(notes) != 7:
            raise ValueError(f"Scale '{name}' must have 7 notes, has {len(notes)}: {notes}")

    # chords must be length 3
    for name, notes in CHORDS.items():
        if len(notes) != 3:
            raise ValueError(f"Chord '{name}' must have 3 notes, has {len(notes)}: {notes}")

# ----------------------------
# UI functions (non-recursive loops)
# ----------------------------

def show_key():
    while True:
        raw = input("What key do you want to see?\n")
        cmd = normalize(raw)

        if cmd == "quit":
            raise SystemExit
        if cmd == "back":
            return
        if cmd == "help":
            print("\nInput examples: c major, c minor, d# minor, eb major\n")
            continue

        key = normalize_key_name(raw)
        notes = SCALES.get(key)
        if not notes:
            print("\nIncorrect input. Type help if confused.\n")
            continue

        qualities = MAJOR_TRIADS if key.endswith("major") else MINOR_TRIADS
        print("")
        for i in range(7):
            print(f"{SCALE_POSITION[i]}\t {notes[i].upper()}\t {qualities[i]}")
        print("")
        return

def show_chord():
    while True:
        raw = input("What chord do you want to see?\n")
        cmd = normalize(raw)

        if cmd == "quit":
            raise SystemExit
        if cmd == "back":
            return
        if cmd == "help":
            print("\nInput examples: c major, c minor, d# minor, eb major, e diminished\n")
            continue

        chord = normalize_key_name(raw)  # same normalizer works for "c diminished" etc.
        notes = CHORDS.get(chord)
        if not notes:
            print("\nIncorrect input. Type help if confused.\n")
            continue

        print("")
        for i in range(3):
            print(f"{CHORD_POSITION[i]}\t {notes[i].upper()}")
        print("")
        return

def show_freq():
    while True:
        raw = input("What note do you want to see the frequency of?\n")
        cmd = normalize(raw)

        if cmd == "quit":
            raise SystemExit
        if cmd == "back":
            return
        if cmd == "help":
            print("\nInput examples: c four, c4, c# 4, eb 4, cb 6\n")
            continue

        note = normalize_note_octave(raw)
        hz = FREQS.get(note)
        if hz is None:
            print("\nIncorrect input. Type help if confused.\n")
            continue

        print(f"{hz} Hz")
        return

def main():
    validate()

    print("\n------------------------------------------------------------------")
    print("                   Pin Point Music 1.1                 ")
    print("------------------------------------------------------------------")
    print("Choose: 1 = Key, 2 = Chord, 3 = Frequency")
    print("Type help if confused. Type quit to exit.\n")

    while True:
        ans = normalize(input("Where would you like to go?\n"))
        if ans == "1":
            show_key()
        elif ans == "2":
            show_chord()
        elif ans == "3":
            show_freq()
        elif ans == "help":
            print("\nType 1 for keys, 2 for chords, 3 for frequencies.\n")
        elif ans == "quit":
            raise SystemExit
        else:
            print("\nIncorrect response. Type help if confused.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit

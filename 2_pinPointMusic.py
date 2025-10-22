#pinPointMusic 1.0
#---------------------------------------------------------------------------------------
#GLOBALS
#---------------------------------------------------------------------------------------
#---------------------------------42 keys of music
cMajor = ["c", "d", "e", "f", "g", "a", "b"] 
cMinor = ["c", "d", "e♭", "f", "g", "a♭", "b♭"]
dMajor = ["d", "e", "f#", "g", "a", "b", "c#"]
dMinor = ["d", "e", "f", "g", "a", "b♭", "c"]
eMajor = ["e", "f#", "g#", "a", "b", "c#", "d#"]
eMinor = ["e", "f#", "g", "a", "b", "c", "d"]
fMajor = ["f", "g", "a", "b♭", "c", "d", "e"]
fMinor = ["f", "g", "a♭", "b♭", "c", "d♭", "e♭"]
gMajor = ["g", "a", "b", "c", "d", "e", "f#"]
gMinor = ["g", "a", "b♭", "c", "d", "e♭", "f"]
aMajor = ["a", "b", "c#", "d", "e", "f#", "g#"]
aMinor = ["a", "b", "c", "d", "e", "f", "g"]
bMajor = ["b", "c#", "d#", "e", "f#", "g#", "a#"]
bMinor = ["b", "c#", "d", "e", "f#", "g", "a"]
cSharpMajor = ["c#", "d#", "e#", "f#", "g#", "a#", "b#"]
cSharpMinor = ["c#", "d#", "e", "f#", "g#", "a", "b"]
cFlatMajor = ["c♭", "d♭", "e♭", "f♭", "g♭", "a♭", "b♭"]
cFlatMinor = ["c♭", "d♭","e♭♭", "f♭", "g♭", "a♭♭", "b♭♭"]
dSharpMajor = ["d#", "e#", "f##", "g#", "a#", "b#", "c##"]
dSharpMinor = ["d#", "e#", "f#", "g#", "a#", "b", "c#"]
dFlatMajor = ["d♭", "e♭", "f", "g♭", "a♭", "b♭", "c"]
dFlatMinor = ["d♭", "e♭", "f♭", "g♭", "a♭", "b♭♭","c♭"]
eSharpMajor = ["e#", "f##", "g##", "a#", "b#", "c##", "d##"]
eSharpMinor = ["e#", "f##", "g#", "a#", "b#", "c#", "d#"]
eFlatMajor = ["e♭", "f", "g", "a♭", "b♭", "c", "d"]
eFlatMinor = ["e♭", "f", "g♭", "a♭", "b♭", "c♭", "d♭"]
fSharpMajor = ["f#", "g#", "a#", "b", "c#", "d#", "e#"]
fSharpMinor = ["f#", "g#", "a", "b", "c#", "d", "e"]
fFlatMajor = ["f♭", "g♭", "a♭", "b♭♭", "c♭", "d♭", "e♭"]
fFlatMinor = ["f♭", "g♭", "a♭♭", "b♭♭", "c♭", "d♭♭", "e♭♭"]
gSharpMajor = ["g#", "a#", "b#", "c#", "d#", "e#", "f##"]
gSharpMinor = ["g#", "a#", "b", "c#", "d#", "e", "f#"]
gFlatMajor = ["g♭", "a♭", "b♭", "c♭", "d♭", "e♭", "f"]
gFlatMinor = ["g♭", "a♭", "b♭♭", "c♭", "d♭", "e♭♭", "f♭"]
aSharpMajor = ["a#", "b#", "c##", "d#", "e#", "f##", "g##"]
aSharpMinor = ["a#", "b#", "c#", "d#", "e#", "f#", "g#"]
aFlatMajor = ["a♭", "b♭", "c", "d♭", "e♭", "f", "g"]
aFlatMinor = ["a♭", "b♭", "c♭", "d♭", "e♭", "f♭", "g♭"]
bSharpMajor = ["b#", "c##", "d##", "e#", "f##", "g##", "a##", "b#"]
bSharpMinor = ["b#", "c##", "d#", "e#", "f##", "g#", "a#"]
bFlatMajor = ["b♭", "c", "d", "e♭", "f", "g", "a"]
bFlatMinorr = ["b♭", "c", "d♭", "e♭", "f", "g♭", "a♭"]
#--------------------------------------------Positions
scalePosition =["I", "II", "III", "IV", "V", "VI", "VII"]
chordPosition = ["I", "III", "V"]
majorTriads = ["Major", "minor", "minor", "Major", "Major", "minor", "diminished"]
minorTriads = ["minor", "diminished", "Major", "minor", "minor", "Major", "Major"]
#----------------------------------------------62 Chords
cMaj = ["c", "e", "g"]
cMin = ["c", "e♭", "g"]
dMaj = ["d", "f#", "a"]
dMin = ["d", "f", "a"]
eMaj = ["e", "g#", "b"]
eMin = ["e", "g", "b"]
fMaj = ["f", "a", "c"]
fMin = ["f", "a♭", "c"]
gMaj = ["g", "b", "d"]
gMin = ["g", "b♭", "d"]
aMaj = ["a", "c#", "e"]
aMin = ["a", "c", "e"]
bMaj = ["b", "d#", "f#"]
bMin = ["b", "d", "f#"]
cSharpMaj = ["c#", "e#", "g#"]
cSharpMin = ["c#", "e", "g#"]
cFlatMaj = ["c♭", "e♭", "g♭"]
cFlatMin = ["c♭", "e♭♭", "g♭"]
dSharpMaj = ["d#", "f##", "a#"]
dSharpMin = ["d#", "f#", "a#"]
dFlatMaj = ["d♭", "f", "a♭"]
dFlatMin = ["d♭", "f♭", "a♭"]
eSharpMaj = ["e#","g##", "b#"]
eSharpMin = ["e#", "g#", "b#"]
eFlatMaj = ["e♭", "g", "b♭"]
eFlatMin = ["e♭", "g♭", "b♭"]
fSharpMaj = ["f#", "a#", "c#"]
fSharpMin = ["f#", "a", "c#"]
fFlatMaj = ["f♭", "a♭", "c♭"]
fFlatMin = ["f♭", "a♭♭", "c♭"]
gSharpMaj = ["g#", "b#", "d#"]
gSharpMin = ["g#", "b", "d#"]
gFlatMaj = ["g♭", "b♭", "d♭"]
gFlatMin = ["g♭", "b♭♭", "d♭"]
aSharpMaj = ["a#", "c##", "e#"]
aSharpMin = ["a#", "c#", "e#"]
aFlatMaj = ["a♭", "c", "e♭"]
aFlatMin = ["a♭', c♭", "e♭"]
bSharpMaj = ["b#", "d##", "f##"]
bSharpMin = ["b#", "d#", "f##"]
bFlatMaj = ["b♭", "d", "f"]
bFlatMin = ["b♭", "d♭", "f"]
cDim = ["c", "e♭", "g♭"]
dDim = ["d", "f", "a♭"]
eDim = ["e", "g", "b♭"]
fDim = ["f", "a♭", "c♭"]
gDim = ["g", "b♭", "d♭"]
aDim = ["a", "c", "e♭"]
bDim = ["b", "d", "f"]
cSharpDim = ["c#", "e", "g"]
cFlatDim = ["c♭", "e♭♭", "g♭♭"]
dSharpDim = ["d#", "f#", "a"]
dFlatDim = ["d♭", "f♭", "a♭♭"]
eSharpDim = ["e#", "g#", "b"]
eFlatDim = ["e♭", "g♭", "b"]
fSharpDim = ["f#", "a", "c"]
fFlatDim = ["f♭", "a♭♭", "c♭♭"]
gSharpDim = ["g#", "b", "d"]
gFlatDim = ["g♭", "b♭♭", "d♭♭"]
aSharpDim = ["a#", "c#", "e"]
aFlatDim = ["a♭", "c♭", "e♭♭"]
bSharpDim = ["b#", "d#", "f#"]
bFlatDim = ["b♭", "d♭", "f♭"]
#-------------------------------Frequencies: E0 to D#10/Eb10
eZero = ("20.602")
fZero = ("21.827")
fSharpZero = ("23.125")
gFlatZero = ("23.125")
gZero = ("24.500")
gSharpZero = ("25.957")
aFlatZero = ("25.957")
aZero = ("27.5000")
aSharpZero = ("29.1353")
bFlatZero = ("29.1353")
bZero = ("30.8677")
cOne = ("32.7032")
cSharpOne = ("34.6479")
dFlatOne = ("34.6479")
dOne = ("36.7081")
dSharpOne = ("38.8909")
eFlatOne = ("38.8909")
eOne = ("41.2035")
fOne = ("43.6536")
fSharpOne = ("46.2493")
gFlatOne = ("46.2493")
gOne = ("48.9995")
gSharpOne = ("51.9130")
aFlatOne = ("51.9130")
aOne = ("55.0000")
aSharpOne = ("58.2705")
bFlatOne = ("58.2705")
bOne = ("61.7354")
cTwo = ("65.4064")
cSharpTwo = ("69.2957")
dFlatTwo = ("69.2957")
dTwo = ("73.4162")
dSharpTwo = ("77.7817")
eFlatTwo = ("77.7817")
eTwo = ("82.4069")
fTwo = ("87.3071")
fSharpTwo = ("92.4986")
gFlatTwo = ("92.4986")
gTwo = ("97.9989")
gSharpTwo = ("103.826")
aFlatTwo = ("103.826")
aTwo = ("110.000")
aSharpTwo = ("116.541")
bFlatTwo = ("116.541")
bTwo = ("123.471")
cThree = ("130.813")
cSharpThree = ("138.591")
dFlatThree = ("138.591")
dThree = ("146.832")
dSharpThree = ("155.563")
eFlatThree = ("155.563")
eThree = ("164.814")
fThree = ("174.614")
fSharpThree = ("184.997")
gFlatThree = ("184.997")
gThree = ("195.998")
gSharpThree = ("207.652")
aFlatThree = ("207.652")
aThree = ("220.000")
aSharpThree = ("233.082")
bFlatThree = ("233.082")
bThree = ("246.942")
cFour = ("261.626")
cSharpFour = ("277.183")
dFlatFour = ("277.183")
dFour = ("293.665")
dSharpFour = ("311.127")
eFlatFour = ("311.127")
eFour = ("329.628")
fFour = ("349.228")
fSharpFour = ("369.994")
gFlatFour = ("369.994")
gFour = ("391.995")
gSharpFour = ("415.305")
aFlatFour = ("415.305")
aFour = ("440.000")
aSharpFour = ("466.164")
bFlatFour = ("466.164")
bFour = ("493.883")
cFive = ("523.251")
cSharpFive = ("554.365")
dFlatFive = ("554.365")
dFive = ("587.330")
dSharpFive = ("622.254")
eFlatFive = ("622.254")
eFive = ("659.255")
fFive = ("698.456")
fSharpFive = ("739.989")
gFlatFive = ("739.989")
gFive = ("783.991")
gSharpFive = ("830.609")
aFlatFive = ("830.609")
aFive = ("880.000")
aSharpFive = ("932.328")
bFlatFive = ("932.328")
bFive = ("987.767")
cSix = ("1046.50")
cSharpSix = ("1108.73")
dFlatSix = ("1108.73")
dSix = ("1174.66")
dSharpSix = ("1244.51")
eFlatSix = ("1244.51")
eSix = ("1318.51")
fSix = ("1396.91")
fSharpSix = ("1479.98")
gFlatSix = ("1479.98")
gSix = ("1567.98")
gSharpSix = ("1661.22")
aFlatSix = ("1661.22")
aSix = ("1760.00")
aSharpSix = ("1864.66")
bFlatSix = ("1864.66")
bSix = ("1975.53")
cSeven = ("2093.00")
cSharpSeven = ("2217.46")
dFlatSeven = ("2217.46")
dSeven = ("2349.32")
dSharpSeven = ("2489.02")
eFlatSeven = ("2489.02")
eSeven = ("2637.02")
fSeven = ("2793.83")
fSharpSeven = ("2959.96")
gFlatSeven = ("2959.96")
gSeven = ("3135.96")
gSharpSeven = ("3322.44")
aFlatSeven = ("3322.44")
aSeven = ("3520.00")
aSharpSeven = ("3729.31")
bFlatSeven = ("3729.31")
bSeven = ("3951.07")
cEight = ("4186.01")
cSharpEight = ("4434.9")
dFlatEight = ("4434.9")
dEight = ("4698.6")
dSharpEight = ("4978.0")
eFlatEight = ("4978.0")
eEight = ("5274.0")
fEight = ("5587.7")
fSharpEight = ("5919.9")
gFlatEight = ("5919.9")
gEight = ("6271.9")
gSharpEight = ("6644.9")
aFlatEight = ("6644.9")
aEight = ("7040.0")
aSharpEight = ("7458.6")
bFlatEight = ("7458.6")
bEight = ("7902.1")
cNine = ("8372.0")
cSharpNine = ("8869.8")
dFlatNine = ("8869.8")
dNine = ("9397.3")
dSharpNine = ("9956.1")
eFlatNine = ("9956.1")
eNine = ("10548")
fNine = ("11175")
fSharpNine = ("11840")
gFlatNine = ("11840")
gNine = ("12544")
gSharpNine = ("13290")
aFlatNine = ("13290")
aNine = ("14080")
aSharpNine = ("14917")
bFlatNine = ("14917")
bNine = ("15804")
cTen = ("16744 ")
cSharpTen = ("17740")
dFlatTen = ("17740")
dTen = ("18795")
dSharpTen = ("19912")
eFlatTen = ("19912")
#---------------------------------------------------------------------------------------
#FUNCTIONS
#---------------------------------------------------------------------------------------
#----------------------------------------whatKey()
def whatKey():
    key = input("What key do you want to see?\n")
    if key.lower() == "cmajor" or key.lower() == "c major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + cMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "cminor" or key.lower() == "c minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + cMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "dmajor" or key.lower() == "d major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + dMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "dminor" or key.lower() == "d minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + dMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "emajor" or key.lower() == "e major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + eMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "eminor" or key.lower() == "e minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + eMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "fmajor" or key.lower() == "f major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + fMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "fminor" or key.lower() == "f minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + fMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "gmajor" or key.lower() == "g major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + gMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "gminor" or key.lower() == "g minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + gMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "amajor" or key.lower() == "a major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + aMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "aminor" or key.lower() == "a minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + aMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "bmajor" or key.lower() == "b major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + bMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "bminor" or key.lower() == "b minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + bMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "csharpmajor" or key.lower() == "c sharp major" or key.lower() == "c#major" or key.lower() == "c# major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + cSharpMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "csharpminor" or key.lower() == "c sharp minor" or key.lower() == "c#minor" or key.lower() == "c# minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + cSharpMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "cflatmajor" or key.lower() == "c flat major" or key.lower() == "cbmajor" or key.lower() == "cb major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + cFlatMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "cflatminor" or key.lower() == "c flat minor" or key.lower() == "cbminor" or key.lower() == "cb minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + cFlatMinor[i].upper() + "\t " + minorTriads[i])        
    elif key.lower() == "dsharpmajor" or key.lower() == "d sharp major" or key.lower() == "d#major" or key.lower() == "d# major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + dSharpMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "dsharpminor" or key.lower() == "d sharp minor" or key.lower() == "d#minor" or key.lower() == "d# minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + dSharpMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "dflatmajor" or key.lower() == "d flat major" or key.lower() == "dbmajor" or key.lower() == "db major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + dFlatMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "dflatminor" or key.lower() == "d flat minor" or key.lower() == "dbminor" or key.lower() == "db minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + dFlatMinor[i].upper() + "\t " + minorTriads[i])    
    elif key.lower() == "esharpmajor" or key.lower() == "e sharp major" or key.lower() == "e#major" or key.lower() == "e# major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + eSharpMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "esharpminor" or key.lower() == "e sharp minor" or key.lower() == "e#minor" or key.lower() == "e# minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + eSharpMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "eflatmajor" or key.lower() == "e flat major" or key.lower() == "ebmajor" or key.lower() == "eb major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + eFlatMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "eflatminor" or key.lower() == "e flat minor" or key.lower() == "ebminor" or key.lower() == "eb minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + eFlatMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "fsharpmajor" or key.lower() == "f sharp major" or key.lower() == "f#major" or key.lower() == "f# major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + fSharpMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "fsharpminor" or key.lower() == "f sharp minor" or key.lower() == "f#minor" or key.lower() == "f# minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + fSharpMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "fflatmajor" or key.lower() == "f flat major" or key.lower() == "fbmajor" or key.lower() == "fb major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + fFlatMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "fflatminor" or key.lower() == "f flat minor" or key.lower() == "fbminor" or key.lower() == "fb minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + fFlatMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "gsharpmajor" or key.lower() == "g sharp major" or key.lower() == "g#major" or key.lower() == "g# major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + gSharpMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "gsharpminor" or key.lower() == "g sharp minor" or key.lower() == "g#minor" or key.lower() == "g# minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + gSharpMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "gflatmajor" or key.lower() == "g flat major" or key.lower() == "gbmajor" or key.lower() == "gb major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + gFlatMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "gflatminor" or key.lower() == "g flat minor" or key.lower() == "gbminor" or key.lower() == "gb minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + gFlatMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "asharpmajor" or key.lower() == "a sharp major" or key.lower() == "a#major" or key.lower() == "a# major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + aSharpMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "asharpminor" or key.lower() == "a sharp minor" or key.lower() == "a#minor" or key.lower() == "a# minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + aSharpMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "aflatmajor" or key.lower() == "a flat major" or key.lower() == "abmajor" or key.lower() == "ab major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + aFlatMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "aflatminor" or key.lower() == "a flat minor" or key.lower() == "abminor" or key.lower() == "ab minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + aFlatMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "bsharpmajor" or key.lower() == "b sharp major" or key.lower() == "b#major" or key.lower() == "b# major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + bSharpMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "bsharpminor" or key.lower() == "b sharp minor" or key.lower() == "b#minor" or key.lower() == "b# minor":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + bSharpMinor[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "bflatmajor" or key.lower() == "b flat major" or key.lower() == "bbmajor" or key.lower() == "bb major":
        for i in range(len(scalePosition)):
            print(scalePosition[i] + "\t " + bFlatMajor[i].upper() + "\t " + majorTriads[i])
    elif key.lower() == "bflatminor" or key.lower() == "b flat minor" or key.lower() == "bbminor" or key.lower() == "bb minor":
        for i in range(len(bFlatMinorr)):
            print(scalePosition[i] + "\t " + bFlatMinorr[i].upper() + "\t " + minorTriads[i])
    elif key.lower() == "help":
        print(" ")
        print("------------------------------------------------------------------")
        print("This program shows a key of music after your input.")
        print("Input examples: c major, c minor, d# minor, e flat major")
        print("------------------------------------------------------------------\n")
        whatKey()
    elif key.lower() == "quit":
        exit()
    elif key.lower() == "back":
        print("------------------------------------------------------------------\n")
        main()
    else:
        print("------------------------------------------------------------------")
        print("Incorrect input.")
        print("Type the word help if confused.")
        print("------------------------------------------------------------------\n")
        whatKey()
    print(" ")
    return
#----------------------------------------whatChord()
def whatChord():
    chord=input("What chord do you want to see?\n")
    if chord.lower() == "cmajor" or chord.lower() == "c major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cMaj[i].upper())
    elif chord.lower() == "cminor" or chord.lower() == "c minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cMin[i].upper())
    elif chord.lower() == "dmajor" or chord.lower() == "d major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dMaj[i].upper())
    elif chord.lower() == "dminor" or chord.lower() == "d minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dMin[i].upper())
    elif chord.lower() == "emajor" or chord.lower() == "e major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eMaj[i].upper())
    elif chord.lower() == "eminor" or chord.lower() == "e minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eMin[i].upper())
    elif chord.lower() == "fmajor" or chord.lower() == "f major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fMaj[i].upper())
    elif chord.lower() == "fminor" or chord.lower() == "f minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fMin[i].upper())
    elif chord.lower() == "gmajor" or chord.lower() == "g major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gMaj[i].upper())
    elif chord.lower() == "gminor" or chord.lower() == "g minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gMin[i].upper())
    elif chord.lower() == "amajor" or chord.lower() == "a major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aMaj[i].upper())
    elif chord.lower() == "aminor" or chord.lower() == "a minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aMin[i].upper())
    elif chord.lower() == "bmajor" or chord.lower() == "b major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bMaj[i].upper())
    elif chord.lower() == "bminor" or chord.lower() == "b minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bMin[i].upper())
    elif chord.lower() == "csharpmajor" or chord.lower() == "c sharp major" or chord.lower() == "c#major" or chord.lower() == "c# major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cSharpMaj[i].upper())
    elif chord.lower() == "csharpminor" or chord.lower() == "c sharp minor" or chord.lower() == "c#minor" or chord.lower() == "c# minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cSharpMin[i].upper())
    elif chord.lower() == "cflatmajor" or chord.lower() == "c flat major" or chord.lower() == "cbmajor" or chord.lower() == "cb major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cFlatMaj[i].upper())
    elif chord.lower() == "cflatminor" or chord.lower() == "c flat minor" or chord.lower() == "cbminor" or chord.lower() == "cb minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cFlatMin[i].upper())
    elif chord.lower() == "dsharpmajor" or chord.lower() == "d sharp major" or chord.lower() == "d#major" or chord.lower() == "d# major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dSharpMaj[i].upper())
    elif chord.lower() == "dsharpminor" or chord.lower() == "d sharp minor" or chord.lower() == "d#minor" or chord.lower() == "d# minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dSharpMin[i].upper())
    elif chord.lower() == "dflatmajor" or chord.lower() == "d flat major" or chord.lower() == "dbmajor" or chord.lower() == "db major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dFlatMaj[i].upper())
    elif chord.lower() == "dflatminor" or chord.lower() == "d flat minor" or chord.lower() == "dbminor" or chord.lower() == "db minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dFlatMin[i].upper())
    elif chord.lower() == "esharpmajor" or chord.lower() == "e sharp major" or chord.lower() == "e#major" or chord.lower() == "e# major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eSharpMaj[i].upper())
    elif chord.lower() == "esharpminor" or chord.lower() == "e sharp minor" or chord.lower() == "e#minor" or chord.lower() == "e# minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eSharpMin[i].upper())
    elif chord.lower() == "eflatmajor" or chord.lower() == "e flat major" or chord.lower() == "ebmajor" or chord.lower() == "eb major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eFlatMaj[i].upper())
    elif chord.lower() == "eflatminor" or chord.lower() == "e flat minor" or chord.lower() == "ebminor" or chord.lower() == "eb minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eFlatMin[i].upper())
    elif chord.lower() == "fsharpmajor" or chord.lower() == "f sharp major" or chord.lower() == "f#major" or chord.lower() == "f# major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fSharpMaj[i].upper())
    elif chord.lower() == "fsharpminor" or chord.lower() == "f sharp minor" or chord.lower() == "f#minor" or chord.lower() == "f# minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fSharpMin[i].upper())
    elif chord.lower() == "fflatmajor" or chord.lower() == "f flat major" or chord.lower() == "fbmajor" or chord.lower() == "fb major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fFlatMaj[i].upper())
    elif chord.lower() == "fflatminor" or chord.lower() == "f flat minor" or chord.lower() == "fbminor" or chord.lower() == "fb minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fFlatMin[i].upper())
    elif chord.lower() == "gsharpmajor" or chord.lower() == "g sharp major" or chord.lower() == "g#major" or chord.lower() == "g# major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gSharpMaj[i].upper())
    elif chord.lower() == "gsharpminor" or chord.lower() == "g sharp minor" or chord.lower() == "g#minor" or chord.lower() == "g# minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gSharpMin[i].upper())
    elif chord.lower() == "gflatmajor" or chord.lower() == "g flat major" or chord.lower() == "gbmajor" or chord.lower() == "gb major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gFlatMaj[i].upper())
    elif chord.lower() == "gflatminor" or chord.lower() == "g flat minor" or chord.lower() == "gbminor" or chord.lower() == "gb minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gFlatMin[i].upper())
    elif chord.lower() == "asharpmajor" or chord.lower() == "a sharp major" or chord.lower() == "a#major" or chord.lower() == "a# major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aSharpMaj[i].upper())
    elif chord.lower() == "asharpminor" or chord.lower() == "a sharp minor" or chord.lower() == "a#minor" or chord.lower() == "a# minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aSharpMin[i].upper())
    elif chord.lower() == "aflatmajor" or chord.lower() == "a flat major" or chord.lower() == "abmajor" or chord.lower() == "ab major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aFlatMaj[i].upper())
    elif chord.lower() == "aflatminor" or chord.lower() == "a flat minor" or chord.lower() == "abminor" or chord.lower() == "ab minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aFlatMin[i].upper())
    elif chord.lower() == "bsharpmajor" or chord.lower() == "b sharp major" or chord.lower() == "b#major" or chord.lower() == "b# major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bSharpMaj[i].upper())
    elif chord.lower() == "bsharpminor" or chord.lower() == "b sharp minor" or chord.lower() == "b#minor" or chord.lower() == "b# minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bSharpMin[i].upper())
    elif chord.lower() == "bflatmajor" or chord.lower() == "b flat major" or chord.lower() == "bbmajor" or chord.lower() == "bb major":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bFlatMaj[i].upper())
    elif chord.lower() == "bflatminor" or chord.lower() == "b flat minor" or chord.lower() == "bbminor" or chord.lower() == "bb minor":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bFlatMin[i].upper())
    elif chord.lower() == "cdiminished" or chord.lower() == "c diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cDim[i].upper())
    elif chord.lower() == "ddiminished" or chord.lower() == "d diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dDim[i].upper())
    elif chord.lower() == "ediminished" or chord.lower() == "e diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eDim[i].upper())
    elif chord.lower() == "fdiminished" or chord.lower() == "f diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fDim[i].upper())
    elif chord.lower() == "gdiminished" or chord.lower() == "g diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gDim[i].upper())
    elif chord.lower() == "adiminished" or chord.lower() == "a diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aDim[i].upper())
    elif chord.lower() == "bdiminished" or chord.lower() == "b diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bDim[i].upper())
    elif chord.lower() == "csharpdiminished" or chord.lower() == "c sharp diminished" or chord.lower() == "c#diminished" or chord.lower() == "c# diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cSharpDim[i].upper())
    elif chord.lower() == "cflatdiminished" or chord.lower() == "c flat diminished" or chord.lower() == "cbdiminished" or chord.lower() == "cb diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + cFlatDim[i].upper())
    elif chord.lower() == "dsharpdiminished" or chord.lower() == "d sharp diminished" or chord.lower() == "d#diminished" or chord.lower() == "d# diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dSharpDim[i].upper())
    elif chord.lower() == "dflatdiminished" or chord.lower() == "d flat diminished" or chord.lower() == "dbdiminished" or chord.lower() == "db diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + dFlatDim[i].upper())
    elif chord.lower() == "esharpdiminished" or chord.lower() == "e sharp diminished" or chord.lower() == "e#diminished" or chord.lower() == "e# diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eSharpDim[i].upper())
    elif chord.lower() == "eflatdiminished" or chord.lower() == "e flat diminished" or chord.lower() == "ebdiminished" or chord.lower() == "eb diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + eFlatDim[i].upper())
    elif chord.lower() == "fsharpdiminished" or chord.lower() == "f sharp diminished" or chord.lower() == "f#diminished" or chord.lower() == "f# diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fSharpDim[i].upper())
    elif chord.lower() == "fflatdiminished" or chord.lower() == "f flat diminished" or chord.lower() == "fbdiminished" or chord.lower() == "fb diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + fFlatDim[i].upper())
    elif chord.lower() == "gsharpdiminished" or chord.lower() == "g sharp diminished" or chord.lower() == "g#diminished" or chord.lower() == "g# diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gSharpDim[i].upper())
    elif chord.lower() == "gflatdiminished" or chord.lower() == "g flat diminished" or chord.lower() == "gbdiminished" or chord.lower() == "gb diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + gFlatDim[i].upper())
    elif chord.lower() == "asharpdiminished" or chord.lower() == "a sharp diminished" or chord.lower() == "a#diminished" or chord.lower() == "a# diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aSharpDim[i].upper())
    elif chord.lower() == "aflatdiminished" or chord.lower() == "a flat diminished" or chord.lower() == "abdiminished" or chord.lower() == "ab diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + aFlatDim[i].upper())
    elif chord.lower() == "bsharpdiminished" or chord.lower() == "b sharp diminished" or chord.lower() == "b#diminished" or chord.lower() == "b# diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bSharpDim[i].upper())
    elif chord.lower() == "bflatdiminished" or chord.lower() == "b flat diminished" or chord.lower() == "bbdiminished" or chord.lower() == "bb diminished":
        for i in range(len(chordPosition)):
            print(chordPosition[i] + "\t " + bFlatDim[i].upper())
    elif chord.lower() == "help":
        print(" ")
        print("------------------------------------------------------------------")
        print("This program shows the notes that make a chord")
        print("Input examples: c major, c minor, d# minor, e flat major, e diminished")
        print("------------------------------------------------------------------\n")
        whatChord()
    elif chord.lower() == "back":
        print("------------------------------------------------------------------\n")
        main()
    elif chord.lower() == "quit":
        exit()
    else:
        print(" ")
        print("------------------------------------------------------------------")
        print("Incorrect input.")
        print("Type the word help if confused.")
        print("------------------------------------------------------------------\n")
        whatChord()
    return
#----------------------------------------whatFreq()
def whatFreq():
    freq = input("What note do you want to see the frequency of?\n")
    if freq.lower() == "ezero" or freq.lower() == "e zero" or freq.lower() == "e0" or freq.lower() == "e 0":
        print(eZero + " Hz")
    elif freq.lower() == "fzero" or freq.lower() == "f zero" or freq.lower() == "f0" or freq.lower() == "f 0":
        print(fZero + " Hz")
    elif freq.lower() == "fsharpzero" or freq.lower() == "f sharp zero" or freq.lower() == "f#zero" or freq.lower() == "f# zero" or freq.lower() == "f#0" or freq.lower() == "f# 0":
        print(fSharpZero + " Hz")
    elif freq.lower() == "gflatzero" or freq.lower() == "g flat zero" or freq.lower() == "gbzero" or freq.lower() == "gb zero" or freq.lower() == "gb0" or freq.lower() == "gb 0":
        print(gFlatZero + " Hz")    
    elif freq.lower() == "gzero" or freq.lower() == "g zero" or freq.lower() == "g0" or freq.lower() == "g 0":
        print(gZero + " Hz")    
    elif freq.lower() == "gsharpzero" or freq.lower() == "g sharp zero" or freq.lower() == "g#zero" or freq.lower() == "g# zero" or freq.lower() == "g#0" or freq.lower() == "g# 0":
        print(gSharpZero + " Hz") 
    elif freq.lower() == "aflatzero" or freq.lower() == "a flat zero" or freq.lower() == "abzero" or freq.lower() == "ab zero" or freq.lower() == "ab0" or freq.lower() == "ab 0":
        print(aFlatZero + " Hz")   
    elif freq.lower() == "azero" or freq.lower() == "a zero" or freq.lower() == "a0" or freq.lower() == "a 0":
        print(aZero + " Hz")               
    elif freq.lower() == "asharpzero" or freq.lower() == "a sharp zero" or freq.lower() == "a#zero" or freq.lower() == "a# zero" or freq.lower() == "a#0" or freq.lower() == "a# 0":
        print(aSharpZero + " Hz")
    elif freq.lower() == "bflatzero" or freq.lower() == "b flat zero" or freq.lower() == "bbzero" or freq.lower() == "bb zero" or freq.lower() == "bb0" or freq.lower() == "bb 0":
        print(bFlatZero + " Hz")
    elif freq.lower() == "bzero" or freq.lower() == "b zero" or freq.lower() == "b0" or freq.lower() == "b 0":
        print(bZero + " Hz")
    elif freq.lower() == "cone" or freq.lower() == "c one" or freq.lower() == "c1" or freq.lower() == "c 1":
        print(cOne + " Hz")
    elif freq.lower() == "csharpone" or freq.lower() == "c sharp one" or freq.lower() == "c#one" or freq.lower() == "c# one" or freq.lower() == "c#1" or freq.lower() == "c# 1":
        print(cSharpOne + " Hz")
    elif freq.lower() == "dflatone" or freq.lower() == "d flat one" or freq.lower() == "dbone" or freq.lower() == "db one" or freq.lower() == "db1" or freq.lower() == "db 1":
        print(dFlatOne + " Hz")  
    elif freq.lower() == "done" or freq.lower() == "d one" or freq.lower() == "d1" or freq.lower() == "d 1":
        print(dOne + " Hz")  
    elif freq.lower() == "dsharpone" or freq.lower() == "d sharp one" or freq.lower() == "d#one" or freq.lower() == "d# one" or freq.lower() == "d#1" or freq.lower() == "d# 1":
        print(dSharpOne + " Hz")
    elif freq.lower() == "eflatone" or freq.lower() == "e flat one" or freq.lower() == "ebone" or freq.lower() == "eb one" or freq.lower() == "eb1" or freq.lower() == "eb 1":
        print(eFlatOne + " Hz")  
    elif freq.lower() == "eone" or freq.lower() == "e one" or freq.lower() == "e1" or freq.lower() == "e 1":
        print(eOne + " Hz")  
    elif freq.lower() == "fone" or freq.lower() == "f one" or freq.lower() == "f1" or freq.lower() == "f 1":
        print(fOne + " Hz")  
    elif freq.lower() == "fsharpone" or freq.lower() == "f sharp one" or freq.lower() == "f#one" or freq.lower() == "f# one" or freq.lower() == "f#1" or freq.lower() == "f# 1":
        print(fSharpOne + " Hz")
    elif freq.lower() == "gflatone" or freq.lower() == "g flat one" or freq.lower() == "gbone" or freq.lower() == "gb one" or freq.lower() == "gb1" or freq.lower() == "gb 1":
        print(gFlatOne + " Hz")
    elif freq.lower() == "gone" or freq.lower() == "g one" or freq.lower() == "g1" or freq.lower() == "g 1":
        print(gOne + " Hz")  
    elif freq.lower() == "gsharpone" or freq.lower() == "g sharp one" or freq.lower() == "g#one" or freq.lower() == "g# one" or freq.lower() == "g#1" or freq.lower() == "g# 1":
        print(gSharpOne + " Hz")
    elif freq.lower() == "aflatone" or freq.lower() == "a flat one" or freq.lower() == "abone" or freq.lower() == "ab one" or freq.lower() == "ab1" or freq.lower() == "ab 1":
        print(aFlatOne + " Hz") 
    elif freq.lower() == "aone" or freq.lower() == "a one" or freq.lower() == "a1" or freq.lower() == "a 1":
        print(aOne + " Hz") 
    elif freq.lower() == "asharpone" or freq.lower() == "a sharp one" or freq.lower() == "a#one" or freq.lower() == "a# one" or freq.lower() == "a#1" or freq.lower() == "a# 1":
        print(aSharpOne + " Hz")
    elif freq.lower() == "bflatone" or freq.lower() == "b flat one" or freq.lower() == "bbone" or freq.lower() == "bb one" or freq.lower() == "bb1" or freq.lower() == "bb 1":
        print(bFlatOne + " Hz")
    elif freq.lower() == "bone" or freq.lower() == "b one" or freq.lower() == "b1" or freq.lower() == "b 1":
        print(bOne + " Hz") 
    elif freq.lower() == "ctwo" or freq.lower() == "c two" or freq.lower() == "c2" or freq.lower() == "c 2":
        print(cTwo + " Hz") 
    elif freq.lower() == "csharptwo" or freq.lower() == "c sharp two" or freq.lower() == "c#two" or freq.lower() == "c# two" or freq.lower() == "c#2" or freq.lower() == "c# 2":
        print(cSharpTwo + " Hz")
    elif freq.lower() == "dflattwo" or freq.lower() == "d flat two" or freq.lower() == "dbtwo" or freq.lower() == "db two" or freq.lower() == "db2" or freq.lower() == "db 2":
        print(dFlatTwo + " Hz")
    elif freq.lower() == "dtwo" or freq.lower() == "d two" or freq.lower() == "d2" or freq.lower() == "d 2":
        print(dTwo + " Hz") 
    elif freq.lower() == "dsharptwo" or freq.lower() == "d sharp two" or freq.lower() == "d#two" or freq.lower() == "d# two" or freq.lower() == "d#2" or freq.lower() == "d# 2":
        print(dSharpTwo + " Hz") 
    elif freq.lower() == "eflattwo" or freq.lower() == "e flat two" or freq.lower() == "ebtwo" or freq.lower() == "eb two" or freq.lower() == "eb2" or freq.lower() == "eb 2":
        print(eFlatTwo + " Hz")
    elif freq.lower() == "etwo" or freq.lower() == "e two" or freq.lower() == "e2" or freq.lower() == "e 2":
        print(eTwo + " Hz") 
    elif freq.lower() == "ftwo" or freq.lower() == "f two" or freq.lower() == "f2" or freq.lower() == "f 2":
        print(fTwo + " Hz") 
    elif freq.lower() == "fsharptwo" or freq.lower() == "f sharp two" or freq.lower() == "f#two" or freq.lower() == "f# two" or freq.lower() == "f#2" or freq.lower() == "f# 2":
        print(fSharpTwo + " Hz")
    elif freq.lower() == "gflattwo" or freq.lower() == "g flat two" or freq.lower() == "gbtwo" or freq.lower() == "gb two" or freq.lower() == "gb2" or freq.lower() == "gb 2":
        print(gFlatTwo + " Hz")
    elif freq.lower() == "gtwo" or freq.lower() == "g two" or freq.lower() == "g2" or freq.lower() == "g 2":
        print(gTwo + " Hz") 
    elif freq.lower() == "gsharptwo" or freq.lower() == "g sharp two" or freq.lower() == "g#two" or freq.lower() == "g# two" or freq.lower() == "g#2" or freq.lower() == "g# 2":
        print(gSharpTwo + " Hz")
    elif freq.lower() == "aflattwo" or freq.lower() == "a flat two" or freq.lower() == "abtwo" or freq.lower() == "ab two" or freq.lower() == "ab2" or freq.lower() == "ab 2":
        print(aFlatTwo + " Hz")
    elif freq.lower() == "atwo" or freq.lower() == "a two" or freq.lower() == "a2" or freq.lower() == "a 2":
        print(aTwo + " Hz") 
    elif freq.lower() == "asharptwo" or freq.lower() == "a sharp two" or freq.lower() == "a#two" or freq.lower() == "a# two" or freq.lower() == "a#2" or freq.lower() == "a# 2":
        print(aSharpTwo + " Hz")
    elif freq.lower() == "bflattwo" or freq.lower() == "b flat two" or freq.lower() == "bbtwo" or freq.lower() == "bb two" or freq.lower() == "bb2" or freq.lower() == "bb 2":
        print(bFlatTwo + " Hz")
    elif freq.lower() == "btwo" or freq.lower() == "b two" or freq.lower() == "b2" or freq.lower() == "b 2":
        print(bTwo + " Hz") 
    elif freq.lower() == "cthree" or freq.lower() == "c three" or freq.lower() == "c3" or freq.lower() == "c 3":
        print(cThree + " Hz") 
    elif freq.lower() == "csharpthree" or freq.lower() == "c sharp three" or freq.lower() == "c#three" or freq.lower() == "c# three" or freq.lower() == "c#3" or freq.lower() == "c# 3":
        print(cSharpThree + " Hz")
    elif freq.lower() == "dflatthree" or freq.lower() == "d flat three" or freq.lower() == "dbthree" or freq.lower() == "db three" or freq.lower() == "db3" or freq.lower() == "db 3":
        print(dFlatThree + " Hz")
    elif freq.lower() == "dthree" or freq.lower() == "d three" or freq.lower() == "d3" or freq.lower() == "d 3":
        print(dThree + " Hz") 
    elif freq.lower() == "dsharpthree" or freq.lower() == "d sharp three" or freq.lower() == "d#three" or freq.lower() == "d# three" or freq.lower() == "d#3" or freq.lower() == "d# 3":
        print(dSharpThree + " Hz")
    elif freq.lower() == "eflatthree" or freq.lower() == "e flat three" or freq.lower() == "ebthree" or freq.lower() == "eb three" or freq.lower() == "eb3" or freq.lower() == "eb 3":
        print(eFlatThree + " Hz") 
    elif freq.lower() == "ethree" or freq.lower() == "e three" or freq.lower() == "e3" or freq.lower() == "e 3":
        print(eThree + " Hz") 
    elif freq.lower() == "fthree" or freq.lower() == "f three" or freq.lower() == "f3" or freq.lower() == "f 3":
        print(fThree + " Hz") 
    elif freq.lower() == "fsharpthree" or freq.lower() == "f sharp three" or freq.lower() == "f#three" or freq.lower() == "f# three" or freq.lower() == "f#3" or freq.lower() == "f# 3":
        print(fSharpThree + " Hz")
    elif freq.lower() == "gflatthree" or freq.lower() == "g flat three" or freq.lower() == "gbthree" or freq.lower() == "gb three" or freq.lower() == "gb3" or freq.lower() == "gb 3":
        print(gFlatThree + " Hz") 
    elif freq.lower() == "gthree" or freq.lower() == "g three" or freq.lower() == "g3" or freq.lower() == "g 3":
        print(gThree + " Hz") 
    elif freq.lower() == "gsharpthree" or freq.lower() == "g sharp three" or freq.lower() == "g#three" or freq.lower() == "g# three" or freq.lower() == "g#3" or freq.lower() == "g# 3":
        print(gSharpThree + " Hz")
    elif freq.lower() == "aflatthree" or freq.lower() == "a flat three" or freq.lower() == "abthree" or freq.lower() == "ab three" or freq.lower() == "ab3" or freq.lower() == "ab 3":
        print(aFlatThree + " Hz") 
    elif freq.lower() == "athree" or freq.lower() == "a three" or freq.lower() == "a3" or freq.lower() == "a 3":
        print(aThree + " Hz") 
    elif freq.lower() == "asharpthree" or freq.lower() == "a sharp three" or freq.lower() == "a#three" or freq.lower() == "a# three" or freq.lower() == "a#3" or freq.lower() == "a# 3":
        print(aSharpThree + " Hz")
    elif freq.lower() == "bflatthree" or freq.lower() == "b flat three" or freq.lower() == "bbthree" or freq.lower() == "bb three" or freq.lower() == "bb3" or freq.lower() == "bb 3":
        print(bFlatThree + " Hz") 
    elif freq.lower() == "bthree" or freq.lower() == "b three" or freq.lower() == "b3" or freq.lower() == "b 3":
        print(bThree + " Hz") 
    elif freq.lower() == "cfour" or freq.lower() == "c four" or freq.lower() == "c4" or freq.lower() == "c 4":
        print(cFour + " Hz") 
    elif freq.lower() == "csharpfour" or freq.lower() == "c sharp four" or freq.lower() == "c#four" or freq.lower() == "c# four" or freq.lower() == "c#4" or freq.lower() == "c# 4":
        print(cSharpFour + " Hz") 
    elif freq.lower() == "dflatfour" or freq.lower() == "d flat four" or freq.lower() == "dbfour" or freq.lower() == "db four" or freq.lower() == "db4" or freq.lower() == "db 4":
        print(dFlatFour + " Hz") 
    elif freq.lower() == "dfour" or freq.lower() == "d four" or freq.lower() == "d4" or freq.lower() == "d 4":
        print(dFour + " Hz") 
    elif freq.lower() == "dsharpfour" or freq.lower() == "d sharp four" or freq.lower() == "d#four" or freq.lower() == "d# four" or freq.lower() == "d#4" or freq.lower() == "d# 4":
        print(dSharpFour + " Hz") 
    elif freq.lower() == "eflatfour" or freq.lower() == "e flat four" or freq.lower() == "ebfour" or freq.lower() == "eb four" or freq.lower() == "eb4" or freq.lower() == "eb 4":
        print(eFlatFour + " Hz") 
    elif freq.lower() == "efour" or freq.lower() == "e four" or freq.lower() == "e4" or freq.lower() == "e 4":
        print(eFour + " Hz")
    elif freq.lower() == "ffour" or freq.lower() == "f four" or freq.lower() == "f4" or freq.lower() == "f 4":
        print(fFour + " Hz")
    elif freq.lower() == "fsharpfour" or freq.lower() == "f sharp four" or freq.lower() == "f#four" or freq.lower() == "f# four" or freq.lower() == "f#4" or freq.lower() == "f# 4":
        print(fSharpFour + " Hz") 
    elif freq.lower() == "gflatfour" or freq.lower() == "g flat four" or freq.lower() == "gbfour" or freq.lower() == "gb four" or freq.lower() == "gb4" or freq.lower() == "gb 4":
        print(gFlatFour + " Hz") 
    elif freq.lower() == "gfour" or freq.lower() == "g four" or freq.lower() == "g4" or freq.lower() == "g 4":
        print(gFour + " Hz")
    elif freq.lower() == "gsharpfour" or freq.lower() == "g sharp four" or freq.lower() == "g#four" or freq.lower() == "g# four" or freq.lower() == "g#4" or freq.lower() == "g# 4":
        print(gSharpFour + " Hz") 
    elif freq.lower() == "aflatfour" or freq.lower() == "a flat four" or freq.lower() == "abfour" or freq.lower() == "ab four" or freq.lower() == "ab4" or freq.lower() == "ab 4":
        print(aFlatFour + " Hz") 
    elif freq.lower() == "afour" or freq.lower() == "a four" or freq.lower() == "a4" or freq.lower() == "a 4":
        print(aFour + " Hz")
    elif freq.lower() == "asharpfour" or freq.lower() == "a sharp four" or freq.lower() == "a#four" or freq.lower() == "a# four" or freq.lower() == "a#4" or freq.lower() == "a# 4":
        print(aSharpFour + " Hz")
    elif freq.lower() == "bflatfour" or freq.lower() == "b flat four" or freq.lower() == "bbfour" or freq.lower() == "bb four" or freq.lower() == "bb4" or freq.lower() == "bb 4":
        print(bFlatFour + " Hz") 
    elif freq.lower() == "bfour" or freq.lower() == "b four" or freq.lower() == "b4" or freq.lower() == "b 4":
        print(bFour + " Hz")
    elif freq.lower() == "cfive" or freq.lower() == "c five" or freq.lower() == "c5" or freq.lower() == "c 5":
        print(cFive + " Hz")
    elif freq.lower() == "csharpfive" or freq.lower() == "c sharp five" or freq.lower() == "c#five" or freq.lower() == "c# five" or freq.lower() == "c#5" or freq.lower() == "c# 5":
        print(cSharpFive + " Hz")   
    elif freq.lower() == "dflatfive" or freq.lower() == "d flat five" or freq.lower() == "dbfive" or freq.lower() == "db five" or freq.lower() == "db5" or freq.lower() == "db 5":
        print(dFlatFive + " Hz")  
    elif freq.lower() == "dfive" or freq.lower() == "d five" or freq.lower() == "d5" or freq.lower() == "d 5":
        print(dFive + " Hz")     
    elif freq.lower() == "dsharpfive" or freq.lower() == "d sharp five" or freq.lower() == "d#five" or freq.lower() == "d# five" or freq.lower() == "d#5" or freq.lower() == "d# 5":
        print(dSharpFive + " Hz") 
    elif freq.lower() == "eflatfive" or freq.lower() == "e flat five" or freq.lower() == "ebfive" or freq.lower() == "eb five" or freq.lower() == "eb5" or freq.lower() == "eb 5":
        print(eFlatFive + " Hz")   
    elif freq.lower() == "efive" or freq.lower() == "e five" or freq.lower() == "e5" or freq.lower() == "e 5":
        print(eFive + " Hz")  
    elif freq.lower() == "ffive" or freq.lower() == "f five" or freq.lower() == "f5" or freq.lower() == "f 5":
        print(fFive + " Hz")      
    elif freq.lower() == "fsharpfive" or freq.lower() == "f sharp five" or freq.lower() == "f#five" or freq.lower() == "f# five" or freq.lower() == "f#5" or freq.lower() == "f# 5":
        print(fSharpFive + " Hz")    
    elif freq.lower() == "gflatfive" or freq.lower() == "g flat five" or freq.lower() == "gbfive" or freq.lower() == "gb five" or freq.lower() == "gb5" or freq.lower() == "gb 5":
        print(gFlatFive + " Hz")  
    elif freq.lower() == "gfive" or freq.lower() == "g five" or freq.lower() == "g5" or freq.lower() == "g 5":
        print(gFive + " Hz")   
    elif freq.lower() == "gsharpfive" or freq.lower() == "g sharp five" or freq.lower() == "g#five" or freq.lower() == "g# five" or freq.lower() == "g#5" or freq.lower() == "g# 5":
        print(gSharpFive + " Hz")  
    elif freq.lower() == "aflatfive" or freq.lower() == "a flat five" or freq.lower() == "abfive" or freq.lower() == "ab five" or freq.lower() == "ab5" or freq.lower() == "ab 5":
        print(aFlatFive + " Hz")  
    elif freq.lower() == "afive" or freq.lower() == "a five" or freq.lower() == "a5" or freq.lower() == "a 5":
        print(aFive + " Hz") 
    elif freq.lower() == "asharpfive" or freq.lower() == "a sharp five" or freq.lower() == "a#five" or freq.lower() == "a# five" or freq.lower() == "a#5" or freq.lower() == "a# 5":
        print(aSharpFive + " Hz") 
    elif freq.lower() == "bflatfive" or freq.lower() == "b flat five" or freq.lower() == "bbfive" or freq.lower() == "bb five" or freq.lower() == "bb5" or freq.lower() == "bb 5":
        print(bFlatFive + " Hz")       
    elif freq.lower() == "bfive" or freq.lower() == "b five" or freq.lower() == "b5" or freq.lower() == "b 5":
        print(bFive + " Hz")  
    elif freq.lower() == "csix" or freq.lower() == "c six" or freq.lower() == "c6" or freq.lower() == "c 6":
        print(cSix + " Hz")   
    elif freq.lower() == "csharpsix" or freq.lower() == "c sharp six" or freq.lower() == "c#six" or freq.lower() == "c# six" or freq.lower() == "c#6" or freq.lower() == "c# 6":
        print(cSharpSix + " Hz") 
    elif freq.lower() == "dflatsix" or freq.lower() == "d flat six" or freq.lower() == "dbsix" or freq.lower() == "db six" or freq.lower() == "db6" or freq.lower() == "db 6":
        print(dFlatSix + " Hz")  
    elif freq.lower() == "dsix" or freq.lower() == "d six" or freq.lower() == "d6" or freq.lower() == "d 6":
        print(dSix + " Hz")   
    elif freq.lower() == "dsharpsix" or freq.lower() == "d sharp six" or freq.lower() == "d#six" or freq.lower() == "d# six" or freq.lower() == "d#6" or freq.lower() == "d# 6":
        print(dSharpSix + " Hz") 
    elif freq.lower() == "eflatsix" or freq.lower() == "e flat six" or freq.lower() == "ebsix" or freq.lower() == "eb six" or freq.lower() == "eb6" or freq.lower() == "eb 6":
        print(eFlatSix + " Hz") 
    elif freq.lower() == "esix" or freq.lower() == "e six" or freq.lower() == "e6" or freq.lower() == "e 6":
        print(eSix + " Hz") 
    elif freq.lower() == "fsix" or freq.lower() == "f six" or freq.lower() == "f6" or freq.lower() == "f 6":
        print(fSix + " Hz") 
    elif freq.lower() == "fsharpsix" or freq.lower() == "f sharp six" or freq.lower() == "f#six" or freq.lower() == "f# six" or freq.lower() == "f#6" or freq.lower() == "f# 6":
        print(fSharpSix + " Hz")    
    elif freq.lower() == "gflatsix" or freq.lower() == "g flat six" or freq.lower() == "gbsix" or freq.lower() == "gb six" or freq.lower() == "gb6" or freq.lower() == "gb 6":
        print(gFlatSix + " Hz")  
    elif freq.lower() == "gsix" or freq.lower() == "g six" or freq.lower() == "g6" or freq.lower() == "g 6":
        print(gSix + " Hz")     
    elif freq.lower() == "gsharpsix" or freq.lower() == "g sharp six" or freq.lower() == "g#six" or freq.lower() == "g# six" or freq.lower() == "g#6" or freq.lower() == "g# 6":
        print(gSharpSix + " Hz")      
    elif freq.lower() == "aflatsix" or freq.lower() == "a flat six" or freq.lower() == "absix" or freq.lower() == "ab six" or freq.lower() == "ab6" or freq.lower() == "ab 6":
        print(aFlatSix + " Hz")  
    elif freq.lower() == "asix" or freq.lower() == "a six" or freq.lower() == "a6" or freq.lower() == "a 6":
        print(aSix + " Hz")    
    elif freq.lower() == "asharpsix" or freq.lower() == "a sharp six" or freq.lower() == "a#six" or freq.lower() == "a# six" or freq.lower() == "a#6" or freq.lower() == "a# 6":
        print(aSharpSix + " Hz")   
    elif freq.lower() == "bflatsix" or freq.lower() == "b flat six" or freq.lower() == "bbsix" or freq.lower() == "bb six" or freq.lower() == "bb6" or freq.lower() == "bb 6":
        print(bFlatSix + " Hz")      
    elif freq.lower() == "bsix" or freq.lower() == "b six" or freq.lower() == "b6" or freq.lower() == "b 6":
        print(bSix + " Hz")  
    elif freq.lower() == "cseven" or freq.lower() == "c seven" or freq.lower() == "c7" or freq.lower() == "c 7":
        print(cSeven + " Hz")   
    elif freq.lower() == "csharpseven" or freq.lower() == "c sharp seven" or freq.lower() == "c#seven" or freq.lower() == "c# seven" or freq.lower() == "c#7" or freq.lower() == "c# 7":
        print(cSharpSeven + " Hz")  
    elif freq.lower() == "dflatseven" or freq.lower() == "d flat seven" or freq.lower() == "dbseven" or freq.lower() == "db seven" or freq.lower() == "db7" or freq.lower() == "db 7":
        print(dFlatSeven + " Hz") 
    elif freq.lower() == "dseven" or freq.lower() == "d seven" or freq.lower() == "d7" or freq.lower() == "d 7":
        print(dSeven + " Hz")    
    elif freq.lower() == "dsharpseven" or freq.lower() == "d sharp seven" or freq.lower() == "d#seven" or freq.lower() == "d# seven" or freq.lower() == "d#7" or freq.lower() == "d# 7":
        print(dSharpSeven + " Hz")  
    elif freq.lower() == "eflatseven" or freq.lower() == "e flat seven" or freq.lower() == "ebseven" or freq.lower() == "eb seven" or freq.lower() == "eb7" or freq.lower() == "eb 7":
        print(eFlatSeven + " Hz") 
    elif freq.lower() == "eseven" or freq.lower() == "e seven" or freq.lower() == "e7" or freq.lower() == "e 7":
        print(eSeven + " Hz")   
    elif freq.lower() == "fseven" or freq.lower() == "f seven" or freq.lower() == "f7" or freq.lower() == "f 7":
        print(fSeven + " Hz") 
    elif freq.lower() == "fsharpseven" or freq.lower() == "f sharp seven" or freq.lower() == "f#seven" or freq.lower() == "f# seven" or freq.lower() == "f#7" or freq.lower() == "f# 7":
        print(fSharpSeven + " Hz") 
    elif freq.lower() == "gflatseven" or freq.lower() == "g flat seven" or freq.lower() == "gbseven" or freq.lower() == "gb seven" or freq.lower() == "gb7" or freq.lower() == "gb 7":
        print(gFlatSeven + " Hz")   
    elif freq.lower() == "gseven" or freq.lower() == "g seven" or freq.lower() == "g7" or freq.lower() == "g 7":
        print(gSeven + " Hz") 
    elif freq.lower() == "gsharpseven" or freq.lower() == "g sharp seven" or freq.lower() == "g#seven" or freq.lower() == "g# seven" or freq.lower() == "g#7" or freq.lower() == "g# 7":
        print(gSharpSeven + " Hz") 
    elif freq.lower() == "aflatseven" or freq.lower() == "a flat seven" or freq.lower() == "abseven" or freq.lower() == "ab seven" or freq.lower() == "ab7" or freq.lower() == "ab 7":
        print(aFlatSeven + " Hz") 
    elif freq.lower() == "aseven" or freq.lower() == "a seven" or freq.lower() == "a7" or freq.lower() == "a 7":
        print(aSeven + " Hz") 
    elif freq.lower() == "asharpseven" or freq.lower() == "a sharp seven" or freq.lower() == "a#seven" or freq.lower() == "a# seven" or freq.lower() == "a#7" or freq.lower() == "a# 7":
        print(aSharpSeven + " Hz") 
    elif freq.lower() == "bflatseven" or freq.lower() == "b flat seven" or freq.lower() == "bbseven" or freq.lower() == "bb seven" or freq.lower() == "bb7" or freq.lower() == "bb 7":
        print(bFlatSeven + " Hz") 
    elif freq.lower() == "bseven" or freq.lower() == "b seven" or freq.lower() == "b7" or freq.lower() == "b 7":
        print(bSeven + " Hz")
    elif freq.lower() == "ceight" or freq.lower() == "c eight" or freq.lower() == "c8" or freq.lower() == "c 8":
        print(cEight + " Hz")
    elif freq.lower() == "csharpeight" or freq.lower() == "c sharp eight" or freq.lower() == "c#eight" or freq.lower() == "c# eight" or freq.lower() == "c#8" or freq.lower() == "c# 8":
        print(cSharpEight + " Hz") 
    elif freq.lower() == "dflateight" or freq.lower() == "d flat eight" or freq.lower() == "dbeight" or freq.lower() == "db eight" or freq.lower() == "fb8" or freq.lower() == "db 8":
        print(dFlatEight + " Hz") 
    elif freq.lower() == "deight" or freq.lower() == "d eight" or freq.lower() == "d8" or freq.lower() == "d 8":
        print(dEight + " Hz")    
    elif freq.lower() == "dsharpeight" or freq.lower() == "d sharp eight" or freq.lower() == "d#eight" or freq.lower() == "d# eight" or freq.lower() == "d#8" or freq.lower() == "d# 8":
        print(dSharpEight + " Hz") 
    elif freq.lower() == "eflateight" or freq.lower() == "e flat eight" or freq.lower() == "ebeight" or freq.lower() == "eb eight" or freq.lower() == "eb8" or freq.lower() == "eb 8":
        print(eFlatEight + " Hz") 
    elif freq.lower() == "eeight" or freq.lower() == "e eight" or freq.lower() == "e8" or freq.lower() == "e 8":
        print(eEight + " Hz") 
    elif freq.lower() == "feight" or freq.lower() == "f eight" or freq.lower() == "f8" or freq.lower() == "f 8":
        print(fEight + " Hz") 
    elif freq.lower() == "fsharpeight" or freq.lower() == "f sharp eight" or freq.lower() == "f#eight" or freq.lower() == "f# eight" or freq.lower() == "f#8" or freq.lower() == "f# 8":
        print(fSharpEight + " Hz")  
    elif freq.lower() == "gflateight" or freq.lower() == "g flat eight" or freq.lower() == "gbeight" or freq.lower() == "gb eight" or freq.lower() == "gb8" or freq.lower() == "gb 8":
        print(gFlatEight + " Hz")   
    elif freq.lower() == "geight" or freq.lower() == "g eight" or freq.lower() == "g8" or freq.lower() == "g 8":
        print(gEight + " Hz") 
    elif freq.lower() == "gsharpeight" or freq.lower() == "g sharp eight" or freq.lower() == "g#eight" or freq.lower() == "g# eight" or freq.lower() == "g#8" or freq.lower() == "g# 8":
        print(gSharpEight + " Hz") 
    elif freq.lower() == "aflateight" or freq.lower() == "a flat eight" or freq.lower() == "abeight" or freq.lower() == "ab eight" or freq.lower() == "ab8" or freq.lower() == "ab 8":
        print(aFlatEight + " Hz")  
    elif freq.lower() == "aeight" or freq.lower() == "a eight" or freq.lower() == "a8" or freq.lower() == "a 8":
        print(aEight + " Hz")    
    elif freq.lower() == "asharpeight" or freq.lower() == "a sharp eight" or freq.lower() == "a#eight" or freq.lower() == "a# eight" or freq.lower() == "a#8" or freq.lower() == "a# 8":
        print(aSharpEight + " Hz")  
    elif freq.lower() == "bflateight" or freq.lower() == "b flat eight" or freq.lower() == "bbeight" or freq.lower() == "bb eight" or freq.lower() == "bb8" or freq.lower() == "bb 8":
        print(bFlatEight + " Hz")  
    elif freq.lower() == "beight" or freq.lower() == "b eight" or freq.lower() == "b8" or freq.lower() == "b 8":
        print(bEight + " Hz")    
    elif freq.lower() == "cnine" or freq.lower() == "c nine" or freq.lower() == "c9" or freq.lower() == "c 9":
        print(cNine + " Hz")    
    elif freq.lower() == "csharpnine" or freq.lower() == "c sharp nine" or freq.lower() == "c#nine" or freq.lower() == "c# nine" or freq.lower() == "c#9" or freq.lower() == "c# 9":
        print(cSharpNine + " Hz")  
    elif freq.lower() == "dflatnine" or freq.lower() == "d flat nine" or freq.lower() == "dbnine" or freq.lower() == "db nine" or freq.lower() == "db9" or freq.lower() == "db 9":
        print(dFlatNine + " Hz")  
    elif freq.lower() == "dnine" or freq.lower() == "d nine" or freq.lower() == "d9" or freq.lower() == "d 9":
        print(dNine + " Hz")   
    elif freq.lower() == "dsharpnine" or freq.lower() == "d sharp nine" or freq.lower() == "d#nine" or freq.lower() == "d# nine" or freq.lower() == "d#9" or freq.lower() == "d# 9":
        print(dSharpNine + " Hz")  
    elif freq.lower() == "eflatnine" or freq.lower() == "e flat nine" or freq.lower() == "ebnine" or freq.lower() == "eb nine" or freq.lower() == "eb9" or freq.lower() == "eb 9":
        print(eFlatNine + " Hz")  
    elif freq.lower() == "enine" or freq.lower() == "e nine" or freq.lower() == "e9" or freq.lower() == "e 9":
        print(eNine + " Hz")    
    elif freq.lower() == "fnine" or freq.lower() == "f nine" or freq.lower() == "f9" or freq.lower() == "f 9":
        print(fNine + " Hz")   
    elif freq.lower() == "fsharpnine" or freq.lower() == "f sharp nine" or freq.lower() == "f#nine" or freq.lower() == "f# nine" or freq.lower() == "f#9" or freq.lower() == "f# 9":
        print(fSharpNine + " Hz") 
    elif freq.lower() == "gflatnine" or freq.lower() == "g flat nine" or freq.lower() == "gbnine" or freq.lower() == "gb nine" or freq.lower() == "gb9" or freq.lower() == "gb 9":
        print(gFlatNine + " Hz") 
    elif freq.lower() == "gnine" or freq.lower() == "g nine" or freq.lower() == "g9" or freq.lower() == "g 9":
        print(gNine + " Hz") 
    elif freq.lower() == "gsharpnine" or freq.lower() == "g sharp nine" or freq.lower() == "g#nine" or freq.lower() == "g# nine" or freq.lower() == "g#9" or freq.lower() == "g# 9":
        print(gSharpNine + " Hz") 
    elif freq.lower() == "aflatnine" or freq.lower() == "a flat nine" or freq.lower() == "abnine" or freq.lower() == "ab nine" or freq.lower() == "ab9" or freq.lower() == "ab 9":
        print(aFlatNine + " Hz") 
    elif freq.lower() == "anine" or freq.lower() == "a nine" or freq.lower() == "a9" or freq.lower() == "a 9":
        print(aNine + " Hz") 
    elif freq.lower() == "asharpnine" or freq.lower() == "a sharp nine" or freq.lower() == "a#nine" or freq.lower() == "a# nine" or freq.lower() == "a#9" or freq.lower() == "a# 9":
        print(aSharpNine + " Hz") 
    elif freq.lower() == "bflatnine" or freq.lower() == "b flat nine" or freq.lower() == "bbnine" or freq.lower() == "bb nine" or freq.lower() == "bb9" or freq.lower() == "bb 9":
        print(bFlatNine + " Hz")
    elif freq.lower() == "bnine" or freq.lower() == "b nine" or freq.lower() == "b9" or freq.lower() == "b 9":
        print(bNine + " Hz") 
    elif freq.lower() == "cten" or freq.lower() == "c ten" or freq.lower() == "c10" or freq.lower() == "c 10":
        print(cTen + " Hz") 
    elif freq.lower() == "csharpten" or freq.lower() == "c sharp ten" or freq.lower() == "c#ten" or freq.lower() == "c# ten" or freq.lower() == "c#10" or freq.lower() == "c# 10":
        print(cSharpTen + " Hz") 
    elif freq.lower() == "dflatten" or freq.lower() == "d flat ten" or freq.lower() == "dbten" or freq.lower() == "db ten" or freq.lower() == "db10" or freq.lower() == "db 10":
        print(dFlatTen + " Hz")
    elif freq.lower() == "dten" or freq.lower() == "d ten" or freq.lower() == "d10" or freq.lower() == "d 10":
        print(dTen + " Hz")  
    elif freq.lower() == "dsharpten" or freq.lower() == "d sharp ten" or freq.lower() == "d#ten" or freq.lower() == "d# ten" or freq.lower() == "d#10" or freq.lower() == "d# 10":
        print(dSharpTen + " Hz") 
    elif freq.lower() == "eflatten" or freq.lower() == "e flat ten" or freq.lower() == "ebten" or freq.lower() == "eb ten" or freq.lower() == "eb10" or freq.lower() == "eb 10":
        print(eFlatTen + " Hz")
    elif freq.lower() == "help":
        print(" ")
        print("------------------------------------------------------------------")
        print("This program shows you a frequency of a note.")
        print("Human hearing is from 20Hz to 20kHz.")
        print("Notes range from E0 to D#10/Eb10")
        print("Input examples: c one, c 2, c sharp three, c# 4, c flat five, cb 6")
        print("------------------------------------------------------------------\n")
        whatFreq()
    elif freq.lower() == "back":
        print("------------------------------------------------------------------\n")
        main()
    elif freq.lower() == "quit":
        exit()
    else:
        print(" ")
        print("------------------------------------------------------------------")
        print("Incorrect input.")
        print("Type help if confused.")
        print("------------------------------------------------------------------\n")
        whatFreq()
    return
#---------------------------------------------------------------------------------------
#MAIN FUNCTION
#---------------------------------------------------------------------------------------
print(" ")
print("------------------------------------------------------------------")
print("                   Pin Point Music 1.0                            ")
print("------------------------------------------------------------------")
print("---------------- Welcome to Pin Point Music-----------------------")
print(" ")
print("                    Choose:                                       ")
print("                         1 = Key                                  ")
print("                         2 = Chord                                ")
print("                         3 = Frequency                            ")
print(" ")
print("                 Type the word help if confused.                  ")
print("                 Type the word back for main menu.                ")
print("                 Type the word quit to exit software.             ")
print("------------------------------------------------------------------")
print(" ")
def main():
    print("Where would you like to go?")
    answer = input(" ")
    if answer.lower() == "1":
        whatKey()
        print("------------------------------------------------------------------\n")
        main()
    elif answer.lower() == "2":
        whatChord()
        print("------------------------------------------------------------------\n")
        main()
    elif answer.lower() == "3":
        whatFreq()
        print("------------------------------------------------------------------\n")
        main()
    elif answer.lower() == "help":
        print(" ")
        print("------------------------------------------------------------------")
        print("Type a number.")
        print("1 takes you to choose a key.")
        print("2 takes you to choose a chord.")
        print("3 takes you to choose a frequency.")
        print("------------------------------------------------------------------\n")
        main()
    elif answer.lower() == "quit":
        exit()
    else:
        print(" ")
        print("------------------------------------------------------------------")
        print("Incorrect response.")
        print("Type help if confused.")
        print("------------------------------------------------------------------\n")
        main()
    return
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
        

customMapping = {
    '430': 'a',
    '921': 'b',
    '815': 'c',
    '694': 'd',
    '128': 'e',
    '341': 'f',
    '255': 'g',
    '879': 'h',
    '772': 'i',
    '636': 'j',
    '985': 'k',
    '543': 'l',
    '204': 'm',
    '168': 'n',
    '329': 'o',
    '482': 'p',
    '191': 'q',
    '763': 'r',
    '362': 's',
    '612': 't',
    '289': 'u',
    '451': 'v',
    '701': 'w',
    '849': 'x',
    '567': 'y',
    '998': 'z',
    '597': 'A',
    '309': 'B',
    '681': 'C',
    '429': 'D',
    '885': 'E',
    '676': 'F',
    '792': 'G',
    '107': 'H',
    '376': 'I',
    '185': 'J',
    '464': 'K',
    '240': 'L',
    '732': 'M',
    '711': 'N',
    '963': 'O',
    '654': 'P',
    '802': 'Q',
    '520': 'R',
    '276': 'S',
    '444': 'T',
    '586': 'U',
    '503': 'V',
    '915': 'W',
    '407': 'X',
    '149': 'Y',
    '222': 'Z',
    '707': ' ',    
    '936': ',',    
    '764': '.',    
    '295': '/',    
    '111': '#',    
    '150': ';',    
    '723': '0',    
    '908': '1',
    '219': '2',
    '555': '3',
    '512': '4',
    '666': '5',
    '398': '6',
    '647': '7',
    '267': '8',
    '179': '9',
}


def ham2(ham2):
    nothe = ham2
    now = ""
    result = ""
    for i in range(len(ham2)):
        if i/3 == i//3:
            now += nothe[i+0]
            now += nothe[i+1]
            now += nothe[i+2]

            if '430' in now: result += customMapping['430']
            if '921' in now: result += customMapping['921']
            if '815' in now: result += customMapping['815']
            if '694' in now: result += customMapping['694']
            if '128' in now: result += customMapping['128']
            if '341' in now: result += customMapping['341']
            if '255' in now: result += customMapping['255']
            if '879' in now: result += customMapping['879']
            if '772' in now: result += customMapping['772']
            if '636' in now: result += customMapping['636']
            if '985' in now: result += customMapping['985']
            if '543' in now: result += customMapping['543']
            if '204' in now: result += customMapping['204']
            if '168' in now: result += customMapping['168']
            if '329' in now: result += customMapping['329']
            if '482' in now: result += customMapping['482']
            if '191' in now: result += customMapping['191']
            if '763' in now: result += customMapping['763']
            if '362' in now: result += customMapping['362']
            if '612' in now: result += customMapping['612']
            if '289' in now: result += customMapping['289']
            if '451' in now: result += customMapping['451']
            if '701' in now: result += customMapping['701']
            if '849' in now: result += customMapping['849']
            if '567' in now: result += customMapping['567']
            if '998' in now: result += customMapping['998']
            if '597' in now: result += customMapping['597']
            if '309' in now: result += customMapping['309']
            if '681' in now: result += customMapping['681']
            if '429' in now: result += customMapping['429']
            if '885' in now: result += customMapping['885']
            if '676' in now: result += customMapping['676']
            if '792' in now: result += customMapping['792']
            if '107' in now: result += customMapping['107']
            if '376' in now: result += customMapping['376']
            if '185' in now: result += customMapping['185']
            if '464' in now: result += customMapping['464']
            if '240' in now: result += customMapping['240']
            if '732' in now: result += customMapping['732']
            if '711' in now: result += customMapping['711']
            if '963' in now: result += customMapping['963']
            if '654' in now: result += customMapping['654']
            if '802' in now: result += customMapping['802']
            if '520' in now: result += customMapping['520']
            if '276' in now: result += customMapping['276']
            if '444' in now: result += customMapping['444']
            if '586' in now: result += customMapping['586']
            if '503' in now: result += customMapping['503']
            if '915' in now: result += customMapping['915']
            if '407' in now: result += customMapping['407']
            if '149' in now: result += customMapping['149']
            if '222' in now: result += customMapping['222']
            if '707' in now: result += customMapping['707']
            if '936' in now: result += customMapping['936']
            if '764' in now: result += customMapping['764']
            if '295' in now: result += customMapping['295']
            if '111' in now: result += customMapping['111']# it stops
            if '150' in now: result += customMapping['150']
            if '723' in now: result += customMapping['723']
            if '908' in now: result += customMapping['908']
            if '219' in now: result += customMapping['219']
            if '555' in now: result += customMapping['555']
            if '512' in now: result += customMapping['512']
            if '666' in now: result += customMapping['666']
            if '398' in now: result += customMapping['398']
            if '647' in now: result += customMapping['647']
            if '267' in now: result += customMapping['267']
            if '179' in now: result += customMapping['179']
        now = ""
    return result

print(ham2("879128543543329"))
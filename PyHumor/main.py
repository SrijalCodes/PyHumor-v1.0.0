import random

def _loadJokes(): return {"jokes": {"en": ["Why did the python programmer go broke? Because he missed too many commas.", "Why did the snake get a job at the tech company? Because it could Python-tastically code.", "What do you call a python who likes to play video games? A snake gamer.", "Why do python programmers prefer eating Subway sandwiches? Because they're great at handling strings.","What is a snake's favorite subject in school? Hiss-tory.", "How do you make a python laugh? You give it a good hiss-terical code pun.","Why did the python cross the road? To eat the chicken and then swallow-compress it.","What do you call a python that works at a circus? A snake charmer.","Why don't snakes use email? Because they don't have hands to press the send key.","How does a python programmer travel? In byte-sized chunks.","What do you call two neighboring pythons? A snake-eighbors.","Why did the python programmer get bitten by a mosquito? Because he forgot to use a conditional if-skeet statement.","What do you call a python with excellent rhythm? A hiss-ter dancer.", "What do you call a python with a fancy car? A hiss-ter.","Why did the python go to the doctor? It was feeling slippery.","When it comes to coding, Python is my best hiss-tory."]}}
    
def getPyHumor(lang="en"):
    langCodes = ["en"]
    if lang not in langCodes: raise ValueError(f"Unknown Language/Lang Code >>> {lang} <<< Are you sure this version supports {lang}? at <STDIN> LN 9 COL 115 PyHumor-v1.0.0\nVersion: 1.0.0")
    allJokes = dict(_loadJokes())["jokes"]
    langJokes = list(allJokes[lang])
    return random.choice(langJokes)
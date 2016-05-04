import random

adjectives = ['Neutral', 'Future', 'Mad', 'Bright', 'Another', 'Red', 'Revolving', 'Polar', 'Pretty', 'Grand', '13th', 'Old', 'Broken', 'Public', 'Artful', 'British', 'Legendary', 'Acid', 'Astral']

flex = ['Magic', 'Control', 'Analog', 'Forest', 'Chaos', 'Iron', 'Girl', 'Boy', 'Assault', 'Social', 'Colour', 'Mortal', 'Jazz', 'Chemical', 'Midnight', 'Mountain', 'River', 'Hellfire']

nouns = ['Hotel', 'Sister', 'Fire', 'Mission', 'Club', 'Shelter', 'Day', 'Society', 'Orchestra', 'Dream', 'Union', 'Winter', 'Cult', 'Gang', 'Group', 'Incorporated', 'Crew', 'Clan', 'Experience']

def generatename():
    first = (random.choice(adjectives))
    second = (random.choice(flex))
    third = (random.choice(nouns))
    name = first + ' ' + second + ' ' + third
    return name

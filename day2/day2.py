# Path: day2/day2.py

# Readability is important
DECODE_HAND_MAP = {
    'A': 'ROCK', 'B': 'PAPER', 'C': 'SCISSORS' 
}
DECODE_HAND_MAP_REVERSED = {v: k for k, v in DECODE_HAND_MAP.items()}
# Task 2 supposed outcome mapping
DECODE_OUTCOME_MAP = {
    'A': 'LOSS', 'B': 'DRAW', 'C': 'WIN'
}
# Game rules - what beats what
UPPER_HAND = {
    'PAPER': 'ROCK',
    'SCISSORS': 'PAPER',
    'ROCK': 'SCISSORS'
}
LOSING_HAND = {v: k for k, v in UPPER_HAND.items()}
# Outcome points
GANE_POINTS_MAP = {
'WIN': 6,
'DRAW': 3,
'LOSS': 0
}

# ceasar cipher -23 ascii
def decrypthand(hand):
    return chr(ord(hand) - 23)

score = 0
scoreTask2 = 0

with open('./input.txt') as f:
    for line in f.readlines():
        line = line.strip().split(' ') # remove whitespace
        elfHandShowsChar = line[0] 
        elfHandShows = DECODE_HAND_MAP[elfHandShowsChar]
        dectyptedHandChar = decrypthand(line[1])
        suggestedHand = DECODE_HAND_MAP[dectyptedHandChar]
        supposedOutcome = DECODE_OUTCOME_MAP[dectyptedHandChar]
         
        print(
        """
        Elf shows: {}, suggested hand: {}, supposed outcome (task 2): {}
        """
        .format(elfHandShows, suggestedHand, supposedOutcome))
       
        # Task 1
         # Add hand value (same as ascii - 64 A = 1)
        score += ord(dectyptedHandChar) - 64
        # SAME HAND
        if suggestedHand == elfHandShows: 
            score += GANE_POINTS_MAP['DRAW']

        # WIN
        elif UPPER_HAND[suggestedHand] == elfHandShows: 
            score += GANE_POINTS_MAP['WIN']

        # LOSS
        elif UPPER_HAND[elfHandShows] == suggestedHand: 
            score += GANE_POINTS_MAP['LOSS']

        # Task 2
        if supposedOutcome == 'WIN':
            scoreTask2 += ord(DECODE_HAND_MAP_REVERSED[LOSING_HAND[elfHandShows]]) - 64
            scoreTask2 += GANE_POINTS_MAP['WIN']
        if supposedOutcome == 'LOSS':
            scoreTask2 += ord(DECODE_HAND_MAP_REVERSED[UPPER_HAND[elfHandShows]]) - 64
            scoreTask2 += GANE_POINTS_MAP['LOSS']    
        if supposedOutcome == 'DRAW':
            scoreTask2 += ord(DECODE_HAND_MAP_REVERSED[elfHandShows]) - 64
           
            scoreTask2 += GANE_POINTS_MAP['DRAW']


print("task1", score, "task2", scoreTask2)


def takeNames():
    plyr1=input("🌟 Step right up, brave soul! What is your name, Player 1? ")
    plyr2=input("🌟 And what about you, Player 2? ")
    return plyr1.lower(), plyr2.lower()

def remove_duplicate(plyr1, plyr2):
    plyr1=list(plyr1)
    plyr2=list(plyr2)
    plyr1_copy = plyr1.copy()
    for i in plyr1_copy:
        if i in plyr2:
            plyr2.remove(i)
            plyr1.remove(i)
    
    return len(plyr2)+len(plyr1)
    
def relation(count):
    flames=list("flames")
    idx = 0
    while  len(flames)>1:      
        idx = (idx + count - 1) % len(flames)
        flames.pop(idx)
    return flames[0]

while(1):
    flames = {
    "f": "👫 Just friends! You two are the ultimate buddy duo—Netflix and popcorn, anyone?",
    "l": "💖 Love is in the air! Cupid definitely approves of this match.",
    "a": "😊 Affection overload! You both are as sweet as a double scoop of ice cream.",
    "m": "💍 Wedding bells! Start planning your big fat imaginary wedding.",
    "e": "😈 Enemies! Uh-oh, better keep a safe distance (or start a prank war).",
    "s": "👨‍👩‍👧 Siblings! You fight, you laugh, you steal each other's snacks—classic sibling vibes."
    }
    plyr1,plyr2=takeNames()
    count=remove_duplicate(plyr1, plyr2)
    print(flames[relation(count)])
    
    exit=input("🔮 Press Enter to play again, or type 'bye' to escape Cupid's clutches: ")
    if exit.lower()=="bye":
        break

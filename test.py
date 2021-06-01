import requests

username = "ktomaszewski20".lower()

archives = requests.get(f'https://api.chess.com/pub/player/{username}/games/archives').json()["archives"]

def eco_codes(code):
    code_letter = code[0]
    code_number = int(code[1:])

    if code_letter == "A":
        if code_number == 0:
            return "Polish (Sokolsky) opening"
        elif code_number == 1:
            return "Nimzovich-Larsen attack"
        elif code_number == 2 or code_number == 3:
            return "Bird's opening"
        elif code_number >= 4 and code_number <= 9:
            return "Reti opening"
        elif code_number >= 10 and code_number <= 39:
            return "English opening"
        elif code_number >= 40 and code_number <= 41:
            return "Queen's pawn"
        elif code_number == 42:
            return "Modern defence, Averbakh system"
        elif code_number >= 43 and code_number <= 44:
            return "Old Benoni defence"
        elif code_number >= 45 and code_number <= 46:
            return "Queen's pawn game"
        elif code_number == 47:
            return "Queen's Indian defence"
        elif code_number == 48 or code_number == 49:
            return "King's Indian, East Indian defence"
        elif code_number == 50:
            return "Queen's pawn game"
        elif code_number >= 51 and code_number <= 52:
            return "Budapest defence"
        elif code_number >= 53 and code_number <= 55:
            return "Old Indian defence"
        elif code_number == 56:
            return "Benoni defence"
        elif code_number >= 57 and code_number <= 59:
            return "Benko gambit"
        elif code_number >= 60 and code_number <= 79:
            return "Benoni defence"
        else:
            return "Dutch"
    elif code_letter == "B":
        if code_number == 0:
            return "King's pawn opening"
        elif code_number == 1:
            return "Scandinavian (centre counter) defence"
        elif code_number >= 2 and code_number <= 5:
            return "Alekhine's defence"
        elif code_number == 6:
            return "Robatsch (modern) defence"
        elif code_number >= 7 and code_number <= 9:
            return "Pirc defence"
        elif code_number >= 10 and code_number <= 19:
            return "Caro-Kann defence"
        else: 
            return "Sicilian defence"
    elif code_letter == "C":
        if code_number >=0 and code_number <= 19:
            return "French defence"
        elif code_number == 20 or code_number == 44 or code_number == 50:
            return "King's pawn game"
        elif code_number >= 21 and code_number <= 22:
            return "Centre Game"
        elif code_number >= 23 and code_number <= 24:
            return "Bishop's opening"
        elif code_number >= 25 and code_number <= 29:
            return "Vienna game"
        elif code_number >= 30 and code_number <= 39:
            return "King's gambit"
        elif code_number == 40:
            return "King's knight opening"
        elif code_number == 41:
            return "Philidor's defence"
        elif code_number >= 42 and code_number <= 43:
            return "Petrov's defence"
        elif code_number == 45:
            return "Scotch game"   
        elif code_number == 46:
            return "Three knights game"
        elif code_number >= 47 and code_number <= 49:
            return "Four knights, Scotch variation"
        elif code_number >= 51 and code_number <= 52:
            return "Evans gambit"
        elif code_number >= 53 and code_number <= 54:
            return "Giuoco Piano"    
        elif code_number >= 55 and code_number <= 59:
            return "Two knights defence"
        else:
            return "Ruy Lopez (Spanish opening)" 
    elif code_letter == "D":
        if code_number == 0 or code_number == 2 or code_number == 4 or code_number == 5:
            return "Queen's pawn game"
        elif code_number == 1:
            return "Richter-Veresov attack"
        elif code_number == 3:
            return "Torre attack (Tartakower variation)"
        elif code_number == 6:
            return "Queen's Gambit"
        elif code_number >= 7 and code_number <= 9:
            return "Queen's Gambit Declined, Chigorin defence"
        elif code_number >= 10 and code_number <= 15:
            return "Queen's Gambit Declined Slav defence" 
        elif code_number == 16:
            return "Queen's Gambit Declined Slav accepted, Alapin variation"
        elif code_number >= 17 and code_number <= 19:
            return "Queen's Gambit Declined Slav, Czech defence"
        elif code_number >= 20 and code_number <= 29:
            return "Queen's gambit accepted"
        elif code_number >= 30 and code_number <= 42:
            return "Queen's gambit declined"
        elif code_number >= 43 and code_number <= 49:
            return "Queen's Gambit Declined semi-Slav" 
        elif code_number >= 50 and code_number <= 69:
            return "Queen's Gambit Declined, 4.Bg5"
        elif code_number >= 70 and code_number <= 79:
            return "Neo-Gruenfeld defence"
        else:
            return "Gruenfeld defence"
    else:
        if code_number == 0 or code_number == 10: 
            return "Queen's pawn game"
        elif code_number >= 1 and code_number <= 9:
            return "Catalan, closed"
        elif code_number == 11:
            return "Bogo-Indian defence"
        elif code_number >= 12 and code_number <= 19:
            return "Queen's Indian defence"
        elif code_number >= 20 and code_number <= 59:
            return "Nimzo-Indian defence"
        else:
            return "King's Indian defence"

# last 50 games
i = len(archives)-1
games = 0
results = [[0,0,0], [0,0,0]]
openings = {}

while i>=0 and games<50:
    month = requests.get(archives[i]).json()["games"]
    j = len(month)
    while j>=0 and games<50:
        j-=1
        try:
            pgn = month[j]["pgn"].split("\n")

            # time
            time = pgn[15].split("\"")[1].split("+")
            if len(time) == 1:
                seconds = int(time[0])
            else:
                seconds = int(time[0])+40*int(time[1])

            if seconds >= 600:
                games+=1
            else:
                continue

            # color
            if pgn[4].split("\"")[1].lower() == username:
                # white 
                color = 0
            else:
                # black
                color = 1
            
            # result

            print(pgn[6])
            result = pgn[6].split("\"")[1].split("-")

            # openings

            opening = eco_codes(pgn[9].split("\"")[-2])

            if opening not in list(openings.keys()):
                openings[opening] = [[0, 0, 0], [0, 0, 0]]
            
            print(f"{opening} {result} {color}")

            if result[color] == "1": # wygrana
                results[color][0] += 1 
                openings[opening][color][0] += 1
            elif result[color] == "1/2": # remis
                results[color][1] += 1 
                openings[opening][color][1] += 1
            else: # porażka
                results[color][2] += 1 
                openings[opening][color][2] += 1

        except:
            pass

    i-=1

print(openings)

"""
month = requests.get(archives[16]).json()["games"]
for i in range(len(month)-1, -1, -1):
    pgn = month[i]["pgn"].split("\n")
    if pgn[4].split("\"")[1] == username:
        color = "white"
    else:
        color = "black"
    print(color)
    time = pgn[15].split("\"")[1].split("+")
    if len(time) == 1:
        seconds = int(time[0])
    else:
        seconds = int(time[0])+40*int(time[1])
    if seconds > 600:
        print("rapid")
"""
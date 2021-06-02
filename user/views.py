from user.functions.eco_codes import eco_codes

from django.http.response import Http404
from django.shortcuts import render

import requests

def num_to_color(num):
    if num == 0:
        return "white"
    else:
        return "black"

# Create your views here.

def user(request, username):
    profile = requests.get(f'https://api.chess.com/pub/player/{username}')

    if profile.status_code != 200:
        raise Http404()

    stats = requests.get(f'https://api.chess.com/pub/player/{username}/stats').json()
    archives = requests.get(f'https://api.chess.com/pub/player/{username}/games/archives').json()["archives"]

    # last 50 games
    i = len(archives)-1
    # games = 0
    results = [[0,0,0], [0,0,0]]
    openings = {}
    tags = []

    while i>=0: #games
        month = requests.get(archives[i]).json()["games"]
        j = len(month)-1 # z jakiegoś powodu jak nie odejmuje to liczy mi 2krotnie ostatnią partię :?
        while j>=0: #games
            j-=1
            try:
                pgn = month[j]["pgn"].split("\n")

                # time
                time = pgn[15].split("\"")[1].split("+")
                if len(time) == 1: #bez dodawanego czasu
                    seconds = int(time[0])
                else:
                    seconds = int(time[0])+40*int(time[1])

                if seconds >= 600:
                    pass
                    #games+=1
                else:
                    continue #jeżeli nie jest to rapid to dalej nie wykonuje tego obrotu pętli 

                # color
                if pgn[4].split("\"")[1].lower() == username:
                    # white 
                    color = 0
                else:
                    # black
                    color = 1
                
                # result

                result = pgn[6].split("\"")[1].split("-")

                # openings

                opening = eco_codes(pgn[9].split("\"")[-2])

                if opening not in list(openings.keys()):
                    openings[opening] = {
                        "white": {
                            "wins": 0,
                            "draws": 0,
                            "loses": 0
                        },
                        "black": {
                            "wins": 0,
                            "draws": 0,
                            "loses": 0
                        }
                    }
                
                if result[color] == "1": # wygrana
                    results[color][0] += 1 
                    openings[opening][num_to_color(color)]["wins"] += 1
                elif result[color] == "1/2": # remis
                    results[color][1] += 1 
                    openings[opening][num_to_color(color)]["draws"] += 1
                else: # porażka
                    results[color][2] += 1 
                    openings[opening][num_to_color(color)]["loses"] += 1
            except:
                pass

        i-=1

    # KONIEC PĘTLI PARTIA PO PARTII

    # tagi

    for opening_name, opening_results in openings.items():
        # 75% wr w co najmneij 10 partii 
        games = opening_results['white']['wins'] + opening_results['white']['draws'] + opening_results['white']['loses'] + opening_results['black']['wins'] + opening_results['black']['draws'] + opening_results['black']['loses']
        if games >= 10:
            if games > 100:
                tags.append({"title": opening_name+" enjoyer", "type": "enjoyer"})
            wins = opening_results['white']['wins'] + opening_results['black']['wins']
            if wins>=0.75*games:
                tags.append({"title": "good in "+opening_name, "type": "good"})
            elif wins<= 0.33*games: # mniej niż 33% wr w co najmniej 10
                tags.append({"title": "week in "+opening_name, "type": "week"})
    
                
    # zmiana na lepsze do przekazania
    overall_results = {
        "white": {
            "wins": results[0][0],
            "draws": results[0][1],
            "loses": results[0][2]
        }, 
        "black": {
            "wins": results[1][0],
            "draws": results[1][1],
            "loses": results[1][2]
        }
    }
    

    return render(request, "user/user.html", {
        "username": username,
        "rapid_rating": stats["chess_rapid"]["last"]["rating"],
        "overall_results": overall_results,
        "openings": openings,
        "tags": tags
    })
    
def index(request):
    return render(request, "user/index.html")
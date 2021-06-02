from user.functions.eco_codes import eco_codes

from django.http.response import Http404
from django.shortcuts import render

import requests, re, math

def num_to_color(num):
    if num == 0:
        return "white"
    else:
        return "black"

# Create your views here !!!.

def user(request, username):
    username = username.lower()
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
    total_time = 0
    total_time_used = 0

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

                # color and time at the end
                split_to_time = re.split('{|}', pgn[-2])
                if pgn[4].split("\"")[1].lower() == username:
                    # white 
                    color = 0
                    if (len(split_to_time) - 1)%4 == 0:
                        #skończyły czarne
                        index = len(split_to_time)-4
                    else:
                        index = len(split_to_time)-2
                    time_at_end = split_to_time[index]
                    num_of_moves = math.ceil(len(split_to_time)//4)
                else:
                    # black
                    color = 1
                    if (len(split_to_time) - 1)%4 == 0:
                        #skończyły czarne
                        index = len(split_to_time)-2
                    else:
                        index = len(split_to_time)-4
                    time_at_end = split_to_time[index]
                    num_of_moves = math.floor(len(split_to_time)//4)

                time_at_end_split = re.split(':| ' ,time_at_end)
                sec_at_end = int(time_at_end_split[1])*3600+int(time_at_end_split[2])*60+float(time_at_end_split[3][:-1])

                if len(time) != 1:
                    game_time = int(time[0])+int(time[1])*num_of_moves
                else:
                    game_time = seconds

                total_time += game_time
                total_time_used += game_time-sec_at_end
                
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
        # 75% wr w co najmneij 10 partii, nie liczymy remisów do wr
        games = opening_results['white']['wins'] + opening_results['white']['draws'] + opening_results['white']['loses'] + opening_results['black']['wins'] + opening_results['black']['draws'] + opening_results['black']['loses']
        if games >= 10:
            wins = opening_results['white']['wins'] + opening_results['black']['wins']
            loses = opening_results['white']['loses']+opening_results['black']['loses']

            if games > 100 and wins > loses:
                tags.append({"title": opening_name+" enjoyer", "type": "enjoyer"})
            
            if wins>=0.75*(wins+loses) and wins>loses:
                tags.append({"title": "good in "+opening_name, "type": "good"})
            elif wins<= 0.33*(wins+loses) and loses>wins: # mniej niż 33% wr w co najmniej 10, nie liczymy remisów do wr
                tags.append({"title": "week in "+opening_name, "type": "week"})
    
    percentage_time = round(total_time_used/(total_time/100))

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
        "tags": tags,
        "percentage_time": percentage_time
    })
    
def index(request):
    return render(request, "user/index.html")
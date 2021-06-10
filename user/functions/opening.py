def f_opening(open_name):
    openings = {
        'Sicilian': {
            'color': 'black',
            'name': 'Sicilian Defense'
        },
        'Queens Gambit': {
            'color': 'white',
            'name': 'Queen\'s Gambit'
        },
        'Kings Gambit': {
            'color': 'white',
            'name': 'King\'s Gambit'
        },
        'Kings Indian Defense': {
            'color': 'black',
            'name': 'King\'s Indian Defense'
        },
        'Italian': {
            'color': 'white',
            'name': 'Italian Game'
        },
        'Giuoco': {
            'color': 'white', #ostatecznie włoska
            'name': 'Italian Game'
        },
        'Ruy': {
            'color': 'white',
            'name': 'Ruy López Opening'
        },
        'French': {
            'color': 'black',
            'name': 'French Defense'
        },
        'Caro': {
            'color': 'white',
            'name': 'Caro-Kann Defense'
        },
        'Scandinavian': {
            'color': 'black',
            'name': 'Scandinavian Defense'
        },
        'English': {
            'color': 'white',
            'name': 'English Opening'
        },
        'Bishops': {
            'color': 'white',
            'name': 'Bishop\'s Opening'
        },
        'Kings Fianchetto': {
            'color': 'white',
            'name': 'King\'s Fianchetto Opening'
        },
        'Modern': {
            'color': 'black',
            'name': 'Modern Defense'
        },
        'Alekhines': {
            'color': 'black',
            'name': 'Alekhine\'s Defense'
        },
        'Petrovs': {
            'color': 'black',
            'name': 'Petrov\'s Defense'
        },
        'Grunfeld': {
            'color': 'black',
            'name': 'Grünfeld Defense'
        },
        'Semi': {
            'color': 'black',
            'name': 'Semi Slav Defense'
        },
        'Kings Indian Attack': {
            'color': 'white',
            'name': 'King\'s Indian Attack'
        },
        'London': {
            'color': 'white',
            'name': 'London System'
        },
        'Nimzo': {
            'color': 'black',
            'name': 'Nimzo-Indian Defense'
        },
        'Benoni': {
            'color': 'black',
            'name': 'Benoni Defense'
        },
        'Scotch':{
            'color': 'white',
            'name': 'Scotch Game'
        },
        'Kings Pawn': {
            'color': 'white',
            'name': 'King\'s Pawn Opening'
        },
        'Queens Pawn': {
            'color': 'white',
            'name': 'Queen\'s Pawn Opening'
        },
        'Three': {
            'color': 'white',
            'name': 'Three Knights Opening'
        },
        'Four': {
            'color': 'black',
            'name': 'Four Knights Game'
        },
        'Slav': {
            'color': 'black',
            'name': 'Slav Defense'
        },
        'Dutch': {
            'color': 'black',
            'name': 'Dutch Defense'
        },
        'Vant': {
            'color': 'white',
            'name': 'Vant Kruijs'
        },
        'Polish': {
            'color': 'white',
            'name': 'Polish Opening'
        },
        'Reti': {
            'color': 'white',
            'name': 'Reti Opening'
        },
        'Nimzowitsch Defense': {
            'color': 'black',
            'name': 'Nimzowitsch Defense'
        },
        'Nimzowitsch Larsen': {
            'color': 'white',
            'name': 'Nimzowitsch-Larsen Attack'
        },
        'Indian': {
            'color': 'black',
            'name': 'Indian Game'
        },
        'Birds': {
            'color': 'white',
            'name': 'Bird\'s Opening'
        },
        'Barnes': {
            'color': 'white',
            'name': 'Barnes Opening'
        },
        'Richter': {
            'color': 'white',
            'name': 'Richter-Veresov Attack'
        },
        'Old Indian': {
            'color': 'black',
            'name': 'Old Indian Defense'
        },
        'Mieses': {
            'color': 'white',
            'name': 'Mieses Opening'
        },
        'Englund': {
            'color': 'black',
            'name': 'Englund Gambit'
        },
        'Ponziani': {
            'color': 'white',
            'name': 'Ponziani Opening'
        },
        'Trompowsky': {
            'color': 'white',
            'name': 'Trompowsky Attack'
        },
        'Vienna': {
            'color': 'white',
            'name': 'Vienna Game'
        },
        'Center': {
            'color': 'white',
            'name': 'Center Game'
        },
        'Van': {
            'color': 'white',
            'name': 'Van Geet Opening'
        },
        'Philidor': {
            'color': 'black',
            'name': 'Philidor Defense'
        },
        'Pirc': {
            'color': 'black',
            'name': 'Pirc Defense'
        },
        'Old Benoni': {
            'color': 'white',
            'name': 'Old Benoni Defense'
        },
        'Grob': {
            'color': 'white',
            'name': 'Grob Opening'
        },
        'Colle': {
            'color': 'white',
            'name': 'Colle System'
        },
        'Torre': {
            'color': 'white',
            'name': 'Torre Attack'
        },
        'Tarrasch': {
            'color': 'black',
            'name': 'Tarrasch Defense'
        },
        'Portuguese': {
            'color': 'white',
            'name': 'Portuguese Opening'
        },
        'Sodium': {
            'color': 'white',
            'name': 'Sodium Attack'
        },
        'Ware': {
            'color': 'white',
            'name': 'Ware Opening'
        },
        'Kadas': {
            'color': 'white',
            'name': 'Kadas Opening'
        },
        'Saragossa': {
            'color': 'white',
            'name': 'Saragossa Opening'
        },
        'Wade': {
            'color': 'black',
            'name': 'Wade Defense'
        },
        'Neo': {
            'color': 'black',
            'name': 'Neo-Grünfeld Defense'
        },
        'Benko': {
            'color': 'black',
            'name': 'Benko Gambit'
        },
        'Clemenz': {
            'color': 'white',
            'name': 'Clemenz Opening'
        },
        'Amar': {
            'color': 'white',
            'name': 'Amar Opening'
        },
        'Anderssen': {
            'color': 'white',
            'name': 'Anderssen Opening'
        }
    }

    openings_list = list(openings.keys())
    open_name_conv = open_name[0]

    for i in range(1, 4):
        if open_name_conv in openings_list:
            return openings[open_name_conv]["name"]
    
        open_name_conv += " "+open_name[i]

    return "NOT IN BASE"
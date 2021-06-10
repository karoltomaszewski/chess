def f_opening(open_name):
    openings = {
        'Sicilian Defense': {
            'color': 'black'
        },
        'Queens Gambit': {
            'color': 'white'
        },
        'Kings Gambit': {
            'color': 'white'
        },
        'Kings Indian Defense': {
            'color': 'black'
        },
        'Italian Game': {
            'color': 'white'
        },
        'Giuoco Piano Game': {
            'color': 'black', #dziwne
            'return': 'Italian Game'
        },
        'Ruy Lopez': {
            'color': 'white'
        },
        'French Defense': {
            'color': 'black'
        },
        'Caro Kann Defense': {
            'color': 'white'
        },
        'Scandinavian Defense': {
            'color': 'black'
        },
        'English Opening': {
            'color': 'white'
        },
        'Bishops Opening': {
            'color': 'white'
        },
        'Kings Fianchetto Opening': {
            'color': 'white'
        },
        'Modern Defense': {
            'color': 'black'
        },
        'Alekhines Defense': {
            'color': 'black'
        },
        'Petrovs Defense': {
            'color': 'black'
        },
        'Grunfeld Defense': {
            'color': 'black'
        },
        'Semi Slav Defense': {
            'color': 'black'
        },
        'Kings Indian Attack': {
            'color': 'white'
        },
        'Nimzo Indian Defense': {
            'color': 'black'
        },
        'Benoni Defense': {
            'color': 'black'
        },
        'Scotch Game':{
            'color': 'white'
        },
        'Scotch Game...4.Nxd4': {
            'color': 'white', #bo ostatecznie jako zwykły Scotch
            'return': 'Scotch Game'
        },
        'Kings Pawn Opening': {
            'color': 'white'
        },
        'Queens Pawn Opening': {
            'color': 'white'
        },
        'Three Knights Opening': {
            'color': 'white'
        },
        'Four Knights Game': {
            'color': 'black'
        },
        'Slav Defense': {
            'color': 'black'
        },
        'Dutch Defense': {
            'color': 'black'
        },
        'Vant Kruijs': {
            'color': 'white'
        },
        'Polish Opening': {
            'color': 'white'
        },
        'Reti Opening': {
            'color': 'white'
        },
        'Nimzowitsch Defense': {
            'color': 'black'
        },
        'Nimzowitsch Larsen Attack': {
            'color': 'white'
        },
        'Indian Game': {
            'color': 'black'
        },
        'Birds Opening': {
            'color': 'white'
        },
        'Barnes Opening': {
            'color': 'white'
        },
        'Richter Veresov Attack': {
            'color': 'white'
        },
        'Old Indian Defense': {
            'color': 'black'
        },
        'Mieses Opening': {
            'color': 'white'
        },
        'Englund Gambit': {
            'color': 'black'
        },
        'Ponziani Opening': {
            'color': 'white'
        },
        'Trompowsky Attack': {
            'color': 'white'
        },
        'Vienna Game': {
            'color': 'white'
        },
        'Center Game': {
            'color': 'white'
        },
        'Van Geet Opening': {
            'color': 'white'
        },
        'Philidor Defense': {
            'color': 'black'
        },
        'Pirc Defense': {
            'color': 'black'
        },
        'Old Benoni Defense': {
            'color': 'white' #???
        },
        'Grob Opening': {
            'color': 'white'
        },
        'Colle System': {
            'color': 'white'
        },
        'Torre Attack': {
            'color': 'white'
        },
        'Tarrasch Defense': {
            'color': 'black'
        },
        'Portuguese Opening': {
            'color': 'white'
        },
        'Sodium Attack': {
            'color': 'white'
        },
        'Ware Opening': {
            'color': 'white'
        },
        'Kadas Opening': {
            'color': 'white'
        },
        'Saragossa Opening': {
            'color': 'white'
        },
        'Clemenz Opening': {
            'color': 'white'
        },
        'Amar Opening': {
            'color': 'white'
        },
        'Anderssen Opening': {
            'color': 'white'
        }
    }

    openings_list = list(openings.keys())
    open_name_conv = open_name[0]

    for i in range(1, 3):
        if open_name_conv in openings_list:
            if 'return' in openings[open_name_conv].keys():
                return openings[open_name_conv]["return"]
            return open_name_conv
        open_name_conv += " "+open_name[i]

    return "NOT IN BASE"
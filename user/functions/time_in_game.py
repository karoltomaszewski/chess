def time_in_game(start_time, end_time):
    start_time = start_time.split("\"")[1].split(":")
    start_time_h = int(start_time[0])
    start_time_m = int(start_time[1])
    start_time_s = int(start_time[2])

    end_time = end_time.split("\"")[1].split(":")
    end_time_h = int(end_time[0])
    end_time_m = int(end_time[1])
    end_time_s = int(end_time[2])

    
    if end_time_h < start_time_h:
        end_time_h += 24
    
    start = start_time_h+start_time_m/60+start_time_s/3600
    end = end_time_h+end_time_m/60+end_time_s/3600

    return(end-start)

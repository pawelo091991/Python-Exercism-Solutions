result= ({"win" : (1,1,0,0,3), "draw": (1,0,1,0,1), "loss": (1,0,0,1,0)},
             {"win" : (1,0,0,1,0), "draw": (1,0,1,0,1), "loss": (1,1,0,0,3)})

def tally(rows):
    
    teams = {}

    for row in rows:
        match = row.split(";")
        for idx in range(0,2):
            if match[idx] not in teams:
                teams[match[idx]] = [0,0,0,0,0]
        
            teams[match[idx]] = [x+y for x,y in zip(teams[match[idx]], result[idx][match[2]])]
            
    
    teams_list = []

    for team in teams.keys():
        teams_list.append("{0:31}|{1:3} |{2:3} |{3:3} |{4:3} |{5:3}".format(team, teams[team][0], teams[team][1], 
                                                                            teams[team][2], teams[team][3], teams[team][4]))
    
    teams_list.sort(key = lambda x: x[0:20])
    teams_list.sort(key = lambda x: x[53:55], reverse=True)
    return ["Team {0:25} | MP |  W |  D |  L |  P".format("")] + teams_list

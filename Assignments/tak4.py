import random

def ipl_game():
    wel = "Welcome to IPL 22k"
    print(wel.center(100))
    teams = ['CSK','RCB','KXIP','KKR','DC','SHR','LSR','RR','GT','MI']
    for i in teams:
        print(i,end=" ")
    team = input("\nEnter your team: ").upper()
    while True:
        if team in teams:
            break
        else:
            team = input("\nEnter your team: ")
    opp_team = random.choice(teams)
    while True:
        if opp_team == team:
           opp_team = random.choice(teams)
        else:
            break
    toss = input("\nEnter your toss in H/T: ").upper()
    while True:
        if toss=='H':
            print(f"Team {team} got Batting")
            break
        elif toss == 'T':
            print(f"Team {team} got Balling")
            break
        else:
            toss = input("Invalid Toss Enter your toss in H/T").upper()
    ball_no = 1
    temp0 = 0
    sum0 = 0
    possible_no = [0,1,2,3,4,6,'out','runout','lbw','wb']
    print(f"My-Team: {team}")
    print(f"Rival-Team: {opp_team}")
    while ball_no<=10:
        input()
        random_run = random.choice(possible_no)
        print(f"{team}-{sum0}/{temp0} Ball-{ball_no} : {random_run}")
        ball_no += 1
        if type(random_run) == int:
            sum0 += random_run
        if random_run == 'out' or random_run == 'runout' or random_run == 'lbw':
            temp0 += 1
        elif random_run == 'wb':
            ball_no -= 1
        else:
            continue
        if temp0 == 2:
            break
    ball_no = 1
    temp0 = 0
    sum1 = 0
    if toss == 'H':
        print(f"Team {opp_team} got batting and requiered {sum0+1} to win the match")     
    if toss == 'T':
        print(f"Team {opp_team} got balling and {team} requiered {sum0+1} to win this match")
    while ball_no<=10:
        input()
        random_run = random.choice(possible_no)
        print(f"\n{opp_team}-{sum1}/{temp0} Ball-{ball_no} : {random_run}")
        ball_no += 1
        if type(random_run)==int:
            sum1 += random_run
        if random_run == 'out' or random_run == 'runout' or random_run == 'lbw':
            temp0 += 1
        elif random_run == 'wb':
            ball_no -= 1
        else:
            continue
        if temp0 == 2:
            break
    if sum0 > sum1:
        if toss == 'H':
            print(f"\nTeam {team} wins with {sum0-sum1} runs")
        else:
            print(f'\nTeam {opp_team} wins with {sum0-sum1} runs')
    elif sum0< sum1:
        if toss == 'H':
            print(f"\nTeam {opp_team} wins with {sum1-sum0} runs")
        else:
            print(f'\nTeam {team} wins with {sum1-sum0} runs')
    else:
        print("\nMatch Tied")
ipl_game()
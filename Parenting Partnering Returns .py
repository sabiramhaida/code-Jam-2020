for t in range(int(input())):
    n = int(input())
    end_C = 0
    end_J = 0
    start_C = 24*60
    start_J = 24*60
    activitySequence = ''
    activities = []
    Impo = False
    for i in range(n):
        ac = list(map(int, input().split()))
        activities.append([i,ac])

    activities = sorted(activities, key = lambda x: x[1])
    for i in range(n):
        start, end = activities[i][1]
        if(start >= end_C or end < start_C):
            activities[i].append('C')
            start_C = start
            end_C =max(end,end_C)
        elif(start >= end_J or end< start_J):
            activities[i].append('J')
            start_J = start
            end_J = max(end,end_J)
=        else:
            Impo = True
    if(Impo):
        print('Case #{}:'.format(t+1),"IMPOSSIBLE")
    else:
        activities.sort()
        for i in range(n):
            activitySequence+=activities[i][2]
        print('Case #{}:'.format(t+1),activitySequence)

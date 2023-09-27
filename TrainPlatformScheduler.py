def platformcount():
    arrive = []
    depart = []
    n = int(input("\nEnter number of trains arriving and departing in a day: "))
    for i in range(n):
        a = int(input("\nEnter arrival time of train (0000<HHMM<2359): "))
        d = int(input("\nEnter departure time of train (Arrival time<HHMM<2359): "))
        arrive.append(a)
        depart.append(d)
    l = []
    for i in range(n):
        train = []
        a = arrive[i]
        d = depart[i]
        train.append(a)
        train.append(d)
        l.append(train)
    #bubble sort l according to arrival times
    
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j][0] > l[j+1][0] :
                l[j], l[j+1] = l[j+1], l[j]
    platform = []
    train = [l[0][0],l[0][1]]
    platform.append(train)
    last = l[0][1]
    system = []
    s = []
    s.append(platform)
    s.append(last)
    system.append(s)
    for i in range(1,n):
        flag = 0
        for j in range(len(system)):
            if l[i][0]>system[j][1]:
                system[j][1]=l[i][1]
                flag = 1
                trains = [l[i][0],l[i][1]]
                system[j][0].append(trains)
                break
        if flag==0:
            newlast = l[i][1]
            train = [l[i][0],l[i][1]]
            trains = [] 
            trains.append(train)
            newplat = []
            newplat.append(trains)
            newplat.append(newlast)
            system.append(newplat)
    for k in range(len(system)):
        print("\nPlatform: ",k+1)
        plat = system[k][0]
        for j in range(len(plat)):
            train = plat[j]
            print("\nTrain ",j+1,": ",train[0]," : ",train[1])
    print("\nNumber of platforms required: ",len(system))
                  
platformcount()
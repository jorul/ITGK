def mshd2s(minutter,sekunder,hundredeler):
    sek = minutter*60 + sekunder + hundredeler*0.01
    return sek

def rundeTid(startTid,sluttTid):
    start_sek = mshd2s (startTid[0],startTid[1],startTid[2])
    slutt_sek = mshd2s(sluttTid[0],sluttTid[1],sluttTid[2])
    tid = slutt_sek - start_sek
    return tid

def alleRunderTider(passeringsTider):
    rundetider = []
    for i in range(1,len(passeringsTider)):
        tid = rundeTid(passeringsTider[i-1],passeringsTider[i])
        rundetider.append(tid)
    return rundetider

print(alleRunderTider([[0,20,0],[0,50,10],[1,21,21],[1,53,33]]))

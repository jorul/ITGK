def bidOK(melding, stikk):
    mld = melding.split()
    if int(mld[0]) + 6 <= stikk:
        return True
    return False

def utgang(melding,stikk):
    mld = melding.split()
    if mld[1]== 'grand':
        if int(mld[0])+6 <= stikk and int(mld[0])+6 >= 9:
            return True
    elif mld[1] == 'ruter' or mld[1] == 'kløver':
        if int(mld[0])+6 <= stikk and int(mld[0])+6 >= 11:
            return True
    elif mld[1] == 'hjerter' or mld[1] == 'spar':
        if int(mld[0])+6 <= stikk and int(mld[0])+6 >= 10:
            return True
    return False

def poeng_for_trekk(melding,stikk):
    mld = melding.split()
    if mld[1]== 'grand':
        return (stikk-6)*30 + 10
    elif mld[1] == 'ruter' or mld[1] == 'kløver':
        return (stikk-6)*20
    elif mld[1] == 'hjerter' or mld[1] == 'spar':
        return (stikk-6)*30



def bridgePoints(melding,stikk):
    poeng = 0
    mld = melding.split()
    if (int(mld[0]) +6)<= stikk:
        if utgang(melding,stikk)== True:
            poeng += 300
        elif bidOK(melding,stikk) == True:
            poeng += 50
        poeng += poeng_for_trekk(melding,stikk)
    else: #beit
        poeng += (stikk-(int(mld[0])+6))*50
    return poeng

print(bridgePoints('3 ruter', 10))

def main():
    spill_liste = []
    Lag = input('Lag (N/S eller Ø/V, annet for å slutte): ')
    while Lag == 'N/S' or Lag == 'Ø/V':
        melding= input('Melding: ')
        stikk = int(input('Stikk: '))
        poeng = bridgePoints(melding,stikk)
        if poeng > 0:
            spill_liste.append([Lag, melding, stikk, poeng,0])
        else:
            spill_liste.append([Lag, melding, stikk, 0,-poeng])
        Lag = input('Lag (N/S eller Ø/V, annet for å slutte): ')
    
    sum_NS = 0
    sum_ØV = 0
    for i in range(len(spill_liste)):
        print(spill_liste[i])
        if spill_liste[i][0] == 'N/S':
            sum_NS += spill_liste[i][3]
            sum_ØV += spill_liste[i][4]
        else:
            sum_ØV += spill_liste[i][3]
            sum_NS += spill_liste[i][4]
    print('Total score:')
    print(f'N/S {sum_NS}')
    print(f'Ø/V {sum_ØV}')
main()
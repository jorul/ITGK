def p_ig(t,v,n,rgas = 8.31452):
    return ((n*rgas*t)/v)


def p_ig_pptable(v,t,n):
    nyliste =[]
    for volum in v:
        delliste = [volum]
        for temp in t:
            delliste.append(p_ig(temp,volum,n))
        nyliste.append(delliste)
    return nyliste



nv = 10 # number of volumes (rows) [-]
nt = 3 # number of temperatures (columns) [-]
 
# Variables.
n = 10 # [mol]
t = [100 + float(j)*200 for j in range(nt)] # [K]
v = [10**(-float(i)/nv) for i in range(1, nv+1)] 
 
table = p_ig_pptable(v,t,n)
print(table)

print("| Volum (m^3)".ljust(21),"|",("Temp. = "+str(t[0])+"K").ljust(19),"|",("Temp. = "+str(t[1])+"K").ljust(19),"|",("Temp. = "+str(t[2])+"K").ljust(19),"|")
print("-"*89)


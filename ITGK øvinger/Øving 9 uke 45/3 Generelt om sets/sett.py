mitt_set = set()
for i in range(1,20,2):
    mitt_set.add(i)

nytt_sett = set()
for i in range(1,10,2):
    nytt_sett.add(i)


set3 = mitt_set-nytt_sett
print(set3)

set4 = mitt_set.union(nytt_sett)
print(set4)

def allUnique(lst):
    settet = set(lst)
    if len(lst)==len(settet):
        return True
    else:
        return False

print(allUnique([1,3,2,6,8]))
print(allUnique([1,3,5,2,3,7]))

def removeDuplicates(lst):
    return list(set(lst))

print(removeDuplicates([1,3,5,2,3,7]))
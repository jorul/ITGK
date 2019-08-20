def to_siste(liste):
    ordet = ''
    for i in liste:
        ordet += i[len(i)-2:]
    return ordet

print(to_siste(["sabel","kan","mestr","kuleis"]))
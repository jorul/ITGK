def seq_search(liste,item):
    for i in liste:
        if i == item:
            return True
    return False

print(seq_search([1,2,3,4,5],5))
print(seq_search([1,2,3,4],5))

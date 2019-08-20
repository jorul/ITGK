def is_six_at_edge(i):
    førsteledd = i[0]
    sisteledd =i[len(i)-1]
    if sisteledd == 6 or førsteledd == 6:
        return True
    else:
        return False

print(is_six_at_edge([1,2,3,4,5,6]))

print(is_six_at_edge([1,2,3,4,5,6,7]))
def lengde(ord):
    if len(ord)==1:
        return '0' + ord
    else:
        return ord

def format_time(variabel):
    timer = str(variabel //3600)
    minutter = str((variabel%3600)//60)
    sekunder = str(variabel%60)


    print(f'{lengde(timer)}:{lengde(minutter)}:{lengde(sekunder)}')

format_time(12305)
def add_data(user):
    user_liste = user.split(', ')
    user_liste[2] = int(user_liste[2])
    return user_liste


def get_person(given_name, facebook):
    nyliste = []
    for i in range(len(facebook)):
        if given_name == facebook[i][0]:
            nyliste.append(facebook[i])
    return nyliste


def main():
    print('Hello, welcome to Facebook. Add a new user by writing "given_name surname age gender relationship_status". ')
    print("Write done when you are done")
    facebook = []
    svar = ''
    while svar != 'done':
        svar = input('Add new user: ')
        if svar != 'done':
            facebook.append(add_data(svar))
    print('Ok')
    search = ''
    while search != 'done':
        search = input('Search for a user: ')
        if search != 'done':
            person = get_person(search, facebook)
            for i in range (len(person)):
                if person[i][3].lower() == 'male':
                    print(f'{person[i][0]} {person[i][1]} is {person[i][2]} years old, his relationship status is {person[i][4]}.')
                elif person[i][3].lower() == 'female':
                    print(f'{person[i][0]} {person[i][1]} is {person[i][2]} years old, her relationship status is {person[i][4]}.')
                else:
                    print(f"{person[i][0]} {person[i][1]} is {person[i][2]} years old, {person[i][0]}'s relationship status is {person[i][4]}.")

                    
main()
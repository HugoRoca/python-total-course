client = {
    'name': 'Hugo',
    'age': 45,
    'profession': 'engineer'
}

movie = {
    'title': 'Matrix',
    'resume': {
        'director': 'Lana y Lilly Wachowski'
    }
}

items = [client, movie, 'book']

for e in items:
    match e:
        case {'name': name, 'age': age, 'profession': profession}:
            print('Is client!')
            print(name, age, profession)
        case {'title': title, 'resume': {'director': director}}:
            print('Is movie!')
            print(title, director)
        case _:
            print('I dont know')

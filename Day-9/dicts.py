first = {
    'iron-man':'And the truth is, I am iron man',
    'captain-america':'I can do this all day!',
    'black-widow':'Hey hulk! Wassup',
    'tanjirou':'Uchino kata',
    'eren yager':'tatake'
}
# print(first['eren yager'])

first['black-widow'] = 'hehe'

first['naruto'] = 'I will marry hinata sama!'

# print(first['naruto'])

for thing in first:
    print(thing)
    print(first[thing])
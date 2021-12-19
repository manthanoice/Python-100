#List Comprehension

num = [1, 2, 3, 4]
new_list = [n+1 for n in num]
print(new_list)

num_2 = [68, 419]
new_list_2 = [n+1 for n in num_2]
print(new_list_2)

name = 'Okabe'
new_name = print([n for n in name])

new_double = [n*2 for n in range(1, 5)]
print(new_double)

the_names = ['Okarinnn', 'Shizume', 'Daru', 'Maho', 'Mikasa', 'Eren Yeger']
new_names = [name for name in the_names if len(name)<9]
print(new_names)

cap_names = [name.upper() for name in the_names if len(name)>5]
print(cap_names)
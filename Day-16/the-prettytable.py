from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Countries",['India', 'USA', 'Canada', 'UK'])
table.add_column("States", ['Gujarat', 'Maharashtra', 'West Bengal', 'Karnataka'])
table.add_column("City",['Junagadh', 'Ahmedabad', 'Mumbai', 'Banglore'])
print(table)

pokemon = PrettyTable()
pokemon.add_column('Pokemon Name',['Pikachu', 'Squirtle', 'Charmander'])
pokemon.add_column('type', ['Electric', 'Water', 'Fire'])
print(pokemon)
from prettytable import PrettyTable

table = PrettyTable()

# adding coloumn and its values
table.add_column("Pokeman Name", ["Pikachu", "Sqirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# changing alignment of data from centre to left
table.align = 'l'

print(table)
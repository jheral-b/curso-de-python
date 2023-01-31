# Sets
# Los sets no permite datos repetidos.
# Los datos siempre se guardan de manera desordenada.

my_set = set()
my_other_set = {}

my_other_set = {"Jheral", "Barrera", 22}

# Por mucho que agreges el mismo valor, este no se repetira en el set
my_other_set.add("Riquelme")
print(my_other_set)

my_other_set.add("Riquelme")
print(my_other_set)

# De esta manera es posible saber si existe o no el string en el set
print("Jheral" in my_other_set)
print("Jherald" in my_other_set)

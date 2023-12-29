set_countries = {"Col","Mex","Bol","Col"} # No se puede repetir elementos en un set.
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,3,4,5,6,7,8,9,10}
print(set_numbers)

set_types = {1, "Hola", False, 12.12, 'Ciao'}
print(set_types)

set_from_string = set("Hola Mundo")
print(set_from_string)

set_from_tuple = set(("Hola", "Mundo", ("Hola", "Mundo")))
print(set_from_tuple)

numbers = [1,2,3,4,1,2,3,4]
set_from_list = set(numbers)
print(set_from_list)
unique_numbers = list(set_from_list)
print(unique_numbers)

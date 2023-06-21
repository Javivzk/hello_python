### Strings ###

my_string = "My String"
my_other_string = 'My other String'

print(len(my_string))
print(len(my_other_string))

print (my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Javier", "Vizcaino", 30
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #Parsea todo a la vez LA MAS CORRECTA Y MAS RAPIDA
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) # string %s int %d ESTA ES LA MAS CORRECTA
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #La mejor de todas

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo

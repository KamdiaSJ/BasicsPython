def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    elif lang == 'ger':
        return "Hallo"
    elif lang == "hindi":
        return "Namaste"
    else:
        return "Hello"
print(greet('en'),'Glen')
print(greet('es'),'Alma')
print(greet('fr'),'Barrete')
print(greet('ger'),'Mikael')
print(greet('hindi'),'Suraj')
print(greet('urdu'),'Karim')

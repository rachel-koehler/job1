#JOB1
def My_print_hello():
    print("Hello world")
My_print_hello()

#JOB2
def My_print_name(name:str):
    print(name)
My_print_name("Rachel")

#JOB3
def Add(a:int, b:int):
    result = a+b
    return result
print(Add(1,2))

#JOB 4
def GetHello():
    print("Hello la Plateforme")
GetHello()

#JOB5 -> trouver une sous-fonction pour opérateurs pour aller plus loin
# eventuellement penser à insérer méthode input_user
def calcule(num1:int, operator:str, num2:int):
    if operator =="+":
        result = num1+num2
    elif operator == "-":
        result= num1-num2
    elif operator == "/":
        result = num1/num2
    else: 
        result= num1*num2

    operation = "{} {} {} = {}"
    print(operation.format(num1, operator, num2, result))
calcule(91, "*", 9)

#JOB6
def pos_or_neg(nombre:int):
    if nombre > 0:
        print("positif")
    else:
        print("négatif")
pos_or_neg(5) #à tester avec 5 iy -5

#JOB7
def language(langage:str): # afficher 'return' à la place des 'print'
    if langage == "Javascript":
        print("tu es un développeur web")
    elif langage == "python":
        print("tu es un développeur IA")
    elif langage == "java":
        print("tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es un développeur mobile")
    else:
       print("un jour, je serai le meilleur développeur...")

language("java")

#OU
def language(langage:str): # afficher 'return' à la place des 'print'
    if langage == "Javascript":
        return("tu es un développeur web")
    elif langage == "python":
        return("tu es un développeur IA")
    elif langage == "java":
        return("tu es un développeur logiciel")
    elif langage == "reactjs":
        return("tu es un développeur mobile")
    else:
       print("un jour, je serai le meilleur développeur...")

language("java")

#JOB8
def saisons(type:str, saison:str):
    if type == "fruits" and saison=="hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison=="été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison=="hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison=="été":
        print("artichaut, aubergine, navet")
    else:
        print("Erreur!")

saisons("fruits", "été")

#JOB9
def moyenne(a, b, c):
    result = (a+b+c)/3
    if 15<result<20:
        print("Très bon élève")
    elif 11<result<14:
         print("Bon élève")
    elif 8<result<10:
         print("Elève moyen")
    else:
         print("Elève devant faire des efforts")

a, b, c = map(int, input("Saisie trois notes séparées par des espaces: ").split())
moyenne(a, b, c) #méthode .map permet d'inputer un type donnée précis à l'input_user

#JOB10
def pair_ou_impair(a:int):
    if not isinstance(a, int):
        print("Veuillez saisir un nombre entier positif !")
    elif 2%a != 0:
        print("Impair")
    else:
        print("Paire")

pair_ou_impair(5.2)


#JOB11
def min_to_h(a:int):
    x = a/60
    x_to_str = str(x)
    X = x_to_str[0:2]
    y = a%60
    y_to_str = str(y)
    Heures = "Il est {} heures et {} minutes."
    print(Heures.format(X, y_to_str))

min_to_h(738)

# OU

def time_to_txt(a:int):
    x = a/60
    x_to_str = str(x)
    X = x_to_str[0:2]
    y = a%60
    y_to_str = str(y)
    print(f"Il est {X} heures et {y_to_str} minutes.")

min_to_h(738)

# Autre proposition:
def time_to_txt(a:int):
    x = a/60
    x_to_str = str(x)
    y = a%60
    y_to_str = str(y)
    if len(x_to_str)< 4:
        X = x_to_str[0]
    else:
        X = x_to_str[0:2]
        
    print(f"Il est {X} heures et {y_to_str} minutes.")

min_to_h(150)

# Pour aller plus loin:

def reverse_string(a:str):
    return a[::-1]

test = reverse_string("nikana")
print(test)

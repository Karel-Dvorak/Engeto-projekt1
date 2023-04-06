"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Dvořák
email: dvorak.karl@seznam.cz
discord: Karel_D#8832
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = {
    'bob':'123', 
    'ann':'pass123', 
    'mike':'password123',
    'liz':'pass123'
}
oddelovac = '-' * 40
# Vyžádá si od uživatele přihlašovací jméno a heslo

user_name = input('User name:')
password = input('password:')

# Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů

if uzivatele.get(user_name) == password:
    print(oddelovac)
    print('Welcome to the app, bob \n We have 3 texts to be analyzed.')
    print(oddelovac)
else:
    print('unregistered user, terminating the program..')
    quit()

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
print(f"Text č.1 {TEXTS[0]}", oddelovac, sep='\n')
print(f"Text č.2\n {TEXTS[1]}", oddelovac, sep='\n')
print(f"Text č.3\n {TEXTS[2]}", oddelovac, sep='\n')

# Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
vyber_textu = input('Zadej číslo textu:')

#if vyber_textu not in int(TEXTS[3]):
   # print('Číslo není ve výběru, ukončuji program!')
    #quit()
#pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

# Pro vybraný text spočítá následující statistiky:

# počet slov,
# počet slov začínajících velkým písmenem,
# počet slov psaných velkými písmeny,
# počet slov psaných malými písmeny,
# počet čísel (ne cifer),
# sumu všech čísel (ne cifer) v textu.

# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat 
# četnost různých délek slov v textu. 
# Například takto:
# 7| * 1
# 8| *********** 11
# 9| *************** 15
# 10| ********* 9
# 11| ********** 10
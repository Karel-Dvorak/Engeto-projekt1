"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Dvořák
email: dvorak.karl@seznam.cz
discord: Karel_D#8832
"""
TEXTS = ['''Situated about 10 miles west of Kemmerer,
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
oddelovac = '-' * 60
oddelovac_kapitola = '=' * 60
# Vyžádá si od uživatele přihlašovací jméno a heslo

user_name = input('User name:')
password = input('password:')

# Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů

if uzivatele.get(user_name) == password:
    print(
    oddelovac,
    'Welcome to the app, bob \n We have 3 texts to be analyzed.',
    oddelovac_kapitola,
    sep='\n')
else:
    print('unregistered user, terminating the program..')
    quit()

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
print(f"TEXT 1\n {TEXTS[0]}", oddelovac,
    f"TEXT 2\n {TEXTS[1]}", oddelovac,
    f"TEXT 3\n {TEXTS[2]}", oddelovac_kapitola, sep='\n')

# Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
#pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
vyber_textu = input('Enter a number btw. 1 until 3 to select: ')

if vyber_textu.isnumeric() and 1 <= int(vyber_textu) <= 3:
    print(oddelovac, f"{TEXTS[int(vyber_textu) -1]}", oddelovac_kapitola, sep='\n')
elif vyber_textu.isalpha():
    print('This is not a number, terminating the program..')
    quit()
else:
    print('The number is not in the selection, terminating the program..')
    quit()

# Pro vybraný text spočítá následující statistiky:
# počet slov

cisty_text = []
for slovo in TEXTS[int(vyber_textu) - 1].split():
    ciste_slovo = slovo.strip(',.!?-')
    cisty_text.append(ciste_slovo.lower())
#počet slov začínajících velkým písmenem,
# počet slov psaných malými písmeny,
# počet čísel (ne cifer),
# unikátní (typu 30N )
# sumu všech čísel (ne cifer) v textu.
slova_velkymi = []
slova_malymi = []
slova_cisla = []
slova_velka = []
unikatni = []

for slovo in TEXTS[int(vyber_textu) - 1].split():
    slovo_v = slovo.strip(',.!?-')
    if slovo.istitle() and slovo.isupper():
        unikatni.append(slovo_v)
    elif slovo.isdigit():
        slova_cisla.append(int(slovo_v))
    elif slovo.istitle() or slovo.isupper():
        slova_velkymi.append(slovo_v)
    else:
        slova_malymi.append(slovo_v)
for velka_p in slova_velkymi:
    if velka_p.isupper():
        slova_velka.append(velka_p)

print(f"""There are {len(cisty_text)} words in the select text.
There are {len(slova_velkymi)} titlecase words.
There are {len(slova_velka)} uppercase words.
There are {len(slova_malymi)} lowercase words.
There are {len(slova_cisla)} numeric strings.
The sum of all the numbers {sum(slova_cisla[:])}""")

# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat 
# četnost různých délek slov v textu. 

print(oddelovac, f"LEN|    OCCURENCES   |NR.", oddelovac, sep = '\n')
delka_slov = {}
for delka in cisty_text:
    if len(delka) not in delka_slov:
        delka_slov[len(delka)] = 1
    else:
        delka_slov[len(delka)] = delka_slov[len(delka)] + 1
for key, value in sorted(delka_slov.items()):
    print(f"{key: ^3}|{value * '*': <17}|{value}")

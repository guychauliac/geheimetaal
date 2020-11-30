alphabet= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

def versleutel_letter(letter, sleutel_letter):
    nieuwe_letter = alphabet.index(letter) + alphabet.index(sleutel_letter)
    if nieuwe_letter >= len(alphabet):
        nieuwe_letter -= len(alphabet)
    return alphabet[nieuwe_letter]

def ontsleutel_letter(letter, sleutel_letter):
    nieuwe_letter = alphabet.index(letter) -  alphabet.index(sleutel_letter)
    if nieuwe_letter < 0:
        nieuwe_letter += len(alphabet)
    return alphabet[nieuwe_letter]

def versleutel_zin(zin, sleutel):
    huidige_sleutel_positie = 0
    versleutelde_zin = ""
    for character in zin:
        versleutelde_zin += versleutel_letter(character, sleutel[huidige_sleutel_positie])
        huidige_sleutel_positie = volgende_sleutel_positie(huidige_sleutel_positie, sleutel)
    return versleutelde_zin

def volgende_sleutel_positie(huidige_positie, sleutel):
    huidige_positie += 1
    if huidige_positie >= len(sleutel):
        huidige_positie = 0
    return huidige_positie

def ontsleutel_zin(zin, sleutel):
    huidige_sleutel_positie = 0
    ontsleutelde_zin = ""
    for character in zin:
        ontsleutelde_zin += ontsleutel_letter(character, sleutel[huidige_sleutel_positie])
        huidige_sleutel_positie = volgende_sleutel_positie(huidige_sleutel_positie, sleutel)
    return ontsleutelde_zin
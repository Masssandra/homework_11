import random
import json
import datetime

def getScores():
    highscore_data = readFile("highscore.txt")

    scores = json.loads(highscore_data)

    return scores

def addScore(score):
    score_date = str(datetime.datetime.now())

    score_record = {
        "date": score_date,
        "attempts": score,
        "name": player,
        "secret": secret_number,
        "mistakes": wrong_guesses
    }

    scores = getScores() #gaunam esamus taskus

    scores.append(score_record)#pridedam naujus taskus

    data = json.dumps(scores) #isverciam lista i json atgal

    writeFile("highscore.txt", data) #irasom i rezultatu faila nauja lista

def readFile(filename):
    file = open(filename, "r")

    return file.read()

def writeFile(filename, data):
    file = open(filename, "w")

    file.write(str(data))

    return readFile(filename)

scores = getScores()

print("Sveiki! Top rezultatas yra:")

place = 1

top_high_score = sorted(scores, key=lambda k: k['attempts'])[:3]

for score in top_high_score:
    print(str(place) + " vieta: " + "Zaidejas " + score["name"] + " slaptasis skaicius buvo " + str(score["secret"]) + " klaidingu spejimu  " + " (" + str(score["date"]) + ")")
    # print("data", score["date"], "atspeta per", score["attempts"], "kartu")
    place += 1

# highscore = readFile("highscore.txt")

# print("Geriausias rezultatas: " + highscore + ". Permusk jei gali.")
print("-----")

player = input("Iveskite savo varda: ")
nuo = int(input("Nuo kurio skaiciaus spesim? Kokia intervalo pradzia?"))
iki = int(input("Iki kurio skaiciaus spesim? Kokia intervalo pabaiga?"))

skaicius = random.randint(nuo, iki)

turn = 0

paskutinis_spejimas = 0

secret_number = skaicius

# r - read
# w - write (perrasys tai, kas viduje yra)
# a - add write (dades iki to, kas viduje yra)

def checkNumber(numberProvided, numberToGuess):
    if numberProvided == numberToGuess:
        return True
    else:
        return False

wrong_guesses = []

while skaicius != paskutinis_spejimas:
    print("Musu skaicius " + str(skaicius))

    turn = turn + 1

    currentTurn = str(turn)

    guess = int(input(currentTurn + " guess. Guess the number:"))

    if checkNumber(guess, skaicius):
        print("Congratulations")
    else:
        print("Try again")

    paskutinis_spejimas = guess

wrong_guesses.append(int(currentTurn) - 1)

addScore(turn)

# if turn < int(highscore):
#     writeFile("highscore.txt", turn)

print("Zaidimas baigtas, pabaiga cia")
print("Atspeti tau uztruko " + str(turn) + " spejimus")

import winsound

dico_morse = {
    "A": [".-", "A"],
    "B": ["-...", "B"],
    "C": ["-.-.", "C"],
    "D": ["-..", "D"],
    "E": [".", "E"],
    "F": ["..-.", "F"],
    "G": ["--.", "G"],
    "H": ["....", "H"],
    "I": ["..", "I"],
    "J": [".---", "J"],
    "K": ["-.-", "K"],
    "L": [".-..", "L"],
    "M": ["--", "M"],
    "N": ["-.", "N"],
    "O": ["---", "O"],
    "P": [".--.", "P"],
    "Q": ["--.-", "Q"],
    "R": [".-.", "R"],
    "S": ["...", "S"],
    "T": ["-", "T"],
    "U": ["..-", "U"],
    "V": ["...-","V"],
    "W": [".--", "W"],
    "X": ["-..-", "X"],
    "Y": ["-.--", "Y"],
    "Z": ["--..", "Z"],

    " ": ["/", " "],

    "1": [".----", "1"],
    "2": ["..---", "2"],
    "3": ["...--", "3"],
    "4": ["....-", "4"],
    "5": [".....", "5"],
    "6": ["-....", "6"],
    "7": ["--...", "7"],
    "8": ["---..", "8"],
    "9": ["----.", "9"],
    "0": ["-----", "0"],
}

# Traducteur de Alphabet vers Morse
def text_to_morse(dico_morse):
    alphabet = input("Entrez votre texte : ")

    morse_tran = ""
    morse_tran_forma = ""

    for i in range(len(alphabet)):
        for k in dico_morse.keys():
            if alphabet[i] == k:
                morse_tran = morse_tran + " " + dico_morse[k][0]

    for k in range(len(morse_tran)):
        if morse_tran[k] == " ":
            morse_tran_forma = morse_tran_forma + " "
        elif morse_tran[k] == "-":
            morse_tran_forma = morse_tran_forma + "taah"
        elif morse_tran[k] == ".":
            morse_tran_forma = morse_tran_forma + "ti"

    print("Traduction en morse :", morse_tran, "\nReprésentation/cadence :", morse_tran_forma)

    play_sound(morse_tran)

    return morse_tran, morse_tran_forma

def play_sound(morse_tran):
    for n in range(len(morse_tran)):
        if morse_tran[n] == " ":
            winsound.Beep(37, 200)
        elif morse_tran[n] == ".":
            winsound.Beep(500, 200)
        elif morse_tran[n] == "-":
            winsound.Beep(500, 600)


# Traducteur de Morse vers Alphabet
def morse_to_text(dico_morse):
    morse = input("Entrez votre texte en morse : ")
    list_morse = morse.split(" ", len(morse))

    text = ""

    for i in range(len(list_morse)):
        for key, value in dico_morse.items():
            if list_morse[i] == value[0]:
                text = text + key

    return print(text)

# Initilisation du programme
print("Traducteur de L'Alphabet/Morse\n")
print("Commandes du programme:\n[1] Traducteur de Alphabet vers Morse\n[2] Traducteur de Morse vers Alphabet")

choice = int(input(">>>> "))

if choice == 1:
    text_to_morse(dico_morse)
elif choice == 2:
    morse_to_text(dico_morse)
else:
    print("Erreur : Vous n'avez pas entré une option valable.")

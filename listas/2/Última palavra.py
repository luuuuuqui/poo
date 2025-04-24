sentence = input("Digite uma frase:\n")

lastSpace = sentence.rfind(" ")
lastWord = sentence[lastSpace + 1:]

print(lastWord)
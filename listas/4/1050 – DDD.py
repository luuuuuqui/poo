dddToCityMapping = {
    61: "Brasilia",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    71: "Salvador",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

userInputDDD = int(input())
if userInputDDD not in dddToCityMapping:
    print("DDD nao cadastrado")
else:
    print(dddToCityMapping[userInputDDD])
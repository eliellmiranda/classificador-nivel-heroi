# código para classificar o nível do herói
for i in range(3):  #faz para 3 heróis (3 execuções em 1)
    nome = input("Digite o nome do herói: ")
    xp = int(input(f"Digite a quantidade de XP do herói {nome}: "))

    # Estrutura de decisão para definir o nível
    if xp < 1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Platina"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    # Saída final
    print(f"O Herói de nome **{nome}** está no nível de **{nivel}**\n")

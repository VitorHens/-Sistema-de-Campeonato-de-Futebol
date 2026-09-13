times = list()
qtd = 0

while True:
    valido = False
    r = input("Deseja começar o programa? S = Sim N - Não ")
    if r == 'N':
        break
    elif r != 'S':
        print("\n")
    else:
      while valido == False:
        nometime = input("\nDigite o nome do time: ")
        nometime = nometime.strip()
        if nometime != '':
            valido = True
            dic = {"nome" : nometime,
                    "pontos_partidas" : 0,
                    "total" : 0 ,
                    "vitorias" : 0 ,
                    "aproveitamento" : 0.0
                    }
            qtd += 1
            ponto = tuple()
            pontoT = list()
            soma = 0
            qtdvit = 0
            for cont in range(0,5):
                while True:
                    pon = input(f"\nDigite os pontos da {cont + 1}° partida: ")
                    if pon.isdigit() == True:
                        intpon = int(pon)
                        if intpon == 3:
                            pontoT.append(intpon)
                            soma += intpon
                            qtdvit += 1
                            break
                        if intpon == 1 or intpon == 0:
                            pontoT.append(intpon)
                            soma += intpon

                            break

            ponto = tuple(pontoT)
            dic["pontos_partidas"] =  ponto
            dic["total"] = soma
            dic["vitorias"] = qtdvit
            dic["aproveitamento"] = (soma / 15) * 100
            times.append(dic)
    maisvit = 0
    Campeao = 0
    ViceCampeao = 0
    menor = 0
    contvit = 0
    contCampeao = 0
    contViceCampeao = 0
    contMenor = 0
    for cont in range (0, qtd ):
        if cont == 0:
            maisvit = times[cont]['vitorias']
            contvit = 0
        elif times[cont]['vitorias'] > maisvit:
            maisvit = times[cont]['vitorias']
            contvit = cont
        if cont == 0:
            Campeao = times[cont]['total']
            contCampeao = cont
            menor = times[cont]['total']
            contMenor = cont
        elif times[cont]['total'] > Campeao:
            ViceCampeao = Campeao
            contViceCampeao = contCampeao
            Campeao = times[cont]['total']
            contCampeao = cont
        elif times[cont]['total'] > ViceCampeao:
            ViceCampeao = times[cont]['total']
            contViceCampeao = cont
        if times[cont]['total'] < menor:
            menor = times[cont]['total']
            contMenor = cont
if qtd > 1:
    print("=" * 120)
    print("Tabela de Resultados")
    print("=" * 120)
    for time in times:
        print('Time:', time['nome'])
        print('Pontos das partidas:', time['pontos_partidas'])
        print('Total de pontos:', time['total'])
        print('Vitórias:', time['vitorias'])
        print('Aproveitamento: {:.2f}%'.format(time['aproveitamento']))
        print("")
    print("=" * 120)
    print ("Campeão:", times[contCampeao]['nome'] ,"|| Vice Campeão:", times[contViceCampeao]['nome'])
    print("=" * 120)
    print ("Time com Mais Vitórias:", times[contvit]['nome'])
    print("=" * 120)
    print ("Time com Menor Pontuação:", times[contMenor]['nome'])
    print("=" * 120)

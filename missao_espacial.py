print("Parabéns!! Você foi convidado pela Agência Espacial Brasileira para participar de uma simulação de voo espacial") 

nome = input('Digite seu nome Completo ')  # primeira variável - nome completo 

distancia = int(input('Digite a distância da viagem, em quilômetros ')) # variável da distância

vm = int(input('Digite a velocidade média da nave, em km/h ')) # variável da Velocidade média

tempo_horas = distancia / vm  # cálculo do tempo, em horas

tempo_dias = tempo_horas / 24  # cálculo do tempo, em dias

#     \n para quebrar linha e f para formatar a variável com casa decimal
print("\n\nAstronauta ", nome, ", bem-vindo à simulação!", 
      "\n A viagem terá uma distância de ", distancia, " km(até a Lua).",
       "\n Com velocidade média de ", vm, " km/h, o tempo estimado é:",
        f"\n {tempo_horas:,.2f} horas ( {tempo_dias:,.2f} dias ).",  
        "\n Boa Sorte na missão!")

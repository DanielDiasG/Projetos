#-----------------------------consumo de energia ------------------------------------------------------------------------------------------


print("\n" * 3,("-"*98 ), # linha de separação para melhor visualização
      "\n\t\t\t    CONSUMO DE ENERGIA" ) # queba de linha para melhor visualização

print("-" * 100 ) # linha de separação para melhor visualização

# ---------------------------------------- Saudações --------------------------------------------------------------------------------------

print("\n\t\t Bem-vindo ao programa de cálculo de consumo de energia!" ) # queba de linha para melhor visualização

# --------------------------- Entrada de dados ---------------------------------------------------------------------------------------

aparelho = input("\n\t\t\t - Digite o nome do aparelho: ")

potencia = float(input("\n\t\t\t - Digite a potência do aparelho em watts (W): "))

horas_uso = float(input("\n\t\t\t - Digite o número de horas que o aparelho\n\t\t\t é usado em média por dia: "))


print("\n\n\n","-" * 98 ) # linha de separação para melhor visualização


# ------------------------ Cálculo do consumo diário em kWh ----------------------------------------------------------------------------

consumo_mensal_kwh = (potencia * horas_uso * 30) / 1000 # 30 dias no mês e conversão de watts para kilowatts

custo_estimado = consumo_mensal_kwh * 0.75 # custo estimado considerando o valor médio (R$ 0,75 por kWh)

# ------------------------- Saída de dados --------------------------------------------------------------------------------------

print("\t\t\tRESULTADOS DO CÁLCULO DE CONSUMO DE ENERGIA" ) # queba de linha para melhor visualização
print("-" * 100 ) # linha de separação para melhor visualização

print("\n\n\t\t\t  Aparelho: ",aparelho)
print(f"\n\t\t\t  Consumo mensal estimado: {consumo_mensal_kwh:.2f} kWh")
print(f"\n\t\t\t  Custo mensal estimado: R$ {custo_estimado:,.2f} \n\n\n")

print("-" * 100 ) # linha de separação para melhor visualização

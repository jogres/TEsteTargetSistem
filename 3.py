#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Carregar dados de faturamento do arquivo JSON
with open('faturamento.json') as file:
    data = json.load(file)
    faturamento_diario = data['faturamento']

# Ignorar dias sem faturamento
dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]

# Calcular menor e maior valor
menor_valor = min(dias_com_faturamento)
maior_valor = max(dias_com_faturamento)

# Calcular média mensal
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contar dias acima da média
dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")

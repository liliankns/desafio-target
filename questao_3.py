import json

def calcular_faturamento(json_file):
   with open(json_file, 'r') as file:
       dados = json.load(file)

   faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] != 0]

   menor_faturamento = min(faturamento_diario)
   maior_faturamento = max(faturamento_diario)
   media_mensal = sum(faturamento_diario) / len(faturamento_diario)
   dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

   return menor_faturamento, maior_faturamento, dias_acima_media

menor, maior, acima_media = calcular_faturamento('dados.json')

print(f"O menor valor de faturamento ocorrido em um dia do mês foi {menor}.")
print(f"O maior valor de faturamento ocorrido em um dia do mês foi {maior}.")
print(f"O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foram {acima_media} dias.")
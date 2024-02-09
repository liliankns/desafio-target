faturamento_estadual = {
   'SP': 67836.43,
   'RJ': 36678.66,
   'MG': 29229.88,
   'ES': 27165.48,
   'Outros': 19849.53
}

valor_total = sum(faturamento_estadual.values())

percentuais_por_estado = {estado: (faturamento / valor_total) * 100 for estado, faturamento in faturamento_estadual.items()}

# Imprimindo os percentuais de representação de cada estado
for estado, percentual in percentuais_por_estado.items():
   print(f"{estado}: {percentual:.2f}%")

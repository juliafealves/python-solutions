# coding: utf-8
# Resumo Passagem
# (C) 2017, Júlia Alves / UFCG Programação 1

# Entrada dos dados.
identificador = raw_input()
horario = raw_input()
assento = raw_input()
portao = raw_input()
preco_sem_imposto = float(raw_input())
preco_total = float(raw_input())

# Calculando o percentual de impostos
porcentagem_imposto = (preco_total - preco_sem_imposto) * 100 / preco_total

# Imprimindo os dados do cartão de embarque
print '### Cartão de Embarque ###'
print 'Identificador do voo: %s. Horário: %s. Assento: %s. Portão: %s.' % (identificador, horario, assento, portao)
print 'Total de Imposto: %.1f%%.' % (porcentagem_imposto)
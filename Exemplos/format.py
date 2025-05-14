nome = "Monica"
mensagem = "Olá, {}!".format(nome)
print(mensagem)  
# Olá, Monica!

nome = "Monica"
idade = 25
mensagem = "{} tem {} anos.".format(nome, idade)
print(mensagem)  #
# Monica tem 25 anos.

sapos = 15
total = 50
percentual = sapos * 100 / total
mensagem = "Percentual de sapos: {:.2f} %".format(percentual)
print(mensagem)  
# Saída: Percentual de sapos: 30.00 %
rua           = "Avenida Senador Salgado Filho"
numero        = 1559
bairro        = "Tirol"
cidade_estado = "Natal-RN"
pais          = "Brasil"
cep           = "59015-000"

email    = "ccs.cnat@ifrn.edu.br"
telefone = "4005-2600"

endereco_str = rua + ", " + str(numero) + ", \n" + bairro + ", " + cidade_estado + ", " + pais + "\n" + cep
contato_str  = "E-mail: "+ email + "\n" + "Telefone: " + telefone

print(endereco_str , "\n" , contato_str , sep = "")

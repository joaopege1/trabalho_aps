mensagem = input("Digite a mensagem: ")
chave = input("Digite a chave: ")


def xor_criptografar(mensagem, chave):
    mensagem_criptografada = []
    
    for i in range(len(mensagem)):
        caractere_mensagem = mensagem[i]
        caractere_chave = chave[i % len(chave)]  # A chave é repetida conforme necessário
        resultado_xor = ord(caractere_mensagem) ^ ord(caractere_chave)
        mensagem_criptografada.append(resultado_xor)
    
    return mensagem_criptografada

mensagem_criptografada = xor_criptografar(mensagem, chave)
print("Mensagem criptografada:", mensagem_criptografada)

for numero in mensagem_criptografada:
    print(numero, end=' ')

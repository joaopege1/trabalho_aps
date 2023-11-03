mensagem_criptografada = input("Digite a mensagem criptografada (números separados por espaço): ")
chave = input("Digite a chave: ")

def xor_descriptografar(mensagem_criptografada, chave):
    mensagem_descriptografada = []
    
    for i in range(len(mensagem_criptografada)):
        caractere_criptografado = mensagem_criptografada[i]
        caractere_chave = chave[i % len(chave)]  # A chave é repetida conforme necessário
        resultado_xor = caractere_criptografado ^ ord(caractere_chave)
        mensagem_descriptografada.append(resultado_xor)
    
    return mensagem_descriptografada

def ascii_para_texto(valores_ascii):
    mensagem_texto = ''.join(chr(val) for val in valores_ascii)
    return mensagem_texto

# Converte a entrada em uma lista de números inteiros
mensagem_criptografada = [int(num) for num in mensagem_criptografada.split()]

mensagem_descriptografada = xor_descriptografar(mensagem_criptografada, chave)
mensagem_original = ascii_para_texto(mensagem_descriptografada)

print("Mensagem descriptografada:", mensagem_original)

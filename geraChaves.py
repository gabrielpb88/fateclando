#python3 version
import rsa
print('Gerador de chaves assimetricas')
print('Digite as seguintes informacoes')
size = input('Tamanho da chave: ')

##gero as chaves com o tamanho informado
(pub, pri) = rsa.newkeys(int(size))

##crio o arquivo pub
arquivo_publico = 'public'
#codifico o exponente e modulo da chave para o formate PEM
arq = open(arquivo_publico,'wb')
arq.write(pub.save_pkcs1(format='PEM'))
arq.close()

## Define o nome do arquivo privado
arquivo_privado = 'private'

# Abre o arquivo em escrita binaria
arq = open(arquivo_privado,'wb')

# Codifico o exponente e modulo da chave para o formate PEM
arq.write(pri.save_pkcs1(format='PEM'))
arq.close()

# Printa localização dos arquivos
print('Chaves geradas com sucesso')
print(arquivo_publico)
print(arquivo_privado)
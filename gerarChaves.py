import rsa
print('Gerador de chaves assimetricas')

(pub, pri) = rsa.newkeys(256)

with open('./public.pem', 'wb') as f:
    f.write(pub.save_pkcs1(format='PEM'))

with open('./private.pem', 'wb') as f:
    f.write(pri.save_pkcs1(format='PEM'))

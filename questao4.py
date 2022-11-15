#Implemente um python uma função que recebe como entrada uma lista de valores e retorne uma string que representa a compressão com o método RLE. Considere que ‘FF’ será o código de compactação.

#Considere que a entrada será com valores separados por vírgula.

#Por exemplo:

#Entrada	Resultado
#22,23,23,23,23,23,25,24,21,21,21,21,21,21,21,27
#22,23,23,23,23,23,25,24,21,21,21,21,21,21,21,27
#22FF2352524FF21727

#data=[22,23,23,23,23,23,25,24,21,21,21,21,21,21,21,27]
data=input().split(',')
cod = 'FF'
freq={}
for d in data:
    if d in freq.keys():
        freq[d]=freq[d]+1
    else:
        freq[d]=1
scomp=""        
for d in freq.keys():
    
    if freq[d]>1:
        p = cod+d+str(freq[d])
    else:
        p=d
    scomp=scomp+p
print(scomp)
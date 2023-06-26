from num2words import num2words

def letra_gerador(n):
    n_patinhos = n
    letra = ''
    for pato in range(n_patinhos,2,-1):
        pato_extenso = num2words(pato, lang='pt_BR').capitalize()
        pato_txt = f"só {num2words(pato-1, lang='pt_BR')} patinhos voltaram"
        letra += f"<p>{pato_extenso} patinhos foram passear<br>Além das montanhas para brincar<br>A mamãe gritou: 'Quá quá quá quá'<br>Mas {pato_txt} de lá<p>"
    
    letra += "<p>Dois patinhos foram passear <br>Além das montanhas para brincar<br>A mamãe gritou: 'Quá quá quá quá'<br>Mas só um patinho voltou de lá <p><p>Um patinho foi passear <br>Além das montanhas para brincar<br>A mamãe gritou: 'Quá quá quá quá'<br>Mas nenhum patinho voltou de lá <p><p>Poxa, a mamãe patinha ficou tão triste naquele dia<br>Aonde será que estavam os seus filhotinhos?<br>Mas essa história vai ter um final feliz <br>Sabe por quê?<p>" 
    
    if(n_patinhos == 1):
        pato_txt = "nenhum patinho voltou"
        letra += f"<p>A mamãe patinha foi procurar<br>Além das montanhas, na beira do mar<br>A mamãe gritou: 'Quá quá quá quá'<br>E o patinho voltou de lá<p>" 
    else:
         letra += f"<p>A mamãe patinha foi procurar<br>Além das montanhas, na beira do mar<br>A mamãe gritou: 'Quá quá quá quá'<br>E os {num2words(n_patinhos, lang='pt_BR')} patinhos voltaram de lá<p>"    
    
    letra_terminal = letra.replace('<br>','\n')
    letra_terminal = letra_terminal.replace('<p>','\n')
    print(letra_terminal)
    return letra
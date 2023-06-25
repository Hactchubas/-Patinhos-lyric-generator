from num2words import num2words

def letra_gerador(n):
    n_patinhos = n
    letra = ''
    for pato in range(n_patinhos,0,-1):
        pato_extenso = num2words(pato, lang='pt_BR').capitalize()
        if(pato == 1):
            pato_txt = "nenhum patinho voltou"
            letra += f"<p>{pato_extenso} patinho foi passear <br>Além das montanhas para brincar<br>A mamãe gritou: 'Quá quá quá quá'<br>Mas {pato_txt} de lá <p>"
            continue
        elif (pato == 2):
            pato_txt = "só um patinho voltou"
        else:
            pato_txt = f"só {num2words(pato-1, lang='pt_BR')} patinhos voltaram"

        letra += f"<p>{pato_extenso} patinhos foram passear<br>Além das montanhas para brincar<br>A mamãe gritou: 'Quá quá quá quá'<br>Mas {pato_txt} de lá<p>"

    letra += "<p>Poxa, a mamãe patinha ficou tão triste naquele dia<br>Aonde será que estavam os seus filhotinhos?<br>Mas essa história vai ter um final feliz <br>Sabe por quê?<p>" 
    if(n_patinhos == 1):
        pato_txt = "nenhum patinho voltou"
        letra += f"<p>A mamãe patinha foi procurar<br>Além das montanhas, na beira do mar<br>A mamãe gritou: 'Quá quá quá quá'<br>E o seu patinho voltou de lá<p>" 
    else:
         letra += f"<p>A mamãe patinha foi procurar<br>Além das montanhas, na beira do mar<br>A mamãe gritou: 'Quá quá quá quá'<br>E os {num2words(n_patinhos, lang='pt_BR')} patinhos voltaram de lá<p>"    
    
    letra_terminal = letra.replace('<br>','\n')
    letra_terminal = letra_terminal.replace('<p>','\n')
    print(letra_terminal)
    return letra
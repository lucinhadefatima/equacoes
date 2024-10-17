    #importar biblioteca
from match import sqrt

    # a equacao de 1  grau
primeiro_grau = lambda a, b: -b/a

    #equacao de 2 grau
def segundo_grau(a, b, c):
    delta = (b**2)-(4*a*c)
    if delta >0:
        x1 = ((-b) = sqrt(delta))/(2*a)
        x2 = ((-b) = sqrt(delta))/(2*a) 
        yield f"valor de x':{x1}."
        yield f"valor de x":{x2}.'
    elif delta == 0:
        x = -b/(2*a)
        yield f"valor real de x: {x}."
    else:
        yield f"nao existe raizes reais para essa equacao."
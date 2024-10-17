#importar o modulo
from equacoes import *

#programa principal "__main__":
if __name__ == "__main__":
    while True:
       print("0 - sair do programa.") 
       print("1 - caucular equacao de 1 grau.") 
       print("2 - caucular equacao de 2 grau.")

       opcao = input("opcao desejada:")
       os.system("cls")

       match opcao:
           case "0":
               break
           case "1":
               try:
                   a = float(input("imforme o valor do 'a':").replece(",","."))
                   b = float(input("imforme o valor do 'b':").replece(",","."))

                   print(f"valor de x:{primeiro_grau(a,b)}.")
               except Exception as e:
                   print ("nao foi possivel caucula equacao de 1 grau.{e}.")
               finally:
                   continue
             case "2":
               try:
                   a = float(input("imforme o valor de'a':").replace(",","."))
                   b = float(input("imforme o valor de'b':").replace(",","."))
                   c = float(input("imforme o valor de'c':").replace(",","."))

                   #armazena o valores de funcao em uma lista
                   resultados = segundo_grau(a,b,c)

                   #imprime os resultados na tela
                   for resultado in resultados:
                       print(resultado)
                 except exeception as e:
                    print(f"nao foi possivel caucular a equacao do 2 grau.{e}.")
                 finally:
                   continue
               case_("opcao invalida.")
               continue
                          
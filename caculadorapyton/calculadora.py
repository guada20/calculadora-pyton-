import math
num_1=int(input("ingrese primer numero"))
num_2=int(input("ingrese segundo numero"))

elegir=0
while elegir != 8:
  print("""ingrese el numero de la operacion que desea realizar:
    \t 1)suma
    \t 2)resta
    \t 3)multiplicacion
    \t.4)Division
    \t 5)potenciacion
    \t 6)raiz cuadrada"
    \t 7)cambiar numeros
    \t 8) SALIR""")
  elegir=int(input())
  if elegir== 1:
    ResultadoSuma = num_1 +num_2
    print(ResultadoSuma)
  elif elegir==2:
    ResultadoResta=num_1-num_2
    print(ResultadoResta)
  elif elegir==3:
    ResultadoMultiplicacion=num_1 * num_2
    print(ResultadoMultiplicacion)
  elif elegir==4:
    ResultadoDivision=num_1 //num_2
    print(ResultadoDivision)
  elif elegir==5:
    Base=int(input("INGRESE EL NUMERO DE LA BASE: "))
    Exponente=int(input("INGRESA EXPONENTE: "))
    ResultadoPotencia  =pow(Base,Exponente)
    print(ResultadoPotencia)
  elif elegir==6:
    ResultadoRaizcuadrada1 = math.sqrt(num_1)
    ResultadoRaizcuadrada2 = math.sqrt(num_2)
    print(ResultadoRaizcuadrada1)
    print(ResultadoRaizcuadrada2)
  elif elegir==7:
    num_1=int(input("ingrese primer numero"))
    num_2=int(input("ingrese segundo numero"))
  else:
    print("adios")


 

    

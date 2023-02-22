# import kivy
#
# import kivy.app

# import kivy.uix.labelfrom kivy.app import App
'''from kivy.uix.button import Button

class FristApp(App):
    def build(self):
        btn1 = Button(text="Hola mundo", font_size=30, size_hint=(0.3, 0.2), pos=(250, 250), background_color=("cyan") )
        return btn1
if __name__ =="__main__":
    FristApp().run()'''

#Declarando definicion de dunciones para la calculadora
def sumar(a,b):
    return a +b
def restar(a,b):
    return a - b
def mutiplicar(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        print("Error: no se puede dividir por cero.")
        return
    return a / b
    # return a / b
    # while True:
    #     try:
    #         b == 0
    #         break
    #     except:
    #         print("La divicion por cero es invalida")
    #         return a / b
def leerEntero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            break
        except:
            print(">>>Ingrese un entero")
    return num

def menu ():
    print("0- Salir")
    print("1- Suma ")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- division")
    return leerEntero(">>Ingrese una opcion:")

def main():
    opcion=menu()
    print("Opcion:",opcion)
    if opcion == 0:
        print("Hasta pronto Gaaaa")
    else:
        if opcion == 1:
            print("El resultado de la suma es:",sumar(leerEntero("Ingrese primer numero: "), leerEntero("Ingrese el segundo numero: ")))
        else:
            if opcion == 2:
                print("El resultado de la restas es:",restar(leerEntero("Ingrese primer numero: "), leerEntero("Ingrese el segundo numero: ")))
            else:
                if opcion == 3:
                    print("El resultado de multiplicacion es:",mutiplicar(leerEntero("Ingrese primer numero: "), leerEntero("Ingrese el segundo numero: ")))
                else:
                    if opcion == 4:
                        print("El resultado de la division es:",dividir(leerEntero("Ingrese primer numero: "), leerEntero("Ingrese el segundo numero: ")))
                    else:
                        print("Opcion invalida <<ingrese un numero entero>>")

main()
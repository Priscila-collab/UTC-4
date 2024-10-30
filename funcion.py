def sumar (n1,n2): #funcion con susparametros para asignar valores a sus variables 
    return n1+n2 
def restar (n1,n2):
    return n1-n2 
def multiplicacion (n1,n2):
    return n1*n2
def divicion (n1,n2):
    return n1/n2
n1=int (input("ingresa el numero 1: ")) # almacenar los valores
n2=int (input("ingresa el numero 2: "))

print ("la suma es :", sumar (n1,n2))
print ("la resta es :", restar (n1,n2))
print ("la multiplicacion es :", multiplicacion (n1,n2))
print ("la division es :", divicion (n1,n2))
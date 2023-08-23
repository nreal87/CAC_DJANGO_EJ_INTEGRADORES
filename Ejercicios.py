# 1. Escribir una función que calcule el máximo común divisor entre dos números.
def mcd(a,b):
    result = 1   
    for i in range(1,min(a,b)+1): #dividiendo entre todos los números anteriores al mínimo de los dos números a y b  
        if (a%i) == 0 and (b%i) == 0: # si al dividir ambos a y b entre i la división es exacta indicará que ese i es un divisor común a ambos 
            result = i #buscamos el máximo común divisor de ambos  
    return result

print("Test ejercicio 1")
x=300  
y=33880  
print("MCD({},{}) = {}".format(x,y,mcd(x,y)))  # MCD(300,33880) = 20
print()  

# **************************************************************************************************
# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def mcm(a,b):
    mult_a=[]  
    mult_b=[]  
    for i in range(1,a*b+1):  
        mult_a.append(i*a)  
        mult_b.append(i*b)  
        if i*a in mult_b:  
            return i*a  
        elif i*b in mult_a:  
            return i*b  
    return a*b  

print("Test ejercicio 2")
x=12  
y=22  
print('El mínimo común múltiplo de {} y {} es {}.'.format(x,y,mcm(x,y)))
print() 

# **************************************************************************************************
# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
input_str = str("Cadena de prueba prueba prueba")
splitted_str = input_str.split()
unique_words = set(splitted_str)
output = dict.fromkeys(unique_words,0)
for unique_word_i in unique_words:
    for word_j in splitted_str:
        if unique_word_i == word_j:
            output[unique_word_i] += 1
print("Test ejercicio 3")
print(output)
print()           

# **************************************************************************************************
# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.
def freq_splitter(input_str):
    splitted_str = str(input_str).split()
    unique_words = set(splitted_str)
    output = dict.fromkeys(unique_words,0)
    for unique_word_i in unique_words:
        for word_j in splitted_str:
            if unique_word_i == word_j:
                output[unique_word_i] += 1
    return output

def most_repeated_word(input_dict):
    max_freq_word = ""
    max_freq = 0
    for word in input_dict:
        if input_dict[word] > max_freq:
            max_freq = input_dict[word]
            max_freq_word = word
    return (word,max_freq)

print("Test ejercicio 4")
print(most_repeated_word(freq_splitter("Cadena de prueba prueba prueba")))
print()

# **************************************************************************************************
# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.
def get_int():
    input_a = None
    while input_a is None:
        try: 
            print('Ingrese un entero: ')
            input_a = int(input())
        except ValueError:
            print('Incorrecto')
            pass

def get_int_rec():
    try: 
        print('Ingrese un entero: ')
        input_a = int(input())
    except ValueError:
        print('Incorrecto')
        get_int_rec()
        pass

print("Test ejercicio 5")
get_int()
get_int_rec()
print()

# **************************************************************************************************
# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
class Persona:
    def __init__(self, nombre="", edad=0, DNI=0):
        self._nombre = nombre
        self._edad = edad
        self._DNI = DNI

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nom):
        if type(nom) == "<class 'str'>":
            self._nombre = nom

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,e):
        if type(e) == "<class 'int'>" and e>=0:
            self._edad = e
    
    @property
    def DNI(self):
        return self._DNI

    @DNI.setter
    def DNI(self,dni):
        if type(dni) == "<class 'int'>" and dni>=0:
            self._DNI = dni
    

    def mostrar(self):
        print(f'Nombre: {self._nombre}\nEdad: {self._edad}\nDNI: {self._DNI}\n')

    def Es_mayor_de_edad(self):
        if self._edad >=18:
            return True
        return False

print("Test ejercicio 6")
Juan = Persona("Juan",30,33032540)
Juan.mostrar()
print(f'Juan es mayor de edad: {Juan.Es_mayor_de_edad()}')
print(f'Nombre: {Juan.nombre}')
print()

# **************************************************************************************************
# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.
class Cuenta:
    def __init__(self,tit,cant=0):
        self._titular = tit
        self._cantidad = cant

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self,tit):
        self._titular = tit
    
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self,cant):
        self._cantidad = cant
    
    def mostrar(self):
        print(f'Titular de la cuenta: {self._titular.nombre}\nCantidad: {self._cantidad}')
    
    def ingresar(self,cant):
        if cant>0:
            self.cantidad += cant
    
    def retirar(self,cant):
        if cant>0:
            self.cantidad -= cant

print("Test ejercicio 7")
Juan = Persona("Juan",30,33032540)
CuentaJuan = Cuenta(Juan,0)
CuentaJuan.mostrar()
CuentaJuan.ingresar(10)
CuentaJuan.mostrar()
CuentaJuan.retirar(10)
CuentaJuan.mostrar()
print()

# **************************************************************************************************
# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.

class CuentaJoven(Cuenta):
    def __init__(self,tit,cant,bon=0):
        Cuenta.__init__(self,tit,cant)
        self._bonificacion = bon
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bon):
        self._bonificacion = bon

    def es_titular_valido(self):
        if self.titular.edad >= 18 and self.titular.edad < 25:
            return True
        return False
    
    def retirar(self,cant):
        if self.es_titular_valido():
            Cuenta.retirar(self,cant)
    
    def mostrar(self):
        print(f'Cuenta Joven\nBonificacion: {self._bonificacion}%')
        Cuenta.mostrar(self)

print("Test ejercicio 8")
Pedro = Persona("Pedro",21,12345678)
CuentaPedro = CuentaJoven(Pedro,0,20)
CuentaPedro.mostrar()
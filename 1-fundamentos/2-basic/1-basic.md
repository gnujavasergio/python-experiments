## Conceptos basicos

## Mi primer programa
- [Ejemplo1](../examples/2-basic/ejemplo1/README.md)
```python
python3
Python 3.4.3 (default, Nov 12 2018, 22:25:49) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> print('hola mundo')
hola mundo
>>> 
>>> quit();
```
## Valores y Tipos de datos
- Integer <int>
- Float <float>
- String <str>
- Boolean <bool>
```python
# Int
print(type(33)) # <class 'int'>
# Float
print(type(5.3)) # <class 'float'>
# String
print(type('Sergio Ochoa')) # <class 'str'>
# bool
print(type(True))  # <class 'bool'>
```
- [Ejemplo5](../examples/2-basic/ejemplo5/README.md)

### Tipo Logico
- Minima expresion racional
- Representada por dos valores `True` y `False`.
- Ejemplo
    - Contexto Linguistico: Estoy vivo esto es verdadero es igual a `True`
    - Contexto Matematico: `1+1 = 3` es falso y es igual a `False`
```
```

## Variables
- Para crear variables en python se utiliza el formato snake case.
- Variable: Espacios en memoria para almacenar un valor
- Las variables tienen que tener nombre significativos
- Una variable no puedo comenzar por numeros
- Una variable no puedo contener espacios y tampoco simbolos especiales
- No deben ser keywords(palabras reservadas)
- [Ejemplo2](../examples/2-basic/ejemplo2/README.md)

## Constantes
- Constante en python no existe
- Para poder declarar una constante un Python se puede declarar la variable todo en mayuscula.
```python
PI = 3.1416
print(PI)
```
- [Ejemplo3](../examples/2-basic/ejemplo3/README.md)

# Operadores
## Operadores Aritmeticos
- En que orden se evaluan las matematicas operaciones complejas
    1. Parentesis
    2. Exponenetes
    3. Multiplicacion/Division
    4. Adición/Sustracción
- Una forma facil de recordar este orden es usando el acronimo PENDAS(ParentesisExponentesMultiplicaciónDivisiónAdiciónSustracción)

- Suma `+`
- Resta `-`
- Multiplicación `*`
- División `/`
- Division de enteros `//`
- Modulo `%` es el restante de una división
- Potencia `**` calcula la potencia de un numero
- [Ejemplo4](../examples/2-basic/ejemplo4/README.md)

## Operadores de comparación
- `==` igual
- `!=` No igual o diferente
- `<` menor que
- `>` mayor que
- `<=` menor o igual que
- `>=` mayor o igual que
- [Ejemplo6](../projects/2-basic/ejemplo6/README.md)

## Operadores de Asignación
- Un operador de asignación asigna un valor a su operando izquierdo en funcion de su valor de su operando derecho.u
- En python se puede realizar asignación multiple

```python
# Asignación
x = y

# Asignacion de Suma
x += y 	# short
x = x + y # full

# Asignacion de resta
x -= y 	# short
x = x - y # full

# Asignación de multiplicación
x *= y # short
x = x * y # full

// Asignación de División
var x /= y; // Short 	
var x = x / y; // full

// Asignación de residuo
var x %= y; // short
var	x = x % y; // full

// Asignación de exponenciación
var x **= y; // short
var	x = x ** y; // full
```
- [Ejemplo7](../examples/2-basic/ejemplo7/README.md)

### Operadores Logicos
- `not expresión` Realiza una negación en la expresión
- `and` AND es Unión
- `or` OR es Separación
- [Ejemplo8](../examples/2-basic/ejemplo8/README.md)

## Entrada de datos por Teclado
- En python 3 se utiliza la función `input()`
```python
name = input("Introduzca su nombre \n")
```
- [Ejemplo9](../examples/2-basic/ejemplo9/README.md)

## Comentarios
- Los comentarios son fragmentos de código que el intérprete de Python ignora.
- Los comentarios se los escribe para que otros desarrolladores puedan entender porciones de codigo o funcionalidades que tienen cierta complejidad porque todos sabemos la memoria es fragil y podemos colocar un comentario 
- Dos formas de comentario
```python
# Comentario en linea
"""
Comentario 
en varias Lineas
"""
```
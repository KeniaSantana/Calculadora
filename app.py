from flask import Flask
app = Flask(__name__)

@app.route('/')  
def Calculadora():
    return '''<h1>Bienvenidos a la calculadora de Python</h1>
<p>1.- Para Sumar escribe en el navegador 127.0.0.1:5000/sumar/num1/num2 </p>
<p>2.- Para Restar escribe en el navegador 127.0.0.1:5000/restar/num1/num2 </p>
<p>3.- Para Multiplicar escribe en el navegador 127.0.0.1:5000/multiplicar/num1/num2 </p>
<p>4.- Para Dividir escribe en el navegador 127.0.0.1:5000/dividir/num1/num2 </p>
<p>5.- Para Numero mayor escribe en el navegador 127.0.0.1:5000/mayor/num1/num2 </p>
<p>6.- Para Numero menor escribe en el navegador 127.0.0.1:5000/menor/num1/num2 </p>    
<h4>Informacion</h4>
<p>Santana Ruiz Kenia Alejandra</p>
<p>5-D</p>
<p>Especialidad:Programacion</p>
<p>Numero de control:23308060610371</p>'''

    
@app.route('/sumar/<float:num1>/<float:num2>')
def sumar(num1, num2):
    resultado = num1 + num2
    return f'El resultado de la suma es: {resultado}'

@app.route('/restar/<float:num1>/<float:num2>')
def restar(num1, num2):
    resultado = num1 - num2
    return f'El resultado de la resta es: {resultado}'

@app.route('/multiplicar/<float:num1>/<float:num2>')
def multiplicar(num1, num2):
    resultado = num1 * num2
    return f'El resultado de la multiplicación es: {resultado}'

@app.route('/dividir/<float:num1>/<float:num2>')
def dividir(num1, num2):
    if num2 == 0:
        return 'Error: División por cero no está permitida.'
    resultado = num1 / num2
    return f'El resultado de la división es: {resultado}'

@app.route('/mayor/<int:num1>/<int:num2>')
def mayor(num1, num2):
    if num1 > num2:
        return f'El número mayor es: {num1}'
    elif num2 > num1:
        return f'El número mayor es: {num2}'
    else:
        return 'Ambos números son iguales.'
    
@app.route('/menor/<int:num1>/<int:num2>')
def menor(num1, num2):
    if num1 < num2:
        return f'El número menor es: {num1}'
    elif num2 < num1:
        return f'El número menor es: {num2}'
    else:
        return 'Ambos números son iguales.'
    

if __name__ == '__main__':
    app.run(debug=True)
    
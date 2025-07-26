# English: Flask app acting as the Controller in MVC
# Español: Aplicación Flask que actúa como el Controlador en MVC
from flask import Flask, render_template, request
from bubble_sort_model import bubble_sort

app = Flask(__name__)

# English: Route to handle sorting request
# Español: Ruta para manejar la solicitud de ordenamiento
@app.route('/', methods=['GET', 'POST'])
def sort():
    # English: Initialize variables
    // Español: Inicializar variables
    sorted_list = None
    input_list = None
    error = None

    # English: Handle POST request from form
    // Español: Manejar solicitud POST desde el formulario
    if request.method == 'POST':
        # English: Get input from form
        // Español: Obtener entrada desde el formulario
        input_str = request.form.get('numbers')
        try:
            # English: Convert input string to list of integers
            // Español: Convertir cadena de entrada a lista de enteros
            input_list = [int(x) for x in input_str.split(',')]
            # English: Call bubble sort from Model
            // Español: Llamar a bubble sort desde el Modelo
            sorted_list = bubble_sort(input_list.copy())
            if sorted_list is None:
                error = "English: Invalid input. Español: Entrada inválida."
        except ValueError:
            error = "English: Please enter numbers separated by commas. Español: Por favor, ingrese números separados por comas."

    # English: Render the View with results
    // Español: Renderizar la Vista con los resultados
    return render_template('index.html', sorted_list=sorted_list, input_list=input_list, error=error)

# English: Run the Flask app
// Español: Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
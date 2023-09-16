from flask import Flask, request, jsonify

app = Flask(__name__)

class CalculadoraModel:
    def __init__(self, valorA, valorB, resultadoC):
        self.valorA = valorA
        self.valorB = valorB
        self.resultadoC = resultadoC

class CalculadoraCore:
    @staticmethod
    def suma(valorA, valorB):
        return valorA + valorB

    @staticmethod
    def multiplicacion(valorA, valorB):
        return valorA * valorB

    @staticmethod
    def resta(valorA, valorB):
        return valorA - valorB

    @staticmethod
    def division(valorA, valorB):
        if valorB == 0:
            raise ValueError("No se puede dividir por cero")
        return valorA / valorB

@app.route('/api/cristian/larios/suma', methods=['POST'])
def suma():
    data = request.get_json()
    valorA = data.get('ValorA')
    valorB = data.get('ValorB')
    resultado = CalculadoraCore.suma(valorA, valorB)
    return jsonify({'ResultadoC': resultado})

@app.route('/api/cristian/larios/multiplicacion', methods=['POST'])
def multiplicacion():
    data = request.get_json()
    valorA = data.get('ValorA')
    valorB = data.get('ValorB')
    resultado = CalculadoraCore.multiplicacion(valorA, valorB)
    return jsonify({'ResultadoC': resultado})

@app.route('/api/cristian/larios/resta', methods=['GET'])
def resta():
    valorA = float(request.args.get('ValorA'))
    valorB = float(request.args.get('ValorB'))
    resultado = CalculadoraCore.resta(valorA, valorB)
    return jsonify({'ResultadoC': resultado})

@app.route('/api/cristian/larios/division', methods=['GET'])
def division():
    valorA = float(request.args.get('ValorA'))
    valorB = float(request.args.get('ValorB'))
    try:
        resultado = CalculadoraCore.division(valorA, valorB)
        return jsonify({'ResultadoC': resultado})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

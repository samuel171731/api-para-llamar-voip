from flask import Flask, request, jsonify
import subprocess
import logging
import urllib.parse

app = Flask(__name__)

# Configurar el registro para que muestre los mensajes de depuración
logging.basicConfig(level=logging.DEBUG)

@app.route('/realizar_llamada', methods=['POST'])
def realizar_llamada():
    try:
        # Registrar los detalles de la solicitud
        app.logger.debug('Método HTTP: %s', request.method)
        app.logger.debug('Encabezados: %s', request.headers)
        app.logger.debug('Datos de la solicitud: %s', request.get_data(as_text=True))

        # Obtener y decodificar los datos de la solicitud
        data = request.get_data(as_text=True)
        app.logger.debug('Datos de la solicitud (raw): %s', data)

        # Decodificar los datos
        decoded_data = urllib.parse.parse_qs(data)
        app.logger.debug('Datos de la solicitud (decodificados): %s', decoded_data)

        # Formatear los datos decodificados para una mejor legibilidad
        formatted_data = {key: value[0] if len(value) == 1 else value for key, value in decoded_data.items()}
        app.logger.debug('Datos de la solicitud (formateados): %s', formatted_data)

        # Buscar el campo que contiene el número de teléfono
        numero = None
        for key, value in formatted_data.items():
            if 'numero' in key and 'value' in key:
                numero = value
                break

        if not numero:
            return jsonify({'error': 'Número de teléfono no proporcionado'}), 400

        # Comando para realizar la llamada en Asterisk con el número proporcionado
        comando = f'asterisk -rx "channel originate DAHDI/g0/{numero} extension 15"'

        try:
            # Ejecutar el comando
            subprocess.run(comando, shell=True, check=True)
            return jsonify({'message': 'Llamada realizada exitosamente', 'data': formatted_data}), 200
        except subprocess.CalledProcessError as e:
            app.logger.error('Error al realizar la llamada: %s', e)
            return jsonify({'error': f'Error al realizar la llamada: {e}'}), 500
    except Exception as e:
        app.logger.error('Error en el servidor: %s', e)
        return jsonify({'error': f'Error en el servidor: {e}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

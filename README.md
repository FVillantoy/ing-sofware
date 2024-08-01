#sistema de elecciones online 
# ing-sofware
Implementación RESTful
Los recursos se identifican mediante URLs (por ejemplo, /participantes).
Se utilizan métodos HTTP estándar para las operaciones (GET, POST, PUT, DELETE).

    @participantes_bp.route('/participantes', methods=['GET'])
    def obtener_participantes(self):
    ...

    @participantes_bp.route('/participantes', methods=['POST'])
    def crear_participante(self):
    ...

Implementacion Error/Exception Handling
Verifica que los datos de entrada sean correctos y estén presentes.
Proporciona respuestas claras cuando un recurso no existe.
Captura excepciones no previstas y proporciona un mensaje de error genérico.

    @participantes_bp.route('/participantes', methods=['GET'])
    def obtener_participantes(self):
        try:
            participantes = self.servicio.obtener_todos()
            return jsonify(participantes)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
            
Implementacion Pipeline

Permite encapsular la lógica común en un solo lugar.
Facilita el mantenimiento y la comprensión del código al centralizar la lógica repetitiva.

    def pipeline(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                return jsonify({'error': 'Invalid data: ' + str(e)}), 400
            except KeyError as e:
                return jsonify({'error': 'Missing data: ' + str(e)}), 400
            except Exception as e:
                return jsonify({'error': 'Internal server error: ' + str(e)}), 500
        return wrapper

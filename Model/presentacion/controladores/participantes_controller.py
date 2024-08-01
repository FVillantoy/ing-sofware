from flask import Flask, Blueprint, request, jsonify, abort
from servicios.participantes_servicio import ParticipantesServicio

app = Flask(__name__)

# Crear un blueprint para los participantes
participantes_bp = Blueprint('participantes', __name__)

class ParticipantesServicio:
    def __init__(self):
        self.participantes = []
        self.counter = 1

    def obtener_todos(self):
        return self.participantes

    def crear(self, data):
        participante = {
            'id': self.counter,
            'nombre': data['nombre'],
            'edad': data['edad']
        }
        self.participantes.append(participante)
        self.counter += 1
        return participante

    def actualizar(self, id, data):
        for participante in self.participantes:
            if participante['id'] == id:
                participante['nombre'] = data['nombre']
                participante['edad'] = data['edad']
                return participante
        return None

    def eliminar(self, id):
        for participante in self.participantes:
            if participante['id'] == id:
                self.participantes.remove(participante)
                return True
        return False

class ParticipantesController:
    def __init__(self):
        self.servicio = ParticipantesServicio()

    @participantes_bp.route('/participantes', methods=['GET'])
    def obtener_participantes(self):
        try:
            participantes = self.servicio.obtener_todos()
            return jsonify(participantes)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @participantes_bp.route('/participantes', methods=['POST'])
    def crear_participante(self):
        data = request.json
        if not data or 'nombre' not in data or 'edad' not in data:
            abort(400, 'No se proporcionaron datos o faltan campos requeridos')
        if not isinstance(data['nombre'], str) or not isinstance(data['edad'], int) or data['edad'] < 18:
            abort(400, 'Datos inválidos')
        try:
            nuevo_participante = self.servicio.crear(data)
            return jsonify(nuevo_participante), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @participantes_bp.route('/participantes/<int:id>', methods=['PUT'])
    def actualizar_participante(self, id):
        data = request.json
        if not data or 'nombre' not in data or 'edad' not in data:
            abort(400, 'No se proporcionaron datos o faltan campos requeridos')
        if not isinstance(data['nombre'], str) or not isinstance(data['edad'], int) or data['edad'] < 18:
            abort(400, 'Datos inválidos')
        try:
            participante_actualizado = self.servicio.actualizar(id, data)
            if not participante_actualizado:
                abort(404, 'Participante no encontrado')
            return jsonify(participante_actualizado)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @participantes_bp.route('/participantes/<int:id>', methods=['DELETE'])
    def eliminar_participante(self, id):
        try:
            if self.servicio.eliminar(id):
                return '', 204
            else:
                abort(404, 'Participante no encontrado')
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Crear una instancia del controlador
participantes_controller = ParticipantesController()

# Registrar las rutas
participantes_bp.add_url_rule('/participantes', view_func=participantes_controller.obtener_participantes, methods=['GET'])
participantes_bp.add_url_rule('/participantes', view_func=participantes_controller.crear_participante, methods=['POST'])
participantes_bp.add_url_rule('/participantes/<int:id>', view_func=participantes_controller.actualizar_participante, methods=['PUT'])
participantes_bp.add_url_rule('/participantes/<int:id>', view_func=participantes_controller.eliminar_participante, methods=['DELETE'])

# Registrar el blueprint en la aplicación
app.register_blueprint(participantes_bp)

if __name__ == '__main__':
    app.run(debug=True)
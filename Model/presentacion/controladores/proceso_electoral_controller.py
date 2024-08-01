from flask import Blueprint, request, jsonify, abort
from servicios.proceso_electoral_servicio import ProcesoElectoralServicio

proceso_electoral_bp = Blueprint('proceso_electoral', __name__)

class ProcesoElectoralController:
    def __init__(self):
        self.servicio = ProcesoElectoralServicio()

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

    @proceso_electoral_bp.route('/procesos-electorales', methods=['GET'])
    @pipeline
    def obtener_procesos(self):
        procesos = self.servicio.obtener_todos()
        return jsonify(procesos)

    @proceso_electoral_bp.route('/procesos-electorales', methods=['POST'])
    @pipeline
    def crear_proceso(self):
        data = request.json
        if not data:
            raise ValueError('No se proporcionaron datos')
        nuevo_proceso = self.servicio.crear(data)
        return jsonify(nuevo_proceso), 201

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['PUT'])
    @pipeline
    def actualizar_proceso(self, id):
        data = request.json
        if not data:
            raise ValueError('No se proporcionaron datos')
        proceso_actualizado = self.servicio.actualizar(id, data)
        if not proceso_actualizado:
            abort(404, 'Proceso electoral no encontrado')
        return jsonify(proceso_actualizado)

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['DELETE'])
    @pipeline
    def eliminar_proceso(self, id):
        if not self.servicio.eliminar(id):
            abort(404, 'Proceso electoral no encontrado')
        return '', 204

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>/detalle', methods=['GET'])
    @pipeline
    def obtener_detalle_proceso(self, id):
        detalle = self.servicio.obtener_detalle(id)
        if not detalle:
            abort(404, 'Detalle del proceso electoral no encontrado')
        return jsonify(detalle)

controller = ProcesoElectoralController()
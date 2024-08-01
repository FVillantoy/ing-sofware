from flask import Blueprint, request, jsonify
from servicios.Iproceso_electoral import Iproceso_electoral
from servicios.proceso_electoral_servicio import ProcesoElectoralServicio
# Crear un blueprint para los procesos electorales
proceso_electoral_bp = Blueprint('proceso_electoral', __name__)
class ProcesoElectoralController:
    def __init__(self):
        self.servicio = ProcesoElectoralServicio()
    @proceso_electoral_bp.route('/procesos-electorales', methods=['GET'])
    def obtener_procesos(self):
        """
        Obtener todos los procesos electorales.
        """
        procesos = self.servicio.obtener_todos()
        return jsonify(procesos)
    
    @proceso_electoral_bp.route('/procesos-electorales', methods=['POST'])
    def crear_proceso(self):
        """
        Crear un nuevo proceso electoral.
        """
        data = request.json
        nuevo_proceso = self.servicio.crear(data)
        return jsonify(nuevo_proceso), 201

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['PUT'])
    def actualizar_proceso(self, id):
        """
        Actualizar un proceso electoral existente.
        """
        data = request.json
        proceso_actualizado = self.servicio.actualizar(id, data)
        return jsonify(proceso_actualizado)

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['DELETE'])
    def eliminar_proceso(self, id):
        """
        Eliminar un proceso electoral existente.
        """
        self.servicio.eliminar(id)
        return '', 204
    
    @proceso_electoral_bp.route('/procesos-electorales/<int:id>/detalle', methods=['GET'])
    def obtener_detalle_proceso(self, id):
        detalle = self.servicio.obtener_detalle(id)
        return jsonify(detalle)

servicio = ProcesoElectoralServicio()
controller = ProcesoElectoralController(servicio)
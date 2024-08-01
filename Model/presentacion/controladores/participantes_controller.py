from flask import Blueprint, request, jsonify
from servicios.participantes_servicio import ParticipantesServicio
# Crear un blueprint para los participantes
participantes_bp = Blueprint('participantes', __name__)
class ParticipantesController:
    def __init__(self):
        self.servicio = ParticipantesServicio()
    @participantes_bp.route('/participantes', methods=['GET'])
    def obtener_participantes(self):
        """
        Obtener todos los participantes.
        """
        participantes = self.servicio.obtener_todos()
        return jsonify(participantes)

    @participantes_bp.route('/participantes', methods=['POST'])
    def crear_participante(self):
        """
        Crear un nuevo participante.
        """
        data = request.json
        nuevo_participante = self.servicio.crear(data)
        return jsonify(nuevo_participante), 201

    @participantes_bp.route('/participantes/<int:id>', methods=['PUT'])
    def actualizar_participante(self, id):
        """
        Actualizar un participante existente.
        """
        data = request.json
        participante_actualizado = self.servicio.actualizar(id, data)
        return jsonify(participante_actualizado)

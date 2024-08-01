#!/usr/bin/python
#-*- coding: utf-8 -*-

from dominio.proceso_electoral.Iresultados import Iresultados

class Resultados(Iresultados):
    def __init__(self):
        self.total_votos = None
        self.votos_candidatos = None
        self.porcentaje_participacion = None

    def get_votos_totales(self, ):
        pass

    def get_votos_candidato(self, ):
        pass

    def publicar_resultados(self, ):
        pass

    def calcular_resultados(self, ):
        pass


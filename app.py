import requests
import json
from flask import Flask, request, jsonify
from datetime import datetime
from bs4 import BeautifulSoup

class ApiService:
    @staticmethod
    def getUnitF(dateToGetUnitF):
        if not dateToGetUnitF:
            return jsonify({'Error': 'No se especificó fecha de búsqueda'}), 404

        try:
            if not ApiService.validateDate(dateToGetUnitF):
                return jsonify({'Error': 'Fecha fuera del siguente rango (1-1-2013)'}), 404

            url = f'https://mindicador.cl/api/uf/{dateToGetUnitF}'
            response = requests.get(url)
            seriesValues = json.loads(response.text)
        except :
            return jsonify({'Error': 'Se ha producido un error al intentar obtener el dato de la fecha, verifique si el formato es correcto (1-1-2013)'}), 500
        else:
            return ApiService.buildResponse(seriesValues)
               
    @staticmethod
    def validateDate(date):
        ufValue = datetime.strptime(date, '%d-%m-%Y')
        return ufValue >= datetime(2013, 1, 1)

    @staticmethod
    def buildResponse(seriesValues):
        if not seriesValues['serie']:
            return jsonify({'Unidad de Fomento': 'Dato aun no generado'}), 200

        ufValue = seriesValues['serie'][0]['valor']
        return jsonify({'Unidad de Fomento': ufValue}), 200

app = Flask(__name__)

@app.route('/unitDevelop', methods=['GET'])
def getDevelopmentUnit():
    dateToGetUnitF = request.args.get('date') 
    return ApiService.getUnitF(dateToGetUnitF)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
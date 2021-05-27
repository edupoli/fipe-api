#!/usr/bin/env python3
import flask
from flask import Flask, request, Response, jsonify, render_template
import json, requests
from flask_cors import CORS

app = flask.Flask(__name__)
headers_fipe = {
    'Host': 'veiculos.fipe.org.br', 
    'Referer': 'http://veiculos.fipe.org.br', 
    'Content-Type': 'application/json', 
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'
}
PORT = 7091
API_KEY = '$2y$10$8IAZn7HKq7QJWbh37N3GOOeRVv.sM9tcTLBRYwRuf2g98olRyqieW'

app.config['DEBUG'] = True

CORS(app, resources=r'/api/*')
@app.route('/', methods=['POST', 'GET'])
def index():
    chave = request.headers.get('chave')
    if(chave != API_KEY):
        return json.dumps({'mensagem': 'Chave incorreta'})

    return jsonify({"mensagem": "Acesso POST em /api"})

@app.route('/api/ConsultarTabelaDeReferencia', methods=['POST'])
def ConsultarTabelaDeReferencia():
    
    chave = request.headers.get('chave')
    if(chave != API_KEY):
        return json.dumps({'mensagem': 'Chave incorreta'})

    url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia"
    response = requests.post(url,headers=headers_fipe)
    response.headers["Content-Type"] = "application/json"

    return Response(response)

@app.route('/api/ConsultarMarcas', methods=['POST'])
def ConsultarMarcas():

    chave = request.headers.get('chave')
    if(chave != API_KEY):
        return json.dumps({'mensagem': 'Chave incorreta'})
            
    infos = request.get_json()
    codigoTabelaReferencia = infos.get('codigoTabelaReferencia')
    codigoTipoVeiculo = infos.get('codigoTipoVeiculo')

    url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas"
    objeto = json.dumps({
        'codigoTabelaReferencia': codigoTabelaReferencia,
        'codigoTipoVeiculo': codigoTipoVeiculo
    })

    response = requests.post(url, headers=headers_fipe, data = objeto)
    response.headers["Content-Type"] = "application/json"

    return Response(response)

@app.route('/api/ConsultarModelos', methods=['POST'])
def ConsultarModelos():

    chave = request.headers.get('chave')
    if(chave != API_KEY):
        return json.dumps({'mensagem': 'Chave incorreta'})
            
    infos = request.get_json()
    codigoTabelaReferencia = infos.get('codigoTabelaReferencia')
    codigoTipoVeiculo = infos.get('codigoTipoVeiculo')
    codigoMarca = infos.get('codigoMarca')

    url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos"
    objeto = json.dumps({
        'codigoTabelaReferencia': codigoTabelaReferencia,
        'codigoTipoVeiculo': codigoTipoVeiculo,
        'codigoMarca': codigoMarca
    })

    response = requests.post(url, headers=headers_fipe, data = objeto)
    response.headers["Content-Type"] = "application/json"

    return Response(response)

@app.route('/api/ConsultarAnoModelo', methods=['POST'])
def ConsultarAnoModelo():

    chave = request.headers.get('chave')
    if(chave != API_KEY):
        return json.dumps({'mensagem': 'Chave incorreta'})

    infos = request.get_json()
    codigoTabelaReferencia = infos.get('codigoTabelaReferencia')
    codigoTipoVeiculo = infos.get('codigoTipoVeiculo')
    codigoMarca = infos.get('codigoMarca')
    codigoModelo = infos.get('codigoModelo')

    url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarAnoModelo"
    objeto = json.dumps({
        'codigoTabelaReferencia': codigoTabelaReferencia,
        'codigoTipoVeiculo': codigoTipoVeiculo,
        'codigoMarca': codigoMarca,
        'codigoModelo': codigoModelo,
    })

    response = requests.post(url, headers=headers_fipe, data = objeto)
    response.headers["Content-Type"] = "application/json"

    return Response(response)

@app.route('/api/ConsultarModelosAtravesDoAno', methods=['POST'])
def ConsultarModelosAtravesDoAno():

    chave = request.headers.get('chave')
    if(chave != API_KEY):
        return json.dumps({'mensagem': 'Chave incorreta'})
        
    infos = request.get_json()
    codigoTabelaReferencia = infos.get('codigoTabelaReferencia')
    codigoTipoVeiculo = infos.get('codigoTipoVeiculo')
    codigoMarca = infos.get('codigoMarca')
    codigoModelo = infos.get('codigoModelo')
    ano = infos.get('ano')
    codigoTipoCombustivel = infos.get('codigoTipoCombustivel')
    anoModelo = infos.get('anoModelo')

    url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelosAtravesDoAno"
    objeto = json.dumps({
        'codigoTabelaReferencia': codigoTabelaReferencia,
        'codigoTipoVeiculo': codigoTipoVeiculo,
        'codigoMarca': codigoMarca,
        'codigoModelo': codigoModelo,
        'ano': ano,
        'codigoTipoCombustivel': codigoTipoCombustivel,
        'anoModelo': anoModelo,
    })

    response = requests.post(url, headers=headers_fipe, data = objeto)
    response.headers["Content-Type"] = "application/json"

    return Response(response)

@app.route('/api/ConsultarValorComTodosParametros', methods=['POST'])
def ConsultarValorComTodosParametros():

    chave = request.headers.get('chave')
    if(chave != API_KEY):
        return json.dumps({'mensagem': 'Chave incorreta'})

    infos = request.get_json()
    codigoTabelaReferencia = infos.get('codigoTabelaReferencia')
    codigoTipoVeiculo = infos.get('codigoTipoVeiculo')
    codigoMarca = infos.get('codigoMarca')
    ano = infos.get('ano')
    codigoTipoCombustivel = infos.get('codigoTipoCombustivel')
    anoModelo = infos.get('anoModelo')
    codigoModelo = infos.get('codigoModelo')
    tipoConsulta = "avancada"

    url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros"
    objeto = json.dumps({
        'codigoTabelaReferencia': codigoTabelaReferencia,
        'codigoTipoVeiculo': codigoTipoVeiculo,
        'codigoMarca': codigoMarca,
        'ano': ano,
        'codigoTipoCombustivel': codigoTipoCombustivel,
        'anoModelo': anoModelo,
        'codigoModelo': codigoModelo,
	    'tipoConsulta': tipoConsulta
    })

    post_response = requests.post(url, headers=headers_fipe, data = objeto)
    data = post_response.json()
    response = json.dumps({
        'Valor': data['Valor'], 
        'Marca': data['Marca'], 
        'Modelo': data['Modelo'], 
        'AnoModelo': data['AnoModelo'], 
        'Combustivel': data['AnoModelo'], 
        'CodigoFipe': data['CodigoFipe'], 
        'MesReferencia': data['MesReferencia'],
        'TipoVeiculo': data['TipoVeiculo'],
        'SiglaCombustivel': data['SiglaCombustivel']
    })

    return Response(response)

app.run(host="0.0.0.0", port=PORT)

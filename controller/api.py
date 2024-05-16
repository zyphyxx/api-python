import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'API está ON'


@app.route('/vendas')
def vendas():
    df = pd.read_excel('D:/ApiTestes/vendas.xlsx')
    #df['DATA'] = pd.to_datetime(df['DATA']).dt.date
    
    resultado = {}
    for index, row in df.iterrows():
        resultado[index] = dict(row)

    return jsonify(resultado)    


@app.route('/total')
def total():
    df = pd.read_excel('D:/ApiTestes/vendas.xlsx')
    total_vendas = df['VALOR_TOTAL'].sum()    
    resultado = {'Total de Vendas' : total_vendas.astype(str)}    
    return jsonify(resultado)    


app.run(debug = False)

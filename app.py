
import streamlit as st
from flask import Flask, jsonify
from utils import  consulta_dato,columns 
import numpy as np
import pandas as pd
import joblib
from waitress import serve

#model = joblib.load('model_rf.joblib')
st.title('¿Es probable que se cumpla?:')
# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
IMPORTE_PROPUESTA  = st.number_input("Importe Propuesta", 0.0) 
TIPO_PROPUESTA  = st.selectbox("Tipo propuesta", ['PROMESA','CAL_PAGO'])
PROP_VINCULADA   = st.selectbox("Propuesta vinculada", ['QUITA','NO'])
PORCENTAJE_QUITA  = st.slider("Porcentaje de Quita", 0, 70)
DEUDA_INICIAL  = st.number_input("Deuda Inicial", 0.0)
DIAS_IMPAGO  = st.number_input("Dias de impago", 0,7500)
PRODUCTO_AGRUPADO  = st.selectbox("Tipo producto", ['consumo','empresas','hipotecas','resto'])
REL_PER_CUE  = st.selectbox("Tipo relacion", ['TIT','AVA','OTROS'])
MARCA_IND_SME  = st.selectbox("Tipo de cliente", ['INDIVIDUALS','SME','SECURED'])
JUDICIALIZADO = st.selectbox("Judicializado", ['SI','NO'])

'''
app = Flask(__name__)

@app.route('/api/consulta', methods=['POST'])
def consulta():
    try:
        input_data = request.json
        required_columns = [
            'IMPORTE_PROPUESTA', 'TIPO_PROPUESTA', 'PROP_VINCULADA',
            'PORCENTAJE_QUITA', 'DEUDA_INICIAL', 'DIAS_IMPAGO',
            'PRODUCTO_AGRUPADO', 'REL_PER_CUE', 'MARCA_IND_SME', 'JUDICIALIZADO'
        ]
        
        # Verificar que todas las columnas requeridas estén presentes en el input
        if not all(col in input_data for col in required_columns):
            return jsonify({'error': 'Datos de entrada incompletos'}), 400
        
        # Convertir los datos de entrada a un DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Obtener los datos de la consulta
        consulta_df = consulta_dato()
        if consulta_df is None:
            return jsonify({'error': 'Error ejecutando la consulta'}), 500
        
        # Cruzar los datos de entrada con los resultados de la consulta
        merged_df = input_df.merge(consulta_df, how='left', left_on='PRODUCTO_AGRUPADO', right_on='tipo_morosidad')
        
        # Eliminar la columna 'tipo_morosidad'
        if 'tipo_morosidad' in merged_df.columns:
            merged_df = merged_df.drop(columns=['tipo_morosidad'])
        
        # Convertir 'indice_morosidad' a mayúsculas si existe
        if 'indice_morosidad' in merged_df.columns:
            merged_df = merged_df.rename(columns={'indice_morosidad': 'INDICE_MOROSIDAD'})
        
        return jsonify({'resultados': merged_df.to_dict(orient='records')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)

'''
def predict(): 
    row = np.array([IMPORTE_PROPUESTA,TIPO_PROPUESTA,PROP_VINCULADA,PORCENTAJE_QUITA,DEUDA_INICIAL,DIAS_IMPAGO,PRODUCTO_AGRUPADO,REL_PER_CUE,MARCA_IND_SME,JUDICIALIZADO,INDICE_MOROSIDAD]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model_rf.predict(X)
    if prediction[0] == 1: 
        st.success('Es probable que cumpla :thumbsup:')
    else: 
        st.error('Es improbable que cumpla :thumbsdown:') 
      

trigger = st.button('Predicción', on_click=predict)
  '''

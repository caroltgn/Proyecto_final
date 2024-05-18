
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

#from sklearn.base import BaseEstimator, TransformerMixin
#from sklearn.impute import SimpleImputer 
#import re


def get_database_session():
    # Configura tu conexión aquí
    # Datos de conexión para Google Cloud SQL
    project_id = "sonic-airfoil-421707"
    region = "europe-southwest1"
    instance_name = "kcimpagados"


    db_user = "carol"
    db_password = "carol"
    db_name = "kcdebtanalytics"
    db_host = f'/cloudsql/{project_id}:{region}:{instance_name}'

    # Configura el engine
    engine = create_engine(
        f'postgresql+psycopg2://{db_user}:{db_password}@/{db_name}?host={db_host}'
    )

    Session = sessionmaker(bind=engine)
    return Session()

def consulta_dato():
    session = get_database_session()
    try:
        query = """
            SELECT t1.tipo_morosidad, t1.indice_morosidad 
            FROM keep_morosidad_pivot t1 
            INNER JOIN (
                SELECT tipo_morosidad, MAX(DATE) AS ultima 
                FROM keep_morosidad_pivot 
                GROUP BY tipo_morosidad
            ) t2 
            ON t1.tipo_morosidad = t2.tipo_morosidad 
            AND t1.DATE = t2.ultima 
            WHERE t1.tipo_morosidad = 'PRODUCTO_AGRUPADO'
        """
        result = session.execute(query)
        data = result.fetchall()
        if not data:
            return None
        
        # Convertir los resultados a un DataFrame de Pandas
        df = pd.DataFrame(data, columns=['tipo_morosidad', 'indice_morosidad'])
        return df
    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        return None
    finally:
        session.close()
'''
class PrepProcesor(BaseEstimator, TransformerMixin): 
    def fit(self, X, y=None): 
        self.ageImputer = SimpleImputer()
        self.ageImputer.fit(X[['Age']])        
        return self 
        
    def transform(self, X, y=None):
        X['IMPORTE_PROPUESTA'] = X['IMPORTE_PROPUESTA'].fillna(0).apply(lambda x: str(x).replace(",", ".")).apply(lambda x: re.sub(r'[^a-zA-Z]', '', x))
        X['CabinClass'] = X['Cabin'].fillna('M').apply(lambda x: str(x).replace(" ", "")).apply(lambda x: re.sub(r'[^a-zA-Z]', '', x))
        X['CabinNumber'] = X['Cabin'].fillna('M').apply(lambda x: str(x).replace(" ", "")).apply(lambda x: re.sub(r'[^0-9]', '', x)).replace('', 0) 
        X['Embarked'] = X['Embarked'].fillna('M')
        X = X.drop(['PassengerId', 'Name', 'Ticket','Cabin'], axis=1)
        return X
'''
columns = ['IMPORTE_PROPUESTA','TIPO_PROPUESTA','PROP_VINCULADA','PORCENTAJE_QUITA','DEUDA_INICIAL','DIAS_IMPAGO','PRODUCTO_AGRUPADO','REL_PER_CUE','MARCA_IND_SME','JUDICIALIZADO','INDICE_MOROSIDAD']
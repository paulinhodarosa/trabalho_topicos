import streamlit as st
import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn.linear_model import LinearRegression #Regressão linear
from sklearn import metrics #Cálculo do erro
import matplotlib_inline
import matplotlib
from sklearn import tree

# carrega a base de dados
df = pd.read_csv('drugs/drugs_and_riskfactors.csv')

# df = {
#     "age": [1],
#     "education": [2],
#     "father": [4],
#     "mother": [8],
#     "income": [16],
#     "race": [32],
#     "sex": [64],
#     "employment": [128],
#     "alcohol": [256],
#     "cigarettes": [512], 
#     "cocaine": [1024],
#     "crack": [2048], 
#     "heroin": [4096],
#     "marijuana": [8192], 
#     "meth": [16384]
# }

quali = ["age", "education",
        "father", "mother", 
        "income", "race",
        "sex", "employment", 
        "alcohol", "cigarettes", 
        "cocaine", "crack", 
        "heroin", "marijuana", 
        "meth"
] #variaveis quantitativas


dfQuali = df[quali] #Dataframe com quantitativas
alvo = 'crack' #variável alvo
target = df[alvo] #Separa a variável alvo

pd.get_dummies(df['father'])
pd.get_dummies(df['mother'])
pd.get_dummies(df['income'])
pd.get_dummies(df['sex'])
pd.get_dummies(df['age'])


usuario = ['Sim', 'Não']

#nivel de escolaridade
ed = df['education'].unique()
ed_min = int(df['education'].min())
ed_max = int(df['education'].max())

#ausencia de pai e mae
pai = df['father'].unique()
pai_min = int(df['father'].min())
pai_max = int(df['father'].max())

mae = df['mother'].unique()
mae_min = int(df['mother'].min())
mae_max = int(df['mother'].max())

# income/renda
renda = df['income'].unique()
renda_min = int(df['income'].min())
renda_max = int(df['income'].max())

# raça
race = df['race'].unique()
race_min = int(df['race'].min())
race_max = int(df['race'].max())

# sexo
sex = df['sex'].unique()
sex_min = int(df['sex'].min())
sex_max = int(df['sex'].max())

resultado = ['Sim', 'Não']

st.text('Idade por categorias')
st.text('1: 12-17 anos;\n2: 18-25 anos.')
age_count = df['age'].unique()
age_min = int(df['age'].min())
age_max = int(df['age'].max())

income_count = df['income'].unique()
income_min = int(df['income'].min())
income_max = int(df['income'].max())

gender = st.slider('Selecione as faixas etarias [1-6] ', sex_min, sex_max, value=sex_min)
age = st.slider('Selecione as faixas etarias [1-6] ', age_min, age_max, value=age_min)
escolaridade = st.slider('Registre o índice de escolaridade da pessoa: ', ed_min, ed_max, value=ed_min)
renda_registro = st.slider('Registre a renda da pessoa: ', income_min, income_max, value=income_min)
ausencia_pai = st.radio('A pessoa tem o Pai Ausente? ', options=pai)
ausencia_mae = st.radio('A pessoa tem a Mae Ausente? ', options=mae)

pd.get_dummies(df[quali])

# condicaoidade = df['age']=='1'
# UsaSim, UsaNao =  df[condicaoidade] , df[~condicaoidade]

# df = UsaNao
# condicao = df['father']='1', '2'
# condicao2 = df['mother']='1', '2'
# condicao3 = df['education']='2', '4'
# UsaNao_paipresente = df[condicao]
# UsaNao_paiausente = df[~condicao]
# UsaNao_maepresente = df[condicao2]
# UsaNao_maeausente = df[~condicao2]
# UsaNao_edalta = df[condicao3]
# UsaNao_edbaixa= df[~condicao3]

vals = [0,  #pai_presente
        0,  #pai_ausente
        0,  #mae_presente
        0,  #mae_ausente
        0,  #renda alta
        0,  #renda baixa
        0,  #jovem
        0, #adulto
        0, #masculino
        0 #feminino
       ]

arv = tree.DecisionTreeRegressor() #árvore de regressão
arv.fit(dfQuali, target) #cria a árvore
res = arv.predict([vals])   

#pai presente
if ausencia_pai in ['2', '1']:
    vals[0] = 1
elif ausencia_pai in ['3', '4']:
    vals[1] = 1
#mae presente
if ausencia_mae in ['2', '1']:
    vals[2] = 1
elif ausencia_mae in ['3', '4']:
    vals[3] = 1

#renda 
if renda_registro in ['2', '1']: #menos de 49 mil
    vals[4] = 1
elif renda_registro in ['3', '4']: #mais de 50 mil
    vals[5] = 1

# idade
if renda_registro in ['2', '1']: #JOVEM
    vals[6] = 1
elif renda_registro in ['3', '4', '5', '6']: #ADULTO
    vals[7] = 1

if renda_registro == '1': #masculino
    vals[8] = 1
elif renda_registro == 2: #ADULTO
    vals[9] = 1



if res[0] == '1':
    st.write('A pessoa tem a tendencia a não usar crack')
else:
    st.write("A pessoa tem a tendencia a usar crack")

# vento_dia = st.selectbox('Está ventando?: ', vento)

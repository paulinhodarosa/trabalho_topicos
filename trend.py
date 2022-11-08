import streamlit as st
import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn.linear_model import LinearRegression #Regressão linear
from sklearn import metrics #Cálculo do erro
import matplotlib_inline
import matplotlib

# carrega a base de dados
df = pd.read_csv('drugs/drugs_and_riskfactors.csv')



quant = ["age", "education",
        "father", "mother", 
        "income", "race",
        "sex", "employment", 
        "alcohol", "cigarettes", 
        "cocaine", "crack", 
        "heroin", "marijuana", 
        "meth"
        ]

dfQuant = df[quant]

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

age = st.slider('Selecione as faixas etarias [1-6] ', age_min, age_max, value=age_max)
escolaridade = st.slider('Informe o índice de escolaridade: ', ed_min, ed_max, value=ed_min)
ausencia_pai = st.radio('A pessoa tem o Pai Ausente? ', options=pai)
ausencia_mae = st.radio('A pessoa tem a Mae Ausente? ', options=mae)
# vento_dia = st.selectbox('Está ventando?: ', vento)
 

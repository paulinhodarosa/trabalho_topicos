import streamlit as st
import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn import tree
from sklearn.model_selection import train_test_split

# carrega a base de dados
df = pd.read_csv('drugs/drugs_and_riskfactors.csv')

st.title('Realizar uma estimativa se a pessoa tem a tendencia a utilizar algum tipo de droga')

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

st.sidebar.title('Idade por categorias')
st.sidebar.write('1: 12-17 anos')
st.sidebar.write('2: 18-25 anos')
st.sidebar.write('3: 26-34 anos')
st.sidebar.write('4: 35-49 anos')
st.sidebar.write('5: 50-64 anos')
st.sidebar.write('6: 65 anos ou mais')

st.sidebar.title('Ausência pai e mãe')
st.sidebar.write('1: Sim, o pai/mãe está na casa')
st.sidebar.write('2: Não, o pai/mãe não está na casa')
st.sidebar.write('3: Não sabe se o pai/mãe está ou não presente')
st.sidebar.write('4: participante tem 18 anos ou mais')

st.sidebar.title('Renda')
st.sidebar.write('1: Menor que 20 mil')
st.sidebar.write('2: Entre 20 e 49 mil')
st.sidebar.write('3: Entre 50 a 74 mil')
st.sidebar.write('4: Maior que 75 mil')

st.sidebar.title('Usuários')
st.sidebar.write('0: não faz o uso')
st.sidebar.write('1: referente ao uso')


age_count = df['age'].unique()
age_min = int(df['age'].min())
age_max = int(df['age'].max())

income_count = df['income'].unique()
income_min = int(df['income'].min())
income_max = int(df['income'].max())

#marijuana
maconha = df['marijuana'].unique()
marij_min = int(df['marijuana'].min())
marij_max = int(df['marijuana'].max())
#cocaine
cocaina = df['cocaine'].unique()
cocain_min = int(df['cocaine'].min())
cocain_max = int(df['cocaine'].max())
#cigarro
cigarro = df['cigarettes']
cig_min = int(df['cigarettes'].min())
cig_max = int(df['cigarettes'].max())
#heorina
heroina = df['heroin'].unique()
her_min = int(df['heroin'].min())
her_max = int(df['heroin'].max())
#meth
meth = df['meth'].unique()
metanfetamina_min = int(df['meth'].min())
metanfetamina_max = int(df['meth'].max())

gender = st.slider('Informe o gênero [1-M/2-F]', sex_min, sex_max, value=sex_min)
age = st.slider('Selecione as faixas etarias [1-6] ', age_min, age_max, value=age_min)
# escolaridade = st.slider('Registre o índice de escolaridade da pessoa: ', ed_min, ed_max, value=ed_min)
renda_registro = st.slider('Registre a renda da pessoa: ', income_min, income_max, value=income_min)
ausencia_pai = st.radio('A pessoa tem o Pai Ausente? ', options=pai)
ausencia_mae = st.radio('A pessoa tem a Mae Ausente? ', options=mae)

uso_meta = [st.number_input('A pessoa faz o uso de metanfetamina? ', step=1, value=0, max_value=1)]
uso_maconha = [st.number_input('A pessoa faz o uso de maconha(marijuana)?', step=1, value=0, max_value=1)]
uso_heroina = [st.number_input('A pessoa faz o uso de heroína? ', step=1, value=0, max_value=1)]
uso_alcool = [st.number_input('A pessoa consome alcool? ', step=1, value=0, max_value=1)]
uso_cigarro = [st.number_input('A pessoa consome cigarros? ', step=1, value=0, max_value=1)]
uso_cocaina = [st.number_input('A pessoa faz o uso de cocaina? ', step=1, value=0, max_value=1)]
pd.get_dummies(df[quali])

vals = ['0',  #pai_presente
        # '0',  #pai_ausente
        '0',  #mae_presente
        # '0',  #mae_ausente
        # '0',  #renda alta
        # '0',  #renda baixa
        '0',  #jovem
        # '0', #adulto
        '0', #masculino
        # '0', #feminino
        '0', #meth
        '0', #nao meth
        '0', #marijuana
        '0', #nao marij
        '0', #cocain
        '0', #nao coc
        '0', #cigarettes
        '0', #nao cig
        '0', #heroin
        '0', #nao usa
        '0' #uso alcool
        # 0 #NAO USA
       ]
 

#pai presente
if ausencia_pai in ['2', '1']:
    vals[0] = '0'
elif ausencia_pai in ['3', '4']:
    vals[0] = '1'
#mae presente
if ausencia_mae in ['2', '1']:
    vals[1] = '0'
elif ausencia_mae in ['3', '4']:
    vals[1] = '1'

# idade
if age in ['2', '1']: #JOVEM
    vals[2] = '1'
elif age in ['3', '4', '5', '6']: #ADULTO
    vals[2] = '0'

if gender == '1': #masculino
    vals[3] = '1'
if gender == '2': #feminino
    vals[3] = '0'

if uso_meta == '1': #usa
    vals[4] = '1'
if uso_meta == '0': #nao usa
    vals[5] = '0'

if uso_maconha == '1': #usa
    vals[6] = '1'
if uso_maconha == '0': #nao usa
    vals[7] = '0'

if uso_cocaina == '1': #usa
    vals[8] = '1'
if uso_cocaina == '0': #nao usa
    vals[9] = '0'

if uso_cigarro == '1': #usa
    vals[10] = '1'
if uso_cigarro == '0': #nao usa
    vals[11] = '0'

if uso_heroina == '1': #usa
    vals[12] = '1'
if uso_heroina == '0': #nao usa
    vals[13] = '0'

if uso_alcool == '1': #usa
    vals[14] = '1'
if uso_alcool == '0':
    vals[14] = '0'

arv = tree.DecisionTreeRegressor() #árvore de decisão
# Gere a árvore
arv.fit(dfQuali, target) #cria a árvore
res = arv.predict([vals])

st.write(int(res[0]))

if int(res[0]) == 0:
    st.write('A pessoa tem tendencia a não usar crack')
else:
    st.write("A pessoa tem tendencia a usar crack")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:38:37 2019

@author: captain-rogers
"""

import pandas as pd
import numpy as np

# ler do arquivo csv
base = pd.read_csv('credit-data.csv')

# estatisticas para cada um dos atributos
# cont: quantidade
# mean : media
# std : desvio padrão
# min: minimo
# max: maximo
base.describe()


# localizar atributos idade menor que zero
ages_negatives = base.loc[base['age'] < 0]

# apagar os registros com idade menor que 0
base.drop(base[base.age < 0].index, inplace=True)

#peencher os valores manualmente

#media das idades maiores que 0
mean_ages = base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = mean_ages
base.loc[base['age'].isnull()]
    
#separação dos previsores
# no caso [todas as linhas, 1 até a coluna 3]
# não conta os ids pois não farei nada com eles
prevision = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

# tratando valores nulos
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values= np.nan, strategy='mean', verbose=0)
#imputer de linhas e colunas de prevision
imputer = imputer.fit(prevision[:, :3])
prevision[:, :3] = imputer.transform(prevision[:, :3])


# Fazendo escalonamento de atributos
# para atributos na hora do processamento não ser considerado melhores que outros
# por causa de seu valor ser maior
# formula usada : x = ( x - media(x) ) / desvio_padrao(x) -
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
prevision = scaler.fit_transform(prevision)


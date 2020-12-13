# Importar as bibliotecas
import random 
from sklearn.linear_model import LinearRegression
#Crie uma lista vazia para o conjunto de dados de características 'X' e o conjunto de dados de destino 'y'feature_set = []
target_set= []
#Obter o número de linhas desejadas para o conjunto de dados
number_of_rows = 200
#Limitar os valores possíveis no conjunto de dados
random_number_limit = 2000
#Crie o conjunto de dados de treinamento
#Crie e anexe um conjunto de dados gerado aleatoriamente à entrada e saída
for i in range(0,number_of_rows):
  x = random.randint(0, random_number_limit)
  y = random.randint(0, random_number_limit)
  z = random.randint(0, random_number_limit)
#Crie uma função linear para o conjunto de dados de destino 'y'
function = (10*x) + (2*y) + (3*z)
feature_set.append([x,y,z])
target_set.append(function)
model = LinearRegression() #Crie um objeto / modelo de regressão linear
model.fit(feature_set, target_set) 
test_set = [[8,10,0]] 
prediction = model.predict(test_set)
print('Prediction:'+str(prediction)+'\t'+ 'Coefficient:'+str(model.coef_))





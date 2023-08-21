import csv
import numpy as np
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import Dense, Input
from sklearn.metrics import classification_report, confusion_matrix
from keras.utils import to_categorical
from keras.optimizers import Adam
from keras.losses import CategoricalCrossentropy
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from custom_layers import RBFLayer

# template data
# data = [
#     {
#         "temperature": 28.0,
#         "humidity": 72.0,
#         "gasPercentage": 0.05592142728955934,
#         "averageCO": 0.013767248273482555,
#         "averageMethane": 0.00018656185930989146,
#         "label": "normal"
#     },
# ]

# data = [
#     {
#         "temperature": 28.0,
#         "humidity": 72.0,
#         "gasPercentage": 0.05592142728955934,
#         "averageCO": 0.013767248273482555,
#         "averageMethane": 0.00018656185930989146,
#         "label": "normal"
#     },
#     {
#         "temperature": 28.0,
#         "humidity": 72.0,
#         "gasPercentage": 0.05592142728955934,
#         "averageCO": 0.013767248273482555,
#         "averageMethane": 0.00018656185930989146,
#         "label": "normal"
#     },
#     {
#         "temperature": 28.0,
#         "humidity": 72.0,
#         "gasPercentage": 0.05592142728955934,
#         "averageCO": 0.013767248273482555,
#         "averageMethane": 0.00018656185930989146,
#         "label": 'normal'
#     },
#     {
#         'temperature': 28.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.010486280047267498,
#         'averageMethane': 0.00008966498,
#         'label' : 'normal',
#     },{ 
#         'temperature': 28.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.015028040581523995,
#         'averageCO': 0.003062397435194257,
#         'averageMethane': 0.0000368019,
#         'label': 'normal'
#     },{ 
#         'temperature': 28.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.015505878861628901,
#         'averageCO': 0.003131323508789959,
#         'averageMethane': 0.0000368019,
#         'label': 'normal'
#     },{ 
#         'temperature': 28.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.015505878861628901,
#         'averageCO': 0.003131323508789959,
#         'averageMethane': 0.0000368019,
#         'label': 'normal'
#     },{ 
#         'temperature': 28.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.015505878861628901,
#         'averageCO': 0.003493530266022556,
#         'averageMethane': 0.00004443391,
#         'label': 'normal'
#     },{ 
#         'temperature': 28.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.01984153082885561,
#         'averageCO': 0.0041461080675157126,
#         'averageMethane': 0.00005025884,
#         'label': 'normal'
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.01984153082885561,
#         'averageCO': 0.004920975970668217,
#         'averageMethane': 0.0000511125,
#         'label': 'normal'
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.011331655324842668,
#         'averageMethane': 0.00014803333920491995,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.025225756609398558,
#         'averageCO': 0.005459438377906878,
#         'averageMethane': 0.00006808781,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.025225756609398558,
#         'averageCO': 0.005459438377906878,
#         'averageMethane': 0.00006808781,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.025225756609398558,
#         'averageCO': 0.005459438377906878,
#         'averageMethane': 0.00006808781,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.025225756609398558,
#         'averageCO': 0.005459438377906878,
#         'averageMethane': 0.00006808781,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.025225756609398558,
#         'averageCO': 0.005459438377906878,
#         'averageMethane': 0.00006808781,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.025225756609398558,
#         'averageCO': 0.005459438377906878,
#         'averageMethane': 0.00006808781,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.025225756609398558,
#         'averageCO': 0.005459438377906878,
#         'averageMethane': 0.00006808781,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.02930292941749849,
#         'averageCO': 0.008592384185798232,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 72.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.011456750828251231,
#         'averageMethane': 0.000124799655315144,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.026760738178916773,
#         'averageCO': 0.005843456075096806,
#         'averageMethane': 0.0000733705,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.026760738178916773,
#         'averageCO': 0.005843456075096806,
#         'averageMethane': 0.0000733705,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.026760738178916773,
#         'averageCO': 0.005843456075096806,
#         'averageMethane': 0.0000733705,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.026760738178916773,
#         'averageCO': 0.005843456075096806,
#         'averageMethane': 0.0000733705,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.026760738178916773,
#         'averageCO': 0.0065473278331023834,
#         'averageMethane': 0.00007428484,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 29.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 30.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 30.0,
#         'humidity': 73.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label' : 'normal',
#     },{ 
#         'temperature': 31.0,
#         'humidity': 75.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{
#         'temperature': 32.0,
#         'humidity': 76.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{
#         'temperature': 33.0,
#         'humidity': 75.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{
#         'temperature': 34.0,
#         'humidity': 75.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 74.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 73.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 73.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 71.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013423355840365147,
#         'averageMethane': 0.00017147477471326475,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 70.0,
#         'gasPercentage': 0.051501657503263354,
#         'averageCO': 0.012500441525504875,
#         'averageMethane': 0.00016807592677843064,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 69.0,
#         'gasPercentage': 0.051501657503263354,
#         'averageCO': 0.012500441525504875,
#         'averageMethane': 0.00016807592677843064,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 68.0,
#         'gasPercentage': 0.051501657503263354,
#         'averageCO': 0.012500441525504875,
#         'averageMethane': 0.00016807592677843064,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 66.0,
#         'gasPercentage': 0.051501657503263354,
#         'averageCO': 0.012500441525504875,
#         'averageMethane': 0.00016807592677843064,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 65.0,
#         'gasPercentage': 0.051501657503263354,
#         'averageCO': 0.012500441525504875,
#         'averageMethane': 0.00016807592677843064,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 63.0,
#         'gasPercentage': 0.051501657503263354,
#         'averageCO': 0.012702933641931403,
#         'averageMethane': 0.00016845574922908733,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 62.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 60.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 59.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 58.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 57.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 36.0,
#         'humidity': 56.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 35.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{
#         'temperature': 34.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 54.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 34.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 55.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 56.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 56.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 56.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 56.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 56.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 56.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 33.0,
#         'humidity': 56.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 58.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{
#         'temperature': 32.0,
#         'humidity': 58.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 58.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 58.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 59.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 59.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 59.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 59.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'fire'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 60.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 60.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 60.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 60.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 60.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 32.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 31.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 31.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 31.0,
#         'humidity': 61.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 31.0,
#         'humidity': 62.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     },{ 
#         'temperature': 31.0,
#         'humidity': 62.0,
#         'gasPercentage': 0.05592142728955934,
#         'averageCO': 0.013767248273482555,
#         'averageMethane': 0.00018656185930989146,
#         'label': 'normal'
#     }
# ]

# # save data into csv file
# with open('data.csv', 'w', newline='') as csvfile:
#     fieldnames = ['temperature', 'humidity', 'gasPercentage', 'averageCO', 'averageMethane', 'label']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for sample in data:
#         writer.writerow({'temperature': float(sample['temperature']), 'humidity': float(sample['humidity']), 'gasPercentage': float(sample['gasPercentage']), 'averageCO': float(sample['averageCO']), 'averageMethane': float(sample['averageMethane']), 'label': sample['label']})

# Load data from csv file into dictionary
data = []
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Convert data to numpy arrays
features = np.array([[float(sample['temperature']), float(sample['humidity']), float(sample['gasPercentage']), float(sample['averageCO']), float(sample['averageMethane'])] for sample in data])
labels = np.array([sample['label'] for sample in data])

# Convert data to pandas DataFrame
df = pd.DataFrame(features, columns=['temperature', 'humidity', 'gasPercentage', 'averageCO', 'averageMethane'])
df['label'] = labels

# Calculate summary statistics
summary = df.describe()

# Print summary statistics
print(summary)

# Encode labels into numerical values
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
encoded_labels = to_categorical(encoded_labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, encoded_labels, test_size=0.1, random_state=42)

# Number of radial basis functions (hidden neurons)
num_rbf_neurons = 128

# Create an input layer
inputs = Input(shape=(X_train.shape[1],))

# Add the RBF layer
rbf_layer = RBFLayer(num_rbf_neurons, gamma=0.5)(inputs)

# Add a dense layer for classification
num_labels = len(np.unique(labels))
activation = 'softmax' if num_labels > 2 else 'sigmoid'
output_layer = Dense(num_labels, activation=activation)(rbf_layer)

# Create the model
model = Model(inputs=inputs, outputs=output_layer)

# Optimize with different learning rates
learning_rates = [0.001, 0.01, 0.1, 0.2, 0.3]

# Compile the model
model.compile(loss=CategoricalCrossentropy(), optimizer=Adam(learning_rate=learning_rates[0]), metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=400, batch_size=32, verbose=2, validation_data=(X_test, y_test))

# # Save the trained model
# model.save("rbf_classification_model.h5")

# Make predictions
predictions = model.predict(X_test)
predicted_labels = np.argmax(predictions, axis=1)
predicted_labels = label_encoder.inverse_transform(predicted_labels)

print("Predicted labels:", predicted_labels)

# Classification report
target_names = label_encoder.classes_
classification_report_str = classification_report(
    np.argmax(y_test, axis=1), 
    np.argmax(predictions, axis=1), 
    target_names=target_names,
    zero_division=1
)
print(classification_report_str)

# Confusion matrix
confusion = confusion_matrix(np.argmax(y_test, axis=1), np.argmax(predictions, axis=1))
plt.figure(figsize=(8, 6))
sns.heatmap(confusion, annot=True, fmt="d", cmap="Blues", xticklabels=target_names, yticklabels=target_names)
plt.ylabel('Actual Value')
plt.xlabel('Predicted Value')
plt.title('Confusion Matrix')
plt.show()

# Load the saved model
from keras.models import load_model
saved_model = load_model("rbf_classification_model.h5", custom_objects={"RBFLayer": RBFLayer})

# Example usage of the saved model for making predictions
new_data = np.array([[29.0, 72.0, 0.05592142728955934, 0.013767248273482555, 0.00018656185930989146]])

# Load the same scaler used for training
scaler = StandardScaler()
scaler.fit(X_train)  # Fit the scaler on the training data

# Preprocess new data using the same scaler
scaled_new_data = scaler.transform(new_data)

# Make predictions
predictions = saved_model.predict(scaled_new_data)
predicted_class_index = np.argmax(predictions, axis=1)
predicted_class = label_encoder.inverse_transform(predicted_class_index)

print("Predicted class:", predicted_class)
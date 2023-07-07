# -*- coding: utf-8 -*-
"""crop-prediction-analysis-w-classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kBYjiUBcc8JKIlIsZYS2Ubh1pFP56-u2

<a id="1"></a>
# <p style="background-color:#44d180;font-family:roboto;color:#0a0a0b;font-size:150%;text-align:center;border-radius:60px 40px;">Importing Libraries</p>
"""

# Commented out IPython magic to ensure Python compatibility.
from __future__ import print_function
import pandas as pd # data analysis
import numpy as np # linear algebra

#import libraries for data visualization
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings('ignore')

"""<a id="2"></a>
# <p style="background-color:#44d180;font-family:roboto;color:#0a0a0b;font-size:150%;text-align:center;border-radius:60px 40px;">Loading data</p>

<img src='https://i.imgur.com/qpOUo9R.gif'>
"""

crop = pd.read_csv('/content/Crop_recommendation.csv')
crop.head(5)

""" <a id="3"></a>
# <p style="background-color:#44d180;font-family:roboto;color:#0a0a0b;font-size:150%;text-align:center;border-radius:60px 40px;">Exploratory Data Analysis</p>
"""

crop.info()

crop.describe()

crop.columns

crop.shape

crop['label'].unique()

crop['label'].nunique()

crop['label'].value_counts()

sns.heatmap(crop.isnull(),cmap="coolwarm")
plt.show()

plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
# sns.distplot(df_setosa['sepal_length'],kde=True,color='green',bins=20,hist_kws={'alpha':0.3})
sns.distplot(crop['temperature'],color="red",bins=15,hist_kws={'alpha':0.5})
plt.subplot(1, 2, 2)
sns.distplot(crop['ph'],color="green",bins=15,hist_kws={'alpha':0.5})

sns.pairplot(crop,hue = 'label')

sns.jointplot(x="rainfall",y="humidity",data=crop[(crop['temperature']<40) &
                                                  (crop['rainfall']>40)],height=10,hue="label")

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(30,15))
sns.boxplot(x='label',y='ph',data=crop)

fig, ax = plt.subplots(1, 1, figsize=(15, 9))
sns.heatmap(crop.corr(), annot=True,cmap='viridis')
ax.set(xlabel='features')
ax.set(ylabel='features')

plt.title('Correlation between different features', fontsize = 15, c='black')
plt.show()

crop_summary = pd.pivot_table(crop,index=['label'],aggfunc='mean')
crop_summary.head()

fig = go.Figure()
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['N'],
    name='Nitrogen',
    marker_color='mediumvioletred'
))
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['P'],
    name='Phosphorous',
    marker_color='springgreen'
))
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['K'],
    name='Potash',
    marker_color='dodgerblue'
))

fig.update_layout(title="N-P-K values comparision between crops",
                  plot_bgcolor='white',
                  barmode='group',
                  xaxis_tickangle=-45)

fig.show()

""" <a id="4"></a>
# <p style="background-color:#44d180;font-family:roboto;color:#0a0a0b;font-size:150%;text-align:center;border-radius:60px 40px;">Feature Selection</p>
"""

features = crop[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = crop['label']

acc = []
model = []

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(features,target,test_size = 0.2,random_state =2)

"""<a id="5"></a>
# <p style="background-color:#44d180;font-family:roboto;color:#0a0a0b;font-size:150%;text-align:center;border-radius:60px 40px;">Modeling Classification algorithms</p>

<a id="5.4"></a>
# <p style="background-color:#44d180;font-family:roboto;color:#0a0a0b;font-size:150%;text-align:center;border-radius:60px 40px;">Naive Bayes Classifier</p>
"""

from sklearn.naive_bayes import GaussianNB
NaiveBayes = GaussianNB()

NaiveBayes.fit(x_train,y_train)

predicted_values = NaiveBayes.predict(x_test)
x = metrics.accuracy_score(y_test, predicted_values)
acc.append(x)
model.append('Naive Bayes')

import pickle
filename = 'plant_recomendation.pkl'  # Specify the filename for the pickle file
with open(filename, 'wb') as file:
    pickle.dump(NaiveBayes, file)

filename = '/content/plant_recomendation.pkl'  # Specify the filename of the pickle file
with open(filename, 'rb') as file:
    model = pickle.load(file)

temp = [40,90,43,20.87974371,100.00274423,6.502985292000001,200.9355362	]
temp_reshaped = np.array(temp).reshape(1, -1)

predictions = model.predict(temp_reshaped)

predictions
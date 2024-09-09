from river import datasets
from river import naive_bayes
from river import preprocessing
from river import metrics

dataset = datasets.Phishing()

scaler = preprocessing.StandardScaler()
model = naive_bayes.GaussianNB()

metric = metrics.Accuracy()

for x, y in dataset:
    scaler.learn_one(x)
    
    x = scaler.transform_one(x)
    
    y_pred = model.predict_one(x)
    
    if y_pred is not None:
        metric.update(y, y_pred)
        print(f'Predicción: {y_pred}, Real: {y}, Precisión actual: {metric.get():.4f}')
    
    model.learn_one(x, y)

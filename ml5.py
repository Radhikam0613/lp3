import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
from sklearn.pipeline import make_pipeline

uploaded = files.upload()
df = pd.read_csv(next(iter(uploaded)))

X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]

X = X.apply(pd.to_numeric, errors='coerce').fillna(0)
y = pd.to_numeric(y, errors='coerce')

valid = y.isin([0, 1])
X = X.loc[valid]
y = y.loc[valid].astype(int)
#Example	df.iloc[0]	df.loc[0]
#Meaning	Selects the first row	Selects the row whose index label is 0

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# MaxAbsScaler scales numerical features by dividing each
# value by the maximum absolute value of its column
# make_pipeline() runs these steps in order, fitting the scaler on 
# training data before training KNN and applying the same scaling to test data.
knn = make_pipeline( MaxAbsScaler(),KNeighborsClassifier(n_neighbors=5))

knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

svm = make_pipeline(MaxAbsScaler(),SVC(kernel='linear'))

svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

results = []
for name, pred in [('KNN', knn_pred), ('SVM', svm_pred)]:
    results.append({
        'Model': name,
        'Accuracy': accuracy_score(y_test, pred),
        'Precision': precision_score(y_test, pred, zero_division=0),
        'Recall': recall_score(y_test, pred, zero_division=0),
        'F1-Score': f1_score(y_test, pred, zero_division=0)
    })

print("Model Comparison:\n", pd.DataFrame(results).round(4))

fig, axes = plt.subplots(1, 2, figsize=(9, 4))
for ax, name, pred in zip(axes, ['KNN', 'SVM'], [knn_pred, svm_pred]):
    sns.heatmap(confusion_matrix(y_test, pred), annot=True, fmt='d',
                cmap='Blues', ax=ax,
                xticklabels=['Not Spam', 'Spam'],
                yticklabels=['Not Spam', 'Spam'])
    ax.set_title(name)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')

plt.tight_layout()
plt.show()

for name, pred in [('KNN', knn_pred), ('SVM', svm_pred)]:
    print(f"\n{name} Classification Report:\n",
          classification_report(y_test, pred, zero_division=0))
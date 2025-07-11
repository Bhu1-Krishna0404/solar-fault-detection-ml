
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score
import joblib


df = pd.read_csv("LL1.csv") 



X = df[['V', 'I', 'G', 'P']]
y = df[['no_module_fault', 'fault', 'partial_shading']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultiOutputClassifier(RandomForestClassifier(random_state=42))
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy_per_label = {}
for i, label in enumerate(y.columns):
    acc = accuracy_score(y_test[label], y_pred[:, i])
    accuracy_per_label[label] = round(acc * 100, 2)

print("Accuracy for each label:")
print(accuracy_per_label)

joblib.dump(model, "pv_fault_model.pkl")

from sklearn.metrics import accuracy_score


accuracy_per_label = {}
for i, label in enumerate(y.columns):
    acc = accuracy_score(y_test[label], y_pred[:, i])
    accuracy_per_label[label] = round(acc * 100, 2)

overall_accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)


print("\n Accuracy Report using Random Forest Classifier:")
print("----------------------------------------------------")
for label, acc in accuracy_per_label.items():
    print(f" Accuracy for {label}: {acc}%")
print("----------------------------------------------------")
print(f"Overall Subset Accuracy: {overall_accuracy}%")

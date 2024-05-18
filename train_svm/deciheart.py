import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset (gantikan 'data.csv' dengan nama file dataset anda)
data = pd.read_csv('hearts.csv')

# Pisahkan fitur dan label
X = data.drop('target', axis=1)  # Gantikan 'target_column' dengan nama kolom target
y = data['target']

# Pisahkan data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)

# Latih model
dt_model.fit(X_train, y_train)

# Lakukan prediksi
y_pred = dt_model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree Accuracy:", accuracy)

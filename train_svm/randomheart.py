import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (gantikan 'data.csv' dengan nama file dataset anda)
data = pd.read_csv('hearts.csv')

# Pisahkan fitur dan label
X = data.drop('target', axis=1)  # Gantikan 'target_column' dengan nama kolom target
y = data['target']

# Pisahkan data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)  # Anda boleh sesuaikan n_estimators dengan keperluan anda

# Latih model
rf_model.fit(X_train, y_train)

# Lakukan prediksi
y_pred = rf_model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

joblib.dump(rf_model, 'randomf.pkl')
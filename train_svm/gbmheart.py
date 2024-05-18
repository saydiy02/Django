import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Load dataset (gantikan 'data.csv' dengan nama file dataset anda)
data = pd.read_csv('pentest.csv')

# Pisahkan fitur dan label
X = data.drop('suggest', axis=1)  # Gantikan 'target_column' dengan nama kolom target
y = data['suggest']

# Pisahkan data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model Gradient Boosting
gbm_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)  # Anda boleh sesuaikan n_estimators dan learning_rate dengan keperluan anda

# Latih model
gbm_model.fit(X_train, y_train)

# Lakukan prediksi
y_pred = gbm_model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
print("GBM Accuracy:", accuracy)

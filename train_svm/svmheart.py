from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

# Membaca dataset dari file CSV (gantilah 'nama_file.csv' dengan nama file dataset Anda)
dataset = pd.read_csv('hearts.csv')

# Memisahkan fitur-fitur (X) dan label (y)
X = dataset.drop(columns=['target'])  # Ganti 'target_column' dengan nama kolom label
y = dataset['target']

# Bagi dataset menjadi data latihan dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat objek model SVM
svm_model = SVC(kernel='rbf', C=1.0)

# Latih model dengan data latihan
svm_model.fit(X_train, y_train)

# Evaluasi model dengan data uji (opsional)
accuracy = svm_model.score(X_test, y_test)
print("Accuracy:", accuracy)

#print(dataset.head())
joblib.dump(svm_model,'svmheart_model.pkl')

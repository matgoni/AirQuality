import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def split_data(file_path, test_size=0.3):
    df = pd.read_csv(file_path)

    X = df.drop(columns=['Riesgo'])
    y = df['Riesgo']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)
    
    return X_train, X_test, y_train, y_test

def train_svm(X_train, y_train, kernel='linear'):
    svm_model = SVC(kernel=kernel, random_state=42)
    cv_scores = cross_val_score(svm_model, X_train, y_train, cv=5)
    svm_model.fit(X_train, y_train)
    
    return svm_model, cv_scores

def train_random_forest(X_train, y_train, n_estimators=100, max_depth=None):
    rf_model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    cv_scores = cross_val_score(rf_model, X_train, y_train, cv=5)
    rf_model.fit(X_train, y_train)
    
    return rf_model, cv_scores

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions, output_dict=True)
    accuracy = accuracy_score(y_test, predictions)
    confusion = confusion_matrix(y_test, predictions)
    
    print("Informe de Clasificación:\n", classification_report(y_test, predictions))
    print("Exactitud:", accuracy)
    print("Matriz de Confusión:\n", confusion)
    
    return report, accuracy, confusion

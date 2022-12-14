import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt
import seaborn as sns 

def tuning(model, parameters, X_train, y_train):
    
    random_estimator = RandomizedSearchCV(estimator = model,
                                          param_distributions = parameters,
                                          n_iter=10, 
                                          scoring='f1', 
                                          n_jobs=-1, 
                                          cv=5, 
                                          verbose=3, 
                                          random_state=420)
    
    random_estimator.fit(X_train, y_train)

    print ('Best Estimator: ', random_estimator.best_estimator_, ' \n')
    
    chosen_model = random_estimator.best_estimator_
    
    return chosen_model


def fit_n_predict(X_train, X_test, y_train, y_test, model):
    
    fitted_model = model
    fitted_model = fitted_model.fit(X_train, y_train)
    predictions = fitted_model.predict(X_test)
    
    print("Accuracy Score: {:.2f}".format(accuracy_score(y_test, predictions)))
    print("Precision Score: {:.2f}".format(precision_score(y_test, predictions)))
    print("Recall Score: {:.2f}".format(recall_score(y_test, predictions)))
    print("F1 Score: {:.2f}".format(f1_score(y_test, predictions)))
    
    return fitted_model, predictions


def conf_mat(y_test, model_predict):
    cm = confusion_matrix(y_test, model_predict, labels=[0,1])
    plt.style.use('seaborn')
    plt.figure(figsize=(10,7))
    sns.heatmap(cm, annot = True)
    plt.xlabel('Predicted')
    plt.ylabel('True')


def plot_feats(fitted_model, X):
    fitted_model.feature_importances_

    features = X.columns

    importances_clf = pd.Series(data = fitted_model.feature_importances_,
                                index= features)

    # Sort importances
    importances_sorted_clf = importances_clf.sort_values()

    # Draw a horizontal barplot of importances_sorted
    importances_sorted_clf.plot(kind='barh', color='green')
    plt.title('Gini Features Importances', size=15)
    plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, ConfusionMatrixDisplay, confusion_matrix, roc_curve

def evaluate(model, X_test, y_test):

    y_pred = model.predict(X_test)
    mean_abs_err = mean_absolute_error(y_test, y_pred)
    mean_sqr_err = mean_squared_error(y_test, y_pred)
    r2_scr = r2_score(y_test, y_pred)
    print(f"MAE: {mean_abs_err}")
    print(f"MSE: {mean_sqr_err}")
    print(f"R2 Score: {r2_scr}")

    cm = confusion_matrix(y_test,y_pred)
    ConfusionMatrixDisplay(cm)

    fpr, tpr, _ = roc_curve(y_test, y_pred)
    plt.plot(fpr, tpr)
    plt.xlabel("Rate of False Positives")
    plt.ylabel("Rate of True Positives")
    plt.title("ROC Curve of False and True Positive Rates")






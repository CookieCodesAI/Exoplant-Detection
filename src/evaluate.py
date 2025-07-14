import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, accuracy_score, ConfusionMatrixDisplay, confusion_matrix, roc_curve

def evaluate(model, X_test, y_test):

    y_pred = model.predict(X_test)
    print(f"The classification report is: {(classification_report(y_test, y_pred))}")
    print(f"Accuracy Score: {accuracy_score(y_test, y_pred)}")

    cm = confusion_matrix(y_test,y_pred)
    disp = ConfusionMatrixDisplay(cm)
    disp.plot()
    plt.title("Confusion Matrix")
    plt.show()


    fpr, tpr, _ = roc_curve(y_test, y_pred)
    plt.plot(fpr, tpr)
    plt.xlabel("Rate of False Positives")
    plt.ylabel("Rate of True Positives")
    plt.title("ROC Curve of False and True Positive Rates")
    plt.show()






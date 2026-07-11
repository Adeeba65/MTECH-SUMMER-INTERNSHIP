"""
Experiment 7 — Lab Tasks: Model Evaluation & Validation
===========================================================
Note: Matplotlib is used for the ROC curve plot in Task 5.
Install it first if needed:  pip install matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (
    confusion_matrix, classification_report,
    precision_score, recall_score, f1_score,
    mean_squared_error, roc_curve, auc
)
from sklearn.datasets import make_classification, load_iris


# ==========================================================
# Task 1: Split a dataset 70/15/15 and explain why the test
#         set must stay unseen.
# ==========================================================
X, y = make_classification(n_samples=200, random_state=1)

# First split: 70% train, 30% temp
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=1)
# Second split: split the 30% temp into 15% validation, 15% test
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=1)

print("Train size:", len(X_train), "| Validation size:", len(X_val), "| Test size:", len(X_test))
print("""
Why the test set must stay unseen:
If we peek at the test set while training or tuning, we start (often
unintentionally) adjusting the model to do well specifically on that
data. The test score would then no longer reflect how the model will
perform on genuinely new, real-world data. Keeping it unseen until the
very end gives an honest, unbiased final performance estimate.
""")

print("="*50 + "\n")


# ==========================================================
# Task 2: Compute precision, recall and F1 for a classifier
#         of your choice.
# ==========================================================
clf = LogisticRegression(max_iter=200).fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nPrecision:", round(precision_score(y_test, y_pred), 3))
print("Recall:", round(recall_score(y_test, y_pred), 3))
print("F1-score:", round(f1_score(y_test, y_pred), 3))
print("\nFull classification report:\n", classification_report(y_test, y_pred, digits=2))

print("="*50 + "\n")


# ==========================================================
# Task 3: Demonstrate overfitting with a high-degree
#         polynomial and show the train vs test gap.
# ==========================================================
rng = np.random.RandomState(0)
X_poly = np.sort(rng.uniform(0, 1, 30)).reshape(-1, 1)
y_poly = np.sin(2 * np.pi * X_poly.ravel()) + rng.normal(0, 0.2, 30)

Xp_train, Xp_test, yp_train, yp_test = train_test_split(X_poly, y_poly, test_size=0.3, random_state=0)

print("Degree\tTrain Error\tTest Error")
for degree in [1, 4, 15]:
    poly_model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    poly_model.fit(Xp_train, yp_train)
    train_err = mean_squared_error(yp_train, poly_model.predict(Xp_train))
    test_err = mean_squared_error(yp_test, poly_model.predict(Xp_test))
    print(f"{degree}\t{train_err:.4f}\t\t{test_err:.4f}")

print("""
Notice: as the degree increases (especially at 15), the train error keeps
dropping (the model fits the training points almost perfectly), but the
test error goes back up — this growing train/test gap is the signature
of overfitting.
""")

print("="*50 + "\n")


# ==========================================================
# Task 4: Run cross-validation and report the mean score
#         with standard deviation.
# ==========================================================
from sklearn.ensemble import RandomForestClassifier

X_iris, y_iris = load_iris(return_X_y=True)
cv_scores = cross_val_score(RandomForestClassifier(random_state=1), X_iris, y_iris, cv=5)

print("Fold scores:", cv_scores.round(3))
print("Mean accuracy:", round(cv_scores.mean(), 3))
print("Standard deviation:", round(cv_scores.std(), 3))

print("="*50 + "\n")


# ==========================================================
# Task 5: Plot a ROC curve for a binary classifier and
#         state its AUC.
# ==========================================================
y_scores = clf.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, label=f"ROC curve (AUC = {roc_auc:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Random guess")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Task 5: ROC Curve")
plt.legend()
plt.savefig("task5_roc_curve.png")
plt.close()

print("AUC:", round(roc_auc, 3))
print("Task 5 done -> saved plot as task5_roc_curve.png")

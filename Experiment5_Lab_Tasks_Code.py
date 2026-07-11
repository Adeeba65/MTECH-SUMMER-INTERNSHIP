"""
Experiment 5 — Lab Tasks: Supervised Learning (Regression & Classification)
=============================================================================
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
from sklearn.datasets import load_iris


# ==========================================================
# Task 1: Train a LinearRegression model on any real dataset
#         and report R² and RMSE.
# ==========================================================
rng = np.random.RandomState(1)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 2.2 * X.ravel() + 5 + rng.normal(0, 2, 100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
reg_model = LinearRegression().fit(X_train, y_train)
predictions = reg_model.predict(X_test)

print("R2 score:", round(r2_score(y_test, predictions), 3))
print("RMSE:", round(mean_squared_error(y_test, predictions) ** 0.5, 3))

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 2: Train a LogisticRegression classifier and report
#         its accuracy and a sample prediction.
# ==========================================================
X_iris, y_iris = load_iris(return_X_y=True)
Xi_train, Xi_test, yi_train, yi_test = train_test_split(X_iris, y_iris, test_size=0.2, random_state=1)

log_model = LogisticRegression(max_iter=200).fit(Xi_train, yi_train)
accuracy = log_model.score(Xi_test, yi_test)
sample_prediction = log_model.predict([Xi_test[0]])

print("Logistic Regression Accuracy:", accuracy)
print("Sample prediction for first test row:", sample_prediction[0], "| Actual:", yi_test[0])

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 3: Compare KNN with k = 1, 3, 5, 7 on the Iris dataset
#         in a small table.
# ==========================================================
print("k\tAccuracy")
for k in [1, 3, 5, 7]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(Xi_train, yi_train)
    acc = accuracy_score(yi_test, knn.predict(Xi_test))
    print(f"{k}\t{acc:.4f}")

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 4: Train a Decision Tree and describe which two
#         features it found most important.
# ==========================================================
tree_model = DecisionTreeClassifier(max_depth=3, random_state=1).fit(Xi_train, yi_train)
feature_names = load_iris().feature_names
importances = tree_model.feature_importances_

# Sort features by importance, most important first
sorted_features = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)

print("Feature importances (highest to lowest):")
for name, score in sorted_features:
    print(f"  {name}: {score:.3f}")

print("\nTop 2 most important features:", sorted_features[0][0], "and", sorted_features[1][0])

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 5: Explain in your report the difference between
#         regression and classification with examples.
# (Written/explanation task — printed below.)
# ==========================================================
explanation = """
Regression predicts a CONTINUOUS number.
  Example: predicting a house price ($150,000, $210,500, etc.)

Classification predicts a CATEGORY/CLASS.
  Example: predicting whether an email is "Spam" or "Not Spam"

In short: Regression -> "How much / how many?"
          Classification -> "Which category?"
"""
print(explanation)

"""
Experiment 4 — Lab Tasks: Machine Learning Fundamentals & Workflow
=====================================================================
"""

from sklearn.linear_model import LinearRegression
import numpy as np


# ==========================================================
# Task 1: Train a LinearRegression model on hours-vs-marks
#         data and predict for 7 and 8 hours.
# ==========================================================
hours = np.array([[1], [2], [3], [4], [5]])
marks = np.array([35, 50, 65, 80, 95])

model = LinearRegression()
model.fit(hours, marks)

predicted_7 = model.predict([[7]])[0]
predicted_8 = model.predict([[8]])[0]

print("Predicted marks for 7 hours of study:", predicted_7)
print("Predicted marks for 8 hours of study:", predicted_8)

print("\n" + "="*50 + "\n")


# ==========================================================
# Task 2: Write a short note describing each step of the
#         ML workflow with one sentence.
# (This is a written/explanation task, not a coding task —
#  printed below as a summary.)
# ==========================================================
ml_workflow_notes = """
1. Collect Data      -> Gather raw data relevant to the problem.
2. Clean/Preprocess  -> Handle missing values, fix errors, format data.
3. Split Data        -> Divide into training and test sets.
4. Train Model        -> Fit a model on the training data.
5. Evaluate Model     -> Check performance on the test data using metrics.
6. Tune Hyperparameters -> Adjust settings to improve performance.
7. Deploy Model       -> Put the final model into real-world use.
"""
print(ml_workflow_notes)

print("="*50 + "\n")


# ==========================================================
# Task 3: Give three real-world examples each of
#         classification and regression problems.
# (Written/explanation task — printed below.)
# ==========================================================
examples = """
Classification examples (predicting a category):
  1. Email spam detection (Spam / Not Spam)
  2. Disease diagnosis (Positive / Negative)
  3. Image recognition (Cat / Dog / Bird)

Regression examples (predicting a number):
  1. House price prediction
  2. Predicting tomorrow's temperature
  3. Predicting a student's exam score based on study hours
"""
print(examples)

print("="*50 + "\n")


# ==========================================================
# Task 4: For a dataset of your choice, list its features
#         and its label.
# ==========================================================
import pandas as pd

data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Attendance": [60, 70, 75, 85, 95],
    "FinalMarks": [35, 50, 65, 80, 95],   # this is the label (what we predict)
}
df = pd.DataFrame(data)

features = [col for col in df.columns if col != "FinalMarks"]
label = "FinalMarks"

print("Dataset:\n", df)
print("\nFeatures (inputs):", features)
print("Label (output to predict):", label)

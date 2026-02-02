import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")





print("=== FULL DATA ===")
print(df)  # Show entire table
# ------------------------------
# 2. Quick inspection
# ------------------------------
print("\n=== HEAD ===")
print(df.head())  # Show first 5 rows
print("\n=== INFO ===")
print(df.info())  # Column types, missing values
print("\n=== DESCRIBE ===")
print(df.describe())  # Summary stats of numeric columns
# ------------------------------
# 3. Basic cleaning
# ------------------------------
df = df.fillna(0)  # Fill missing values with 0
print("\n=== AFTER FILLING NA ===")
print(df)
# ------------------------------
# 4. Filter data
# ------------------------------
print("\n=== STUDENTS WITH QUIZ SCORE > 85 ===")
print(df[df["quiz_score"] > 85])  # Show only students with quiz score > 85
print("\n=== STUDENTS WITH EXAM SCORE > 90 ===")
print(df[df["exam_score"] > 90])  # Show only students with exam score > 90
print("\n=== STUDENTS WITH ATTENDANCE SCORE > 0.92 ===")
print(df[df["attendance"] > 0.92])  # Show only students with attendance score > 0.92



# visualizing data using matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df["name"], df["quiz_score"], alpha=0.6, label="Quiz Score")
plt.bar(df["name"], df["exam_score"], alpha=0.6, label="Exam Score", bottom=df["quiz_score"])
plt.bar(df["name"], df["attendance"] * 100, alpha=0.6
, label="Attendance (%)", bottom=df["quiz_score"] + df["exam_score"])
plt.xlabel("Student Name")
plt.ylabel("Scores")
plt.title("Student Scores")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


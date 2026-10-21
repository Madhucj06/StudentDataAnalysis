import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the student data
data = pd.read_csv("students.csv")

# Calculate average marks for each student
data["Average"] = np.mean(
    data[["Maths", "Science", "English"]],
    axis=1
)

# Display student performance
print("\n\tStudent Performance:")
print(
    data[
        ["Student_ID", "Name", "Maths", "Science", "English", "Average"]
    ]
)

# Calculate overall subject averages
print("\nSubject Averages:")
print("Maths:", np.mean(data["Maths"]))
print("Science:", np.mean(data["Science"]))
print("English:", np.mean(data["English"]))

# Create a bar graph for student averages
plt.figure(figsize=(10, 5))

plt.bar(data["Name"], data["Average"])

plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Find highest and lowest scorer
highest_scorer = data.loc[data["Average"].idxmax()]
lowest_scorer = data.loc[data["Average"].idxmin()]

print("\nHighest Scorer:")
print("Name:", highest_scorer["Name"])
print("Average:", highest_scorer["Average"])

print("\nLowest Scorer:")
print("Name:", lowest_scorer["Name"])
print("Average:", lowest_scorer["Average"])


# Create graph
plt.figure(figsize=(10, 5))

plt.bar(data["Name"], data["Average"])

# Highlight highest and lowest
plt.bar(
    highest_scorer["Name"],
    highest_scorer["Average"]
)

plt.bar(
    lowest_scorer["Name"],
    lowest_scorer["Average"]
)

plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Attendance Analysis
print("\nAttendance Analysis:")

highest_attendance = data.loc[data["Attendance"].idxmax()]
lowest_attendance = data.loc[data["Attendance"].idxmin()]

print("Highest Attendance:")
print("Name:", highest_attendance["Name"])
print("Attendance:", highest_attendance["Attendance"], "%")

print("\nLowest Attendance:")
print("Name:", lowest_attendance["Name"])
print("Attendance:", lowest_attendance["Attendance"], "%")
# Attendance Category Analysis

excellent = len(data[data["Attendance"] >= 90])
good = len(data[(data["Attendance"] >= 80) & (data["Attendance"] < 90)])
needs_improvement = len(data[data["Attendance"] < 80])

categories = ["Excellent (90%+)", "Good (80-89%)", "Needs Improvement (<80%)"]
students_count = [excellent, good, needs_improvement]

plt.figure(figsize=(7, 7))

plt.pie(
    students_count,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Attendance Categories")

plt.show()
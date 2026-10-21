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
print("\nStudent Performance:")
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
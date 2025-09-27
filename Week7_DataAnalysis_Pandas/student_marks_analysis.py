
---

### **student_marks_analysis.py**

```python
import pandas as pd

# Load CSV file
df = pd.read_csv("student_marks.csv")

# View first 5 rows
print(df.head())

# Summary statistics
print(df.describe())

# Average marks per student
print(df.groupby("Student")["Marks"].mean())

# Optional: save analysis to a new CSV
df.groupby("Student")["Marks"].mean().to_csv("average_marks.csv")

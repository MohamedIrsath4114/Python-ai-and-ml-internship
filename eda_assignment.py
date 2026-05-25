# Assignment: NumPy, Pandas, Matplotlib and EDA

# =========================================================
# 1. Work on NumPy, Pandas, and Matplotlib
# =========================================================

# NumPy Program
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# ---------------------------------------------------------

# Pandas Program
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
print(df.describe())

# ---------------------------------------------------------

# Matplotlib Program
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# =========================================================
# 2. Titanic Dataset EDA
# =========================================================

import seaborn as sns

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

print(titanic_df.head())

# Dataset Information
print(titanic_df.info())
print(titanic_df.describe())
print(titanic_df.isnull().sum())

# Fill Missing Values
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)
titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0], inplace=True)

# Survival Count Plot
survival_count = titanic_df['Survived'].value_counts()

plt.bar(survival_count.index, survival_count.values)
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

# Gender-wise Survival Plot
gender_survival = titanic_df.groupby('Sex')['Survived'].sum()

gender_survival.plot(kind='bar')

plt.title("Gender-wise Survival")
plt.xlabel("Gender")
plt.ylabel("Survivors")

plt.show()

# Age Distribution Histogram
plt.hist(titanic_df['Age'], bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# Passenger Class Pie Chart
pclass = titanic_df['Pclass'].value_counts()

plt.pie(
    pclass.values,
    labels=pclass.index,
    autopct='%1.1f%%'
)

plt.title("Passenger Class Distribution")

plt.show()

# Extra Plot 1 — Fare Distribution
plt.hist(titanic_df['Fare'], bins=30)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")

plt.show()

# Extra Plot 2 — Correlation Heatmap
corr = titanic_df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.show()

# =========================================================
# 3. Kaggle CSV File EDA (Iris Dataset)
# =========================================================

iris_df = pd.read_csv("Iris.csv")

print(iris_df.head())

# Dataset Information
print(iris_df.info())
print(iris_df.describe())
print(iris_df.isnull().sum())

# Species Count Plot
species_count = iris_df['Species'].value_counts()

species_count.plot(kind='bar')

plt.title("Species Count")
plt.xlabel("Species")
plt.ylabel("Count")

plt.show()

# Sepal Length Histogram
plt.hist(iris_df['SepalLengthCm'], bins=20)

plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")

plt.show()

# Scatter Plot
plt.scatter(
    iris_df['SepalLengthCm'],
    iris_df['PetalLengthCm']
)

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")

plt.show()

# Box Plot
plt.boxplot(iris_df['PetalLengthCm'])

plt.title("Petal Length Box Plot")

plt.show()

# Pair Plot
sns.pairplot(iris_df, hue='Species')

plt.show()

print("EDA Assignment Completed Successfully!")

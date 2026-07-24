import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------
# Load the cleaned dataset (Excel file)
# ---------------------------------------------
df = pd.read_csv(r'C:\Users\HP\Desktop\FinTwin-ai\clean_financial_health_dataset.csv')  # replace with the actual file name

# ---------------------------------------------
# 1. Summary Statistics
# ---------------------------------------------
key_vars = ['Monthly_Income', 'Monthly_Expenses', 'Monthly_Savings',
            'Loan_Amount', 'Debt_to_Income_Ratio', 'Savings_Rate']

print("Summary Statistics:")
print(df.columns.tolist())
print(df[key_vars].describe())

# ---------------------------------------------
# 2. Histograms for each variable
# ---------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for i, col in enumerate(key_vars):
    if col in df.columns:
        sns.histplot(df[col], bins=30, kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel(col)

plt.tight_layout()
plt.savefig('distribution_plots.png')
plt.show()

# ---------------------------------------------
# 3. Outlier Detection (IQR method)
# ---------------------------------------------
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

print("\nOutlier Summary:")
for col in key_vars:
    if col in df.columns:
        outliers, lower, upper = detect_outliers_iqr(df, col)
        print(f"{col}: {len(outliers)} outliers detected "
              f"(valid range: {lower:.2f} to {upper:.2f})")

# ---------------------------------------------
# 4. Boxplots (visual outlier check)
# ---------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for i, col in enumerate(key_vars):
    if col in df.columns:
        sns.boxplot(y=df[col], ax=axes[i])
        axes[i].set_title(f'Boxplot of {col}')

plt.tight_layout()
plt.savefig('boxplots.png')
plt.show()
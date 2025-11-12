import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
df = pd.read_csv('data/HR_Analytics.csv')
Path('images').mkdir(exist_ok=True)
if 'Department' in df.columns and 'Attrition' in df.columns:
    sns.countplot(data=df, x='Department', hue='Attrition')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/attrition_by_department.png')
    plt.clf()
if 'JobSatisfaction' in df.columns and 'Attrition' in df.columns:
    sns.boxplot(x='Attrition', y='JobSatisfaction', data=df)
    plt.tight_layout()
    plt.savefig('images/satisfaction_vs_attrition.png')
    plt.clf()
num_df = df.select_dtypes(include=[float,int])
if num_df.shape[1] > 1:
    sns.heatmap(num_df.corr(), cmap='coolwarm', center=0)
    plt.tight_layout()
    plt.savefig('images/correlation_heatmap.png')
print('Done')
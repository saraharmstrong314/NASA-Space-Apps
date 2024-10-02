# consider imbalanced classes, use duplicates or not in training
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('exoplanet_names.csv')
    unique_names = df['pl_name'].unique()
    lst = unique_names.tolist()
    print(len(unique_names))
    with open('unique_names.txt', 'w') as f:
        for name in lst:
            f.write(name)
            f.write('\n')
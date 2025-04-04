from sklearn.model_selection import train_test_split
import pandas as pd
import os

def split_and_save(df, config, dataset_name, test_size=0.2):

    #Split and save data into train/test sets

    # Check if target column exists
    target_col = config.get("target")
    
    if target_col and target_col in df.columns:
        X = df.drop(columns=[target_col])
        y = df[target_col]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        # create directory if it doesn't exist
        os.makedirs(f"data/processed/{dataset_name}", exist_ok=True)
        
        # save datasets
        pd.concat([X_train, y_train], axis=1).to_csv(
            f"data/processed/{dataset_name}/{dataset_name}_train.csv", index=False
        )
        pd.concat([X_test, y_test], axis=1).to_csv(
            f"data/processed/{dataset_name}/{dataset_name}_test.csv", index=False
        )
        
        print(f"{dataset_name} split into train/test")
    else:
        print(f"target column '{target_col}' not found in {dataset_name}")
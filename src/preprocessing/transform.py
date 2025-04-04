# transform.py
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

def one_hot_encode(df, config):
    #one-Hot Encoding for specific columns
    if "onehot_cols" in config:
        # filter columns that exist in the dataframe
        cols_to_encode = [col for col in config["onehot_cols"] if col in df.columns]
        
        for col in cols_to_encode:
            # create dummies keeping original name as prefix
            dummies = pd.get_dummies(df[col], prefix=col, dtype=int)
            # remove original column and concatenate new ones
            df = df.drop(col, axis=1)
            df = pd.concat([df, dummies], axis=1)
    
    return df

def encode_target(df, config):
    #encodes target variable according to configuration
    target_col = config.get("target")
    
    if target_col and target_col in df.columns:
        # check if target should remain as string
        if target_col in config.get("keep_as_string", []):
            return df
            
        encoding_type = config.get("target_encoding", "label")
        
        if encoding_type == "label":
            encoder = LabelEncoder()
            df[target_col] = encoder.fit_transform(df[target_col])
        elif encoding_type == "onehot":
            df = one_hot_encode(df, {**config, "onehot_cols": [target_col]})
    
    return df

def encode_categorical(df, config):
    #encoding for general categorical features
    if "categorical_cols" in config:
        # exclude columns with special treatment
        special_cols = config.get("onehot_cols", []) + config.get("keep_as_string", [])
        target_col = config.get("target", "")
        
        cat_cols = [col for col in config["categorical_cols"] 
                   if col in df.columns and 
                   col != target_col and
                   col not in special_cols]
        
        if cat_cols:
            # use label encoding by default for these columns
            encoder = LabelEncoder()
            for col in cat_cols:
                df[col] = encoder.fit_transform(df[col])
    
    return df

def scale_numerical(df, config):
    #standardization of numerical features (no changes)
    if "numerical_cols" in config:
        num_cols = [col for col in config["numerical_cols"] if col in df.columns]
        if num_cols:
            scaler = StandardScaler()
            df[num_cols] = scaler.fit_transform(df[num_cols])
    return df
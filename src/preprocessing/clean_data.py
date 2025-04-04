def handle_missing_values(df, config):
    #Handle missing values according to data type:
    
    # numeric columns
    if "numerical_cols" in config:
        num_cols = [col for col in config["numerical_cols"] if col in df.columns]
        df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    
    # categorical columns
    if "categorical_cols" in config:
        cat_cols = [col for col in config["categorical_cols"] if col in df.columns]
        df[cat_cols] = df[cat_cols].fillna('UNKNOWN')
    
    return df
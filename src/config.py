DATASETS = {  
    # Dataset Iris
    "iris": {
        "path": "data/raw/iris_dataset.csv",
        "has_header": True,
        "target": "species",
        "keep_as_string": ["species"],  
        "numerical_cols": ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    },
    # Dataset Sentiment
    "sentiment": {
        "path": "data/raw/sentiment_dataset.csv",
        "has_header": True,
        "target": "Sentiment",
        "drop_cols": ["Unnamed: 0", "Timestamp", "User"],
        "categorical_cols": ["Sentiment", "Platform"],
        "numerical_cols": ["Retweets", "Likes"]
    },
    
    # Dataset Housing
    "housing": {
        "path": "data/raw/house_prediction_dataset.csv",
        "has_header": False,
        "space_delimited": True,
        "columns": ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"],
        "target": "MEDV",
        "numerical_cols": ["CRIM","ZN","INDUS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT"]
    },
    
    # Dataset Stocks
    "stocks": {
        "path": "data/raw/stock_prices_dataset.csv",
        "has_header": True,
        "target": "symbol",
        "keep_as_string": ["symbol"], 
        "numerical_cols": ["open", "high", "low", "volume", "close"]
    },
    
    # Dataset Churn (80% y 20%)
    "churn_80": {
        "path": "data/raw/churn-bigml-80.csv",  # churn-20.csv 
        "has_header": True,
        "target": "Churn",
        "onehot_cols": ["State"],
        "categorical_cols": ["State", "International plan", "Voice mail plan"],
        "numerical_cols": ["Account length", "Total day minutes", "Total day calls", 
                          "Total eve minutes", "Total night minutes", "Total intl minutes"]
    },
    
    "churn_20": {
        "path": "data/raw/churn-bigml-20.csv",  # churn-20.csv 
        "has_header": True,
        "target": "Churn",
        "onehot_cols": ["State"],
        "categorical_cols": ["State", "International plan", "Voice mail plan"],
        "numerical_cols": ["Account length", "Total day minutes", "Total day calls", 
                          "Total eve minutes", "Total night minutes", "Total intl minutes"]
    }
}
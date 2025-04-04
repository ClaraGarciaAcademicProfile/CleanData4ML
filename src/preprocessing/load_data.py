# load_data.py
import pandas as pd
import re
from src.config import DATASETS

def load_dataset(name):
    # load any dataset according to its config
    config = DATASETS[name]
    
    # for files with multiple spaces as separators
    if config.get("space_delimited", False):
        with open(config["path"], 'r') as f:
            lines = f.readlines()
        
        # process each line: split by multiple spaces and clean
        data = []
        for line in lines:
            # remove leading/trailing spaces and split by multiple spaces
            cleaned = re.sub(r'\s+', ' ', line.strip()).split(' ')
            data.append([float(x) for x in cleaned if x])
        
        # create df
        df = pd.DataFrame(data, columns=config["columns"])
        
    # standard load for CSV
    elif config["has_header"]:
        df = pd.read_csv(config["path"])
    else:
        df = pd.read_csv(config["path"], header=None, names=config["columns"])
    
    # remove unnecessary columns (if they exist)
    if "drop_cols" in config:
        df = df.drop(columns=[col for col in config["drop_cols"] if col in df.columns])
    
    return df
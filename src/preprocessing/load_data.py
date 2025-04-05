import pandas as pd
import re
from src.config import DATASETS

def load_dataset(name): # load any dataset according to its config
    config = DATASETS[name]
    
    if config.get("space_delimited", False):  # for files with multiple spaces as separators
        with open(config["path"], 'r') as f:
            lines = f.readlines()
        
        data = []  # process each line: split by multiple spaces and clean
        for line in lines:
            cleaned = re.sub(r'\s+', ' ', line.strip()).split(' ') # remove leading/trailing spaces
            data.append([float(x) for x in cleaned if x])
        
        # create df
        df = pd.DataFrame(data, columns=config["columns"])
        
    elif config["has_header"]:  # standard load for CSV
        df = pd.read_csv(config["path"])
    else:
        df = pd.read_csv(config["path"], header=None, names=config["columns"])
    
    if "drop_cols" in config: # remove unnecessary columns (if they exist)
        df = df.drop(columns=[col for col in config["drop_cols"] if col in df.columns])
    
    return df

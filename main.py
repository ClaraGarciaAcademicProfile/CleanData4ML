from src.preprocessing.load_data import load_dataset
from src.preprocessing.clean_data import handle_missing_values
from src.preprocessing.transform import encode_target, encode_categorical, scale_numerical, one_hot_encode
from src.preprocessing.split_data import split_and_save
from src.config import DATASETS

def process_dataset(name):
    #complete pipeline for a dataset
    print(f"\nProcessing: {name}")
    config = DATASETS[name]
    
    try:
        # 1.- load data
        df = load_dataset(name)
        
        # 2.- cleaning
        df = handle_missing_values(df, config)
        
        # 3.- transformations
        df = one_hot_encode(df, config)  
        df = encode_target(df, config)
        df = encode_categorical(df, config)
        df = scale_numerical(df, config)
        
        # 4.- split and save
        split_and_save(df, config, name)
        
        return True
    
    except Exception as e:
        print(f"Error processing {name}: {str(e)}")
        return False

if __name__ == "__main__":
    # Process all datasets
    for dataset_name in DATASETS.keys():
        process_dataset(dataset_name)
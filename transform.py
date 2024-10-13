import os
import pandas as pd
import json


def load_csv(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        df = pd.json_normalize(data)  
        return df
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None


def save_to_excel(data, filename="video_details.xlsx"):
    try:
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        
        file_path = os.path.join(script_dir, filename)
        
        
        data.to_excel(file_path, index=False, engine='openpyxl')  
        print(f"Data has been saved to {file_path}")
    except Exception as e:
        print(f"Error saving to Excel: {e}")


def auto_process_file():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    
    csv_file = os.path.join(script_dir, "video_details.csv")
    json_file = os.path.join(script_dir, "video_details.json")

    if os.path.exists(csv_file):
        print(f"Found CSV file: {csv_file}")
        data = load_csv(csv_file)
        if data is not None:
            save_to_excel(data)
    elif os.path.exists(json_file):
        print(f"Found JSON file: {json_file}")
        data = load_json(json_file)
        if data is not None:
            save_to_excel(data)
    else:
        print("No CSV or JSON file found in the current directory.")
        return


if __name__ == "__main__":
    auto_process_file()

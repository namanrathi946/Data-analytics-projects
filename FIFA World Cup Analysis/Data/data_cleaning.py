# data_cleaning.py
# This script will handle the data cleaning and preprocessing steps for the FIFA World Cup dataset.

import pandas as pd

def clean_world_cup_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Remove any rows with missing values
    df.dropna(inplace=True)

    # Convert relevant columns to appropriate data types
    df['Year'] = df['Year'].astype(int)
    
    # Example cleaning: remove unnecessary columns (if any)
    # df.drop(columns=['Unnecessary_Column'], inplace=True)

    # Save the cleaned dataset to a new CSV file
    df.to_csv('data/cleaned_world_cup_data.csv', index=False)
    
    return df

if __name__ == "__main__":
    # Specify the path to the raw dataset
    file_path = 'data/world_cup_data.csv'
    
    # Clean the dataset
    cleaned_df = clean_world_cup_data(file_path)
    print("Data cleaning complete. Cleaned data saved to 'data/cleaned_world_cup_data.csv'")

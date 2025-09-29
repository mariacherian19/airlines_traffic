import pandas as pd
import numpy as np

class DataPreProcessor:
    """
    class DataPreProcessor handles preprocessing tasks including handling missing values, removing duplicates,
    converting columns to the correct format, and adding additional time-based features which could make easy data analysis.
    """
    def __init__(self, dataframe):
        
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()

    def convert_date_columns(self):
        """
        Convert 'Activity Period' column to datetime format and extract year and month.
        """
        # Converting 'Activity Period' to datetime, handling invalid date entries by coercing them
        self.df['Activity Period'] = pd.to_datetime(self.df['Activity Period'], errors='coerce')
        
        # Drop rows where the 'Activity Period' could not be converted to a valid date
        self.df.dropna(subset=['Activity Period'], inplace=True)
        
        # Extract year and month from the 'Activity Period' column
        self.df['Year'] = self.df['Activity Period'].dt.year
        self.df['Month'] = self.df['Activity Period'].dt.month
        
        return self.df

    def handle_missing_values(self):
        """
        Handle missing values by filling with  the previous valid values.
        """
        self.df.fillna(method='ffill', inplace=True)
        return self.df

    def remove_duplicates(self):
        """
        Remove duplicate rows.
        """
        self.df.drop_duplicates(inplace=True)
        return self.df

    def add_additional_features(self):
        """
        Add features 'Year_Num' and 'Month_Name' .
        """
        # Create 'Year_Num' column for easier numeric analysis
        self.df['Year_Num'] = self.df['Activity Period'].dt.year
        
        # Create 'Month_Name' column to represent the month name
        self.df['Month_Name'] = self.df['Activity Period'].dt.month_name()
        
        return self.df

    def preprocess(self):
        """
        Here performing all preprocessing steps together: date conversion, handle missing values, remove duplicates, and add new features.
        """
        self.df = self.convert_date_columns()
        self.df = self.handle_missing_values()
        self.df = self.remove_duplicates()
        self.df = self.add_additional_features()
        return self.df


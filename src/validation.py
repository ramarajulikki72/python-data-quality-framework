"""
Validation Module

This module contains reusable functions for validating
data quality in ETL pipelines.
"""

import pandas as pd


def check_null_values(df: pd.DataFrame):
    """
    Returns the number of null values in each column.
    """

    return df.isnull().sum()


def check_duplicate_records(df: pd.DataFrame):
    """
    Returns the number of duplicate rows.
    """

    return df.duplicated().sum()

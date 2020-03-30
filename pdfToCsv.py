#!/usr/bin/env python
# coding: utf-8
import tabula


def performDataCleaning(inDataFrame):
    subset_df = inDataFrame

    # Make column headers generic
    subset_df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Split the merged column into exact two columns
    split_col_df = subset_df['C'].str.split(expand=True, n=1)

    # Rename split columns
    split_col_df.columns = ['C1', 'C2']

    # Append new split columns to original dataframe
    subset_df['C1'], subset_df['C2'] = split_col_df['C1'], split_col_df['C2']

    col_list = subset_df.columns.tolist()
    # Redefine the column headers for new dataframe (filtered)
    new_col_list = ['A', 'B', 'C1', 'C2', 'E', 'F', 'G']

    # Create New Dataframe with the selected new headers
    new_df = subset_df[new_col_list]

    # Rename the column names to the original values
    new_df.columns = ['Particulars', '2015', '2016', 'Particulars', '', '2015', '2016']

    # Return the new dataframe
    return new_df


def convertFile(source_file, target_file):
    # read file
    df = tabula.read_pdf(source_file, multiple_tables=False, stream=True, lattice=False,
                         pages='all')
    subset_df = df[0]

    # Performing Data Cleaning
    cleanDataframe = performDataCleaning(subset_df)

    # Saving the data into file
    cleanDataframe.to_csv(target_file, index=False)


if __name__ == '__main__':
    try:
        source_file = r".\source_files\BalSheet.pdf"
        target_file = r'.\output_files\BalSheet.csv'
        convertFile(source_file, target_file)
    except Exception as err:
        print(err.args)
    finally:
        pass
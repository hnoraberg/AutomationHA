import pandas as pd

def get_top_five(file_path, new_file_path):
    try:
        with open(file_path) as file:
            df = pd.read_csv(file_path, sep="\t")
            df_descending = df.sort_values(['Rating'], ascending=False)
            df_top_five = df_descending.head()
            top_five_csv = df_top_five.to_csv(new_file_path, sep='\t', index=False)
            return top_five_csv
    except Exception as e:
        print(e)
        return


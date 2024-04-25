import pandas as pd

# Read the CSV files
test_df = pd.read_csv("datasets/Politics/fakenewskaggle/test.csv")
train_df = pd.read_csv("datasets/Politics/fakenewskaggle/train.csv")

# Merge the dataframes
merged_df = pd.concat([test_df, train_df])

#remove id,title,author
merged_df = merged_df.drop(columns=['id', 'title', 'author'])

# Save the merged dataframe to a new CSV file
merged_df.to_csv("datasets/Politics/fakenewskaggle/combined.csv", index=False)
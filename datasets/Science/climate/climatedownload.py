# Import necessary libraries
from datasets import load_dataset
import pandas as pd

def import_dataset():
    # Load the dataset
    dataset = load_dataset("climate_fever")

    # Convert the train dataset to pandas DataFrame
    df = pd.DataFrame(dataset['test'])

    # Return the DataFrame
    return df
    
# Call the function
df = import_dataset()

#droping the rows with claim label 2
df = df[df.claim_label != 2]

#chang ethe claim albels 0 to 5
df['claim_label'] = df['claim_label'].replace(0, 5)

#chagne the claim label 3,1 to 0
df['claim_label'] = df['claim_label'].replace([1, 3], 0)

#change the claim label 5 to 1
df['claim_label'] = df['claim_label'].replace(5, 1)

# Display the first 5 rows of the DataFrame
print(df.head())

# save the dataframe to a csv file
df.to_csv('climate_fever.csv', index=False)

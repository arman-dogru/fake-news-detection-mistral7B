# Import necessary libraries
from datasets import load_dataset
import pandas as pd

def import_dataset():
    # Load the dataset
    dataset = load_dataset("liar")

    # Convert the train dataset to pandas DataFrame
    df = pd.DataFrame(dataset['test'])

    # Return the DataFrame
    return df
    
# Call the function
df = import_dataset()

#drop all except label and statement:id,label,statement,subject,speaker,job_title,state_info,party_affiliation,barely_true_counts,false_counts,half_true_counts,mostly_true_counts,pants_on_fire_counts,context
df = df.drop(columns=['id', 'subject', 'speaker', 'job_title', 'state_info', 'party_affiliation', 'barely_true_counts', 'false_counts', 'half_true_counts', 'mostly_true_counts', 'pants_on_fire_counts', 'context'])

# Display the first 5 rows of the DataFrame
print(df.head())

# save the dataframe to a csv file
df.to_csv('datasetsPolitics/liar/liar_train.csv', index=False)

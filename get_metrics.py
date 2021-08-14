import pandas as pd

def compare_accuracy(df):
    right_answers = 0
    for i in range(df.shape[0]):
        if df["y_actual"].iloc[i] == df["y_predicted"].iloc[i]:
            right_answers += 1
    
    return round((right_answers/df.shape[0])*100,2)

def merge_df(df1,df2):
    return df1.merge(df2, on="path")
    

df1 = pd.read_csv("dataset.csv")
df2 = pd.read_csv("dataset_predicted_updated.csv")


final_df = merge_df(df1, df2)
final_df.to_csv("combined_updated.csv", index=False)

print("Final Accuracy: ", compare_accuracy(final_df), "%")
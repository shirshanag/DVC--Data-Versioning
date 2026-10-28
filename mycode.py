import pandas as pd
import os
data={
    "Name":["Sam","Alice","Bob","Mukesh"],
    "Age":[27,23,34,45],
    "Dept":["Sales","HR","Marketing","Operations"],
    "Designation":["Manager","Intern","Manager","Manager"]
}
df=pd.DataFrame(data=data)

# New data 1
new_row_1={"Name":"Maggie","Age":33,"Dept":"Sales","Designation":"Manager"}
df.loc[len(df.index)]=new_row_1

new_row_2={"Name":"Rubi","Age":23,"Dept":"SDE","Designation":"Intern"}
df.loc[len(df.index)]=new_row_2

data_dir='data'

os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file uploaded {file_path}")
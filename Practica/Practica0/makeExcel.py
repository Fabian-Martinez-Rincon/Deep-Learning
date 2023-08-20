import pandas as pd

df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  

print(df)

df.to_excel(pd.ExcelWriter("path_to_file.xlsx"))
with pd.ExcelWriter("path_to_file.xlsx") as writer:
    df.to_excel(writer)  
    

#Converts .asc file to .parquet
import pandas as pd
import numpy as np
data = np.loadtxt(r"C:\Users\chinm\Desktop\python_train\InnoCentive\Data\data3.asc") #Specify source of your .asc file
df = pd.DataFrame(data, columns = ['Lat','Lng','time','D','Intensity'])#Gvining column names
df.to_parquet('output.parquet')#O/P destination same as file txt2parq.py file location
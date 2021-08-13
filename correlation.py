from scipy.stats import pearsonr
import pandas as pd

df_assingment = pd.read_csv("210802_assignment_data_1_edit.csv", usecols=['time','insulation_resistance_1','insulation_resistance_2','insulation_resistance_3','insulation_resistance_4','insulation_resistance_5','irradiance_1','irradiance_2'])
#,'wspd','pres','coco'
df_wheather = pd.read_csv("exampledata.csv", usecols=['time','temp','dwpt','rhum','prcp','wdir'])


print(pearsonr(df_wheather['dwpt'],df_assingment['insulation_resistance_1']))

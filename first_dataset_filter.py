import pandas as pd

df_2013=pd.read_csv('Parking_Violations_Issued_-_Fiscal_Year_2014__August_2013___June_2014_.csv',low_memory=False)
print("letto il primo dataset")
df_2015=pd.read_csv('Parking_Violations_Issued_-_Fiscal_Year_2015.csv',low_memory=False)
print("letto il secondo dataset")

union1315=pd.concat([df_2013,df_2015],ignore_index=True)
print("Ho unito i primi 2 dataset")
df_2016=pd.read_csv('Parking_Violations_Issued_-_Fiscal_Year_2016.csv',low_memory=False)
print('letto il terzo dataset')
union1316=pd.concat([union1315,df_2016],ignore_index=True)
print('ho unito i primi 3 dataset')


union1316=union1316.drop(columns=['Latitude','Longitude','Community Board','Community Council ','BIN','BBL','NTA'])
print('Elimino le colonne in più')
df_2017=pd.read_csv('Parking_Violations_Issued_-_Fiscal_Year_2017.csv',low_memory=False)

print('letto il quarto dataset')
union1317=pd.concat([union1316,df_2017],ignore_index=True)

print('Ho unito tutti i dataset ')
union1317['Issue Date']=pd.to_datetime(union1317['Issue Date'].str.strip())
indexDateover=union1317[union1317['Issue Date']> '2017-12-31'].index
indexDateunder=union1317[union1317['Issue Date']<'2013'].index
union1317.drop(indexDateover, inplace=True, axis=0)
union1317.drop(indexDateunder, inplace=True, axis=0)
print("Dataset ripuliti")

union1317.to_csv('/Users/Corrado/Downloads/datasetmulteny/nyc_tickets_13_17.csv', index=False, header=True)

print("dataset salvato")

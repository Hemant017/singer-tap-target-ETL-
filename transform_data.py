#Transform data : Transform the timestamp from UTC to IST

import pandas as pd

#String to datetime
def convdf(df,cols):
    for col in cols:
        df[col]=pd.to_datetime(df[col])
    return df
        

#Timezoneconvert
def convertTimeZone(dataAttr):
    dataAttr = pd.to_datetime(dataAttr).dt.tz_convert('Asia/Kolkata') 
    return dataAttr

#convert to string
def convdfStr(df_new,cols):
    for col in cols:
        df_new[col]=df_new[col].astype(str)
    return df_new

#pandas function to tranform the date
def transform_data(data):
    df = pd.read_json(data)
    df.drop(['date','astronomicalDawn','astronomicalDusk','civilDawn','civilDusk','goldenHourEveningStart','goldenHourMorningEnd','nadir','nauticalDawn','nauticalDusk','solarNoon'],axis=1, inplace=True)
    cols=['sunriseStart', 'sunriseEnd', 'sunsetStart', 'sunsetEnd']
    df=convdf(df,cols)
    df_new = df.apply(lambda row:convertTimeZone(row))
    df_new=convdfStr(df_new,cols)
    data_dict = df_new.to_dict('records')
    return data_dict
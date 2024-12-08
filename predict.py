import numpy as np 
import pandas as pd 

class MyModel:

    def removeOutliers(self,list):
        list= sorted(list)
        n = len(list)
        i1 = 0.25 * (n - 1)
        i3 = 0.75 * (n - 1)
        q1 = list[int(np.floor(i1))] + (i1 - np.floor(i1)) * (list[int(np.ceil(i1))] - list[int(np.floor(i1))])
        q3 = list[int(np.floor(i3))] + (i3 - np.floor(i3)) * (list[int(np.ceil(i3))] - list[int(np.floor(i3))])
        IQR=q3-q1
        filteredList = [x for x in list if q1 - 1.5 * IQR <= x <= q3 + 1.5 * IQR]
        return filteredList   

    def predictMedals(self,list):
        x=np.arange(1, len(list)+1)
        y=np.array(list)
        a,b=np.polyfit(x, y, deg=1)
        pMedals=a*(len(list)+1)+b
        return round(pMedals)
        
    def getMedals(self,file_path, country_name):
        df = pd.read_excel(file_path)
        df.fillna(0)
        country_data = df[df['Country'] == country_name]
        if not country_data.empty:
            medals = country_data.iloc[0, 1:].tolist()
        else:
            medals = []
        return self.removeOutliers(medals)
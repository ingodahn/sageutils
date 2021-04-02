import pandas as pd

def dateString(x):
    s=str(x)
    return s[6:8]+"."+s[4:6]+"."+s[0:4]

def invert(L):
    return [(p[1],p[0]) for p in L]

class flight:
    '''Class describing one flight of a weather balloon'''
    def __init__(self,data):
        self.__dataV=data
        print("Ready to analyze",len(self.__dataV),"data points from one flight on",dateString(self.__dataV[0][1])+".")
    def __col(self,X):
        if X=='height':
            return 4
        if X=='temperature':
            return 11
        if X=='pressure':
            return 3
        print('Unknown data type',X)
    def dataPoints(self,X,Y):
        return [(self.__dataV[n][self.__col(X)],self.__dataV[n][self.__col(Y)]) for n in range(0,len(self.__dataV))]

class station:
    '''Weather station class'''
    def __init__(self):
        self.__id='02385'
        self.name='Idar-Oberstein'
        self.height=376
        self.coords='49.6927°N 7.3264°E'
        self.__defaultFlightUrl='https://github.com/ingodahn/sageutils/blob/master/sampleIO02385.zip'

    def description(self):
        return 'Weather station '+self.name+' is situated at '+self.coords+' at a height of '+str(self.height)+' m.'
    def __recentFlightsUrl(self):
        return 'https://opendata.dwd.de/climate_environment/CDC/observations_germany/radiosondes/low_resolution/recent/punktwerte_aero_'+self.__id+'_akt.zip'
    def __dataCorrect(self,p):
        if -999 in p:
            return False
        return True
    def getFlight(self,id='default'):
        if id == 'default':
            dataRaw=pd.read_csv(self.__defaultFlightUrl,';').values
        else:
            url=self.__recentFlightsUrl()
            print("Loading data from German Weather Service. Please, be patient.")
            dataVRemote=pd.read_csv(url,';').values
            flights=len(set([d[1] for d in dataVRemote]))
            print(len(dataVRemote),"data points from",flights,"flights between",dateString(dataVRemote[0][1]),"and",dateString(dataVRemote[len(dataVRemote)-1][1])," loaded.")
            if id == 'random':
                date=dataVRemote[ZZ.random_element(0,len(dataVRemote)-1)][1]
            else:
                date=id
            dataRaw=[p for p in dataVRemote if p[1]==date]
        return flight([p for p in dataRaw if self.__dataCorrect(p)])

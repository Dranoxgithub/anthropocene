#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 01:48:08 2020

@author: wzy
"""

import numpy as np
import pandas as pd
import json


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import ElasticNet

#%%
def initialize():
    filename = 'Dataset.csv'
    datall = pd.read_csv(filename).dropna()
    datadd = datall.iloc[0:0]
    
    for i in range(len(datall)):
        list_county = datall.iloc[i,0].split(", ")
        for county in list_county:
            temp = datall.iloc[i,1:]
            temp['incident_county'] = county
            datadd=datadd.append(temp)
    datadd=datadd.reset_index()
    datadd=datadd.drop(["index"],axis=1)
    datadd=datadd.drop(506, axis=0)
    datadd=datadd.drop(1125, axis=0)
    datadd=datadd.drop(1130, axis=0)
    datadd=datadd.drop(1131, axis=0)
    datadd=datadd.reset_index()
    datadd=datadd.drop(["index"],axis=1)
    return datadd

#%%
def makecountylistdict():
    counties_file = 'counties.csv'
    countydat = pd.read_csv(counties_file)
    countyname_list = countydat['County'].values.tolist()
    county_list=[[],[]]
    dict_county_pop = {}
    for i in range(len(countyname_list)):
        county_list[0].append(countyname_list[i].replace(" County",""))
        county_list[1].append(int(countydat['Population'].iloc[i].replace(",","")))
        dict_county_pop[county_list[0][i]]=county_list[1][i]
    return county_list,dict_county_pop

def dropbadloc(datadd,county_list):
    locations = datadd.iloc[:,0].astype(str)
    for df in locations:
        if not(df in county_list[0]):
            datadd.drop(datadd[datadd.incident_county==df].index, inplace=True)
    datadd=datadd.reset_index()
    datadd=datadd.drop(["index"],axis=1)
    return datadd

#%%
datadd = initialize()
county_list,dict_county_pop = makecountylistdict()
datadd = dropbadloc(datadd, county_list)
def recstatdict(county_list):
    with open('stationwfields.json') as f:
        stations_to_longlat = json.load(f)
    stat_dict={}
    for dicts in stations_to_longlat:
        key = dicts['STN']
        infol=[dicts['county'],dicts['longlang']]
        if not dicts['county'] in county_list[0]:
            continue
        stat_dict[key]=infol
    return stat_dict

#%%
class Station:
    def __init__(self, name, lang, long):
        self.name = name
        self.lang = lang
        self.long = long
        self.distance = 0
    def set_distance(self,distance):
        self.distance = distance

def makestatliststat_dict(stat_dict):
    stlist=[]
    for stations in stat_dict:
        st = Station(stations, stat_dict[stations][1][0],stat_dict[stations][1][1])
        stlist.append(st)
    return stlist

def searchstation(stlist, lang, long):
    dislist=[]
    for stations in stlist:
        distance = (lang-stations.lang)**2+(long-stations.long)**2
        stations.set_distance(distance)
        dislist.append(stations)
    dislist.sort(key=lambda stations: stations.distance)
    return dislist

def getdat(dislist, time, dict_weather):
    dat = np.zeros(7)
    for i in range(7):
        for stations in dislist:
            starow = dict_weather[stations.name][weatherdat['Date']==time]
            #print(starow)
            if (not np.isnan(starow.iloc[0,i+2])):
                dat[i]=starow.iloc[0,i+2]
                break
    dat=dat.reshape(1,7)
    rec = pd.DataFrame(dat, columns = ["Precip","Air_max","Air_min", "Wind_dir", "speed",\
                                  "RH_max", "RH_min"])
    return rec


#%%
stat_dict = recstatdict(county_list)
stlist = makestatliststat_dict(stat_dict)
filename = "out.csv"
weatherdat = pd.read_csv(filename)
dict_weather={}
for i in range(238):
    dict_weather[weatherdat.iloc[2556*i,0]] = weatherdat.iloc[2556*i:2556*(i+1),:]
df = pd.DataFrame(columns = ["Precip","Air_max","Air_min", "Wind_dir", "speed",\
                                  "RH_max", "RH_min"])
"""
for i in range(0,len(datadd)):
    lang = float(datadd.iloc[i,2])
    long = float(datadd.iloc[i,3])
    dislist = searchstation(stlist,lang,long)
    rec = getdat(dislist,datadd.iloc[i,4],dict_weather)
    df = df.append(rec)
    print(rec)
df=df.reset_index()
df=df.drop(["index"],axis=1)
datadd=datadd.reset_index()
datadd=datadd.drop(["index"],axis=1)
datadd[["Precip","Air_max","Air_min", "Wind_dir", "speed","RH_max", "RH_min"]]=df
"""
        
#%%
for i in range(len(datadd['incident_dateonly_created'])):
    i_value=int(datadd['incident_dateonly_created'][i].split("/")[0])
    datadd['incident_dateonly_created'][i]=i_value
poplist=[]
for counties in datadd['incident_county']:
    poplist.append(dict_county_pop[counties])
datadd['Population']=poplist
locenc = LabelEncoder()
locenc.fit(datadd.iloc[:,0].astype(str))
loc_encoded = locenc.transform(datadd.iloc[:,0].astype(str))
datadd['incident_county'] = loc_encoded
acres_target = datadd['incident_acres_burned']
independent=datadd.drop(['incident_acres_burned'],axis=1)

def writefile(data,filename):
    print('Writing file: '+filename)
    data.to_csv(filename+'.csv',index=False)

writefile(independent, 'independent')

#%%
pca1 = PCA()
pcatransformer=StandardScaler().fit_transform(independent)
independent_p = pca1.fit_transform(pcatransformer)
explained_variance1 = pca1.explained_variance_ratio_
independent_p=independent_p[0:8]

acres_std = StandardScaler().fit_transform(np.array(acres_target).reshape(-1,1))

writefile(pd.DataFrame(independent_p), 'independent_p')
writefile(acres_target, 'acres_target')
params = np.zeros(91)
kf = KFold(n_splits=5)
for train_index, test_index in kf.split(independent):
    train_features, test_features =independent.iloc[train_index],independent.iloc[test_index]
    train_labels, test_labels = acres_target[train_index], acres_target[test_index]
    poly = PolynomialFeatures(degree = 2)
    X_poly = poly.fit_transform(train_features)
    poly_l = ElasticNet()
    poly_l.fit(X_poly,train_labels)
    test_trans =  poly.fit_transform(test_features)
    predictions=poly_l.predict(test_trans)
    params+=poly_l.coef_
    print(mean_squared_error(test_labels, predictions))
    

#%%
from sklearn.ensemble import RandomForestRegressor
train_features, test_features, train_labels, test_labels = \
train_test_split(pcatransformer, acres_std, test_size = 0.25, random_state = 0)
rf = RandomForestRegressor(n_estimators = 500, random_state = 0)
rf.fit(train_features, train_labels)
ped=rf.predict(test_features)
mean_squared_error(test_labels, ped)




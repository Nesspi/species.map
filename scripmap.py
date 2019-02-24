# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:44:29 2019

@author: rocks
"""

import pandas as pd
import folium

specie=pd.read_csv('abies_pinsapo.csv',sep='\t')

specie2=pd.read_csv('agrostis_nevadensis.csv',sep='\t')
frames = [specie,specie2]
species = pd.concat(frames)
species=species.dropna(subset=['decimalLongitude'])

species=species.dropna(subset=['decimalLatitude'])

specie.map=folium.Map(location=[40,-4], zoom_start=6)

for indice, ocurrence in species.iterrows():
    latitud=ocurrence['decimalLatitude']
    longitud=ocurrence['decimalLongitude']
    
    if not pd.isnull(latitud):
        marca1=folium.Marker(
                location=[latitud,longitud],
                popup='Abies pinsapo',
                icon=folium.Icon(color='green', icon='info-sign')
                )
        marca2=folium.Marker(
                location=[latitud,longitud],
                popup='Agrostis nevadensis',
                icon=folium.Icon(color='blue', icon='info-sign')
                )
        if ocurrence['species']== 'Abies pinsapo':
            marca1.add_to(specie.map)
        elif ocurrence ['species'] == 'Agrostis nevadensis':
            marca2.add_to(specie.map) 

specie.map.save('mapa.html')  
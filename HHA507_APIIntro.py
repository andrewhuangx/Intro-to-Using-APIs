# -*- coding: utf-8 -*-
"""
@author: andre
"""
## Import the request, pandas and json packages 

import pandas as pd
import requests


## GET request to pull data from API for lyrics to Coldplay's Viva la Vida

response1 = requests.get('https://api.lyrics.ovh/v1/Coldplay/Viva la Vida')

## Printing status code to display what happened

print(response1.status_code)

## Retrieving the data in a json format

response1.json()

## Was successful in finding and displaying the lyrics to Viva la Vida by Coldplay, a song in English

## GET request to pull data from API for lyrics to imagine dragon's whatever it takes

response2 = requests.get('https://api.lyrics.ovh/v1/imagine dragons/whatever it takes')

## Printing status code to display what happened

print(response2.status_code)

## Retrieving the data in a json format

response2.json()

## Was successful in finding and displaying the lyrics to whatever it takes by imagine dragons, a song in English 

## GET request to pull data from API for lyrics to Kana-Boon's Silhouette

response3 = requests.get('https://api.lyrics.ovh/v1/KANA BOON/SILHOUETTE')

## Printing status code to display what happened

print(response3.status_code)

## Retrieving the data in a json format

response3.json()

## Was successful in finding and displaying the lyrics to Silhouette by Kana-Boon, a song in Japanese

## GET request to pull data from API for lyrics to Jay Chou's An Jing

response4 = requests.get('https://api.lyrics.ovh/v1/Jay Chou/An Jing')

## Printing status code to display what happened

print(response4.status_code)

## Retrieving the data in a json format

response4.json()

## Was successful in finding and displaying the lyrics to An Jing by Jay Chou, a song in Chinese

## GET request to pull data from API for lyrics to Black Pink's Boombayah

response5 = requests.get('https://api.lyrics.ovh/v1/Black Pink/BooMBaYah')

## Printing status code to display what happened

print(response5.status_code)

## Retrieving the data in a json format

response5.json()

## Was successful in finding and displaying the lyrics to Boombayah by Black Pink, a song in Korean

## GET request to pull data from API for lyrics to Luis Fonsi's Despacito

response6 = requests.get('https://api.lyrics.ovh/v1/Luis Fonsi/Despacito')

## Printing status code to display what happened

print(response6.status_code)

## Retrieving the data in a json format

response6.json()

## Was successful in finding and displaying the lyrics to Despacito by Luis Fonsi, a song in Spanish
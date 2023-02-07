from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt
from tabulate import tabulate
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from PIL import Image
import streamlit as st
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Adicionar título e subtítulo
st.write("""
# Análise do cenário competitivo de League of Legends
## Giuliano Andia & Lucas Noale
""")
           
#img = Image.open('fgv.png')

#st.sidebar.image(img)            
###Base Geral (df)
        
df = pd.read_excel("/Users/lunoa/Python Avançado/Streamlit/base_geral.xlsx")
               
df[df.columns[5:]] = df[df.columns[5:]].apply(lambda x: x.replace({'%':'', 'k':''}, regex=True))


df[df.columns[4:]] = df[df.columns[4:]].apply(pd.to_numeric)

df['dmgpergold'] = df['damage']/df['gold']

df["teamdamage"] = df.groupby("team")["damage"].transform('sum')


df["damageshare"] = df["damage"]/ df["teamdamage"]*100

df[df.columns[4:]] = df[df.columns[4:]].apply(pd.to_numeric)

###

##Definindo a base para cada liga##

LCK = df.loc[(df.liga == "LCK")]
LCK = LCK[["team","name","lane","kda", "cspmin", "goldpmin", "damagepmin", "dmgpergold", "damageshare"]]
LCK = LCK.rename(columns={"name" : "Name", "lane" : "Lane", "cspmin" : "CS por Min", "goldpmin" : "Gold por Min", "damagepmin" : "Dano por Min", "dmgpergold" : "Dano por Gold", "damageshare" : "% de Dano", "kda" : "KDA"})


LPL = df.loc[(df.liga == "LPL")]
LPL = LPL[["team","name","lane","kda", "cspmin", "goldpmin", "damagepmin", "dmgpergold", "damageshare"]]
LPL = LPL.rename(columns={"name" : "Name", "lane" : "Lane", "cspmin" : "CS por Min", "goldpmin" : "Gold por Min", "damagepmin" : "Dano por Min", "dmgpergold" : "Dano por Gold", "damageshare" : "% de Dano", "kda" : "KDA"})

CBLOL = df.loc[(df.liga == "CBLOL")]
CBLOL = CBLOL[["team","name","lane","kda", "cspmin", "goldpmin", "damagepmin", "dmgpergold", "damageshare"]]
CBLOL = CBLOL.rename(columns={"name" : "Name", "lane" : "Lane", "cspmin" : "CS por Min", "goldpmin" : "Gold por Min", "damagepmin" : "Dano por Min", "dmgpergold" : "Dano por Gold", "damageshare" : "% de Dano", "kda" : "KDA"})

LEC = df.loc[(df.liga == "LEC")]
LEC = LEC[["team","name","lane","kda", "cspmin", "goldpmin", "damagepmin", "dmgpergold", "damageshare"]]
LEC = LEC.rename(columns={"name" : "Name", "lane" : "Lane", "cspmin" : "CS por Min", "goldpmin" : "Gold por Min", "damagepmin" : "Dano por Min", "dmgpergold" : "Dano por Gold", "damageshare" : "% de Dano", "kda" : "KDA"})

LCS = df.loc[(df.liga == "LCS")]
LCS = LCS[["team","name","lane","kda", "cspmin", "goldpmin", "damagepmin", "dmgpergold", "damageshare"]]
LCS = LCS.rename(columns={"name" : "Name", "lane" : "Lane", "cspmin" : "CS por Min", "goldpmin" : "Gold por Min", "damagepmin" : "Dano por Min", "dmgpergold" : "Dano por Gold", "damageshare" : "% de Dano", "kda" : "KDA"})


##Definindo a base para cada Time##

#LCK#
teams = ['Hanwha Life Esports', 'KT Rolster', 'DRX', 'T1', 'Nongshim RedForce',
         'Kwangdong Freecs', 'Liiv SANDBOX', 'DWG KIA', 'Gen.G', 'Fredit BRION']

for team in teams:
    team_df = LCK.loc[(LCK.team == team)].drop_duplicates()
    team_df = team_df.reset_index()
    team_df = team_df[team_df.columns[1:]]
    team_df = team_df[["Name","Lane","KDA", "CS por Min", "Gold por Min", "Dano por Min", "Dano por Gold", "% de Dano"]]
    
    team_name = team.replace(" ", "_") # replace spaces with underscores
    team_name = team_name.replace("'", "") # remove any single quotes
    team_name = team_name.replace(".", "") # remove any single quotes
    
    globals()[team_name] = team_df # create a global variable with the team name

##Base para cada lane##
st.set_option('deprecation.showPyplotGlobalUse', False)

list_of_dfs = list()
leagues = ["LPL", "LCK", "CBLOL","LCS","LEC"]
roles = ["Top", 'Jg', "Mid", "Adc", "Sup"]

for x in leagues:
    for y in roles:
        a = df.loc[(df.liga == x) & (df.lane == y)]
        list_of_dfs.append(a)

LPL_Top = list_of_dfs[0].reset_index()
LPL_Jg = list_of_dfs[1].reset_index()
LPL_Mid = list_of_dfs[2].reset_index()
LPL_Adc = list_of_dfs[3].reset_index()
LPL_Sup = list_of_dfs[4].reset_index()
LCK_Top = list_of_dfs[5].reset_index()
LCK_Jg = list_of_dfs[6].reset_index()
LCK_Mid = list_of_dfs[7].reset_index()
LCK_Adc = list_of_dfs[8].reset_index()
LCK_Sup = list_of_dfs[9].reset_index()
LEC_top = list_of_dfs[9].reset_index()
CBLOL_Top = list_of_dfs[10].reset_index()
CBLOL_Jg = list_of_dfs[11].reset_index()
CBLOL_Mid = list_of_dfs[12].reset_index()
CBLOL_Adc = list_of_dfs[13].reset_index()
CBLOL_Sup = list_of_dfs[14].reset_index()
LCS_Top = list_of_dfs[15].reset_index()
LCS_Jg = list_of_dfs[16].reset_index()
LCS_Mid = list_of_dfs[17].reset_index()
LCS_Adc = list_of_dfs[18].reset_index()
LCS_Sup = list_of_dfs[19].reset_index()
LEC_Top = list_of_dfs[20].reset_index()
LEC_Jg = list_of_dfs[21].reset_index()
LEC_Mid = list_of_dfs[22].reset_index()
LEC_Adc = list_of_dfs[23].reset_index()
LEC_Sup = list_of_dfs[24].reset_index()
    
#LPL#
teams = ['Invictus Gaming',
 'Royal Never Give Up',
 'Oh My God',
 'JD Gaming',
 'Bilibili Gaming',
 'Rare Atom',
 'Weibo Gaming',
 'EDward Gaming',
 'Victory Five',
 "Anyone's Legend",
 'Top Esports',
 'Ultra Prime',
 'LGD Gaming',
 'ThunderTalk Gaming',
 'LNG Esports',
 'Team WE',
 'FunPlus Phoenix']

for team in teams:
    team_df = LPL.loc[(LPL.team == team)].drop_duplicates()
    team_df = team_df.reset_index()
    team_df = team_df[team_df.columns[1:]]
    team_df = team_df[["Name","Lane","KDA", "CS por Min", "Gold por Min", "Dano por Min", "Dano por Gold", "% de Dano"]]
    
    team_name = team.replace(" ", "_") # replace spaces with underscores
    team_name = team_name.replace("'", "") # remove any single quotes
    team_name = team_name.replace(".", "") # remove any single quotes
    
    globals()[team_name] = team_df # create a global variable with the team name
    
#CBLOL#
teams = ['FURIA',
 'LOUD',
 'PaiN Gaming',
 'KaBuM! Esports',
 'Miners',
 'Liberty',
 'Flamengo Los Grandes',
 'INTZ',
 'Rensga Esports',
 'RED Canids']

for team in teams:
    team_df = CBLOL.loc[(CBLOL.team == team)].drop_duplicates()
    team_df = team_df.reset_index()
    team_df = team_df[team_df.columns[1:]]
    team_df = team_df[["Name","Lane","KDA", "CS por Min", "Gold por Min", "Dano por Min", "Dano por Gold", "% de Dano"]]
    
    team_name = team.replace(" ", "_") # replace spaces with underscores
    team_name = team_name.replace("'", "") # remove any single quotes
    team_name = team_name.replace(".", "") # remove any single quotes
    team_name = team_name.replace("!", "") # remove any single quotes
    
    globals()[team_name] = team_df # create a global variable with the team name    
    
#LEC#
teams = ['Misfits Gaming',
 'Excel Esports',
 'Fnatic',
 'Team Vitality',
 'MAD Lions',
 'G2 Esports',
 'Rogue (European Team)',
 'SK Gaming',
 'Astralis',
 'Team BDS']

for team in teams:
    team_df = LEC.loc[(LEC.team == team)].drop_duplicates()
    team_df = team_df.reset_index()
    team_df = team_df[team_df.columns[1:]]
    team_df = team_df[["Name","Lane","KDA", "CS por Min", "Gold por Min", "Dano por Min", "Dano por Gold", "% de Dano"]]
    
    team_name = team.replace(" ", "_") # replace spaces with underscores
    team_name = team_name.replace("'", "") # remove any single quotes
    team_name = team_name.replace(".", "") # remove any single quotes
    team_name = team_name.replace("(", "") # remove any single quotes
    team_name = team_name.replace(")", "") # remove any single quotes
    
    globals()[team_name] = team_df # create a global variable with the team name
    
#LCS#
teams = ['Cloud9',
 'FlyQuest',
 'Evil Geniuses.NA',
 '100 Thieves',
 'Team Liquid',
 'Counter Logic Gaming',
 'Golden Guardians',
 'Immortals',
 'Dignitas',
 'TSM']

for team in teams:
    team_df = LCS.loc[(LCS.team == team)].drop_duplicates()
    team_df = team_df.reset_index()
    team_df = team_df[team_df.columns[1:]]
    team_df = team_df[["Name","Lane","KDA", "CS por Min", "Gold por Min", "Dano por Min", "Dano por Gold", "% de Dano"]]
    
    team_name = team.replace(" ", "_") # replace spaces with underscores
    team_name = team_name.replace("'", "") # remove any single quotes
    team_name = team_name.replace("1", "") # remove any single quotes
    team_name = team_name.replace("0", "") # remove any single quotes
    team_name = team_name.replace(".", "") # remove any single quotes
    
    globals()[team_name] = team_df # create a global variable with the team name
    
##TABELAS##

list_of_cats = list()
cats = ["kda", "cspmin", "goldpmin", "damagepmin", "dmgpergold", "damageshare"]
        
for x in cats:
        b = df.sort_values(x, ascending = False).head(25)
        list_of_cats.append(b)
        
df_kda = list_of_cats[0].reset_index()
df_cspmin = list_of_cats[1].reset_index()
df_goldpmin = list_of_cats[2].reset_index()
df_damagepmin = list_of_cats[3].reset_index()
df_dmgpergold = list_of_cats[4].reset_index()
df_damageshare = list_of_cats[5].reset_index()

df_kda = df_kda[["team","name","lane","liga","kda"]]
df_cspmin = df_cspmin[["team","name","lane","liga","cspmin"]]
df_goldpmin = df_goldpmin[["team","name","lane","liga","goldpmin"]]
df_damagepmin = df_damagepmin[["team","name","lane","liga","damagepmin"]]
df_dmgpergold = df_dmgpergold[["team","name","lane","liga","dmgpergold"]]
df_damageshare = df_damageshare[["team","name","lane","liga","damageshare"]]

df_kda_lane =pd.DataFrame(data= df_kda["lane"].astype("category").value_counts(dropna = False))
df_kda_lane.reset_index(inplace=True)
df_kda_lane.rename(columns={"lane": "KDA", "index":"Role"}, inplace=True)

df_kda_liga =pd.DataFrame(data= df_kda["liga"].astype("category").value_counts(dropna = False))
df_kda_liga.reset_index(inplace=True)
df_kda_liga.rename(columns={"liga": "KDA", "index":"Liga"}, inplace=True)

df_cspmin_lane =pd.DataFrame(data= df_cspmin["lane"].astype("category").value_counts(dropna = False))
df_cspmin_lane.reset_index(inplace=True)
df_cspmin_lane.rename(columns={"lane": "CS por Minuto", "index":"Role"}, inplace=True)

df_cspmin_liga =pd.DataFrame(data= df_cspmin["liga"].astype("category").value_counts(dropna = False))
df_cspmin_liga.reset_index(inplace=True)
df_cspmin_liga.rename(columns={"liga": "CS por Minuto", "index":"Liga"}, inplace=True)

df_goldpmin_lane =pd.DataFrame(data= df_goldpmin["lane"].astype("category").value_counts(dropna = False))
df_goldpmin_lane.reset_index(inplace=True)
df_goldpmin_lane.rename(columns={"lane": "Gold por Minuto", "index":"Role"}, inplace=True)

df_goldpmin_liga =pd.DataFrame(data= df_goldpmin["liga"].astype("category").value_counts(dropna = False))
df_goldpmin_liga.reset_index(inplace=True)
df_goldpmin_liga.rename(columns={"liga": "Gold por Minuto", "index":"Liga"}, inplace=True)

df_damagepmin_lane =pd.DataFrame(data= df_damagepmin["lane"].astype("category").value_counts(dropna = False))
df_damagepmin_lane.reset_index(inplace=True)
df_damagepmin_lane.rename(columns={"lane": "Dano por Minuto", "index":"Role"}, inplace=True)

df_damagepmin_liga =pd.DataFrame(data= df_damagepmin["liga"].astype("category").value_counts(dropna = False))
df_damagepmin_liga.reset_index(inplace=True)
df_damagepmin_liga.rename(columns={"liga": "Dano por Minuto", "index":"Liga"}, inplace=True)

df_dmgpergold_lane =pd.DataFrame(data= df_dmgpergold["lane"].astype("category").value_counts(dropna = False))
df_dmgpergold_lane.reset_index(inplace=True)
df_dmgpergold_lane.rename(columns={"lane": "Dano por Ouro", "index":"Role"}, inplace=True)

df_dmgpergold_liga =pd.DataFrame(data= df_dmgpergold["liga"].astype("category").value_counts(dropna = False))
df_dmgpergold_liga.reset_index(inplace=True)
df_dmgpergold_liga.rename(columns={"liga": "Dano por Ouro", "index":"Liga"}, inplace=True)

df_damageshare_lane =pd.DataFrame(data= df_damageshare["lane"].astype("category").value_counts(dropna = False))
df_damageshare_lane.reset_index(inplace=True)
df_damageshare_lane.rename(columns={"lane": "Dano percent", "index":"Role"}, inplace=True)

df_damageshare_liga =pd.DataFrame(data= df_damageshare["liga"].astype("category").value_counts(dropna = False))
df_damageshare_liga.reset_index(inplace=True)
df_damageshare_liga.rename(columns={"liga": "Dano percent", "index":"Liga"}, inplace=True)

df_kda = df_kda.rename(columns={"team" : "Team","name" : "Name", "lane" : "Lane", "liga": "Liga", "kda" : "KDA"})
df_cspmin = df_cspmin.rename(columns={"team" : "Team","name" : "Name", "lane" : "Lane", "liga": "Liga", "cspmin" : "CS por Minuto"})
df_goldpmin = df_goldpmin.rename(columns={"team" : "Team","name" : "Name", "lane" : "Lane", "liga": "Liga", "goldpmin" : "Gold por Minuto"})
df_damagepmin = df_damagepmin.rename(columns={"team" : "Team","name" : "Name", "lane" : "Lane", "liga": "Liga", "damagepmin" : "Dano por Minuto"})
df_dmgpergold = df_dmgpergold.rename(columns={"team" : "Team","name" : "Name", "lane" : "Lane", "liga": "Liga", "dmgpergold" : "Dano por Gold"})
df_damageshare = df_damageshare.rename(columns={"team" : "Team","name" : "Name", "lane" : "Lane", "liga": "Liga", "damageshare" : "% de Dano"})

###GRAFICO PARA AS LANES###

role = ["Top", "Jg", "Mid", "Adc", "Sup"]
geral = pd.DataFrame({'Role':role})

geral = geral.merge(df_kda_lane[['Role', 'KDA']], on = 'Role', how = 'left')

geral =  geral.merge(df_cspmin_lane[['Role', 'CS por Minuto']], on = 'Role', how = 'left')

geral = geral.merge(df_goldpmin_lane[['Role', 'Gold por Minuto']], on = 'Role', how = 'left')
geral =geral.merge(df_damagepmin_lane[['Role', 'Dano por Minuto']], on = 'Role', how = 'left')
geral =geral.merge(df_dmgpergold_lane[['Role', 'Dano por Ouro']], on = 'Role', how = 'left')
geral =geral.merge(df_damageshare_lane[['Role', 'Dano percent']], on = 'Role', how = 'left')
geral = geral.drop(columns=['Role'])

geral = geral.melt().rename(columns={'variable':'Categoria','value':'Quantidade'})

role = ["Top", "Jg", "Mid", "Adc", "Sup", "Top", "Jg", "Mid", "Adc", "Sup", "Top", "Jg", "Mid", "Adc", "Sup", "Top", "Jg", "Mid", "Adc", "Sup","Top", "Jg", "Mid", "Adc", "Sup","Top", "Jg", "Mid", "Adc", "Sup"]
geral["Roles"] = role

###GRAFICO PARA AS LIGAS###
liga = ['LCK', 'LPL', 'CBLOL', 'LCS', 'LEC']
geral_liga = pd.DataFrame({'Liga':liga})

geral_liga = geral_liga.merge(df_kda_liga[['Liga', 'KDA']], on = 'Liga', how = 'left')
geral_liga =  geral_liga.merge(df_cspmin_liga[['Liga', 'CS por Minuto']], on = 'Liga', how = 'left')
geral_liga = geral_liga.merge(df_goldpmin_liga[['Liga', 'Gold por Minuto']], on = 'Liga', how = 'left')
geral_liga =geral_liga.merge(df_damagepmin_liga[['Liga', 'Dano por Minuto']], on = 'Liga', how = 'left')
geral_liga =geral_liga.merge(df_dmgpergold_liga[['Liga', 'Dano por Ouro']], on = 'Liga', how = 'left')
geral_liga =geral_liga.merge(df_damageshare_liga[['Liga', 'Dano percent']], on = 'Liga', how = 'left')
geral_liga = geral_liga.drop(columns=['Liga'])

geral_liga = geral_liga.melt().rename(columns={'variable':'Categoria','value':'Quantidade'})

liga = ['LCK', 'LPL', 'CBLOL', 'LCS', 'LEC','LCK', 'LPL', 'CBLOL', 'LCS', 'LEC','LCK', 'LPL', 'CBLOL', 'LCS', 'LEC','LCK', 'LPL', 'CBLOL', 'LCS', 'LEC','LCK', 'LPL', 'CBLOL', 'LCS', 'LEC','LCK', 'LPL', 'CBLOL', 'LCS', 'LEC']
geral_liga["Ligas"] = liga

##GRAFICO TIMES LCK##
Times = LCK.groupby("team").mean().reset_index()
Times_kda = Times[["team","KDA"]].rename(columns={"KDA":'Variable'})
Times_cspmin = Times[["team","CS por Min"]].rename(columns={"CS por Min":'Variable'})
Times_goldpmin = Times[["team","Gold por Min"]].rename(columns={"Gold por Min":'Variable'})
Times_damagepmin = Times[["team","Dano por Min"]].rename(columns={"Dano por Min":'Variable'})
Times_dmgpergold = Times[["team","Dano por Gold"]].rename(columns={"Dano por Gold":'Variable'})
Times_damageshare = Times[["team","% de Dano"]].rename(columns={"% de Dano":'Variable'})

KDA = "KDA"
Times_kda['Categoria'] = KDA

cspmin = "CS por Minuto"
Times_cspmin['Categoria'] = cspmin

goldpmin = "Gold por Minuto"
Times_goldpmin['Categoria'] = goldpmin

damagepmin = "Dano por Minuto"
Times_damagepmin['Categoria'] = damagepmin

dmgpergold = "Dano por Gold"
Times_dmgpergold['Categoria'] = dmgpergold

damageshare = "% de Dano"
Times_damageshare['Categoria'] = damageshare

Times_LCK = pd.concat([Times_kda, Times_cspmin, Times_goldpmin, Times_damagepmin, Times_dmgpergold, Times_damageshare], ignore_index=True)

##GRAFICO TIMES LPL##
Times = LPL.groupby("team").mean().reset_index()
Times_kda = Times[["team","KDA"]].rename(columns={"KDA":'Variable'})
Times_cspmin = Times[["team","CS por Min"]].rename(columns={"CS por Min":'Variable'})
Times_goldpmin = Times[["team","Gold por Min"]].rename(columns={"Gold por Min":'Variable'})
Times_damagepmin = Times[["team","Dano por Min"]].rename(columns={"Dano por Min":'Variable'})
Times_dmgpergold = Times[["team","Dano por Gold"]].rename(columns={"Dano por Gold":'Variable'})
Times_damageshare = Times[["team","% de Dano"]].rename(columns={"% de Dano":'Variable'})

KDA = "KDA"
Times_kda['Categoria'] = KDA

cspmin = "CS por Minuto"
Times_cspmin['Categoria'] = cspmin

goldpmin = "Gold por Minuto"
Times_goldpmin['Categoria'] = goldpmin

damagepmin = "Dano por Minuto"
Times_damagepmin['Categoria'] = damagepmin

dmgpergold = "Dano por Gold"
Times_dmgpergold['Categoria'] = dmgpergold

damageshare = "% de Dano"
Times_damageshare['Categoria'] = damageshare

Times_LPL = pd.concat([Times_kda, Times_cspmin, Times_goldpmin, Times_damagepmin, Times_dmgpergold, Times_damageshare], ignore_index=True)


##GRAFICO TIMES CBLOL##

Times = CBLOL.groupby("team").mean().reset_index()
Times_kda = Times[["team","KDA"]].rename(columns={"KDA":'Variable'})
Times_cspmin = Times[["team","CS por Min"]].rename(columns={"CS por Min":'Variable'})
Times_goldpmin = Times[["team","Gold por Min"]].rename(columns={"Gold por Min":'Variable'})
Times_damagepmin = Times[["team","Dano por Min"]].rename(columns={"Dano por Min":'Variable'})
Times_dmgpergold = Times[["team","Dano por Gold"]].rename(columns={"Dano por Gold":'Variable'})
Times_damageshare = Times[["team","% de Dano"]].rename(columns={"% de Dano":'Variable'})

KDA = "KDA"
Times_kda['Categoria'] = KDA

cspmin = "CS por Minuto"
Times_cspmin['Categoria'] = cspmin

goldpmin = "Gold por Minuto"
Times_goldpmin['Categoria'] = goldpmin

damagepmin = "Dano por Minuto"
Times_damagepmin['Categoria'] = damagepmin

dmgpergold = "Dano por Gold"
Times_dmgpergold['Categoria'] = dmgpergold

damageshare = "% de Dano"
Times_damageshare['Categoria'] = damageshare

Times_CBLOL = pd.concat([Times_kda, Times_cspmin, Times_goldpmin, Times_damagepmin, Times_dmgpergold, Times_damageshare], ignore_index=True)

##GRAFICO TIMES LEC##

Times = LEC.groupby("team").mean().reset_index()
Times_kda = Times[["team","KDA"]].rename(columns={"KDA":'Variable'})
Times_cspmin = Times[["team","CS por Min"]].rename(columns={"CS por Min":'Variable'})
Times_goldpmin = Times[["team","Gold por Min"]].rename(columns={"Gold por Min":'Variable'})
Times_damagepmin = Times[["team","Dano por Min"]].rename(columns={"Dano por Min":'Variable'})
Times_dmgpergold = Times[["team","Dano por Gold"]].rename(columns={"Dano por Gold":'Variable'})
Times_damageshare = Times[["team","% de Dano"]].rename(columns={"% de Dano":'Variable'})

KDA = "KDA"
Times_kda['Categoria'] = KDA

cspmin = "CS por Minuto"
Times_cspmin['Categoria'] = cspmin

goldpmin = "Gold por Minuto"
Times_goldpmin['Categoria'] = goldpmin

damagepmin = "Dano por Minuto"
Times_damagepmin['Categoria'] = damagepmin

dmgpergold = "Dano por Gold"
Times_dmgpergold['Categoria'] = dmgpergold

damageshare = "% de Dano"
Times_damageshare['Categoria'] = damageshare

Times_LEC = pd.concat([Times_kda, Times_cspmin, Times_goldpmin, Times_damagepmin, Times_dmgpergold, Times_damageshare], ignore_index=True)

##GRAFICO TIMES LCS##

Times = LCS.groupby("team").mean().reset_index()
Times_kda = Times[["team","KDA"]].rename(columns={"KDA":'Variable'})
Times_cspmin = Times[["team","CS por Min"]].rename(columns={"CS por Min":'Variable'})
Times_goldpmin = Times[["team","Gold por Min"]].rename(columns={"Gold por Min":'Variable'})
Times_damagepmin = Times[["team","Dano por Min"]].rename(columns={"Dano por Min":'Variable'})
Times_dmgpergold = Times[["team","Dano por Gold"]].rename(columns={"Dano por Gold":'Variable'})
Times_damageshare = Times[["team","% de Dano"]].rename(columns={"% de Dano":'Variable'})

KDA = "KDA"
Times_kda['Categoria'] = KDA

cspmin = "CS por Minuto"
Times_cspmin['Categoria'] = cspmin

goldpmin = "Gold por Minuto"
Times_goldpmin['Categoria'] = goldpmin

damagepmin = "Dano por Minuto"
Times_damagepmin['Categoria'] = damagepmin

dmgpergold = "Dano por Gold"
Times_dmgpergold['Categoria'] = dmgpergold

damageshare = "% de Dano"
Times_damageshare['Categoria'] = damageshare

Times_LCS = pd.concat([Times_kda, Times_cspmin, Times_goldpmin, Times_damagepmin, Times_dmgpergold, Times_damageshare], ignore_index=True)

#######################################################################################################
############MENU GERAL INICIAL
   
st.sidebar.write("MENU")

    
    
#OPCOES DE BOX
    
opcoes = ['MENU','GERAL', 'LANES', 'LCK', 'LPL', 'CBLOL', 'LEC', 'LCS', 'REGRESSÃO']
lanes = ['Top', 'Jg', 'Mid', 'Adc', 'Sup']
dados = ['Liga', 'Lane', 'Tabelas', 'Times', 'Jogadores']
opcao_selecionada = st.sidebar.selectbox("O que deseja ver:", opcoes)

if opcao_selecionada == "MENU":
    st.sidebar.write("Selecione:")
    ##Introducao
    if st.sidebar.button("Introdução"):
        st.header("Introdução ao trabalho")
        st.write("O trabalho apresentado visa coletar dados do jogo League of Legends(LOL) com o intuito de fazer análises descritivas em relação às diferentes ligas, os times e os jogadores.")
        st.write("Os dados são do segundo semestre de 2022 e foram coletados via webscrapping do site LeaguePedia, um site que é especializado no cenário competitivo do jogo.")
        st.write("Foram coletados e analisados dados das ligas LCK, LPL, CBLOL, LEC e LCS, além de todos os times e jogadores dessas ligas")
        st.write("Para a análise descritiva focamos nas variáveis KDA, CS por Minuto, Dano por Minuto, Gold por Minuto, Dano por Gold e % de Dano, já que são dados que mostram fundamentos básicos do jogo que influenciam a vitória. Além da análise descritiva, fizemos uma regressão linear com estimador de MQO para ver a significancia de nossas variáveis na taxa de vitória(winrate).")

        
       
    if st.sidebar.button("Glossário"):
        st.header("Segue um glossário das principais estatísticas e termos utilizados:")
        st.write("winrate: taxa de vitórias do jogador (calculada como win/games).")
        st.write("kda: ratio de matanças, mortes e assistências (calculado como (kill + assist) / death).")
        st.write("cs: o número de creeps (monstros inimigos) mortos pelo jogador.")
        st.write("gold: quantidade de ouro acumulado pelo jogador durante a partida.")
        st.write("kpar: porcentagem de participação de um jogador em kills (abates) durante a partida. É calculado como KPAR = (Kills + Assists) / Total Kills do time.")
        st.write("killshare: porcentagem de kills (abates) do total do time que um jogador participou. É calculado como Kill Share = (Kills + Assists) / Total Kills do time.")
        st.write(" goldshare: porcentagem de ouro do total do time que um jogador possui. É calculado como Gold Share = Gold do jogador / Total Gold do time.")
        st.write("champplayed: campeões jogados pelo jogador durante o campeonato.")
        
        
    if st.sidebar.button("Como Utilizar"):
        st.header("Uma ajudinha...")
        st.write("No box abaixo de 'O que deseja ver:' é possível selecionar diversas categorias. Na primeira, GERAL, serão encontrados dados gerais de 'Lane', 'Liga', 'Times' e 'jogadores', além de uma seção de tabelas que mostram os 25 melhores jogadores para cada característica do jogo que foi julgada importante. Na segunda, LANES, são apresentados dados para cada lane em cada liga distinta. As últimas cinco categorias são específicas para as ligas e, quando selecionadas apresentam dados para cada um dos times na liga.")

if opcao_selecionada == "GERAL":
        st.sidebar.write("Selecione a opção desejada para dados Gerais:")
        
        dado_selecionado = st.sidebar.selectbox("Quais dados gerais deseja ver:", dados)
        
        if dado_selecionado == "Liga":
            st.write("No gráfico interativo abaixo mostra-se a quantidade de jogadores de cada liga que apareceram como top 25 de cada uma das categorias. É possível mudar a categoria desejada ao clicar na legenda do gráfico.")
            
            
            st.plotly_chart(px.bar(geral_liga, x = 'Ligas', y = 'Quantidade', color = "Categoria"))
                          
        if dado_selecionado == "Lane":
            st.write("No gráfico interativo abaixo mostra-se a quantidade de jogadores de cada lane que apareceram como top 25 de cada uma das categorias. É possível mudar a categoria desejada ao clicar na legenda do gráfico.")
            
            
            st.plotly_chart(px.bar(geral, x = 'Roles', y = 'Quantidade', color = "Categoria"))
           
        if dado_selecionado == "Tabelas":
            st.header("Top 25")
            st.write("Nas tabelas mostraremos os 25 melhores jogadores de determinada categoria. Essas categorias são: KDA, CS por Minuto, Gold por Minuto, Dano por Minuto, Dano por Gold e % de Dano e elas podem ser accessadas clicando ao lado.")
            
            if st.sidebar.button("KDA"):
                st.write("A tabela a seguir mostra os 25 jogadores com maior KDA")
                        
                KDA_table = tabulate(df_kda, headers = 'keys', tablefmt = 'html',showindex = range(1, df_kda.shape[0]+1))        
                st.write(KDA_table, unsafe_allow_html=True)
                
            if st.sidebar.button("CS por Minuto"):
                st.write("A tabela a seguir mostra os 25 jogadores com maior CS por Minuto.")
                        
                df_cspmin_table = tabulate(df_cspmin, headers = 'keys', tablefmt = 'html',showindex = range(1, df_cspmin.shape[0]+1))        
                st.write(df_cspmin_table, unsafe_allow_html=True)
               
            if st.sidebar.button("Gold por Minuto"):
                st.write("A tabela a seguir mostra os 25 jogadores com maior Gold por Minuto.")
                        
                df_goldpmin_table = tabulate(df_goldpmin, headers = 'keys', tablefmt = 'html',showindex = range(1, df_goldpmin.shape[0]+1))        
                st.write(df_goldpmin_table, unsafe_allow_html=True)
               
            if st.sidebar.button("Dano por Minuto"):
                st.write("A tabela a seguir mostra os 25 jogadores com maior Dano por Minuto.")
                        
                df_damagepmin_table = tabulate(df_damagepmin, headers = 'keys', tablefmt = 'html',showindex = range(1, df_damagepmin.shape[0]+1))        
                st.write(df_damagepmin_table, unsafe_allow_html=True)
               
            if st.sidebar.button("Dano por Gold"):
                st.write("A tabela a seguir mostra os 25 jogadores com maior Gold por Minuto.")
                        
                df_dmgpergold_table = tabulate(df_dmgpergold, headers = 'keys', tablefmt = 'html',showindex = range(1, df_dmgpergold.shape[0]+1))        
                st.write(df_dmgpergold_table, unsafe_allow_html=True)
               
            if st.sidebar.button("% de Dano"):
                st.write("A tabela a seguir mostra os 25 jogadores com maior % de Dano.")
                        
                df_damageshare_table = tabulate(df_damageshare, headers = 'keys', tablefmt = 'html',showindex = range(1, df_damageshare.shape[0]+1))        
                st.write(df_damageshare_table, unsafe_allow_html=True)
           
        if dado_selecionado == "Times":
            st.write("Escolha ao lado a liga para ver dados dos times da liga que foi escolhida.")
            st.sidebar.write("Escolha a liga para a qual deseja ver os times:")
            if st.sidebar.button("LCK"):
                st.write("No gráfico interativo abaixo é apresentado os times da LCK e seus dados médios para cada categoria. Para mudar a categoria basta clicar na legenda do gráfico.")
                st.plotly_chart(px.bar(Times_LCK, x = 'team', y = 'Variable', color = "Categoria"))
                
                st.write("A seguir são apresentados gráficos que mostram os dados de Kill, Death e Assist para os jogadores de cada time")
                
                teams = df[df["liga"] == "LCK"]["team"].unique()

                for team in teams:
                    team_df = df[(df["team"] == team) & (df["liga"] == "LCK")]
                    names = team_df["name"]
                
                    theta = np.linspace(0, 2*np.pi, len(names), endpoint=False)
                
                    kills = team_df["kill"].astype(float)
                    deaths = team_df["death"].astype(float)
                    assists = team_df["assist"].astype(float)
                
                    ax = plt.subplot(polar=True)
                    ax.plot(theta, kills, label='Kills')
                    ax.plot(theta, deaths, label='Deaths')
                    ax.plot(theta, assists, label='Assists')
                
                    ax.set_xticks(theta)
                    ax.set_xticklabels(names)
                    ax.set_ylim(0, max(kills.max(), deaths.max(), assists.max()) * 1.2)
                
                    plt.title(f"Desempenho por jogador para o time {team}")
                    plt.legend(loc="center left", bbox_to_anchor=(1.1, 0.5), frameon=False)
                    st.pyplot()
                
            if st.sidebar.button("LPL"):
                st.write("No gráfico interativo abaixo é apresentado os times da LPL e seus dados médios para cada categoria. Para mudar a categoria basta clicar na legenda do gráfico.")
                st.plotly_chart(px.bar(Times_LPL, x = 'team', y = 'Variable', color = "Categoria"))
                
                st.write("A seguir são apresentados gráficos que mostram os dados de Kill, Death e Assist para os jogadores de cada time")
                
                teams = df[df["liga"] == "LPL"]["team"].unique()

                for team in teams:
                    team_df = df[(df["team"] == team) & (df["liga"] == "LPL")]
                    names = team_df["name"]
                
                    theta = np.linspace(0, 2*np.pi, len(names), endpoint=False)
                
                    kills = team_df["kill"].astype(float)
                    deaths = team_df["death"].astype(float)
                    assists = team_df["assist"].astype(float)
                
                    ax = plt.subplot(polar=True)
                    ax.plot(theta, kills, label='Kills')
                    ax.plot(theta, deaths, label='Deaths')
                    ax.plot(theta, assists, label='Assists')
                
                    ax.set_xticks(theta)
                    ax.set_xticklabels(names)
                    ax.set_ylim(0, max(kills.max(), deaths.max(), assists.max()) * 1.2)
                
                    plt.title(f"Desempenho por jogador para o time {team}")
                    plt.legend(loc="center left", bbox_to_anchor=(1.1, 0.5), frameon=False)
                    st.pyplot()                
            
            if st.sidebar.button("CBLOL"):
                st.write("No gráfico interativo abaixo é apresentado os times do CBLOL e seus dados médios para cada categoria. Para mudar a categoria basta clicar na legenda do gráfico.")
                st.plotly_chart(px.bar(Times_CBLOL, x = 'team', y = 'Variable', color = "Categoria"))
                
                st.write("A seguir são apresentados gráficos que mostram os dados de Kill, Death e Assist para os jogadores de cada time")
                
                teams = df[df["liga"] == "CBLOL"]["team"].unique()

                for team in teams:
                    team_df = df[(df["team"] == team) & (df["liga"] == "CBLOL")]
                    names = team_df["name"]
                
                    theta = np.linspace(0, 2*np.pi, len(names), endpoint=False)
                
                    kills = team_df["kill"].astype(float)
                    deaths = team_df["death"].astype(float)
                    assists = team_df["assist"].astype(float)
                
                    ax = plt.subplot(polar=True)
                    ax.plot(theta, kills, label='Kills')
                    ax.plot(theta, deaths, label='Deaths')
                    ax.plot(theta, assists, label='Assists')
                
                    ax.set_xticks(theta)
                    ax.set_xticklabels(names)
                    ax.set_ylim(0, max(kills.max(), deaths.max(), assists.max()) * 1.2)
                
                    plt.title(f"Desempenho por jogador para o time {team}")
                    plt.legend(loc="center left", bbox_to_anchor=(1.1, 0.5), frameon=False)
                    st.pyplot()                
            
            if st.sidebar.button("LEC"):
                st.write("No gráfico interativo abaixo é apresentado os times da LEC e seus dados médios para cada categoria. Para mudar a categoria basta clicar na legenda do gráfico.")
                st.plotly_chart(px.bar(Times_LEC, x = 'team', y = 'Variable', color = "Categoria"))
                
                st.write("A seguir são apresentados gráficos que mostram os dados de Kill, Death e Assist para os jogadores de cada time")
                
                teams = df[df["liga"] == "LEC"]["team"].unique()

                for team in teams:
                    team_df = df[(df["team"] == team) & (df["liga"] == "LEC")]
                    names = team_df["name"]
                
                    theta = np.linspace(0, 2*np.pi, len(names), endpoint=False)
                
                    kills = team_df["kill"].astype(float)
                    deaths = team_df["death"].astype(float)
                    assists = team_df["assist"].astype(float)
                
                    ax = plt.subplot(polar=True)
                    ax.plot(theta, kills, label='Kills')
                    ax.plot(theta, deaths, label='Deaths')
                    ax.plot(theta, assists, label='Assists')
                
                    ax.set_xticks(theta)
                    ax.set_xticklabels(names)
                    ax.set_ylim(0, max(kills.max(), deaths.max(), assists.max()) * 1.2)
                
                    plt.title(f"Desempenho por jogador para o time {team}")
                    plt.legend(loc="center left", bbox_to_anchor=(1.1, 0.5), frameon=False)
                    st.pyplot()                
            
            if st.sidebar.button("LCS"):
                st.write("No gráfico interativo abaixo é apresentado os times da LCS e seus dados médios para cada categoria. Para mudar a categoria basta clicar na legenda do gráfico.")
                st.plotly_chart(px.bar(Times_LCS, x = 'team', y = 'Variable', color = "Categoria"))
                
                st.write("A seguir são apresentados gráficos que mostram os dados de Kill, Death e Assist para os jogadores de cada time")
                
                teams = df[df["liga"] == "LCS"]["team"].unique()

                for team in teams:
                    team_df = df[(df["team"] == team) & (df["liga"] == "LCS")]
                    names = team_df["name"]
                
                    theta = np.linspace(0, 2*np.pi, len(names), endpoint=False)
                
                    kills = team_df["kill"].astype(float)
                    deaths = team_df["death"].astype(float)
                    assists = team_df["assist"].astype(float)
                
                    ax = plt.subplot(polar=True)
                    ax.plot(theta, kills, label='Kills')
                    ax.plot(theta, deaths, label='Deaths')
                    ax.plot(theta, assists, label='Assists')
                
                    ax.set_xticks(theta)
                    ax.set_xticklabels(names)
                    ax.set_ylim(0, max(kills.max(), deaths.max(), assists.max()) * 1.2)
                
                    plt.title(f"Desempenho por jogador para o time {team}")
                    plt.legend(loc="center left", bbox_to_anchor=(1.1, 0.5), frameon=False)
                    st.pyplot()                
           
        if dado_selecionado == "Jogadores":
            st.write("Escolha ao lado a liga para ver dados dos jogadores da liga que foi escolhida.")
            st.sidebar.write("Escolha a liga para a qual deseja ver os jogadores:")
            
            if st.sidebar.button("LCK"):
                st.write("No gráfico interativo abaixo é apresentado os jogadores da LCK e seus times. Para escolher os times que deseja ver basta clicar na legenda do gráfico.")
                
                fig = px.scatter(LCK, x="Gold por Min", y="Dano por Min", color='team', hover_data=["Gold por Min"], text = 'Name',
                 labels={
                     'Gold por Min' : "Gold por Min",
                     'Dano por Min' : "Dano por Min",
                     'team' : "Times"},
                title=("Gold x Dano para todos os Jogadores da LCK"))
                fig.update_traces(textposition="bottom right")

                st.plotly_chart(fig)
                
                st.write("Nesse gráfico é feito uma análise bivariada entre as variáveis 'Gold por minuto' e 'Dano por minuto'. O objetivo é saber quanto o jogador consegue impactar na partida conforme a quantidade de recurso que ele tem. Os melhores jogadores são os que conseguem captar mais recursos e conseguem causar a maior quantidade de dano, ou seja, o quadrante superior direito representam, supostamente, os jogadores mais impactantes.") 
                             
            if st.sidebar.button("LPL"):
                st.write("No gráfico interativo abaixo é apresentado os jogadores da LPL e seus times. Para escolher os times que deseja ver basta clicar na legenda do gráfico.")
                
                fig = px.scatter(LPL, x="Gold por Min", y="Dano por Min", color='team', hover_data=["Gold por Min"], text = 'Name',
                 labels={
                     'Gold por Min' : "Gold por Min",
                     'Dano por Min' : "Dano por Min",
                     'team' : "Times"},
                title=("Gold x Dano para todos os Jogadores da LPL"))
                fig.update_traces(textposition="bottom right")

                st.plotly_chart(fig)
                
                st.write("Nesse gráfico é feito uma análise bivariada entre as variáveis 'Gold por minuto' e 'Dano por minuto'. O objetivo é saber quanto o jogador consegue impactar na partida conforme a quantidade de recurso que ele tem. Os melhores jogadores são os que conseguem captar mais recursos e conseguem causar a maior quantidade de dano, ou seja, o quadrante superior direito representam, supostamente, os jogadores mais impactantes.")
               
            if st.sidebar.button("CBLOL"):
                st.write("No gráfico interativo abaixo é apresentado os jogadores do CBLOL e seus times. Para escolher os times que deseja ver basta clicar na legenda do gráfico.")
                
                fig = px.scatter(CBLOL, x="Gold por Min", y="Dano por Min", color='team', hover_data=["Gold por Min"], text = 'Name',
                 labels={
                     'Gold por Min' : "Gold por Min",
                     'Dano por Min' : "Dano por Min",
                     'team' : "Times"},
                title=("Gold x Dano para todos os Jogadores da CBLOL"))
                fig.update_traces(textposition="bottom right")

                st.plotly_chart(fig)
                
                st.write("Nesse gráfico é feito uma análise bivariada entre as variáveis 'Gold por minuto' e 'Dano por minuto'. O objetivo é saber quanto o jogador consegue impactar na partida conforme a quantidade de recurso que ele tem. Os melhores jogadores são os que conseguem captar mais recursos e conseguem causar a maior quantidade de dano, ou seja, o quadrante superior direito representam, supostamente, os jogadores mais impactantes.")
               
            if st.sidebar.button("LEC"):
                st.write("No gráfico interativo abaixo é apresentado os jogadores da LEC e seus times. Para escolher os times que deseja ver basta clicar na legenda do gráfico")
                
                fig = px.scatter(LEC, x="Gold por Min", y="Dano por Min", color='team', hover_data=["Gold por Min"], text = 'Name',
                 labels={
                     'Gold por Min' : "Gold por Min",
                     'Dano por Min' : "Dano por Min",
                     'team' : "Times"},
                title=("Gold x Dano para todos os Jogadores da LEC"))
                fig.update_traces(textposition="bottom right")

                st.plotly_chart(fig)
                
                st.write("Nesse gráfico é feito uma análise bivariada entre as variáveis 'Gold por minuto' e 'Dano por minuto'. O objetivo é saber quanto o jogador consegue impactar na partida conforme a quantidade de recurso que ele tem. Os melhores jogadores são os que conseguem captar mais recursos e conseguem causar a maior quantidade de dano, ou seja, o quadrante superior direito representam, supostamente, os jogadores mais impactantes.")
               
            if st.sidebar.button("LCS"):
                st.write("No gráfico interativo abaixo é apresentado os jogadores da LCS e seus times. Para escolher os times que deseja ver basta clicar na legenda do gráfico")
                
                fig = px.scatter(LCS, x="Gold por Min", y="Dano por Min", color='team', hover_data=["Gold por Min"], text = 'Name',
                 labels={
                     'Gold por Min' : "Gold por Min",
                     'Dano por Min' : "Dano por Min",
                     'team' : "Times"},
                title=("Gold x Dano para todos os Jogadores da LCS"))
                fig.update_traces(textposition="bottom right")

                st.plotly_chart(fig)
                
                st.write("Nesse gráfico é feito uma análise bivariada entre as variáveis 'Gold por minuto' e 'Dano por minuto'. O objetivo é saber quanto o jogador consegue impactar na partida conforme a quantidade de recurso que ele tem. Os melhores jogadores são os que conseguem captar mais recursos e conseguem causar a maior quantidade de dano, ou seja, o quadrante superior direito representam, supostamente, os jogadores mais impactantes.")
            
if opcao_selecionada == "LANES":    
        st.sidebar.write("Selecione a opção desejada para dados de Lane:")
        st.write("Aqui poderá ser visualizado scatterplots das variáveis 'Gold por minuto' e 'Dano por minuto' para os jogadores de cada lane em cada região. O objetivo é observar o impacto de determinados jogadores dentro de suas próprias ligas quando comparados a jogadores que jogam em sua mesma lane.")
        
        lane_selecionada = st.sidebar.selectbox("Qual lane deseja ver:", lanes)
        
        if lane_selecionada == 'Top':
            
            st.sidebar.write("Selecione qual liga deseja ver:")
            if st.sidebar.button("LCK"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCK_Top, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCK TOP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCK_Top.shape[0]):
                    plt.text(x=LCK_Top.goldpmin[i]+1.25,y=LCK_Top.damagepmin[i]+1.25,s=LCK_Top.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
           
            if st.sidebar.button("LPL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LPL_Top, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LPL TOP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LPL_Top.shape[0]):
                    plt.text(x=LPL_Top.goldpmin[i]+1.25,y=LPL_Top.damagepmin[i]+1.25,s=LPL_Top.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
              
            if st.sidebar.button("CBLOL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=CBLOL_Top, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : CBLOL TOP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(CBLOL_Top.shape[0]):
                    plt.text(x=CBLOL_Top.goldpmin[i]+1.25,y=CBLOL_Top.damagepmin[i]+1.25,s=CBLOL_Top.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
               
            if st.sidebar.button("LCS"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCS_Top, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCS TOP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCS_Top.shape[0]):
                    plt.text(x=LCS_Top.goldpmin[i]+1.25,y=LCS_Top.damagepmin[i]+1.25,s=LCS_Top.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
            if st.sidebar.button("LEC"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LEC_Top, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LEC TOP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LEC_Top.shape[0]):
                    plt.text(x=LEC_Top.goldpmin[i]+1.25,y=LEC_Top.damagepmin[i]+1.25,s=LEC_Top.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
               
        if lane_selecionada == 'Jg':
            
            st.sidebar.write("Selecione qual liga deseja ver:")
            if st.sidebar.button("LCK"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCK_Jg, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCK JG", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCK_Jg.shape[0]):
                    plt.text(x=LCK_Jg.goldpmin[i]+1.25,y=LCK_Jg.damagepmin[i]+1.25,s=LCK_Jg.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
            
            if st.sidebar.button("LPL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LPL_Jg, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LPL JG", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LPL_Jg.shape[0]):
                    plt.text(x=LPL_Jg.goldpmin[i]+1.25,y=LPL_Jg.damagepmin[i]+1.25,s=LPL_Jg.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
            if st.sidebar.button("CBLOL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=CBLOL_Jg, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : CBLOL JG", fontsize = 20)
                plt.tight_layout()
                
                for i in range(CBLOL_Jg.shape[0]):
                    plt.text(x=CBLOL_Jg.goldpmin[i]+1.25,y=CBLOL_Jg.damagepmin[i]+1.25,s=CBLOL_Jg.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
            if st.sidebar.button("LCS"):
                              
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCS_Jg, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCS JG", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCS_Jg.shape[0]):
                    plt.text(x=LCS_Jg.goldpmin[i]+1,y=LCS_Jg.damagepmin[i]+1,s=LCS_Jg.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
            if st.sidebar.button("LEC"):
                                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LEC_Jg, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LEC JG", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LEC_Jg.shape[0]):
                    plt.text(x=LEC_Jg.goldpmin[i]+1.25,y=LEC_Jg.damagepmin[i]+1.25,s=LEC_Jg.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
        if lane_selecionada == 'Mid':
            
            st.sidebar.write("Selecione qual liga deseja ver:")
            if st.sidebar.button("LCK"):
                
                st.sidebar.write("Selecione qual liga deseja ver:")
            if st.sidebar.button("LCK"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCK_Mid, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCK MID", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCK_Mid.shape[0]):
                    plt.text(x=LCK_Mid.goldpmin[i]+1.25,y=LCK_Mid.damagepmin[i]+1.25,s=LCK_Mid.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
            
            if st.sidebar.button("LPL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LPL_Mid, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LPL MID", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LPL_Mid.shape[0]):
                    plt.text(x=LPL_Mid.goldpmin[i]+1.25,y=LPL_Mid.damagepmin[i]+1.25,s=LPL_Mid.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
              
            if st.sidebar.button("CBLOL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=CBLOL_Mid, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : CBLOL MID", fontsize = 20)
                plt.tight_layout()
                
                for i in range(CBLOL_Mid.shape[0]):
                    plt.text(x=CBLOL_Mid.goldpmin[i]+1.25,y=CBLOL_Mid.damagepmin[i]+1.25,s=CBLOL_Mid.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
               
            if st.sidebar.button("LCS"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCS_Mid, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCS MID", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCS_Mid.shape[0]):
                    plt.text(x=LCS_Mid.goldpmin[i]+1.25,y=LCS_Mid.damagepmin[i]+1.25,s=LCS_Mid.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
            if st.sidebar.button("LEC"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LEC_Mid, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LEC MID", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LEC_Mid.shape[0]):
                    plt.text(x=LEC_Mid.goldpmin[i]+1.25,y=LEC_Mid.damagepmin[i]+1.25,s=LEC_Mid.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                                  
        if lane_selecionada == 'Adc':
            
            st.sidebar.write("Selecione qual liga deseja ver:")
            if st.sidebar.button("LCK"):
                st.write("LCK FOI ESCOLHIDA")
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCK_Adc, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCK ADC", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCK_Adc.shape[0]):
                    plt.text(x=LCK_Adc.goldpmin[i]+1.25,y=LCK_Adc.damagepmin[i]+1.25,s=LCK_Adc.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
            
            if st.sidebar.button("LPL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LPL_Adc, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LPL ADC", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LPL_Adc.shape[0]):
                    plt.text(x=LPL_Adc.goldpmin[i]+1.25,y=LPL_Adc.damagepmin[i]+1.25,s=LPL_Adc.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
              
            if st.sidebar.button("CBLOL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=CBLOL_Adc, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : CBLOL ADC", fontsize = 20)
                plt.tight_layout()
                
                for i in range(CBLOL_Adc.shape[0]):
                    plt.text(x=CBLOL_Adc.goldpmin[i]+1.25,y=CBLOL_Adc.damagepmin[i]+1.25,s=CBLOL_Adc.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
               
            if st.sidebar.button("LCS"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCS_Adc, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCS ADC", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCS_Adc.shape[0]):
                    plt.text(x=LCS_Adc.goldpmin[i]+1.25,y=LCS_Adc.damagepmin[i]+1.25,s=LCS_Adc.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
            if st.sidebar.button("LEC"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LEC_Adc, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LEC ADC", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LEC_Adc.shape[0]):
                    plt.text(x=LEC_Adc.goldpmin[i]+1.25,y=LEC_Adc.damagepmin[i]+1.25,s=LEC_Adc.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
        if lane_selecionada == 'Sup':
                           
            st.sidebar.write("Selecione qual liga deseja ver:")
            if st.sidebar.button("LCK"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCK_Sup, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCK SUP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCK_Sup.shape[0]):
                    plt.text(x=LCK_Sup.goldpmin[i]+1.25,y=LCK_Sup.damagepmin[i]+1.25,s=LCK_Sup.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
            
            if st.sidebar.button("LPL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LPL_Sup, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LPL SUP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LPL_Sup.shape[0]):
                    plt.text(x=LPL_Sup.goldpmin[i]+1.25,y=LPL_Sup.damagepmin[i]+1.25,s=LPL_Sup.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
              
            if st.sidebar.button("CBLOL"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=CBLOL_Sup, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : CBLOL SUP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(CBLOL_Sup.shape[0]):
                    plt.text(x=CBLOL_Sup.goldpmin[i]+1.25,y=CBLOL_Sup.damagepmin[i]+1.25,s=CBLOL_Sup.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
               
            if st.sidebar.button("LCS"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LCS_Sup, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LCS SUP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LCS_Sup.shape[0]):
                    plt.text(x=LCS_Sup.goldpmin[i]+1.25,y=LCS_Sup.damagepmin[i]+1.25,s=LCS_Sup.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
                
            if st.sidebar.button("LEC"):
                
                sns.set_context("talk", font_scale=0.6)
                plt.figure(figsize=(15,6))
                sns.scatterplot("goldpmin", "damagepmin", data=LEC_Sup, hue= "team")
                plt.xlabel("Gold/min",fontsize=10)
                plt.ylabel("Damage/min", fontsize=10)
                plt.legend(bbox_to_anchor=(1.01, 1),
                           borderaxespad=0)
                plt.title("Gold x Damage : LEC SUP", fontsize = 20)
                plt.tight_layout()
                
                for i in range(LEC_Sup.shape[0]):
                    plt.text(x=LEC_Sup.goldpmin[i]+1.25,y=LEC_Sup.damagepmin[i]+1.25,s=LEC_Sup.name[i], 
                          fontdict=dict(color= 'black',size=6),
                          bbox=dict(facecolor='white',alpha=0.8))
                
                st.pyplot()
            

if opcao_selecionada == "LCK":
        st.sidebar.write("Selecione a opção desejada para dados da LCK:")
        st.write("Ao clicar ao lado é possível ver uma tabela para cada time da LCK. Nesta tabela são fornecidos os principais dados médios de como os jogadores impactam em seus times.")
        
        if st.sidebar.button("Hanwha Life Esports"):
            
            HLE_table = tabulate(Hanwha_Life_Esports, headers = 'keys', tablefmt = 'html',showindex = range(1, Hanwha_Life_Esports.shape[0]+1))        
            st.write(HLE_table, unsafe_allow_html=True)
            
        if st.sidebar.button("KT Rolster"):
            
            
            KT_Rolster_table = tabulate(KT_Rolster, headers = 'keys', tablefmt = 'html',showindex = range(1, KT_Rolster.shape[0]+1))        
            st.write(KT_Rolster_table, unsafe_allow_html=True)
            
        if st.sidebar.button("DRX"):
            
            
            DRX_table = tabulate(DRX, headers = 'keys', tablefmt = 'html',showindex = range(1, DRX.shape[0]+1))        
            st.write(DRX_table, unsafe_allow_html=True)
            
        if st.sidebar.button("T1"):
            
            
            T1_table = tabulate(T1, headers = 'keys', tablefmt = 'html',showindex = range(1, T1.shape[0]+1))        
            st.write(T1_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Nongshim RedForce"):
            
            
            Nongshim_RedForce_table = tabulate(Nongshim_RedForce, headers = 'keys', tablefmt = 'html',showindex = range(1, Nongshim_RedForce.shape[0]+1))        
            st.write(Nongshim_RedForce_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Kwangdong Freecs"):
            
            
            Kwangdong_Freecs_table = tabulate(Kwangdong_Freecs, headers = 'keys', tablefmt = 'html',showindex = range(1, Kwangdong_Freecs.shape[0]+1))        
            st.write(Kwangdong_Freecs_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Liiv SANDBOX"):
            
            
            Liiv_SANDBOX_table = tabulate(Liiv_SANDBOX, headers = 'keys', tablefmt = 'html',showindex = range(1, Liiv_SANDBOX.shape[0]+1))        
            st.write(Liiv_SANDBOX_table, unsafe_allow_html=True)
            
        if st.sidebar.button("DWG KIA"):
            
            
            DWG_KIA_table = tabulate(DWG_KIA, headers = 'keys', tablefmt = 'html',showindex = range(1, DWG_KIA.shape[0]+1))        
            st.write(DWG_KIA_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Gen.G"):
            
            
            GenG_table = tabulate(GenG, headers = 'keys', tablefmt = 'html',showindex = range(1, GenG.shape[0]+1))        
            st.write(GenG_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Fredit BRION"):
            
            
            Fredit_BRION_table = tabulate(Fredit_BRION, headers = 'keys', tablefmt = 'html',showindex = range(1, Fredit_BRION.shape[0]+1))        
            st.write(Fredit_BRION_table, unsafe_allow_html=True)

##LPL##            
            
elif opcao_selecionada == "LPL":
        st.write("Ao clicar ao lado é possível ver uma tabela para cada time da LPL. Nesta tabela são fornecidos os principais dados médios de como os jogadores impactam em seus times.")
        if st.sidebar.button("Invictus Gaming"):
            
            
            Invictus_Gaming_table = tabulate(Invictus_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, Invictus_Gaming.shape[0]+1))        
            st.write(Invictus_Gaming_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Royal Never Give Up"):
            
            
            Royal_Never_Give_Up_table = tabulate(Royal_Never_Give_Up, headers = 'keys', tablefmt = 'html',showindex = range(1, Royal_Never_Give_Up.shape[0]+1))        
            st.write(Royal_Never_Give_Up_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Oh My God"):
            
            
            Oh_My_God_table = tabulate(Oh_My_God, headers = 'keys', tablefmt = 'html',showindex = range(1, Oh_My_God.shape[0]+1))        
            st.write(Oh_My_God_table, unsafe_allow_html=True)
            
        if st.sidebar.button("JD Gaming"):
            
            
            JD_Gaming_table = tabulate(JD_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, JD_Gaming.shape[0]+1))        
            st.write(JD_Gaming_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Bilibili Gaming"):
            
            
            Bilibili_Gaming_table = tabulate(Bilibili_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, Bilibili_Gaming.shape[0]+1))        
            st.write(Bilibili_Gaming_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Rare Atom"):
            
            
            Rare_Atom_table = tabulate(Rare_Atom, headers = 'keys', tablefmt = 'html',showindex = range(1, Rare_Atom.shape[0]+1))        
            st.write(Rare_Atom_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Weibo Gaming"):
            
            
            Weibo_Gaming_table = tabulate(Weibo_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, Weibo_Gaming.shape[0]+1))        
            st.write(Weibo_Gaming_table, unsafe_allow_html=True)
            
        if st.sidebar.button("EDward Gaming"):
            
            
            EDward_Gaming_table = tabulate(EDward_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, EDward_Gaming.shape[0]+1))        
            st.write(EDward_Gaming_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Victory Five"):
            
            
            Victory_Five_table = tabulate(Victory_Five, headers = 'keys', tablefmt = 'html',showindex = range(1, Victory_Five.shape[0]+1))        
            st.write(Victory_Five_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Anyone's Legend"):
            
            
            Anyones_Legend_table = tabulate(Anyones_Legend, headers = 'keys', tablefmt = 'html',showindex = range(1, Anyones_Legend.shape[0]+1))        
            st.write(Anyones_Legend_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Top Esports"):
            
            
            Top_Esports_table = tabulate(Top_Esports, headers = 'keys', tablefmt = 'html',showindex = range(1, Top_Esports.shape[0]+1))        
            st.write(Top_Esports_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Ultra Prime"):
            
            
            Ultra_Prime_table = tabulate(Ultra_Prime, headers = 'keys', tablefmt = 'html',showindex = range(1, Ultra_Prime.shape[0]+1))        
            st.write(Ultra_Prime_table, unsafe_allow_html=True)
            
        if st.sidebar.button("LGD Gaming"):
            
            
            LGD_Gaming_table = tabulate(LGD_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, LGD_Gaming.shape[0]+1))        
            st.write(LGD_Gaming_table, unsafe_allow_html=True)
            
        if st.sidebar.button("ThunderTalk Gaming"):
            
            
            ThunderTalk_Gaming_table = tabulate(ThunderTalk_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, ThunderTalk_Gaming.shape[0]+1))        
            st.write(ThunderTalk_Gaming_table, unsafe_allow_html=True)
            
        if st.sidebar.button("LNG Esports"):
            
            
            LNG_Esports_table = tabulate(LNG_Esports, headers = 'keys', tablefmt = 'html',showindex = range(1, LNG_Esports_Up.shape[0]+1))        
            st.write(LNG_Esports_table, unsafe_allow_html=True)
            
        if st.sidebar.button("Team WE"):
            
            
            Team_WE_table = tabulate(Team_WE, headers = 'keys', tablefmt = 'html',showindex = range(1, Team_WE.shape[0]+1))        
            st.write(Team_WE_table, unsafe_allow_html=True)
            
        if st.sidebar.button("FunPlus Phoenix"):
            
            
            FunPlus_Phoenix_table = tabulate(FunPlus_Phoenix, headers = 'keys', tablefmt = 'html',showindex = range(1, FunPlus_Phoenix.shape[0]+1))        
            st.write(FunPlus_Phoenix, unsafe_allow_html=True)

##CBLOL##            
            
elif opcao_selecionada == "CBLOL":
        st.write("Ao clicar ao lado é possível ver uma tabela para cada time do CBLOL. Nesta tabela são fornecidos os principais dados médios de como os jogadores impactam em seus times.")
        if st.sidebar.button("FURIA"):
            
            
            FURIA = tabulate(FURIA, headers = 'keys', tablefmt = 'html',showindex = range(1, FURIA.shape[0]+1))        
            st.write(FURIA, unsafe_allow_html=True)
            
        if st.sidebar.button("LOUD"):
            
            
            LOUD = tabulate(LOUD, headers = 'keys', tablefmt = 'html',showindex = range(1, LOUD.shape[0]+1))        
            st.write(LOUD, unsafe_allow_html=True)
            
        if st.sidebar.button("PaiN Gaming"):
            
            
            PaiN_Gaming = tabulate(PaiN_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, PaiN_Gaming.shape[0]+1))        
            st.write(PaiN_Gaming, unsafe_allow_html=True)
            
        if st.sidebar.button("KaBuM! Esports"):
            
            
            KaBuM_Esports = tabulate(KaBuM_Esports, headers = 'keys', tablefmt = 'html',showindex = range(1, KaBuM_Esports.shape[0]+1))        
            st.write(KaBuM_Esports, unsafe_allow_html=True)
            
        if st.sidebar.button("Miners"):
            
            
            Miners = tabulate(Miners, headers = 'keys', tablefmt = 'html',showindex = range(1, Miners.shape[0]+1))        
            st.write(Miners, unsafe_allow_html=True)
            
        if st.sidebar.button("Liberty"):
            
            
            Liberty = tabulate(Liberty, headers = 'keys', tablefmt = 'html',showindex = range(1, Liberty.shape[0]+1))        
            st.write(Liberty, unsafe_allow_html=True)
            
        if st.sidebar.button("Flamengo Los Grandes"):
            
            
            Flamengo_Los_Grandes = tabulate(Flamengo_Los_Grandes, headers = 'keys', tablefmt = 'html',showindex = range(1, Flamengo_Los_Grandes.shape[0]+1))        
            st.write(Flamengo_Los_Grandes, unsafe_allow_html=True)
            
        if st.sidebar.button("INTZ"):
            
            
            INTZ = tabulate(INTZ, headers = 'keys', tablefmt = 'html',showindex = range(1, INTZ.shape[0]+1))        
            st.write(INTZ, unsafe_allow_html=True)
            
        if st.sidebar.button("Rensga Esports"):
            
            
            Rensga_Esports = tabulate(Rensga_Esports, headers = 'keys', tablefmt = 'html',showindex = range(1, Rensga_Esports.shape[0]+1))        
            st.write(Rensga_Esports, unsafe_allow_html=True)
            
        if st.sidebar.button("RED Canids"):
            
            
            RED_Canids = tabulate(RED_Canids, headers = 'keys', tablefmt = 'html',showindex = range(1, RED_Canids.shape[0]+1))        
            st.write(RED_Canids, unsafe_allow_html=True)

##LEC##            
            
elif opcao_selecionada == "LEC":
        st.write("Ao clicar ao lado é possível ver uma tabela para cada time da LEC. Nesta tabela são fornecidos os principais dados médios de como os jogadores impactam em seus times.")
        if st.sidebar.button("Misfits Gaming"):
            
            
            Misfits_Gaming = tabulate(Misfits_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, Misfits_Gaming.shape[0]+1))        
            st.write(Misfits_Gaming, unsafe_allow_html=True)
            
        if st.sidebar.button("Excel Esports"):
            
            
            Excel_Esports = tabulate(Excel_Esports, headers = 'keys', tablefmt = 'html',showindex = range(1, Excel_Esports.shape[0]+1))        
            st.write(Excel_Esports, unsafe_allow_html=True)
            
        if st.sidebar.button("Fnatic"):
            
            
            Fnatic = tabulate(Fnatic, headers = 'keys', tablefmt = 'html',showindex = range(1, Fnatic.shape[0]+1))        
            st.write(Fnatic, unsafe_allow_html=True)
            
        if st.sidebar.button("Team Vitality"):
            
            
            Team_Vitality = tabulate(Team_Vitality, headers = 'keys', tablefmt = 'html',showindex = range(1, Team_Vitality.shape[0]+1))        
            st.write(Team_Vitality, unsafe_allow_html=True)
            
        if st.sidebar.button("MAD Lions"):
            
            
            MAD_Lions = tabulate(MAD_Lions, headers = 'keys', tablefmt = 'html',showindex = range(1, MAD_Lions.shape[0]+1))        
            st.write(MAD_Lions, unsafe_allow_html=True)
            
        if st.sidebar.button("G2 Esports"):
            
            
            G2_Esports = tabulate(G2_Esports, headers = 'keys', tablefmt = 'html',showindex = range(1, G2_Esports.shape[0]+1))        
            st.write(G2_Esports, unsafe_allow_html=True)
            
        if st.sidebar.button("Rogue"):
            
            
            Rogue_European_Team = tabulate(Rogue_European_Team, headers = 'keys', tablefmt = 'html',showindex = range(1, Rogue_European_Team.shape[0]+1))        
            st.write(Rogue_European_Team, unsafe_allow_html=True)
            
        if st.sidebar.button("SK Gaming"):
            
            
            SK_Gaming = tabulate(SK_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, SK_Gaming.shape[0]+1))        
            st.write(SK_Gaming, unsafe_allow_html=True)
            
        if st.sidebar.button("Astralis"):
            
            
            Astralis = tabulate(Astralis, headers = 'keys', tablefmt = 'html',showindex = range(1, Astralis.shape[0]+1))        
            st.write(Astralis, unsafe_allow_html=True)
            
        if st.sidebar.button("Team BDS"):
            
            
            Team_BDS = tabulate(Team_BDS, headers = 'keys', tablefmt = 'html',showindex = range(1, Team_BDS.shape[0]+1))        
            st.write(Team_BDS, unsafe_allow_html=True)

##LCS##            
            
elif opcao_selecionada == "LCS":
        st.write("Ao clicar ao lado é possível ver uma tabela para cada time da LCS. Nesta tabela são fornecidos os principais dados médios de como os jogadores impactam em seus times.")
        if st.sidebar.button("Cloud9"):
            
            
            Cloud9 = tabulate(Cloud9, headers = 'keys', tablefmt = 'html',showindex = range(1, Cloud9.shape[0]+1))        
            st.write(Cloud9, unsafe_allow_html=True)
            
        if st.sidebar.button("FlyQuest"):
            
            
            FlyQuest = tabulate(FlyQuest, headers = 'keys', tablefmt = 'html',showindex = range(1, FlyQuest.shape[0]+1))        
            st.write(FlyQuest, unsafe_allow_html=True)
            
        if st.sidebar.button("Evil Geniuses"):
            
            
            Evil_GeniusesNA = tabulate(Evil_GeniusesNA, headers = 'keys', tablefmt = 'html',showindex = range(1, Evil_GeniusesNA.shape[0]+1))        
            st.write(Evil_GeniusesNA, unsafe_allow_html=True)
            
        if st.sidebar.button("100 Thieves"):
            
            
            _Thieves = tabulate(_Thieves, headers = 'keys', tablefmt = 'html',showindex = range(1, _Thieves.shape[0]+1))        
            st.write(_Thieves, unsafe_allow_html=True)
            
        if st.sidebar.button("Team Liquid"):
            
            
            Team_Liquid = tabulate(Team_Liquid, headers = 'keys', tablefmt = 'html',showindex = range(1, Team_Liquid.shape[0]+1))        
            st.write(Team_Liquid, unsafe_allow_html=True)
            
        if st.sidebar.button("Counter Logic Gaming"):
            
            
            Counter_Logic_Gaming = tabulate(Counter_Logic_Gaming, headers = 'keys', tablefmt = 'html',showindex = range(1, Counter_Logic_Gaming.shape[0]+1))        
            st.write(Counter_Logic_Gaming, unsafe_allow_html=True)
            
        if st.sidebar.button("Golden Guardians"):
            
            
            Golden_Guardians = tabulate(Golden_Guardians, headers = 'keys', tablefmt = 'html',showindex = range(1, Golden_Guardians.shape[0]+1))        
            st.write(Golden_Guardians, unsafe_allow_html=True)
            
        if st.sidebar.button("Immortals"):
            
            
            Immortals = tabulate(Immortals, headers = 'keys', tablefmt = 'html',showindex = range(1, Immortals.shape[0]+1))        
            st.write(Immortals, unsafe_allow_html=True)
            
        if st.sidebar.button("Dignitas"):
            
            
            Dignitas = tabulate(Dignitas, headers = 'keys', tablefmt = 'html',showindex = range(1, Dignitas.shape[0]+1))        
            st.write(Dignitas, unsafe_allow_html=True)
            
        if st.sidebar.button("TSM"):
            
            
            TSM = tabulate(TSM, headers = 'keys', tablefmt = 'html',showindex = range(1, TSM.shape[0]+1))        
            st.write(TSM, unsafe_allow_html=True)
            
            
elif opcao_selecionada == "REGRESSÃO":
        st.write("Aqui apresentamos uma regressão linear com estimador de MQO")
        
        df["winrate"] = df["win"].astype(int) / (df["win"].astype(int) + df["lose"].astype(int))
        df[["dmgpergold", "champplayed"]] = df[["dmgpergold", "champplayed"]].astype(float)

        y = df["winrate"]
        X = df[["dmgpergold", "champplayed"]]

        model = sm.OLS(y, X)
        results = model.fit()
        
        st.write(results.summary())
        
        st.write('') 
        st.write("A partir dos resultados apresentados, é possível concluir que ambos os coeficientes 'dmgpergold' e 'champplayed' são estatisticamente significativos para o modelo. Além disso, o p-valor para ambos os coeficientes é muito pequeno, o que sugere que há uma forte evidência de que a relação entre as variáveis independentes e a variável dependente é significativa. Como o valor dos coeficientes são positivos é de se esperar que quanto maior for o Dano por Gold e quanto maior for a quantidade de campeões jogados maior será a taxa de vitória.") 
            
           
            
### MLB ALL
# Will using PCA method and cluster all the MLB players based on each positon
# Goals: Graph everything and display plots
# Next Version: Create Graphs based soloy on teams (Ideally with a User interface)

## Packages/functions
import csv
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pylab

## Homebrewed functions

## List of all the Columns the CVS file has
# The this is so we can label each column
Colnames = ['Player','Team','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','SH','SF','HBP','AVG','OBP','SLG','OPS']
Colnames_Batters = ['Player','Team','Pos','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','SH','SF','HBP','AVG','OBP','SLG','OPS']
Colnames_Pitchers = ['Player','Team','G','GS','CG','SHO','IP','H','ER','K','BB','HR','W','L','SV','BS','HLD','ERA','WHIP']
Data_Cols_Names_Pitchers = ['G','GS','CG','SHO','IP','H','ER','K','BB','HR','W','L','SV','BS','HLD','ERA','WHIP']
Data_Cols_Names = ['G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','SH','SF','HBP','AVG','OBP','SLG','OPS']

## Extracting CSV data and labels the Columns with titles
FirstB = pd.read_csv("mlb-player-stats-1B.csv", names = Colnames)
SecondB = pd.read_csv("mlb-player-stats-2B.csv", names = Colnames)
ThirdB = pd.read_csv("mlb-player-stats-3B.csv", names = Colnames)
Batters = pd.read_csv("mlb-player-stats-Batters.csv", names = Colnames_Batters)
Catchers = pd.read_csv("mlb-player-stats-C.csv", names = Colnames)
DesignatedHitters = pd.read_csv("mlb-player-stats-DH.csv", names = Colnames)
Outfielders = pd.read_csv("mlb-player-stats-OF.csv", names = Colnames)
Pitchers = pd.read_csv("mlb-player-stats-P.csv", names = Colnames_Pitchers)
Shortstops = pd.read_csv("mlb-player-stats-SS.csv", names = Colnames)

## Seperating the Players' Names, Team, Position, and the Players' Data
# Note: I think in Baseball, players player more than one position.
# For example: All players have to bat (I think)
# First Base
FirstB_Info = FirstB.loc[1:,['Player', 'Team']].values
FirstB_Names = FirstB.loc[1:,['Player']].values
FirstB_Data = FirstB.loc[1:,Data_Cols_Names].values
# Second Base
SecondB_Info = SecondB.loc[1:,['Player', 'Team']].values
SecondB_Names = SecondB.loc[1:,['Player']].values
SecondB_Data = SecondB.loc[1:,Data_Cols_Names].values
# Third base
ThirdB_Info = ThirdB.loc[1:,['Player', 'Team']].values
ThirdB_Names = ThirdB.loc[1:,['Player']].values
ThirdB_Data = ThirdB.loc[1:,Data_Cols_Names].values
# Batters
Batters_Info = Batters.loc[1:,['Player', 'Team','Pos']].values
Batters_Names = Batters.loc[1:,['Player']].values
Batters_Data = Batters.loc[1:,Data_Cols_Names].values
# Catchers
Catchers_Info = Catchers.loc[1:,['Player', 'Team']].values
Catchers_Names = Catchers.loc[1:,['Player']].values
Catchers_Data = Catchers.loc[1:,Data_Cols_Names].values
# Designated Hitters
DesignatedHitters_Info = DesignatedHitters.loc[1:,['Player', 'Team']].values
DesignatedHitters_Names = DesignatedHitters.loc[1:,['Player']].values
DesignatedHitters_Data = DesignatedHitters.loc[1:,Data_Cols_Names].values
# Outfielders
Outfielders_Info = Outfielders.loc[1:,['Player', 'Team']].values
Outfielders_Names = Outfielders.loc[1:,['Player']].values
Outfielders_Data = Outfielders.loc[1:,Data_Cols_Names].values

# Pitchers
Pitchers_Info = Pitchers.loc[1:,['Player', 'Team']].values
Pitchers_Names = Pitchers.loc[1:,['Player']].values
Pitchers_Data = Pitchers.loc[1:,Data_Cols_Names_Pitchers].values
# Shortstops
Shortstops_Info = Shortstops.loc[1:,['Player', 'Team']].values
Shortstops_Names = Shortstops.loc[1:,['Player']].values
Shortstops_Data = Shortstops.loc[1:,Data_Cols_Names].values

## PCA method
pca = PCA(2) # tells Python that we just want 2 columns
# First Base
FirstB_Data_pca =  pca.fit_transform(FirstB_Data)
FirstB_Data_pca = pd.DataFrame(data = FirstB_Data_pca, columns = ['pc1', 'pc2'])

# Second Base
SecondB_Data_pca =  pca.fit_transform(SecondB_Data)
SecondB_Data_pca = pd.DataFrame(data = SecondB_Data_pca, columns = ['pc1', 'pc2'])
# Third Base
ThirdB_Data_pca =  pca.fit_transform(ThirdB_Data)
ThirdB_Data_pca = pd.DataFrame(data = ThirdB_Data_pca, columns = ['pc1', 'pc2'])
# Batters
Batters_Data_pca =  pca.fit_transform(Batters_Data)
Batters_Data_pca = pd.DataFrame(data = Batters_Data_pca, columns = ['pc1', 'pc2'])
# Catchers
Catchers_Data_pca =  pca.fit_transform(Catchers_Data)
Catchers_Data_pca = pd.DataFrame(data = Catchers_Data_pca, columns = ['pc1', 'pc2'])
# Designated Hitters
DesignatedHitters_Data_pca =  pca.fit_transform(DesignatedHitters_Data)
DesignatedHitters_Data_pca = pd.DataFrame(data = DesignatedHitters_Data_pca, columns = ['pc1', 'pc2'])
# Outfielders
Outfielders_Data_pca =  pca.fit_transform(Outfielders_Data)
Outfielders_Data_pca = pd.DataFrame(data = Outfielders_Data_pca, columns = ['pc1', 'pc2'])
# Pitchers
Pitchers_Data_pca =  pca.fit_transform(Pitchers_Data)
Pitchers_Data_pca = pd.DataFrame(data = Pitchers_Data_pca, columns = ['pc1', 'pc2'])
# Shortstops
Shortstops_Data_pca =  pca.fit_transform(Shortstops_Data)
Shortstops_Data_pca = pd.DataFrame(data = Shortstops_Data_pca, columns = ['pc1', 'pc2'])

## Creating Scatter Plots of the PCA data
# Note: panda's data tables require dataset[row][col] to locate single points

#######################
# First Base
fig_FirstB, ax_FirstB = plt.subplots()
ax_FirstB.scatter(FirstB_Data_pca['pc1'], FirstB_Data_pca['pc2']) # flipping the y-axis of the plot to look similar to matlab's
    # This will add the player names to their data points
for i, txt in enumerate(FirstB_Names):
    ax_FirstB.annotate(txt, (FirstB_Data_pca['pc1'][i], FirstB_Data_pca['pc2'][i]))
fig_FirstB = plt.scatter(FirstB_Data_pca['pc1'], FirstB_Data_pca['pc2'])
plt.title('First Base Cluster')
#pylab.show(fig_FirstB) # Python needs this to keep the figure displayed

# Second Base
fig_SecondB, ax_SecondB = plt.subplots()
ax_SecondB.scatter(SecondB_Data_pca['pc1'], SecondB_Data_pca['pc2'],)
for i, txt in enumerate(SecondB_Names):
    ax_SecondB.annotate(txt, (SecondB_Data_pca['pc1'][i], SecondB_Data_pca['pc2'][i]))
fig_SecondB = plt.scatter(SecondB_Data_pca['pc1'], SecondB_Data_pca['pc2'])
plt.title('Second Base Cluster')

# Third Base
fig_ThirdB, ax_ThirdB = plt.subplots()
ax_ThirdB.scatter(ThirdB_Data_pca['pc1'], ThirdB_Data_pca['pc2'],)
for i, txt in enumerate(ThirdB_Names):
    ax_ThirdB.annotate(txt, (ThirdB_Data_pca['pc1'][i], ThirdB_Data_pca['pc2'][i]))
fig_ThirdB = plt.scatter(ThirdB_Data_pca['pc1'], ThirdB_Data_pca['pc2'])
plt.title('Third Base Cluster')

# Batters
fig_Batters, ax_Batters = plt.subplots()
ax_Batters.scatter(Batters_Data_pca['pc1'], Batters_Data_pca['pc2'],)
for i, txt in enumerate(Batters_Names):
    ax_Batters.annotate(txt, (Batters_Data_pca['pc1'][i], Batters_Data_pca['pc2'][i]))
fig_Batters = plt.scatter(Batters_Data_pca['pc1'], Batters_Data_pca['pc2'])
plt.title('Batters Cluster')

# Catchers
fig_Catchers, ax_Catchers = plt.subplots()
ax_Catchers.scatter(Catchers_Data_pca['pc1'], Catchers_Data_pca['pc2'],)
for i, txt in enumerate(Catchers_Names):
    ax_Catchers.annotate(txt, (Catchers_Data_pca['pc1'][i], Catchers_Data_pca['pc2'][i]))
fig_Catchers = plt.scatter(Catchers_Data_pca['pc1'], Catchers_Data_pca['pc2'])
plt.title('Catchers Cluster')

# DesignatedHitters
fig_DesignatedHitters, ax_DesignatedHitters = plt.subplots()
ax_DesignatedHitters.scatter(DesignatedHitters_Data_pca['pc1'], DesignatedHitters_Data_pca['pc2'],)
for i, txt in enumerate(DesignatedHitters_Names):
    ax_DesignatedHitters.annotate(txt, (DesignatedHitters_Data_pca['pc1'][i], DesignatedHitters_Data_pca['pc2'][i]))
fig_DesignatedHitters = plt.scatter(DesignatedHitters_Data_pca['pc1'], DesignatedHitters_Data_pca['pc2'])
plt.title('Designated Hitters Cluster')

# Outfielders
fig_Outfielders, ax_Outfielders = plt.subplots()
ax_Outfielders.scatter(Outfielders_Data_pca['pc1'], Outfielders_Data_pca['pc2'],)
for i, txt in enumerate(Outfielders_Names):
    ax_Outfielders.annotate(txt, (Outfielders_Data_pca['pc1'][i], Outfielders_Data_pca['pc2'][i]))
fig_Outfielders = plt.scatter(Outfielders_Data_pca['pc1'], Outfielders_Data_pca['pc2'])
plt.title('Outfielders Cluster')

# Pitchers (Yes, there are 600+ pitchers in 2019)
fig_Pitchers, ax_Pitchers = plt.subplots()
ax_Pitchers.scatter(Pitchers_Data_pca['pc1'], Pitchers_Data_pca['pc2'],)
for i, txt in enumerate(Pitchers_Names):
    ax_Pitchers.annotate(txt, (Pitchers_Data_pca['pc1'][i], Pitchers_Data_pca['pc2'][i]))
fig_Pitchers = plt.scatter(Pitchers_Data_pca['pc1'], Pitchers_Data_pca['pc2'])
plt.title('Pitchers Cluster')

#Shortstops
fig_Shortstops, ax_Shortstops = plt.subplots()
ax_Shortstops.scatter(Shortstops_Data_pca['pc1'], Shortstops_Data_pca['pc2'],)
for i, txt in enumerate(Shortstops_Names):
    ax_Shortstops.annotate(txt, (Shortstops_Data_pca['pc1'][i], Shortstops_Data_pca['pc2'][i]))
fig_Shortstops = plt.scatter(Shortstops_Data_pca['pc1'], Shortstops_Data_pca['pc2'])
plt.title('Shortstops Cluster')

pylab.show()
###### Fucntions ########

###### Write to CSV File ##########
# First Base PCA to CSV
dataset = DataFrame(FirstB_Data_pca)
df= dataset.to_csv (r'export/FirstB_pca.csv', index = None, header=True)
print(dataset)

# Second Base PCA to CSV
dataset = DataFrame(SecondB_Data_pca, columns= ['pc1', 'pc2'])
df= dataset.to_csv (r'export/SecondB_pca.csv', index = None, header=True)
print(dataset)

# Third Base PCA to CSV
dataset = DataFrame(ThirdB_Data_pca, columns= ['pc1', 'pc2'])
df= dataset.to_csv (r'export/ThirdB_pca.csv', index = None, header=True)
print(dataset)

# Batters PCA to CSV
dataset = DataFrame(Batters_Data_pca, columns= ['pc1', 'pc2'])
df= dataset.to_csv (r'export/Batters_pca.csv', index = None, header=True)
print(dataset)

# Catchers PCA to CSV
dataset = DataFrame(Catchers_Data_pca, columns= ['pc1', 'pc2'])
df= dataset.to_csv (r'export/Catchers_pca.csv', index = None, header=True)
print(dataset)

# Designated Hitters PCA to CSV
dataset = DataFrame(DesignatedHitters_Data_pca, columns= ['pc1', 'pc2'])
df= dataset.to_csv (r'export/DesignatedHitters_pca.csv', index = None, header=True)
print(dataset)

# Outfielders PCA to CSV
dataset = DataFrame(Outfielders_Data_pca, columns= ['pc1', 'pc2'])
df= dataset.to_csv (r'export/Outfielders_pca.csv', index = None, header=True)
print(dataset)

# Pitchers PCA to CSV
dataset = DataFrame(Pitchers_Data_pca, columns= ['pc1', 'pc2'])
df= dataset.to_csv (r'export/Pitchers_pca.csv', index = None, header=True)
print(dataset)

# Shortstops PCA to CSV
dataset = DataFrame(Shortstops_Data_pca, columns= ['pc1', 'pc2'])
df= dataset.to_csv (r'export/Shortstops_pca.csv', index = None, header=True)
print(dataset)


##### Create List of player names ########
# First Base Names
dataset = DataFrame(FirstB_Info, columns= ['Player','Team'])
df= dataset.to_csv (r'export/FirstB_Names.csv', index = None, header=True)
print(dataset)

# Second Base Names
dataset = DataFrame(SecondB_Info, columns= ['Player','Team'])
df= dataset.to_csv (r'export/SecondB_Names.csv', index = None, header=True)
print(dataset)

# Third Base Names
dataset = DataFrame(ThirdB_Info, columns= ['Player','Team'])
df= dataset.to_csv (r'export/ThirdB_Names.csv', index = None, header=True)
print(dataset)

# Batters Names
dataset = DataFrame(Batters_Info, columns= ['Player','Team','Pos'])
df= dataset.to_csv (r'export/Batters_Names.csv', index = None, header=True)
print(dataset)

# Catchers Names
dataset = DataFrame(Catchers_Info, columns= ['Player','Team'])
df= dataset.to_csv (r'export/Catchers_Names.csv', index = None, header=True)
print(dataset)

# DesignatedHitters Names
dataset = DataFrame(DesignatedHitters_Info, columns= ['Player','Team'])
df= dataset.to_csv (r'export/DesignatedHitters_Names.csv', index = None, header=True)
print(dataset)

# Outfielders Names
dataset = DataFrame(Outfielders_Info, columns= ['Player','Team'])
df= dataset.to_csv (r'export/Outfielders_Names.csv', index = None, header=True)
print(dataset)

# Pitchers Names
dataset = DataFrame(Pitchers_Info, columns= ['Player','Team'])
df= dataset.to_csv (r'export/Pitchers_Names.csv', index = None, header=True)
print(dataset)


# ShortstopsNames
dataset = DataFrame(Shortstops_Info, columns= ['Player','Team'])
df= dataset.to_csv (r'export/Shortstops_Names.csv', index = None, header=True)
print(dataset)

print(Pitchers_Info)

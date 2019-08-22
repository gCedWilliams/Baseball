### MLB ALL Create a list of the 10 best players to pick for a position

## Packages/funcitions
import csv
import numpy as np
from math import sqrt
import pandas as pd
from pandas import DataFrame

# Extracting PCA vectors
FirstB_PCA = pd.read_csv("export/FirstB_pca.csv")

# Extracting Player Names for Positions
FirstB_Names = pd.read_csv("export/FirstB_Names.csv", names = ['Players','Team'])
#print(FirstB_Names)
#FirstB_PCA.drop(['pc1', 'pc2'], axis=1)

#FirstB_max = pd.DataFrame.max(FirstB_PCA['pc1'])
#print(FirstB_max)

# God Player
God = [-150,35] # God[0] = -150 and God[1] = 35
# Combining Datasets
FirstB = FirstB_PCA.join(FirstB_Names)
#print(FirstB['pc1'][0])

# create list of the best Players
Closiest_to_God = np.empty([len(FirstB),1])
count = 0
while count < len(FirstB):
    Closiest_to_God[count][0] = sqrt(((FirstB['pc1'][count] - God[0])**2) + ((FirstB['pc2'][count] - God[1])**2))
    #Closiest_to_God[count][1] = FirstB_Names['Players'][count+1]
    #print(Closiest_to_God[count][0])
#    print(count)
    count += 1
    if count >= len(FirstB):
        break
Closiest_to_God = np.hstack((Closiest_to_God, FirstB_Names[1:]))
# Attaches the names of each player to their Euclidean distance to God

Closiest_to_God = Closiest_to_God[Closiest_to_God[:,0].argsort()]
print(Closiest_to_God)

##Export to CSV
dataset = DataFrame(Closiest_to_God)
df= dataset.to_csv (r'export/FirstB_List.csv', index = None, header=True)
print(dataset)

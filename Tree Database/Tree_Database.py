
''' Variable definitions
defining and opening the file containing information on trees.
Then, defining lists for each of the different tree characteristics.
Creating a matrix for all tree data in the same order as the tree data file.
'''

common_Name = []
symbol = []
scientific_Name = []
family_Symbol = []
family_Common_Name = []
active_Growth_Period = []
fall_Conspicuous = []
flower_Color = []
flower_Conspicuous = []
foliage_Color = []
foliage_Texture = []
fruit_Color = []
fruit_Conspicuous = []
leaf_Retention = []
shape_and_Orientation = []
bloom_Period = []
commercial_Availability = []

treeLibrary = [common_Name, symbol, scientific_Name, family_Symbol, family_Common_Name, active_Growth_Period, 
    fall_Conspicuous, flower_Color, flower_Conspicuous, foliage_Color, foliage_Texture, 
    fruit_Color, fruit_Conspicuous, leaf_Retention, shape_and_Orientation, bloom_Period, commercial_Availability]

#common_Name.append("pacific silver fir")

treeInfo = [] 
#will define each tree characteristic into its associated list. 
#Each of the list's indexes correlate to the same tree using the for loop.

with open("TreeData.csv") as treeData:
    if treeData.tell() == 0:
        treeBuffer = [line for line in treeData] #this automatically breaks each line into a different list element
        x = 0 #variable used to increase the element that treeBuffer changes throughout the while loop. must sequentailly advance to keep pace with loop        
        while len(treeBuffer) - x > 0:
            treeInfo.append(treeBuffer[x].split(','))
            ''' the above line adds each line within the excel file as a new list element but inside each list element,
                each data item that is separated by a comma is put into a different secondary/sublist element'''
            x += 1

'''the below while loop makes each tree's information appropriately fall into its designated category/list. the identical elements of each category
correlate to the same tree so the common_Name[0] is the same tree as flower_Color[0]'''
x = 0
while len(treeBuffer) - x > 0:
    common_Name.append(treeInfo[x][0])
    symbol.append(treeInfo[x][1])
    scientific_Name.append(treeInfo[x][2])
    family_Symbol.append(treeInfo[x][3])
    family_Common_Name.append(treeInfo[x][4])
    active_Growth_Period.append(treeInfo[x][5])
    fall_Conspicuous.append(treeInfo[x][6])
    flower_Color.append(treeInfo[x][7])
    flower_Conspicuous.append(treeInfo[x][8])
    foliage_Color.append(treeInfo[x][9])
    foliage_Texture.append(treeInfo[x][10])
    fruit_Color.append(treeInfo[x][11])
    fruit_Conspicuous.append(treeInfo[x][12])
    leaf_Retention.append(treeInfo[x][13])
    shape_and_Orientation.append(treeInfo[x][14])
    bloom_Period.append(treeInfo[x][15])
    commercial_Availability.append(treeInfo[x][16])
    x+=1



            
            

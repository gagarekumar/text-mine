import  os
import xlrd

directory="Breastcancer"

parent_dir= "F:\BE-PROJECT\TEXT MINING"

path=os.path.join(parent_dir,directory)

os.mkdir(path)

print ("Directory %s created" %directory)

os.chdir(path)

with open('1.txt','w') as fp:
    fp.write('new file created')

loc ="F:\BE-PROJECT\TEXT MINING\hello.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
abstract=[]
for j in range(sheet.ncols):
    for i in range(sheet.nrows):
        abstract.append(sheet.cell_value(i, j))

for i in range(len(abstract)):
    with open('%s.txt'%i,'w',encoding="utf-8") as fp:
        fp.write(abstract[i])
print(abstract)





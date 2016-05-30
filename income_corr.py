import xlrd
import scipy.stats
data = xlrd.open_workbook('../re_new.xlsx')
table = data.sheets()[1]
nrows = table.nrows
x = table.col_values(2);
coln = table.ncols
pear = []
kend = []
spear = []
for i in range(3,coln):
    y = table.col_values(i)
    col,pval = scipy.stats.pearsonr(x,y)
    tau, p_value = scipy.stats.kendalltau(x, y)
    rho, pval = scipy.stats.spearmanr(x, y)
    pear.append(col)
    kend.append(tau)
    spear.append(rho)
file_object = open('result.txt','w')
for i in range(len(pear)):
	file_object.write(str(i)+" "+str(pear[i])+" | "+str(kend[i])+" | "+str(spear[i])+'\n')
#print pear
#print kend
#print spear
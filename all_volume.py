from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import seaborn

import cProfile
import bayesian_changepoint_detection.offline_changepoint_detection as offcd
import bayesian_changepoint_detection.generate_data as gd
from functools import partial
from xlwt import Workbook
import xlwt
import xlrd

if __name__ == '__main__':
  show_plot = True
  dim = 2
  data = xlrd.open_workbook('../re_new.xlsx')
  table1 = data.sheets()[1]
  table2 = data.sheets()[2]
  nrows1 = table1.nrows
  nrows2 = table2.nrows
  x = []
  z = []
  for i in range(nrows1):
    index = table1.cell_value(i,3)
    index = float(index)
    re = table1.cell_value(i,2)
    re = float(re)
    if index == 0 or re == 0:
      continue
    y = []
    z.append(i)
    y.append(index)
    y.append(re)
    x.append(y)
    #print index
  arr1 = np.array(x)
  Q_1, P_1, Pcp_1 = offcd.offline_changepoint_detection(arr1,partial(offcd.const_prior, l=(len(arr1)+1)),offcd.gaussian_obs_log_likelihood, truncate=-20)
  ccc = np.exp(Pcp_1).sum(0)
  file_object = open('volume_days1.txt','w')
  for k in range(len(ccc)):
        if ccc[k]>0.01:
            file_object.write("days "+str(z[k])+" probability "+str(ccc[k])+'\n')
  file_object.close()
#      st.pattern.pattern_fore_colour = 4
#      sheet1.write(k,0,xxx,st)
#    else:
#      st.pattern.pattern_fore_colour = 2
#      sheet1.write(k,0,xxx,st)
#    f= f+1
#  book.save(after.xlsx) 

  #nrows1_2 = table1.nrows
  #nrows2_2 = table2.nrows
#  x = []
#  pre = 0;
#  temp = 0;
#  for i in range(nrows2):
#    index = table2.cell_value(i,3)
#    temp = float(index)
#    if i !=0 and pre != 0:
#        index = float(float(index)-pre)/pre*100
#    else:
#        index = 0
#    pre = temp
#   re = table2.cell_value(i,2)
#    re = float(re)
#    if index == 0 or re == 0:
#      continue
#    y = []
#    y.append(index)
#    y.append(re)
#    x.append(y)
#  arr2 = np.array(x)

#  Q_1, P_1, Pcp_1 = offcd.offline_changepoint_detection(arr1,partial(offcd.const_prior, l=(len(arr1)+1)),offcd.gaussian_obs_log_likelihood, truncate=-20)
#  Q_2, P_2, Pcp_2 = offcd.offline_changepoint_detection(arr2,partial(offcd.const_prior, l=(len(arr2)+1)),offcd.gaussian_obs_log_likelihood, truncate=-20)
  #Q_ifm, P_ifm, Pcp_ifm = offcd.offline_changepoint_detection(arr,partial(offcd.const_prior, l=(len(arr)+1)),offcd.ifm_obs_log_likelihood,truncate=-20)

  #Q_full, P_full, Pcp_full = offcd.offline_changepoint_detection(arr,partial(offcd.const_prior, l=(len(arr)+1)),offcd.fullcov_obs_log_likelihood, truncate=-20)

  if show_plot:
    fig, ax = plt.subplots(figsize=[18, 16])
  #  ax = fig.add_subplot(2, 1, 1)
  #  for p in changes:
  #    ax.plot([p,p],[np.min(data),np.max(data)],'r')
    #for d in range(dim):
    #  ax.plot(arr[:,d])
      #print arr[:,d]
      #print d
    #ax = fig.add_subplot(2, 1, 2, sharex=ax)
    ax.plot(ccc,'r')
  #  ax.plot(np.exp(Pcp_2).sum(0),'b')
    plt.show()
  
  #volume = np.exp(Pcp_1).sum(0)
  #income = np.exp(Pcp_2).sum(0)
  #file_object = open('volume_income.txt','w')
  #for i in range(len(volume)):
  #  file_object.write("days "+str(i)+" volume: "+str(volume[i])+" income: "+str(income[i])+'\n')
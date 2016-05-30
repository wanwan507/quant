from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import seaborn

import cProfile
import bayesian_changepoint_detection.offline_changepoint_detection as offcd
import bayesian_changepoint_detection.generate_data as gd
from functools import partial
import xlrd

if __name__ == '__main__':
  show_plot = True
  dim = 2
  data1 = xlrd.open_workbook('../in_new.xlsx')
  data2 = xlrd.open_workbook('../re_new.xlsx')
  table1 = data1.sheets()[0]
  table2 = data2.sheets()[1]
  nrows1 = table1.nrows
  nrows2 = table2.nrows
  x = []
  pre = 0;
  temp = 0;
  for i in range(nrows1):
    index = table1.cell_value(i,4)
    temp = float(index)
    if i !=0:
      index = float(float(index)-pre)/pre*100
    else:
      index = 0
    pre = temp
    re = table2.cell_value(i,2)
    re = float(re)
    y = []
    y.append(index)
    y.append(re)
    x.append(y)
    #print index
  arr = np.array(x)

  #Q, P, Pcp = offcd.offline_changepoint_detection(arr,partial(offcd.const_prior, l=(len(arr)+1)),offcd.gaussian_obs_log_likelihood, truncate=-20)
  #Q_ifm, P_ifm, Pcp_ifm = offcd.offline_changepoint_detection(arr,partial(offcd.const_prior, l=(len(arr)+1)),offcd.ifm_obs_log_likelihood,truncate=-20)

  Q_full, P_full, Pcp_full = offcd.offline_changepoint_detection(arr,partial(offcd.const_prior, l=(len(arr)+1)),offcd.fullcov_obs_log_likelihood, truncate=-20)

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
    ax.plot(np.exp(Pcp_full).sum(0),'k')
    plt.show()
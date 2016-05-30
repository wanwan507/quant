import cProfile
import bayesian_changepoint_detection.offline_changepoint_detection as offcd
import bayesian_changepoint_detection.generate_data as gd
from functools import partial
import xlrd

if __name__ == '__main__':
  show_plot = True

  data = xlrd.open_workbook('../in_new.xlsx')
  table = data.sheets()[0]
  nrows = table.nrows
  dim = 4
  x = []
  maxn = []
  minn = []
  for q in range(1,5):
    he = table.col_values(q);
    he = [float(mm) for mm in he]
    crr = np.array(he)
    maxn.append(crr.max())
    minn.append(crr.min())

  ope = []
  clo = []
  for p in range(nrows):
    temp = table.row_values(p, start_colx=1,end_colx=5)
    ope.append(float(temp[0]))
    clo.append(float(temp[3]))
    for q in range(len(temp)):
      temp[q] = (float(temp[q])-minn[q])/(maxn[q]-minn[q])
    x.append(temp)
  arr = np.array(x)
  #print arr 



  Q, P, Pcp = offcd.offline_changepoint_detection(arr,partial(offcd.const_prior, l=(len(arr)+1)),offcd.gaussian_obs_log_likelihood, truncate=-20)
  #Q_ifm, P_ifm, Pcp_ifm = offcd.offline_changepoint_detection(arr,partial(offcd.const_prior, l=(len(arr)+1)),offcd.ifm_obs_log_likelihood,truncate=-20)

  #Q_full, P_full, Pcp_full = offcd.offline_changepoint_detection(arr,partial(offcd.const_prior, l=(len(arr)+1)),offcd.fullcov_obs_log_likelihood, truncate=-20)


  if show_plot:
    fig, ax = plt.subplots(figsize=[18, 16])
    #ax = fig.add_subplot(2, 1, 1)
  #  for p in changes:
  #    ax.plot([p,p],[np.min(data),np.max(data)],'r')
    for d in range(dim):
      ax.plot(arr[:,d])
      #print arr[:,d]
      #print d
    #ax = fig.add_subplot(2, 1, 2, sharex=ax)
    ax.plot(np.exp(Pcp_full).sum(0),'k')
    plt.show()

  #print Pcp

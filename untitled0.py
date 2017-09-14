# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 14:41:40 2017

@author: James
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calendar as cal

def make_dict(fun, cols):
    result = {}
    for c in cols:
        result[c] = fun
    return result

df = pd.read_csv('C:\Users\James\Downloads\construction.csv')

list_months = cal.month_abbr[1:13]
months = dict(zip(range(1,13),cal.month_abbr[1:13]))

df = df.assign(mon = df.Month % 12)
df.loc[df.mon == 0, 'mon'] = 12

df = df.assign(Month = df.mon)

mon_abbr = []
for val in df['mon']:
    mon_abbr.append(months[val])

df = df.assign(mon = mon_abbr)

temp = np.array(range(146))
temp = (temp // 12) + 2002
df = df.assign(Year = temp)

by_year = df.groupby('Year')
by_month = df.groupby('Month')
by_m = df.groupby('mon')

cols_list = ['Total Construction', 'Public Construction', 'Private Construction']

means = make_dict('mean', cols_list)
meds = make_dict('median', cols_list)

##keys are months
##values are list of rows (or in this case, the slice of construction amounts)
#totals_list = {}
#public_list = {}
#private_list = {}
#for key in by_m.groups.keys():
#    indices = by_m.groups[key] #indices in df which correspond to 'key' month
#    tottmp = []
#    pubtmp = []
#    pritmp = []
#    for index in indices:
#        const_tots = df.loc[index,][1:4].tolist() #grab list of Total, Private, Public
#        tottmp.append(const_tots[0])
#        pubtmp.append(const_tots[1])
#        pritmp.append(const_tots[2])
#    totals_list.update({key : tottmp})
#    public_list.update({key : pubtmp})
#    private_list.update({key : pritmp})
#
##fig, (ax1, ax2, ax3) = plt.subplots(1,3)
#fig, (ax1, ax2) = plt.subplots(1,2)
#
#tot_data = []
#pub_data = []
#pri_data = []
#for month in list_months:
#    tot_data.append(totals_list[month])
#    pub_data.append(public_list[month])
#    pri_data.append(private_list[month])
#    
#data_max = max([max(sublist) for sublist in tot_data])
#    
#fig.set_figheight(15)
#fig.set_figwidth(35)
#fig.add_axes
#
#ax1.boxplot(pri_data)
#ax2.boxplot(pub_data)
##ax3.boxplot(pri_data)
#
#for ax in (ax1, ax2):#, ax3):
#    ax.set_xticklabels(list_months)
#    ax.yaxis.axes.set_ylim(0, data_max + 10000)
#    ax.set_ylabel('Construction Spending')
#    
#ax1.set_title('Private Construction')
#ax2.set_title('Public Construction')
#
#fig.savefig('test.png')
#
#fig.show()


fig, (ax1, ax2, ax3) = plt.subplots(1,3)
tot_data = []
pub_data = []
pri_data = []

for ind in by_year.groups.keys():
    tot_data.append(df.iloc[by_year.groups[ind].tolist(),1])
    pri_data.append(df.iloc[by_year.groups[ind].tolist(),2])
    pub_data.append(df.iloc[by_year.groups[ind].tolist(),3])

data_max = max([max(sublist) for sublist in tot_data])

fig.set_figheight(15)
fig.set_figwidth(25)
fig.add_axes

ax1.boxplot(tot_data)
ax2.boxplot(pri_data)
ax3.boxplot(pub_data)

for ax in (ax1, ax2, ax3):
    ax.set_xticklabels(by_year.groups.keys())
    ax.yaxis.axes.set_ylim(0, data_max + 10000)
    ax.set_ylabel('Construction Spending')
    
ax1.set_title('Total Construction')
ax2.set_title('Private Construction')
ax3.set_title('Public Construction')

fig.savefig('year.png')

fig.show()

###
###
#seasonality and upward trend over time
###
###

#y = by_month['Total Construction'].agg('mean')
#y1 = by_month['Private Construction'].agg('mean')
#y2 = by_month['Public Construction'].agg('mean')
#plt.plot(x,y,label='Total Construction') # The label parameter is a label for the y axis data that will be used in the legend   
#plt.plot(x,y1,label='Private Construction')
#plt.plot(x,y2,label='Public Construction')
#plt.xlabel('Month')                      # Title for the horizontal axis
#plt.ylabel('Construction Spending')      # Title for the vertical axis
#plt.axis([x.min(),x.max(),0,1.1*y.max()])
#plt.legend()
##plt.savefig('sample.jpg')
#plt.show()
#get our grouped summaries by:
#by_year.agg({'Column' : 'mean'})
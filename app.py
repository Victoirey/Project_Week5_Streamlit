import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from scipy import stats
from matplotlib.axis import Axis

data_clean=pd.read_csv(r'C:\Users\Administrateur\Ironhack\LAB\DAFT_212\module_2\Project_Week_5\data_clean.csv')


################### LAYOUT & INTRO
st.set_page_config(layout="wide")
st.title('BANK LOANS DASHBOARD')
st.write('Analysis of bank loans dataset')
st.sidebar.write('Rana Youssef')
st.sidebar.write('Victoire Rey')
st.write('Dataset of 67000 customers')
st.text("")
st.text("")

sns.set_theme(palette='pastel', style = 'ticks')
sns.set_style({'axes.grid': True,'grid.color': 'lightgrey', 'grid.linestyle': ':', 'axes.spines.right': False,
 'axes.spines.top': False})

cat_colors = sns.color_palette('pastel')
cont_colors = sns.color_palette('crest')

figsize_std = (6,4)
figs=[plt.figure(figsize=figsize_std) for _ in range(0,9)]


################### LOAN AMOUT DISTRIBUTION - HISTOGRAM #######################
#Metrics:
descr1=data_clean['Loan Amount'].describe()
descr1.drop(descr1.index[[0, 2, 4,5,6]], inplace=True)

#Histogram
d1=data_clean['Loan Amount']
figs[0] = plt.figure(figsize=(8, 3))
ax=figs[0].add_subplot(111)
ax=plt.hist(d1)
plt.title("Loans amount distribution", fontsize=10)
plt.xlabel('Loans amounts', fontsize=6)
plt.ylabel('Frequency', fontsize=6)
plt.tight_layout()
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)


################### INTEREST RATES ############################################
#Metrics:
descr2=data_clean['Interest Rate'].describe()
descr2.drop(descr2.index[[0, 2, 4,5,6]], inplace=True)

#Histogram:
d4=data_clean['Loan Amount']
figs[3] = plt.figure(figsize=(8, 3))
ax=figs[3].add_subplot(111)
ax=plt.hist(d4)
plt.title("Interest rates distribution", fontsize=10)
plt.xlabel('Interest rates', fontsize=6)
plt.ylabel('Frequency', fontsize=6)
plt.tight_layout()
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)


################### HOME OWNERSHIP DISTRIBUTION ###############################
d2=data_clean['Home Ownership']
figs[1] = plt.figure(figsize=(10, 5))
ax=plt.hist(d2)
plt.title("Home Ownership distribution", fontsize=23)
plt.xlabel('Amount of home ownership', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.tight_layout()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)


################### TYPE OF HOME OWNERSHIP ####################################
d3=data_clean['Employment Duration'].value_counts()
figs[2]=plt.figure(figsize=(10, 6))
ax=figs[2].add_subplot(111)
ax=d3.plot(kind='bar')
plt.title("Type of home ownership", fontsize=23)
plt.xlabel('Ownership', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.tight_layout()
plt.xticks(fontsize=14, rotation=50, ha='right')
plt.yticks(fontsize=14)


################### APPLICATION TYPE & LOANS GRADES ###########################
figs[4] = plt.figure(figsize=(7,2), dpi=144)
ax1 = figs[4].add_subplot(121)
explode = (0.3, 0.3)
d4=pd.DataFrame(data_clean['Application Type'].value_counts())
ax1.pie(d4['Application Type'], labels=['Individual', 'Joint'], explode=explode, autopct='%1.1f%%', radius=1,textprops={'fontsize': 6}, wedgeprops=dict(width=0.5))
plt.title('Application Type', fontsize=7)
plt.tight_layout()

ax2 = figs[4].add_subplot(122)
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
d5=pd.DataFrame(data_clean['Grade'].value_counts())
ax2.pie(d5.Grade, labels= d5.index, explode=explode, autopct='%1.1f%%', textprops={'fontsize': 6}, radius=1)
plt.title('Loans Grades', fontsize=7)
plt.tight_layout()


################### CORRELATION TABLE ########################################
df_corr=data_clean[['Loan Amount', 'Funded Amount', 'Term', 'Interest Rate', 'Home Ownership', 
             'Revolving Balance', 'Total Accounts', 'Total Current Balance', 'Total Revolving Credit Limit']]
corr_data=df_corr.corr()


################### GRADE AND INTEREST RATES CATEGORIES########################
pd.crosstab(pd.cut(data_clean['Interest Rate'], bins=5, right=False),data_clean['Grade'])
indexbarshart=['[5.32, 8.564)', '[8.564, 11.807)', '[11.807, 15.051)','[15.051, 18.294)','[18.294, 21.554)']
data_chart= pd.crosstab(pd.cut(data_clean['Interest Rate'], bins=5, right=False),data_clean['Grade'])

figs[6] = plt.figure(figsize=(8,4))
bar_ax = figs[6].add_subplot(111)
data_chart = pd.crosstab(pd.cut(data_clean['Interest Rate'], bins=5, right=False),data_clean['Grade'])
bar_ax=data_chart.plot.bar(ax=bar_ax)
plt.title('Interest rate per Grade categories', fontsize=10)
plt.xlabel('Interest rates interval', fontsize=6)
plt.ylabel('Frequency', fontsize=6)
plt.tight_layout()
plt.xticks(fontsize=5,rotation=50, ha='right')
plt.yticks(fontsize=5)
plt.legend(fontsize=4)


#################### CHARACTERISTICS OF LOANS ACCORDING TO OWNERSHIP ##########
data_Employment =data_clean[['Loan Amount', 'Funded Amount', 'Home Ownership']].groupby(data_clean['Employment Duration']).mean().round(2)

indexbarshart=['Mortgage','Own', 'Rent']
data_chart= data_Employment

figs[7] = plt.figure(figsize=(8,4))
bar_ax = figs[7].add_subplot(111)
bar_ax=data_chart.plot.bar(ax=bar_ax)
plt.title('Characteristics of loan per type of ownership', fontsize=10)
plt.xlabel('xx', fontsize=6)
plt.ylabel('Frequency', fontsize=6)
plt.tight_layout()
plt.xticks(fontsize=5,rotation=50, ha='right')
plt.yticks(fontsize=5)
plt.legend(fontsize=4)



###################LAYOUT ORDER OF GRAPHS
col1, col2, col3 = st.columns(3)
col1.metric(label="Average Loan Amount", value=int(descr1[0]))
col2.metric(label="Min Loan Amount", value=int(descr1[1]))
col3.metric(label="Max Loan Amount", value=int(descr1[2]))
st.text("")
st.write(figs[0])
st.text("")
st.text("")
col1, col2, col3 = st.columns(3)
col1.metric(label="Average Interest Rate", value=descr2[0].round(2))
col2.metric(label="Min Interest Rate", value=descr2[1].round(2))
col3.metric(label="Max Interest Rate", value=descr2[2].round(2))
st.text("")
st.write(figs[3])
st.text("")
st.text("")
container1 = st.container()
col1, col2 = st.columns(2)
with container1:
    with col1:
        figs[1]
    with col2:
        figs[2]
st.text("")
st.text("")
st.write(figs[4])
st.text("")
st.text("")       

################### TYPE OF LOANS WITH LOAN AMOUNT AND FUNDED AMOUNT ##########
indexbarshart=['Loan Amount', 'Funded Amount', 'Term', 'Interest Rate']
d6 = data_clean[['Loan Amount', 'Funded Amount', 'Term', 'Interest Rate']].groupby(data_clean[' Purpose_loan']).mean().round(2)
bar_axis = st.multiselect(label="Choose loans to display their purposes:",
                                      options=indexbarshart, default=['Loan Amount', 'Funded Amount'])
if bar_axis:
    figs[5] = plt.figure(figsize=(8,4))
    ax = figs[5].add_subplot(111)
    sub_data_chart = d6[bar_axis]
    sub_data_chart.plot.bar(ax=ax)  
else:
    figs[5] = plt.figure(figsize=(8,4))
    ax = figs[5].add_subplot(111)
    sub_data_chart = d6[['Loan Amount', 'Funded Amount']]
    sub_data_chart.plot.bar(ax=ax)
plt.title("Average amounts of loans according to loan's purpose", fontsize=10)
plt.xlabel("", fontsize=14)
plt.ylabel('Average amounts', fontsize=7)
plt.tight_layout()
plt.xticks(fontsize=7, rotation=50, ha='right')
plt.yticks(fontsize=7)
plt.legend(fontsize=6)
plt.tight_layout()
st.write(figs[5])

st.text("")
st.text("") 
st.write("We analyzed correlation between numeric variables of our dataset and found that there is no significant correlation between variables.")
st.text("") 
cm = sns.light_palette("green", as_cmap=True)
st.dataframe(corr_data.style.background_gradient(cmap=cm))
st.text("")
st.text("") 
st.text("") 
st.write(figs[6])
st.text("")
st.text("") 
st.text("") 
st.write(figs[7])


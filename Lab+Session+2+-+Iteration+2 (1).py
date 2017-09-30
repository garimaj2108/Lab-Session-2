
# coding: utf-8

# In[66]:

import pandas as pd


# In[67]:

security_breaches = pd.read_csv('/Users/garimajain/Desktop/data_viz_1.csv')


# In[68]:

security_breaches.loc[security_breaches['YEAR'] == '0', 'YEAR'] = 2004
security_breaches.loc[security_breaches['YEAR'] == '1', 'YEAR'] = 2005
security_breaches.loc[security_breaches['YEAR'] == '2', 'YEAR'] = 2006
security_breaches.loc[security_breaches['YEAR'] == '3', 'YEAR'] = 2007
security_breaches.loc[security_breaches['YEAR'] == '4', 'YEAR'] = 2008
security_breaches.loc[security_breaches['YEAR'] == '5', 'YEAR'] = 2009
security_breaches.loc[security_breaches['YEAR'] == '6', 'YEAR'] = 2010
security_breaches.loc[security_breaches['YEAR'] == '7', 'YEAR'] = 2011
security_breaches.loc[security_breaches['YEAR'] == '8', 'YEAR'] = 2012
security_breaches.loc[security_breaches['YEAR'] == '9', 'YEAR'] = 2013
security_breaches.loc[security_breaches['YEAR'] == '10', 'YEAR'] = 2014
security_breaches.loc[security_breaches['YEAR'] == '11', 'YEAR'] = 2015
security_breaches.loc[security_breaches['YEAR'] == '12', 'YEAR'] = 2016
security_breaches.loc[security_breaches['YEAR'] == '13', 'YEAR'] = 2017
security_breaches.loc[security_breaches['YEAR'] == '14', 'YEAR'] = 2017


# In[69]:

security_breaches.loc[security_breaches['DATA SENSITIVITY'] == '1', 'DATA SENSITIVITY'] = "Just email address/Online information" 
security_breaches.loc[security_breaches['DATA SENSITIVITY'] == '20', 'DATA SENSITIVITY'] = "SSN/Personal details" 
security_breaches.loc[security_breaches['DATA SENSITIVITY'] == '300', 'DATA SENSITIVITY'] = "Credit card information" 
security_breaches.loc[security_breaches['DATA SENSITIVITY'] == '4000', 'DATA SENSITIVITY'] = "Email password/Health records" 
security_breaches.loc[security_breaches['DATA SENSITIVITY'] == '50000', 'DATA SENSITIVITY'] = "Full bank account details" 


# In[70]:

security_breaches.loc[security_breaches['ORGANISATION'] == 'web', 'ORGANISATION'] = "Tech & Web" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'tech, retail', 'ORGANISATION'] = "Financial, Retail, Media" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'tech, web', 'ORGANISATION'] = "Tech & Web" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'tech, gaming', 'ORGANISATION'] = "Gaming" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'web, tech', 'ORGANISATION'] = "Tech & Web" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'web, gaming', 'ORGANISATION'] = "Gaming" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'gaming', 'ORGANISATION'] = "Gaming" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'tech', 'ORGANISATION'] = "Tech & Web" 


# In[71]:

security_breaches.loc[security_breaches['ORGANISATION'] == 'app', 'ORGANISATION'] = "Tech & Web" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'financial', 'ORGANISATION'] = "Financial, Retail, Media" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'government', 'ORGANISATION'] = "Government" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'government, military', 'ORGANISATION'] = "Military"
security_breaches.loc[security_breaches['ORGANISATION'] == 'legal', 'ORGANISATION'] = "Legal, Transport, Academic" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'military', 'ORGANISATION'] = "Military" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'retail', 'ORGANISATION'] = "Financial, Retail, Media" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'telecoms', 'ORGANISATION'] = "Telecom & Energy" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'web, military', 'ORGANISATION'] = "Military" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'academic', 'ORGANISATION'] = "Legal, Transport, Academic" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'energy', 'ORGANISATION'] = "Telecom & Energy" 
security_breaches.loc[security_breaches['ORGANISATION'] == 'government, healthcare', 'ORGANISATION'] = "Healthcare"
security_breaches.loc[security_breaches['ORGANISATION'] == 'healthcare', 'ORGANISATION'] = "Healthcare"
security_breaches.loc[security_breaches['ORGANISATION'] == 'media', 'ORGANISATION'] = "Financial, Retail, Media"
security_breaches.loc[security_breaches['ORGANISATION'] == 'military, healthcare', 'ORGANISATION'] = "Healthcare"
security_breaches.loc[security_breaches['ORGANISATION'] == 'transport', 'ORGANISATION'] = "Legal, Transport, Academic"



# In[72]:

limited_dataset = security_breaches[["Entity", "YEAR", "records lost", "ORGANISATION", "METHOD OF LEAK", "DATA SENSITIVITY"]]


# In[73]:

data_to_csv = limited_dataset.to_csv("SecurityBreaches-7")


# In[ ]:




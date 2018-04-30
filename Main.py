
# coding: utf-8

# In[27]:

import pandas as pd
import numpy as np


# In[72]:

third_branch = ['CSE3','CSE32','IT3','ME3','ME32','CE3','EEE3','ECE3','ECE32']
second_branch = ['ECE22','ECE2','EEE2','ME22','ME2','CE2','IT2','CSE22','CSE2']


for i in range(0,len(third_branch)):
    second = pd.read_excel("./data/"+ second_branch[i] + ".xls")
    third = pd.read_excel("./data/"+ third_branch[i] + ".xls")
    if (i == 0):
        roll2 = np.array(second['username'])
        roll3 = np.array(third['username'])
    else:
        roll2 = np.concatenate((roll2,np.array(second['username'])),axis=0)
        roll3 = np.concatenate((roll3,np.array(third['username'])),axis=0)




final = []
j = 0
rno = 1
for i in range(0,(roll3.size - 3),3):
    dictionary = []
    dictionary.append(roll2[i])
    dictionary.append(roll3[i])
    dictionary.append(roll2[i+1])
    dictionary.append(roll3[i+1])
    dictionary.append(roll2[i+2])
    dictionary.append(roll3[i+2])
    final.append(dictionary)
    j += 1
    

    if (j%10 == 0):
        

        newframe = pd.DataFrame(final ,columns=['Column 1','Column 2', 'Column 3','Column 4','Column 5','Column 6'])
    

        from jinja2 import Environment, FileSystemLoader
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("report.html")

    
        template_vars = {"title" : "Sitting Arrangement","rno":rno ,"newframe": newframe.to_html()}
        html_out = template.render(template_vars)
        from weasyprint import HTML
        HTML(string=html_out).write_pdf("./report/room"+ str(rno) +".pdf")
        rno += 1
        j = 0
        final = []


# In[ ]:




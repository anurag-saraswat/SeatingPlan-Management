
# coding: utf-8

# In[48]:

import xlwt,random,string


# In[49]:

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 0, "RollNo")
sheet1.write(0, 1, "StudentName")


# In[50]:

for i in range(1,300):
    sheet1.write(i, 0, ("15033" + str(random.randrange(10,15)) + str(random.randrange(100,300)) ))
    sheet1.write(i, 1, ''.join([random.choice(string.ascii_letters) for n in range(6)]))


# In[51]:

book.save("DataSet.xls")


# In[ ]:




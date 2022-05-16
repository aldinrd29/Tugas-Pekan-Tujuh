#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

pizza = {
'Nama': ['Rafa', 'Riki', 'Fatih', 'Johar', 'Aldi', 'Agus', 'Edi', 'Yanuar', 'Ibnu', 'Noval'],
'Tinggi Badan': [160, 145, 165, 170, 160, 165, 168, 172, 164, 166],
'Berat Badan' : [60, 50, 65, 90, 60, 70, 74, 80, 65, 68],
}

pizza_df = pd.DataFrame(pizza)
pizza_df


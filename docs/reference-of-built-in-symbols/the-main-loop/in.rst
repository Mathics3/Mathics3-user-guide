In
==

`WMA <https://reference.wolfram.com/language/ref/In>`_

:code:`In` [:math:`k`]
    gives the :math:`k`-th line of input.





>>> x = 1
  = 1
>>> x = x + 1
  = 2
>>> Do[In[2], {3}]

>>> x
  = 5
>>> In[-1]
  = 5
>>> Definition[In]
  = Attributes[In] = {Listable, Protected}
    
    In[6] = Definition[In]
    
    In[5] = In[-1]
    
    In[4] = x
    
    In[3] = Do[In[2], {3}]
    
    In[2] = x = x + 1
    
    In[1] = x = 1

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:29:32 2019

@author: mwhitten
"""

def g2d1(Fy, Aw, Cv):
    """Nominal shear strength
    
    The nominal shear strength, Vn, of unstiffened or stiffened webs, according
    to the limit states of shear yielding and shear buckling, is
    
        Vn = 0.6*Fy*Aw*Cv
        
    Args:
        Fy (float):
            
        Aw (float):
            
        Cv (float):
    
    """
    
    Vn = 0.6*Fy*Aw*Cv
    
    text = ()
    
    return Vn, text

def g2d2(h, tw, E, Fy):
    """Web shear coefficient, Case (a)
    
    For webs of rolled I-shaped member with
    
    if h/tw <= 2.24*math.sqrt(E,Fy):
        Cv = 1.0
    else:
        Cv = None
    
    Args:
        h (float): 
            web height
        
        tw (float):
            web thickness
            
        E (float):
            modulus of elasticity
        
        Fy (float):
            yield strength of web
            
    Returns:
        Cv (tuple(float, str)):
            web shear coefficient
            
    """
    
    if h/tw <= 2.24*math.sqrt(E/Fy):
        Cv = 1.0
        text = ()
    else:
        Cv = None
        text = ()
        
    return Cv, text

def g2d3(h, tw, kv, E, Fy):
    """Web shear coefficient, Case (b)(i)
    
    For webs of all other doubly symmetric shapes and single symmetric shapes
    and channels, excepts round HSS, the web shear coefficient, Cv, is
    determined as follows
    
    if h/tw <= 1.10*math.sqrt(kv*E/Fy):
        Cv = 1.0
    else:
        Cv = None
        
    Args:
        h (float): 
            web height
        
        tw (float):
            web thickness
            
        kv (float):
            
            
        E (float):
            modulus of elasticity
        
        Fy (float):
            yield strength of web

    Returns:
        Cv (tuple(float, str)):
            web shear coefficient
            
    """
    
    if h/tw <= 1.10*math.sqrt(kv*E/Fy):
        Cv = 1.0
        text = ()
    else:
        Cv = None
        text = ()
        
    return Cv, text


    
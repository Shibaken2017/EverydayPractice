#!/usr/bin/python

import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    print "predictions"
    predictions=np_list(predictions)
    net_worths=np_list(net_worths)
    ### your code goes here
    resid=predictions-net_worths
    abs_resid=np.abs(resid)
   # print abs_resid
   # print abs_resid
    indexes=np.argsort(abs_resid)
   # print indexes
    #print indexes
    ed=int(0.9*float(len(ages)))

    print "aaaaaaaaaaaaaaaaaaa"
    print "ed :{}".format(ed)
    #print indexes
    remained_indexes=indexes[:ed]
    #print remained_indexes
    #print remained_indexes
    for id in remained_indexes:
       print id
       cleaned_data.append((ages[id],net_worths[id],resid[id]))
    return cleaned_data



def np_list(input_list):
    output_list=[]
    for i in input_list:
        output_list.append(i[0])
    return np.array(output_list)
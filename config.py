import numpy as np
import scipy.stats as st
import json

max_score=500
nbars=80
trials=25
se_length=5

functions={'pos_linear':lambda x:x,
           'neg_linear':lambda x:-x,
           'pos_power':lambda x:x**2,
           'neg_power':lambda x:-(x**2),
           'pos_quad':lambda x:(x-(nbars/2.))**2,
           'neg_quad':lambda x:-((x-(nbars/2.))**2),
           'sin':lambda x:np.sin(x),
           'sinc':lambda x:np.sin(x-(nbars/2.))/(x-(nbars/2.)),
           'se':lambda x: st.multivariate_normal.rvs(np.zeros(len(x)),np.array([[np.exp(-((xi-xj)**2/float(2*se_length**2))) for xi in x] for xj in x]))
           
}

def write_functions():
    miny=np.random.uniform(0.,.2)*max_score
    maxy=np.random.uniform(.8,1.)*max_score
    x=np.arange(0,nbars)
    y={f:[1 if np.isnan(yi) else yi for yi in functions[f](x)] for f in functions}
    norm_func={f:[(maxy-miny)/(max(y[f])-min(y[f]))*(val-max(y[f]))+maxy for val in y[f]] for f in functions}
    with open('functions.json', 'w') as fp:
        json.dump(norm_func, fp)

def load():
    with open('data.json') as json_data:
        data=json.load(json_data)
        json_data.close()
    return data
    
def init():
    keys=[u'function', u'describe_goal', u'test_response', u'goal', u'age', u'final_score', u'describe_unclear', u'describe_strategy', u'ID', u'function_name']
    data={key:[] for key in keys}
    with open('data.json', 'w') as json_data:
        json.dump(data,json_data)
        
import pickle
import json

import numpy as np

__data_columns = None
__model = None

def get_estimated_grades(age, medu, fedu, traveltime, studytime, freetime, goout, g1, g2, g3):
   x = np.zeros(len(__data_columns))
   x[0]=0
   x[1] = age
   x[2] =medu
   x[3] =fedu
   x[4] =traveltime
   x[5] =studytime
   x[6] =freetime
   x[7] =goout
   x[8] =g1
   x[9] =g2
   x[10]= g3

   return __model.predict([x])

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/model.pkl', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_grades(10,3,3,3,8,9,5,4,1,15)) #age, medu, fedu, traveltime, studytime, freetime, goout, g1, g2, g3
    print(get_estimated_grades(18,3,3,3,8,9,5,14,20,15))
import pickle
import json
import numpy as np 
__area_type= None
__locations = None
__data_columns = None
__model = None

def get_estimated_price(area_type,location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
        area_type_index= __data_columns.index(area_type.lower())
    except:
        loc_index = -1
        area_type_index=-1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
        x[area_type_index] = 1


    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations
    global __area_type

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[7:]  # first 3 columns are sqft, bath, bhk
        __area_type = __data_columns[4:7]

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_area_type():
    return __area_type    

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_area_type())
    print(get_location_names())
    print(get_estimated_price('area_type_Carpet  Area','location_1st Phase JP Nagar',1000, 2, 2))
    print(get_estimated_price('area_type_Carpet  Area','location_Indira Nagar',1000, 3, 3))
    print(get_estimated_price('area_type_Super built-up  Area','location_other', 1000, 2, 2)) # other location
    print(get_estimated_price('area_type_Plot  Area','location_Yelenahalli', 1000, 2, 2)) 
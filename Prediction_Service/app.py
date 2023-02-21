import streamlit as st
import numpy as np
import pickle
import json
path= "./columns.json"
f1 = open(path)
data = json.load(f1)
data_columns=data['data_columns']
# Closing file
f1.close()


"""
# House price-prediction project
"""
with open('./banglore_home_prices_model.pickle', 'rb') as f:
            model = pickle.load(f)

total_sqft= st.number_input("Enter Sqaure fit")
total_sqft=int(total_sqft)

bath = st.selectbox(
    'select number of bathrooms',
    ('1', '2', '3','4','5'))
bath= int(bath)
st.write('You selected:', bath)

balcony = st.selectbox(
    'select number of balcony',
    ('0', '1', '2','3',))
balcony= int(balcony)
st.write('You selected:', balcony)

bhk= st.selectbox(
    'select number of bhk',
    ('1', '2', '3','4','5'))
bhk=int(bhk)
st.write('You selected:', bhk)

#t= ('location_1st Phase JP Nagar','location_2nd Phase Judicial Layout')
t= ('location_1st Phase JP Nagar','location_2nd Phase Judicial Layout','location_2nd Stage Nagarbhavi',"location_5th Block Hbr Layout","location_5th Phase JP Nagar","location_6th Phase JP Nagar","location_7th Phase JP Nagar","location_8th Phase JP Nagar","location_9th Phase JP Nagar","location_AECS Layout","location_Abbigere","location_Akshaya Nagar","location_Ambalipura","location_Ambedkar Nagar","location_Amruthahalli","location_Anandapura","location_Ananth Nagar","location_Anekal","location_Anjanapura","location_Ardendale","location_Arekere","location_Attibele","location_BEML Layout","location_BTM 2nd Stage","location_BTM Layout","location_Babusapalaya","location_Badavala Nagar","location_Balagere","location_Banashankari","location_Banashankari Stage II","location_Banashankari Stage III","location_Banashankari Stage V","location_Banashankari Stage VI","location_Banaswadi","location_Banjara Layout","location_Bannerghatta","location_Bannerghatta Road","location_Basavangudi","location_Basaveshwara Nagar","location_Battarahalli","location_Begur","location_Begur Road","location_Bellandur","location_Benson Town","location_Bharathi Nagar","location_Bhoganhalli","location_Billekahalli","location_Binny Pete","location_Bisuvanahalli","location_Bommanahalli","location_Bommasandra","location_Bommasandra Industrial Area","location_Bommenahalli","location_Brookefield","location_Budigere","location_CV Raman Nagar","location_Chamrajpet","location_Chandapura","location_Channasandra","location_Chikka Tirupathi","location_Chikkabanavar","location_Chikkalasandra","location_Choodasandra","location_Cooke Town","location_Cox Town","location_Cunningham Road","location_Dasanapura","location_Dasarahalli","location_Devanahalli","location_Devarachikkanahalli","location_Dodda Nekkundi","location_Doddaballapur","location_Doddakallasandra","location_Doddathoguru","location_Domlur","location_Dommasandra","location_EPIP Zone","location_Electronic City","location_Electronic City Phase II","location_Electronics City Phase 1","location_Frazer Town","location_GM Palaya","location_Garudachar Palya","location_Giri Nagar","location_Gollarapalya Hosahalli","location_Gottigere","location_Green Glen Layout","location_Gubbalala","location_Gunjur","location_HAL 2nd Stage","location_HBR Layout","location_HRBR Layout","location_HSR Layout","location_Haralur Road","location_Harlur","location_Hebbal","location_Hebbal Kempapura","location_Hegde Nagar","location_Hennur","location_Hennur Road","location_Hoodi","location_Horamavu Agara","location_Horamavu Banaswadi","location_Hormavu","location_Hosa Road","location_Hosakerehalli","location_Hoskote","location_Hosur Road","location_Hulimavu","location_ISRO Layout","location_ITPL","location_Iblur Village","location_Indira Nagar","location_JP Nagar","location_Jakkur","location_Jalahalli","location_Jalahalli East","location_Jigani","location_Judicial Layout","location_KR Puram","location_Kadubeesanahalli","location_Kadugodi","location_Kaggadasapura","location_Kaggalipura","location_Kaikondrahalli","location_Kalena Agrahara","location_Kalyan nagar","location_Kambipura","location_Kammanahalli","location_Kammasandra","location_Kanakapura","location_Kanakpura Road","location_Kannamangala","location_Karuna Nagar","location_Kasavanhalli","location_Kasturi Nagar","location_Kathriguppe","location_Kaval Byrasandra","location_Kenchenahalli","location_Kengeri","location_Kengeri Satellite Town","location_Kereguddadahalli","location_Kodichikkanahalli","location_Kodigehaali","location_Kodigehalli","location_Kodihalli","location_Kogilu","location_Konanakunte","location_Koramangala","location_Kothannur","location_Kothanur","location_Kudlu","location_Kudlu Gate","location_Kumaraswami Layout","location_Kundalahalli","location_LB Shastri Nagar","location_Laggere","location_Lakshminarayana Pura","location_Lingadheeranahalli","location_Magadi Road","location_Mahadevpura","location_Mahalakshmi Layout","location_Mallasandra","location_Malleshpalya","location_Malleshwaram","location_Marathahalli","location_Margondanahalli","location_Marsur","location_Mico Layout","location_Munnekollal","location_Murugeshpalya","location_Mysore Road","location_NGR Layout","location_NRI Layout","location_Nagarbhavi","location_Nagasandra","location_Nagavara","location_Nagavarapalya","location_Narayanapura","location_Neeladri Nagar","location_Nehru Nagar","location_OMBR Layout","location_Old Airport Road","location_Old Madras Road","location_Padmanabhanagar","location_Pai Layout","location_Panathur","location_Parappana Agrahara","location_Pattandur Agrahara","location_Poorna Pragna Layout","location_Prithvi Layout","location_R.T. Nagar","location_Rachenahalli","location_Raja Rajeshwari Nagar","location_Rajaji Nagar","location_Rajiv Nagar","location_Ramagondanahalli","location_Ramamurthy Nagar","location_Rayasandra","location_Sahakara Nagar","location_Sanjay nagar","location_Sarakki Nagar","location_Sarjapur","location_Sarjapur  Road","location_Sarjapura - Attibele Road","location_Sector 2 HSR Layout","location_Sector 7 HSR Layout","location_Seegehalli","location_Shampura","location_Shivaji Nagar","location_Singasandra","location_Somasundara Palya","location_Sompura","location_Sonnenahalli","location_Subramanyapura","location_Sultan Palaya","location_TC Palaya","location_Talaghattapura","location_Thanisandra","location_Thigalarapalya","location_Thubarahalli","location_Thyagaraja Nagar","location_Tindlu","location_Tumkur Road","location_Ulsoor","location_Uttarahalli","location_Varthur","location_Varthur Road","location_Vasanthapura","location_Vidyaranyapura","location_Vijayanagar","location_Vishveshwarya Layout","location_Vishwapriya Layout","location_Vittasandra","location_Whitefield","location_Yelachenahalli","location_Yelahanka","location_Yelahanka New Town","location_Yelenahalli","location_Yeshwanthpur","location_other")
location=  st.selectbox(
    'Select Location',
    t)

st.write('You selected:', location)

area_type=  st.selectbox(
    'Select Area Type',
    ("area_type_carpet  area", "area_type_plot  area", "area_type_super built-up  area"))

st.write('You selected:', area_type)

def get_estimated_price(sqft,bath,balcony,bhk,location,area_type):
    try:
        loc_index = data_columns.index(location.lower())
        area_index= data_columns.index(area_type.lower())
    except:
        loc_index = -1
        area_index=-1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if (loc_index) and (area_index)>=0:
        x[loc_index] = 1
        x[area_index] = 1


    return round(model.predict([x])[0],2)

if st.button('Estimate Price'):
    st.write(get_estimated_price(total_sqft,bath,balcony,bhk,location,area_type))
    #model.predict([[area_type,location,total_sqft, bath, bhk]][0])
else:
    st.write('Goodbye')
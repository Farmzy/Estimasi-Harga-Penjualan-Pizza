import pickle
import streamlit as st

model = pickle.load(open('estimasi_pizza.sav', 'rb'))

st.title('Estimasi Jumlah Pizza yang terjual')
order_id = st.number_input('Input ID order Pizza')
quantity = st.number_input('Input Kuantitas Pizza yang Di Pesan')
unit_price = st.number_input('Input Harga Pizza dalam USD')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[order_id, quantity, unit_price]]
        )
    st.write ('Estimasi total harga pizza : ', predict)
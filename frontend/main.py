import streamlit as st
import requests
import json
import pandas as pd

df = pd.read_csv("/home/nap-time/HousePriceKazan/House_data.csv")

def front_end():
    st.title("Цена дома в городе Казань")
    
    rooms = st.number_input("Количество комнат")
    square = st.number_input("Плошадь")
    floor = st.number_input("Этаж")
    total_floor = st.number_input("Максимальный этаж")
    metro_station = st.selectbox("Ближайшая станция метро", df['metro_station'].unique())
    time_to_metro = st.number_input("Путь до метро(в минутах)")
    transport = st.selectbox("Пешком или на транспорте", df.transport.unique())

    item = {
        'rooms' : rooms,
        'square': square,
        'floor': floor,
        'total_floor':total_floor,
        'metro_station': metro_station,
        'time_to_metro':time_to_metro,
        'transport': transport,
        'square_room' : square / rooms,
        'floor_coef' : floor / total_floor
    }

    if st.button("Predict"):
        res = requests.post("http://0.0.0.0:8080/predict", json=item)
        predict = res.text
        st.success(f"Цена: {predict}")
if __name__ == '__main__':
    front_end()


from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib


app = FastAPI()

MODEL_PATH = "./model/RFRegression.joblib"

# Данные, которые будет вводить пользователь
class Item(BaseModel):
    rooms: int
    square: float
    floor: int
    total_floor: int
    metro_station: str
    time_to_metro: int
    transport: str

# Достаем нашу модель
rf_pipe = joblib.load(MODEL_PATH)


# Информация о том, что всё успешно запустилось
@app.get('/')
def root():
    return {"message": "Active"}


# Цена для дома
@app.post("/predict")
def predict(item: Item):
    pred = rf_pipe.predict(pd.DataFrame(columns=['rooms',
    'square', 'floor', 'total_floor', 'metro_station', 'time_to_metro',
    'transport', 'square_room', 'floor_coef'], data=np.array([item.rooms, item.square, item.floor, item.total_floor,
    item.metro_station, item.time_to_metro, item.transport, item.square / item.rooms, item.floor / item.total_floor]).reshape(1, 9)))[0]
    return pred

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host='0.0.0.0', reload=True)
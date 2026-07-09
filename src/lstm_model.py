import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


def prepare_sequences(series, window=60):
    scaler = MinMaxScaler()

    scaled = scaler.fit_transform(series.values.reshape(-1,1))

    X=[]
    y=[]

    for i in range(window,len(scaled)):
        X.append(scaled[i-window:i])
        y.append(scaled[i])

    X=np.array(X)
    y=np.array(y)

    return X,y,scaler


def build_lstm(input_shape):

    model=Sequential()

    model.add(LSTM(64,return_sequences=True,input_shape=input_shape))
    model.add(LSTM(32))
    model.add(Dense(1))

    model.compile(
        optimizer="adam",
        loss="mse"
    )

    return model
from fastapi import APIRouter
router = APIRouter()
import pickle
import numpy as np 
from pydantic import BaseModel

class Body(BaseModel):
    nitrogen : float
    phosphorous : float
    potash : float
    temperature : float
    humidity : float
    ph: float
    rainfall : float


@router.post('/')
async def plant_recomendation(body: Body):
    filename = 'app/core/models/plant_recomendation.pkl'  # Specify the filename of the pickle file
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    temp = [body.nitrogen,body.phosphorous,body.potash,body.temperature,body.humidity,body.ph,body.rainfall	]
    temp_reshaped = np.array(temp).reshape(1, -1)
    predictions = model.predict(temp_reshaped)[0]
    return {"message": "Hello World", "plan_recomendation" : predictions}
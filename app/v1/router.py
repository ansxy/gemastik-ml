from fastapi import APIRouter
router = APIRouter()
import pickle
import numpy as np 
from pydantic import BaseModel
import os

class Body(BaseModel):
    nitrogen : float
    phosphorous : float
    potash : float
    temperature : float
    humidity : float
    ph: float
    rainfall : float


@router.post('/plant-recomendation', status_code =200)
async def plant_recomendation(body: Body):
    current_dir = os.getcwd()
    plant_recomendation_models = os.path.join(current_dir,"core","models","plant_recomendation.pkl")
    with open(plant_recomendation_models, 'rb') as file:
        model = pickle.load(file)
    temp = [body.nitrogen,body.phosphorous,body.potash,body.temperature,body.humidity,body.ph,body.rainfall	]
    temp_reshaped = np.array(temp).reshape(1, -1)
    predictions = model.predict(temp_reshaped)[0]
    return {"plan_recomendation" : predictions}

@router.get('/',status_code=200)
async def root():
    return {
        "status" : "ok",
        "Version" : "v1",
        "Team" : [
            "Ansar Fadillah",
            "Dhafa Agusrian Putra",
            "Muhammad Fathurrohim"
        ],
        "Description" : "HarvestMoon Machine Learning API",
        "Api Prefix" : "/v1/",
        "Api Repository" : "https://github.com/ansxy/gemastik-ml"
    }
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: list[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Tea House"}


@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_teas(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index , tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return update_tea
        return {"error": "Tea Not Found"}

@app.delete("/teas/{teas_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return deleted
        return {"error": "Tea not found"}

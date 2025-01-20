import json
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from src.wake_on_lan import router

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to the JSON file
MACHINES_FILE = "src/data/machines.json"


class Machine(BaseModel):
    name: str
    mac_address: str
    ip: str


app.include_router(router)


@app.get("/machines")
async def get_machines():
    with open(MACHINES_FILE, "r") as file:
        machines = json.load(file)
    return machines


@app.post("/machines")
async def add_machine(machine: Machine):
    with open(MACHINES_FILE, "r") as file:
        machines = json.load(file)
    machines.append(machine.dict())
    with open(MACHINES_FILE, "w") as file:
        json.dump(machines, file, indent=4)
    return machine


@app.put("/machines/{machine_name}")
async def update_machine(machine_name: str, machine: Machine):
    with open(MACHINES_FILE, "r") as file:
        machines = json.load(file)
    for m in machines:
        if m["name"] == machine_name:
            m["name"] = machine.name
            m["mac_address"] = machine.mac_address
            m["ip"] = machine.ip
            break
    else:
        raise HTTPException(status_code=404, detail="Machine not found")
    with open(MACHINES_FILE, "w") as file:
        json.dump(machines, file, indent=4)
    return machine


@app.delete("/machines/{machine_name}")
async def delete_machine(machine_name: str):
    with open(MACHINES_FILE, "r") as file:
        machines = json.load(file)
    machines = [m for m in machines if m["name"] != machine_name]
    with open(MACHINES_FILE, "w") as file:
        json.dump(machines, file, indent=4)
    return {"message": "Machine deleted"}


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("src/index.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

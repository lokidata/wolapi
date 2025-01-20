import json

from fastapi import APIRouter, HTTPException
from wakeonlan import send_magic_packet

router = APIRouter()


def load_machines():
    with open("src/data/machines.json") as f:
        return json.load(f)


@router.post("/wake-on-lan/{machine_name}")
async def wake_on_lan(machine_name: str):
    machines = load_machines()
    machine = next((m for m in machines if m["name"] == machine_name), None)

    if machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")

    mac_address = machine["mac_address"]
    ip = machine["ip"]
    send_magic_packet(mac_address, ip_address=ip)

    return {"message": f"Wake on LAN signal sent to {machine_name}"}

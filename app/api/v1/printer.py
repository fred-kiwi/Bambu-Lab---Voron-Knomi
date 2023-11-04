from fastapi import APIRouter
from ...models.printer_status import (PrinterStatus, PrinterProgress, PrinterHomeStatus, PrinterLevelingStatus)

router = APIRouter()


@router.get("/api/printer", response_model=PrinterStatus)
async def get_printer_status():
    # NOTE: This is dummy data for illustration.
    return {
        "temperature": {
            "bed": {"actual": 50.0, "target": 60.0},
            "tool0": {"actual": 200.0, "target": 210.0}
        },
        "state": {
            "flags": {
                "printing": True,
                "paused": False
            }
        }
    }


@router.get("/printer/objects/query")
async def get_printer_details(item: str = ""):
    if item == "display_status":
        return {"result": {"status": {"display_status": {"progress": 0.5}}}}
    elif item == "gcode_macro G28":
        return {"result": {"status": {"gcode_macro G28": {"homing": True}}}}
    elif item == "gcode_macro BED_MESH_CALIBRATE":
        return {"result": {"status": {"gcode_macro BED_MESH_CALIBRATE": {"probing": True}}}}
    else:
        return {}

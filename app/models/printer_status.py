from pydantic import BaseModel

class TemperatureDetail(BaseModel):
    actual: float
    target: float

class ToolTemperature(BaseModel):
    tool0: TemperatureDetail

class PrinterState(BaseModel):
    flags: dict

class PrinterStatus(BaseModel):
    temperature: dict
    state: PrinterState

class DisplayStatus(BaseModel):
    progress: float

class PrinterProgress(BaseModel):
    result: dict

class PrinterHomeStatus(BaseModel):
    result: dict

class PrinterLevelingStatus(BaseModel):
    result: dict

from pydantic import BaseModel

class Observation(BaseModel):
    task: str
    progress: float

class Action(BaseModel):
    action_type: str

class Reward(BaseModel):
    score: float
    done: bool

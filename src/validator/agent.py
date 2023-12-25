import os
import json
from pydantic import BaseModel
from typing import List, Optional, Any


def get_agent_inputs():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.normpath(os.path.join(
        current_directory, '../config/agent.json'))

    inputs = []
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        inputs_data = data.get('inputs', [])

        for input_data in inputs_data:
            input_data.setdefault('data', 'string')
            input_item = InputItem(**input_data)
            inputs.append(input_item)

    return inputs


class InputItem(BaseModel):
    name: str
    type: str
    data: Any


class AgentSchema(BaseModel):
    id: Any
    # inputs: List[InputItem] = get_agent_inputs()
    # webhookUrl: Optional[str] = None


class ApiResponse(BaseModel):
    result: Optional[Any] = None

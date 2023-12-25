from fastapi import APIRouter
from src.controllers.ExecutionController import ExecutionController
from src.validator.agent import ApiResponse, AgentSchema

# prefix="/execute",
router = APIRouter(tags=['Agent execution'])


@router.post('/execute', response_model=ApiResponse)
def execute_agent(request: AgentSchema):
    return ExecutionController().execute(request)

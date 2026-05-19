from fastapi import APIRouter
from .model import UserInput
from .service import ChatServiceDep

chat_router = APIRouter()


@chat_router.post("/chat")
def chat(user_input: UserInput, service: ChatServiceDep):

    return service.run(
        message=user_input.message,
        thread_id=user_input.thread_id
    )
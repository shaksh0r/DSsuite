from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Any
from DSsuite.Stack.Stack import Stack

router = APIRouter()
stack = Stack()

# ----------- Request Body Models --------------

class PushBody(BaseModel):
    item: Any

# ----------- API Endpoints ---------------------

@router.post("/push", status_code=status.HTTP_200_OK)
def push(body: PushBody):
    try:
        stack.push(body.item)
        return {"message": "pushed"}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Push failed due to implementation error"
        )


@router.post("/pop", status_code=status.HTTP_200_OK)
def pop():
    try:
        value = stack.pop()
        return {"message": "popped", "item": value}
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail="Stack is empty"
        )


@router.get("/peek", status_code=status.HTTP_200_OK)
def peek():
    try:
        return {"top": stack.peek()}
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail="Stack is empty"
        )


@router.get("/length", status_code=status.HTTP_200_OK)
def length():
    return {"length": len(stack)}


@router.get("/is_empty", status_code=status.HTTP_200_OK)
def is_empty():
    return {"empty": stack.is_empty()}


@router.get("/full_stack", status_code=status.HTTP_200_OK)
def full_stack():
    return {"stack": list(stack)}

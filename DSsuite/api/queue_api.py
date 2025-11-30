from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Any
from DSsuite.Queue.Queue import Queue

router = APIRouter()
q = Queue()

# ----------- Request Body Models --------------

class EnqueueBody(BaseModel):
    item: Any


# ----------- API Endpoints ---------------------

@router.post("/enqueue", status_code=status.HTTP_200_OK)
def enqueue(body: EnqueueBody):
    q.enqueue(body.item)
    return {"message": "enqueued"}


@router.post("/dequeue", status_code=status.HTTP_200_OK)
def dequeue():
    try:
        value = q.dequeue()
        return {"message": "dequeued", "item": value}
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail="Queue is empty"
        )


@router.get("/front", status_code=status.HTTP_200_OK)
def get_front():
    try:
        return {"front": q.front()}
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail="Queue is empty"
        )


@router.get("/length", status_code=status.HTTP_200_OK)
def get_length():
    return {"length": len(q)}


@router.get("/is_empty", status_code=status.HTTP_200_OK)
def is_empty():
    return {"empty": q.is_empty()}


@router.get("/full_queue", status_code=status.HTTP_200_OK)
def full_queue():
    return {"queue": list(q)}

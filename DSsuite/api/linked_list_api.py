from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Any
from DSsuite.LinkedList.linkedList import LinkedList

router = APIRouter()
ll = LinkedList()

class UpdateBody(BaseModel):
    position: int
    value: Any

class AppendBody(BaseModel):
    item: Any

class RemoveBody(BaseModel):
    position: int

@router.post("/append", status_code=status.HTTP_200_OK)
def append(body: AppendBody):
    try:
        ll.append(body.item)
        return {"message": "appended"}
    except IndexError:
        raise HTTPException(status_code=404, detail="unable to append")

@router.post("/remove", status_code=status.HTTP_200_OK)
def remove(body: RemoveBody):
    try:
        ll.remove(body.position)
        return {"message": "removed"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Not Found")

@router.post("/update", status_code=status.HTTP_200_OK)
def update(body: UpdateBody):
    try:
        ll[body.position] = body.value
        return {"message": "updated"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Index Out of Bounds")

@router.get("/item/{position}", status_code=status.HTTP_200_OK)
def get_item(position: int):
    try:
        return {"item": ll[position]}
    except IndexError:
        raise HTTPException(status_code=404, detail="Index Out of Bounds")

@router.get("/full_list", status_code=status.HTTP_200_OK)
def get_full_list():
    return {"list": list(ll)}

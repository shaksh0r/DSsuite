from fastapi import APIRouter, HTTPException, status, Request, Depends
from pydantic import BaseModel
from typing import Any
from DSsuite.LinkedList.linkedList import LinkedList
from DSsuite.Redis.redis import get_redis

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
async def append(body: AppendBody,redis = Depends(get_redis)):
    try:
        ll.append(body.item)
        await redis.rpush("ll",body.item)
        return {"message": "appended"}
    except IndexError:
        raise HTTPException(status_code=404, detail="unable to append")

@router.post("/remove", status_code=status.HTTP_200_OK)
async def remove(body: RemoveBody,redis = Depends(get_redis)):
    try:
        ll.remove(body.position)
        await redis.lset("ll",body.position,"__DELETE__")
        await redis.lrem("ll",1,"__DELETE__")
        return {"message": "removed"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Not Found")

@router.post("/update", status_code=status.HTTP_200_OK)
async def update(body: UpdateBody, redis = Depends(get_redis)):
    try:
        ll[body.position] = body.value
        await redis.lset("ll",body.position,body.value)
        return {"message": "updated"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Index Out of Bounds")

@router.get("/item/{position}", status_code=status.HTTP_200_OK)
async def get_item(position: int, redis = Depends(get_redis)):
    try:
        cache_value = await redis.lindex("ll",position)
        if cache_value:
            return {"item": cache_value}

        return {"item": ll[position]}
    except IndexError:
        raise HTTPException(status_code=404, detail="Index Out of Bounds")

@router.get("/full_list", status_code=status.HTTP_200_OK)
async def get_full_list(redis = Depends(get_redis)):
    cached_list = await redis.lrange("ll",0,-1)
    if cached_list:
        return {"items": cached_list}
    return {"list": list(ll)}

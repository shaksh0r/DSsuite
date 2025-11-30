from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Any
from DSsuite.BinarySearchTree.BST import BST   # adjust if filename differs

router = APIRouter()
bst = BST()

class InsertBody(BaseModel):
    key: int
    value: Any = None

class RemoveBody(BaseModel):
    key: int

@router.post("/insert", status_code=status.HTTP_200_OK)
def insert(body: InsertBody):
    try:
        bst.insert(body.key, body.value)
        return {"message": "inserted"}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Insertion failed"
        )


@router.get("/find/{key}", status_code=status.HTTP_200_OK)
def find(key: int):
    try:
        node = bst.find(key)
        return {"key": node.key, "value": node.data}
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Key not found"
        )


@router.post("/remove", status_code=status.HTTP_200_OK)
def remove(body: RemoveBody):
    try:
        bst.remove(body.key)
        return {"message": "removed"}
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Key not found"
        )


@router.get("/contains/{key}", status_code=status.HTTP_200_OK)
def contains(key: int):
    return {"contains": key in bst}


@router.get("/min", status_code=status.HTTP_200_OK)
def get_min():
    if bst.is_empty():
        raise HTTPException(status_code=404, detail="Tree is empty")
    node = bst.min()
    return {"key": node.key, "value": node.data}


@router.get("/max", status_code=status.HTTP_200_OK)
def get_max():
    if bst.is_empty():
        raise HTTPException(status_code=404, detail="Tree is empty")
    node = bst.max()
    return {"key": node.key, "value": node.data}


@router.get("/len", status_code=status.HTTP_200_OK)
def length():
    return {"length": len(bst)}


@router.get("/in_order", status_code=status.HTTP_200_OK)
def in_order():
    return {"keys": list(bst.keys())}


@router.get("/items", status_code=status.HTTP_200_OK)
def items():
    return {"items": list(bst.items())}


@router.get("/values", status_code=status.HTTP_200_OK)
def values():
    return {"values": list(bst.values())}


@router.get("/height", status_code=status.HTTP_200_OK)
def height():
    if bst.is_empty():
        return {"height": 0}
    return {"height": bst._heights(bst.root)}

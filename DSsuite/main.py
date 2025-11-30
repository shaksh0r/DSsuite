from fastapi import FastAPI
from api.linked_list_api import router as ll_router
from api.stack_api import router as stack_router
from api.queue_api import router as queue_router
from api.bst_api import router as bst_router

app = FastAPI()

app.include_router(ll_router, prefix="/linkedlist", tags=["linkedlist"])
app.include_router(stack_router, prefix="/stack", tags=["stack"])
app.include_router(bst_router, prefix="/bst", tags=["bst"])
app.include_router(queue_router, prefix="/queue", tags=["queue"])

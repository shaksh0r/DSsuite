import psycopg2
from fastapi import FastAPI
from DSsuite.api.linked_list_api import router as ll_router
from DSsuite.api.stack_api import router as stack_router
from DSsuite.api.queue_api import router as queue_router
from DSsuite.api.bst_api import router as bst_router
from DSsuite.Database.db import init_db

app = FastAPI()

app.include_router(ll_router, prefix="/linkedlist", tags=["linkedlist"])
app.include_router(stack_router, prefix="/stack", tags=["stack"])
app.include_router(bst_router, prefix="/bst", tags=["bst"])
app.include_router(queue_router, prefix="/queue", tags=["queue"])

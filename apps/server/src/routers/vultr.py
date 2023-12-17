from fastapi import APIRouter, Body, Depends
from ..model import vultr
from ..services.vultr.client import vultr_aysnc_client

# TODO add header OAuth validation

router = APIRouter(tags=["provision", "vultr"], prefix="/api/provision/vultr")


@router.post("/servers")
async def create_server(create_instance: vultr.CreateInstance = Body()):
    instance = await vultr_aysnc_client.create_instance(create_instance)
    return instance


@router.get("/servers")
async def get_servers(per_page: int | None = 100, cursor: str | None = None) -> vultr.InstanceList:
    return await vultr_aysnc_client.get_instances(per_page=per_page, cursor=cursor)


@router.get("/servers/{instance_id}")
async def get_server(instance_id: str):
    return vultr_aysnc_client.get_instance(instance_id)


@router.delete("/servers/{instance_id}")
async def delete_server(instance_id: str):
    return vultr_aysnc_client.delete_instance(instance_id)

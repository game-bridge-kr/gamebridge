from ...constants import VULTR_API_KEY
from httpx import AsyncClient
from ...model import vultr


class VultrAsyncClient:
    BASE_URL: str = "https://api.vultr.com/v2"

    async_client: AsyncClient = None

    def init(self):
        headers = {
            "Authorization": "Bearer " + VULTR_API_KEY
        }

        self.async_client = AsyncClient(
            base_url=self.BASE_URL,
            headers=headers,
        )

    async def close(self):
        await self.async_client.aclose()

    # GET and parse data in response content
    async def rest_get(self, uri: str, params: dict = {}) -> dict:
        response = await self.async_client.get(url=uri, params=params)

        response.raise_for_status()
        data = response.json()

        return data

    # POST and parse data in response content
    async def rest_post(self, uri: str, content: dict) -> dict:
        response = await self.async_client.post(uri, content=content)

        response.raise_for_status()
        data = response.json()

        return data

    # PATCH and parse data in response content
    async def rest_patch(self, uri: str, content: dict) -> dict:
        response = await self.async_client.patch(uri, content=content)

        response.raise_for_status()
        data = response.json()

        return data

    async def get_account(self) -> vultr.Account:
        data = await self.rest_get("/account")

        account_data = data['account']
        return vultr.Account(**account_data)

    async def get_instances(self, per_page: int = 100, cursor: str = None) -> vultr.InstanceList:
        params = { 'per_page': per_page, }

        if cursor is not None:
            params['cursor'] = cursor

        data = await self.rest_get("/instances", params=params)
        instance_list = vultr.InstanceList(**data)

        return instance_list

    async def create_instance(self, create_instance: vultr.CreateInstance) -> vultr.Instance:
        content = create_instance.model_dump()

        data = await self.rest_post("/instances", content=content)

        instance_data = data['instance']
        instance = vultr.Instance(**instance_data)

        return instance

    async def get_instance(self, instance_id: str) -> vultr.Instance:
        data = await self.rest_get(f"/instances/{instance_id}")
        instance_data = data['instance']
        return vultr.Instance(**instance_data)

    async def update_instance(self, instance_id: str, update_instance: vultr.UpdateInstance) -> vultr.Instance:
        content = update_instance.model_dump()
        data = await self.rest_patch(f"/instances/{instance_id}", content=content)
        instance_data = data['instance']
        return vultr.Instance(**instance_data)

    async def delete_instance(self, instance_id: str):
        response = await self.async_client.delete(f"/instances/{instance_id}")
        response.raise_for_status()

    async def halt_instances(self, instance_ids: list[str]):
        content = {'instance_ids': instance_ids}
        response = await self.async_client.post("/instances/halt", content=content)
        response.raise_for_status()

    async def reboot_instances(self, instance_ids: list[str]):
        content = {'instance_ids': instance_ids}
        response = await self.async_client.post("/instances/reboot", content=content)
        response.raise_for_status()

    async def start_instances(self, instance_ids: list[str]):
        content = {'instance_ids': instance_ids}
        response = await self.async_client.post("/instances/start", content=content)
        response.raise_for_status()

    async def start_instance(self, instance_id: str):
        response = await self.async_client.post(f"/instances/{instance_id}/start")
        response.raise_for_status()


vultr_aysnc_client = VultrAsyncClient()

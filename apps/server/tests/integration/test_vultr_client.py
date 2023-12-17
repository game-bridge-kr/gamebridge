import pytest
from ...src.services.vultr.client import vultr_aysnc_client


@pytest.mark.asyncio
async def test_provision_permission_account():
    account = await vultr_aysnc_client.get_account()
    assert account.name == "Jeon Hyunjun"
    assert "provisioning" in account.acls

# @pytest.mark.asyncio
# async def test_instances():
#     instances, meta = await vultr_aysnc_client.get_instances()
#     assert meta.total == 0
#     assert len(instances) == 0

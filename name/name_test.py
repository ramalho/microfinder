import pytest

from name.name import app as name_app


@pytest.fixture
def client():
    return name_app.test_client()


@pytest.mark.asyncio
async def test_root(client):
    resp = await client.get("/")
    want = b"This is the microfinder names API server"
    assert await resp.get_data() == want


@pytest.mark.asyncio
async def test_query(client):
    resp = await client.get("/®")
    want = "REGISTERED SIGN"
    assert await resp.get_json() == want


@pytest.mark.asyncio
async def test_query_no_match(client):
    resp = await client.get("/\x00")  # null character
    want_code = 404
    assert resp.status_code == want_code

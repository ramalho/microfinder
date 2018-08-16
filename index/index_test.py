import unicodedata
import pytest

from index.index import add_entry, index
from index.index import app as index_app


def test_single_entry():
    entries = {}
    char, name = "$", "DOLLAR SIGN"

    add_entry(entries, char, name)

    assert "DOLLAR" in entries
    assert "SIGN" in entries
    assert entries["DOLLAR"] == ["$"]
    assert entries["SIGN"] == ["$"]


def test_multiple_entries():
    """
    This test covers the following entries from UnicodeData.txt:

    002D;HYPHEN-MINUS;Pd;0;ES;;;;;N;;;;;
    002E;FULL STOP;Po;0;CS;;;;;N;PERIOD;;;;
    002F;SOLIDUS;Po;0;CS;;;;;N;SLASH;;;;
    0030;DIGIT ZERO;Nd;0;EN;;0;0;0;N;;;;;
    0031;DIGIT ONE;Nd;0;EN;;1;1;1;N;;;;;
    0032;DIGIT TWO;Nd;0;EN;;2;2;2;N;;;;;
    """

    entries = {}
    data = []
    for code in range(0x2d, 0x33):
        char = chr(code)
        data.append((char, unicodedata.name(char)))

    for char, name in data:
        add_entry(entries, char, name)

    assert entries["DIGIT"] == ["0", "1", "2"]
    assert entries["SOLIDUS"] == ["/"]


def test_index():
    entries = index()
    assert entries["REGISTERED"] == ["®"]
    assert len(entries["LETTER"]) > 9000
    assert " " in entries["SPACE"]
    assert "🐱" in entries["CAT"]


@pytest.fixture
def client():
    return index_app.test_client()


@pytest.mark.asyncio
async def test_root(client):
    resp = await client.get("/")
    want = b"This is the microfinder index API server"
    assert await resp.get_data() == want


@pytest.mark.asyncio
async def test_query(client):
    resp = await client.get("/registered")
    want = ["®"]
    assert await resp.get_json() == want


@pytest.mark.asyncio
async def test_multiple_query(client):
    resp = await client.get("/chess")
    assert len(await resp.get_json()) == 12


@pytest.mark.asyncio
async def test_query_no_match(client):
    resp = await client.get("/NO_SUCH_CHARACTER")
    want_code = 404
    assert resp.status_code == want_code

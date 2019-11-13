import json
import logging
import os
import sqlite3
from os import path

import pytest

from common.utilities import get_mock_fyle, fyle_connect
from fyle_db_connector.extract import FyleExtractConnector
from fyle_db_connector.load import FyleLoadConnector

logger = logging.getLogger(__name__)

@pytest.fixture
def mock_fyle():
    return get_mock_fyle()

@pytest.fixture(scope='module')
def fyle():
    return fyle_connect()

@pytest.fixture
def dbconn():
    SQLITE_DB_FILE = '/tmp/test_fyle.db'
    if os.path.exists(SQLITE_DB_FILE):
        os.remove(SQLITE_DB_FILE)
    return sqlite3.connect(SQLITE_DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

@pytest.fixture
def fec(fyle, dbconn):
    res = fyleExtractConnector(fyle_sdk_connection=fyle, dbconn=dbconn)
    res.create_tables()
    return res

import pytest

import sqlite3
import logging
from os import path
import json
from unittest.mock import Mock
from common.utilities import dict_compare_keys, dbconn_table_num_rows

logger = logging.getLogger(__name__)

def test_fyle_mock_setup(fyle):
    assert fyle.Expenses.get_all()[0]['id'] == 'txGC2LMT6mAo', 'fyle mock setup is broken'

def test_dbconn_mock_setup(dbconn):
    with pytest.raises(sqlite3.OperationalError) as e:
        rows = dbconn_table_num_rows(dbconn, 'fyle_extract_employees')

def test_fec_mock_setup(fec):
    # python magic to access private variable for testing db state
    dbconn = fec._FyleExtractConnector__dbconn
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_employees') == 0, 'Unclean db'

def test_dict_compare():
    d1 = {
        'k1' : 'xxx', 'k2' : 2, 'k3' : [1, 2], 'k4' : { 'k41' : [2], 'k42' : { 'k421' : 20}}
    }
    d2 = {
        'k1' : 'xyx', 'k3' : [1, 2], 'k4' : { 'k42' : { 'k421' : 20}}
    }
    d3 = {
        'k1' : 'xyz', 'k3' : [3, 2], 'k4' : { 'k42' : { 'k421' : 40}}
    }
    assert dict_compare_keys(d1, d2) == ['->k2', '->k4->k41'], 'not identifying diff properly'
    assert dict_compare_keys(d2, d3) == [], 'should return no diff'


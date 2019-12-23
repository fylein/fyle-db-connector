import logging

from test.common.utilities import (dbconn_table_num_rows, dbconn_table_row_dict, dict_compare_keys, get_mock_fyle_empty)
from fyle_db_connector.extract import FyleExtractConnector

logger = logging.getLogger(__name__)


def test_employees(fec):
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_employees()
    fyle_data = fyle.Employees.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_employees')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_employees') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 12, 'return value messed up'


def test_settlements(fec):
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_settlements()
    fyle_data = fyle.Settlements.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_settlements')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_settlements') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 3, 'return value messed up'


def test_reimbursements(fec):
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_reimbursements()
    fyle_data = fyle.Reimbursements.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_reimbursements')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_reimbursements') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 3, 'return value messed up'


def test_expenses(fec):
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_expenses()
    fyle_data = fyle.Expenses.get_all()
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_expenses')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_expenses') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 5, 'return value messed up'


def test_categories(fec):
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_categories()
    fyle_data = fyle.Categories.get()['data']
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_categories')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_categories') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 26, 'return value messed up'


def test_projects(fec):
    dbconn = fec._FyleExtractConnector__dbconn
    fyle = fec._FyleExtractConnector__connection
    ids = fec.extract_projects()
    fyle_data = fyle.Projects.get()['data']
    db_data = dbconn_table_row_dict(dbconn, 'fyle_extract_projects')
    assert dict_compare_keys(db_data, fyle_data[0]) == [], 'db table has some columns that fyle doesnt'
    assert dbconn_table_num_rows(dbconn, 'fyle_extract_projects') == len(fyle_data), 'row count mismatch'
    assert len(ids) == 3, 'return value messed up'


def test_empty(dbconn):
    fyle = get_mock_fyle_empty()
    res = FyleExtractConnector(fyle_sdk_connection=fyle, dbconn=dbconn)
    res.create_tables()
    assert res.extract_expenses() == []

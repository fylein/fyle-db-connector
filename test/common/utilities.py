import json
import logging
import os
from os import path
from unittest.mock import Mock
from fylesdk import FyleSDK

logger = logging.getLogger(__name__)


def get_mock_fyle_dict(filename):
    """

    :param filename: filename
    :return: mock_fyle_dict
    """
    basepath = path.dirname(__file__)
    filepath = path.join(basepath, filename)
    mock_fyle_json = open(filepath, 'r').read()
    mock_fyle_dict = json.loads(mock_fyle_json)
    return mock_fyle_dict


def get_mock_fyle_from_file(filename):
    """

    :param filename: filename
    :return: mock_fyle
    """
    mock_fyle_dict = get_mock_fyle_dict(filename)
    mock_fyle = Mock()

    mock_fyle.Expenses.get_all.return_value = mock_fyle_dict['expenses_get_all']
    mock_fyle.Settlements.get_all.return_value = mock_fyle_dict['settlements_get_all']
    mock_fyle.Reimbursements.get_all.return_value = mock_fyle_dict['reimbursements_get_all']
    mock_fyle.Employees.get_all.return_value = mock_fyle_dict['employees_get_all']
    mock_fyle.Reports.get_all.return_value = mock_fyle_dict['reports_get_all']
    mock_fyle.Projects.get.return_value = mock_fyle_dict['projects_get']
    mock_fyle.Categories.get.return_value = mock_fyle_dict['categories_get']

    return mock_fyle


def get_mock_fyle():
    """

    :return: mock_fyle
    """
    return get_mock_fyle_from_file('mock_fyle.json')


def get_mock_fyle_empty():
    """

    :return:mock_fyle
    """
    return get_mock_fyle_from_file('mock_fyle_empty.json')


def dict_compare_keys(d1, d2, key_path=''):
    """ Compare two dicts recursively and see if dict1 has any keys that dict2 does not
    Returns: list of key paths
    """
    res = []
    if not d1:
        return res
    if not isinstance(d1, dict):
        return res
    for k in d1:
        if k not in d2:
            missing_key_path = f'{key_path}->{k}'
            res.append(missing_key_path)
        else:
            if isinstance(d1[k], dict):
                key_path1 = f'{key_path}->{k}'
                res1 = dict_compare_keys(d1[k], d2[k], key_path1)
                res = res + res1
            elif isinstance(d1[k], list):
                key_path1 = f'{key_path}->{k}[0]'
                dv1 = d1[k][0] if len(d1[k]) > 0 else None
                dv2 = d2[k][0] if len(d2[k]) > 0 else None
                res1 = dict_compare_keys(dv1, dv2, key_path1)
                res = res + res1
    return res


def dbconn_table_num_rows(dbconn, tablename):
    """ Helper function to calculate number of rows
    """
    query = f'select count(*) from {tablename}'
    return dbconn.cursor().execute(query).fetchone()[0]


def dbconn_table_row_dict(dbconn, tablename):
    """

    :param dbconn: database connection
    :param tablename: name of the table
    :return: dict containing the first row of the table
    """
    query = f'select * from {tablename} limit 1'
    row = dbconn.cursor().execute(query).fetchone()
    return dict(row)


def fyle_connect():
    """

    :return: fyle_connection
    """
    # Initializing FyleSDK
    fyle_connection = FyleSDK(
        base_url=os.environ.get('FYLE_TPA_BASE_URL'),
        client_id=os.environ.get('FYLE_TPA_CLIENT_ID'),
        client_secret=os.environ.get('FYLE_TPA_CLIENT_SECRET'),
        refresh_token=os.environ.get('FYLE_TPA_REFRESH_TOKEN')
    )
    return fyle_connection


def execute_sqlfile(dbconn, file_path):
    """

    :param dbconn: database connection
    :param file_path: path of the sql file
    :return: sql file
    """
    with open(file_path, 'r') as tf:
        tsql = tf.read()
        sql = tsql
        logger.debug('executing sql %s', sql)
        dbconn.cursor().executescript(sql)

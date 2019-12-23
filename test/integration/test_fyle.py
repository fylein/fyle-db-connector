import logging
from test.common.utilities import dict_compare_keys

logger = logging.getLogger(__name__)


def test_employees(fyle, mock_fyle):
    data = fyle.Employees.get_all()
    mock_data = mock_fyle.Employees.get_all()

    assert dict_compare_keys(data[0], mock_data[0]) == [], 'real fyle has stuff that mock_fyle doesnt'
    assert dict_compare_keys(mock_data[0], data[0]) == [], 'mock_fyle has stuff that real fyle doesnt'

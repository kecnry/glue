from __future__ import absolute_import, division, print_function

from ...config import data_factory

from .pandas import panda_process
from .helpers import has_extension

__all__ = []


@data_factory(label="Excel", identifier=has_extension('xls xlsx'))
def panda_read_excel(path, sheet='Sheet1', **kwargs):
    """ A factory for reading excel data using pandas.
    :param path: path/to/file
    :param sheet: The sheet to read
    :param kwargs: All other kwargs are passed to pandas.read_excel
    :return: core.data.Data object.
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError('Pandas is required for Excel input.')

    indf = pd.read_excel(path, sheet, **kwargs)
    return panda_process(indf)

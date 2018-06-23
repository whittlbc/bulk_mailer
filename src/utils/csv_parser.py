import os
import pandas
from src.utils.slug import to_slug


def csv_as_dict_list(path=None, slugify_headers=False, **kwargs):
  # Ensure CSV exists.
  if not os.path.exists(path):
    raise OSError('CSV file not found at {}'.format(path))

  # Read CSV file from path as a pandas dataframe.
  df = pandas.read_csv(path, **kwargs)

  # Slugify header names into snake case if desired
  if slugify_headers and kwargs['header'] == 0:
    # Create dict of header name changes
    # Ex: {'First Name': 'first_name', ...}
    headers = list(df.columns)
    header_changes = {header: to_slug(header) for header in headers}

    # Rename headers
    df.rename(columns=header_changes, inplace=True)

  # Convert CSV into list of dicts.
  data = list(df.T.to_dict().values())

  return data
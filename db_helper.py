import MySQLdb
import settings

class InventoryDBHelper():
  """Class to encapsulate local MySQL connection and query code."""

  db_connection = None
  result_set = None
  current = -1
  stop = 0

  def __init__(self, db_name='retail-inventory', 
        username=None, password=None, host='localhost' ):
    """Initialize a new connection. Note that if no username or password is
    specified, this class will look in Django's settings to see if any
    username and password was specified there.

    Args:
      db_name: Name of local MySQL database.
      username: Username with which to connect.
      password: Password for the user.
      host: Optional parameter to specify the host.
    """
    if not username or not host:
      username = settings.DATABASES['default']['USER']
      password = settings.DATABASES['default']['PASSWORD']
    self.db_connection = MySQLdb.connect(host=host, 
        user=username, passwd=password, db=db_name)
  
  def getColumnsForTable(self, table):
    """Retrieve a list of columns for the given table.
    
    Args:
      table: Table for which to fetch columns.
    Returns:
      List of column names.
    """
    self.execute('show columns from %s' % table)
    return [col[0] for col in self]
  
  def getIndexOfColumnForTable(self, column, table):
    """Retrieve the index of a column name for a table as it would be returned
    in a result set. This allows code to be database-ordering independent so
    that if someone changes the order of columns code will not break.
    
    Args:
      column: Name of column for which to retrieve the index.
      table: Name of table containing the desired column.
    Returns:
      Index (integer) of the column as it will appear in the result set.
    Raises:
      ValueError if the column is not present in the table.
    """
    cols = self.getColumnsForTable(table)
    if column in cols:
      return cols.index(column)
    raise ValueError("Column '%s' not present in table '%s'" % (column, table))
  
  def escape_string(self, escape):
    """Escape a string for a safer MySQL query.

    Args:
      escape: String to be escaped.
    Returns:
      Escaped string that can be used in a MySQL query.
    """
    return self.db_connection.escape_string(escape)
  
  def execute(self, query_statement):
    """Execute the specified query.
    
    Args:
      query_statement: Statement to execute on db.
    Returns:
      List of resulting rows (lists).
    """
    self.db_connection.query(query_statement)
    results = self.db_connection.store_result()
    if results:
      # Setting maxrows to 0 will cause all results to be returned at once.
      self.result_set = [result for result in results.fetch_row(maxrows=0)]
      self.stop = len(self.result_set)

  def first(self):
    """Fetch the first result of the executed statement.
    
    Returns:
      First row (list or value) in the result set.
    """
    if len(self.result_set) >= 1:
      return self.result_set[0]
    else:
      return None

  def next(self):
    """Iterator for the results returned by a query.

    Returns:
      Next result in the iteration from the query.
    """
    self.current = self.current + 1
    if self.current >= self.stop:
      self.current = -1
      raise StopIteration
    return self.result_set[self.current]
  
  def __iter__(self):
    return self
  
  def commit(self):
    """Commit changes from any insert or update statements."""
    self.db_connection.commit()
  
  def close(self):
    """Close connection to database."""
    self.db_connection.close()
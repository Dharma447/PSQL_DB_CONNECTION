from sqlalchemy import create_engine

class PSQL:
  """establishing a data connection using sqlalchemy"""

    url = 'postgresql+psycopg2://user:password@hostname/database_name'
    conn = None
    cur = None

    def __init__(self, database_name):
        self.database_name = database_name
        if PSQL.conn is None:
            try:
                engine = create_engine(url=PSQL.url.format(database_name=self.database_name))
                self.conn = engine.raw_connection()
                self.cur = self.conn.cursor()
            except Exception as error:
                print(error)

    def sql_execution(self,sql):
      """execute sqls using cursor object"""
        self.cur.execute(sql)
        self.conn.commit()


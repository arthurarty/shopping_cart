class Table():
    """Class to handle creating tables"""

    def __init__(self, db, table_name, sql_query):
        self.table_name = table_name
        db.cur.execute(
            f'''CREATE TABLE IF NOT EXISTS {self.table_name}
            ({sql_query});
            '''
        )
        db.commit_session()

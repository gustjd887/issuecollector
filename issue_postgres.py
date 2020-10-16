import psycopg2

class IssueDB():
    def __init__(self, database="issue", user='gustjd887', password='gustjd25', host='127.0.0.1', port='5432'):
        self.conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.cur = self.conn.cursor()

    def execute(self, data):
        sql = """INSERT INTO issue_issue(site, url, title, reply, name, "date", hit, "like") VALUES %s ON CONFLICT (url) DO UPDATE SET reply=%s, hit=%s, "like"=%s"""
        self.cur.execute(sql, (data, data[3], data[6], data[7]))

    def select(self, query):
        self.cur.execute(query)

        return self.cur.fetchall()

    def update(self, query):
        self.cur.execute(query)

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

from .models import Gist
import datetime

QUERY = """SELECT * FROM gists;
    """

def search_gists(db_connection, **kwargs):
    if not kwargs:
        cursor = db_connection.execute(QUERY)
        return cursor.fetchall()
    else:
        if "created_at" in kwargs:
            cursor = db_connection.execute("SELECT * FROM gists WHERE datetime(created_at) == datetime(:created_at)", kwargs)
        if "github_id" in kwargs:
            cursor = db_connection.execute("SELECT * FROM gists WHERE github_id = :github_id", kwargs)
        #cursor = db_connection.execute("SELECT * FROM gists WHERE github_id = :github_id" OR created_at = :created_at, kwargs)
        
        results = []
        for gist in cursor:
            results.append(Gist(gist))
        return results
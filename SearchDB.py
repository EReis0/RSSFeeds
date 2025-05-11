import sqlite3
from pathlib import Path


def searchDB(db_path, sql_path, subscription=None, catdesc=None, name=None, id=None):
    conn = None
    try:
        # Validate input parameters
        if subscription and subscription not in ("Yes", "No"):
            raise ValueError("Subscription must be 'Yes' or 'No'.")
        if catdesc and catdesc not in ("Other", "News", "Sports"):
            raise ValueError("CatDesc must be 'Other', 'News', or 'Sports'.")
        if id is not None and not isinstance(id, int):
            raise ValueError("ID must be an integer.")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Read the SQL query from a file
        with open(sql_path, 'r', encoding='utf-8') as f:
            sql_query = f.read()

        # Build dynamic WHERE clause
        where_clauses = []
        params = []

        if subscription:
            where_clauses.append("RSSFeeds.Subscription = ?")
            params.append(subscription)
        if catdesc:
            where_clauses.append("Category.CatDesc = ?")
            params.append(catdesc)
        if name:
            where_clauses.append("RSSFeeds.Name LIKE ?")
            params.append(f"%{name}%")
        if id is not None:
            where_clauses.append("RSSFeeds.ID = ?")
            params.append(id)

        if where_clauses:
            sql_query += "\nWHERE " + " AND ".join(where_clauses)

        cursor.execute(sql_query, params)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        results = [dict(zip(columns, row)) for row in rows]

        return results

    except sqlite3.Error as db_err:
        raise Exception(f"Database error: {db_err}")
    except Exception as err:
        raise Exception(f"Unexpected error: {err}")
    finally:
        if conn:
            try:
                conn.close()
            except Exception:
                pass


# Query the database with optional parameters:
if __name__ == "__main__":
    # Get the directory where this script is located
    base_dir = Path(__file__).parent

    # Build paths relative to the script location
    db_path = base_dir / 'rssfeeds.db'
    sql_path = base_dir / 'SearchDB.sql'

    # Parameters for the search
    subscription = ''
    catdesc = ''
    name = ''
    id = 10

    try:
        DBresults = searchDB(db_path, sql_path, subscription, catdesc, name, id)
        print(DBresults)
    except Exception as e:
        print(f"Error: {e}")

# Total number of records returned
    print(f"\033[92mRecord Count: {len(DBresults)}\033[0m")

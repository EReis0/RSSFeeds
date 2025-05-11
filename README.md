# RSSFeeds Database Project

This project provides scripts and a database for querying and managing RSS feed information using Python and SQLite.

---

## Prerequisites

- **Python 3.7+** (comes with `sqlite3` module)
- **SQLite** (for direct DB inspection, optional)

---

## SQLite Installation

### Windows

1. Download the [SQLite tools zip](https://www.sqlite.org/download.html) for Windows.
2. Extract the contents to a folder (e.g., `C:\sqlite`).
3. Add the folder to your system `PATH` (optional, for command-line access).

### Linux

```bash
sudo apt update
sudo apt install sqlite3
```

---

## Setting Up the Python Virtual Environment

1. Open a terminal or command prompt in the project directory.
2. Create a virtual environment:

    ```bash
    python -m venv env
    ```

3. Activate the environment:

    - **Windows (PowerShell):**
      ```powershell
      .\env\Scripts\Activate.ps1
      ```
    - **Windows (cmd):**
      ```cmd
      .\env\Scripts\activate.bat
      ```
    - **Linux/macOS:**
      ```bash
      source env/bin/activate
      ```

4. Install dependencies (if you add any to `requirements.txt`):

    ```bash
    pip install -r requirements.txt
    ```

    > Note: The built-in `sqlite3` module does **not** need to be installed.

---

## How to Execute the Python Script

1. Make sure your virtual environment is activated.
2. Run the desired script. For example:

    ```bash
    python SearchDB.py
    ```

    or

    ```bash
    python Query_All_Records.py
    ```

3. The script will connect to the SQLite database and output the results to the console.

---

### Specifying Variables for Filtering

You can specify filter variables (such as `subscription`, `catdesc`, `name`, or `id`) by editing the script directly in the `if __name__ == "__main__":` section.  
For example, in `SearchDB.py`:

```python
if __name__ == "__main__":
    db_path = 'D:\\Code\\Not Repo\\RSSFeeds\\rssfeeds.db'
    sql_path = 'D:\\Code\\Not Repo\\RSSFeeds\\SearchDB.sql'
    subscription = 'No'      # 'Yes' or 'No'
    catdesc = 'News'         # 'Other', 'News', or 'Sports'
    name = 'Fox'             # Any part of the feed name (optional)
    id = 10                  # Exact ID (optional)

    try:
        DBresults = searchDB(db_path, sql_path, subscription, catdesc, name, id)
        print(DBresults)
    except Exception as e:
        print(f"Error: {e}")
```

**Tip:**  
- Leave a variable as an empty string (`''`) or `None` if you do not want to filter by that field.
- You can combine filters as needed.

---

#### (Optional) Using Command-Line Arguments

If you want to allow users to specify filters from the command line, you can add argument parsing with the `argparse` module.  
Example usage (after modifying the script):

```bash
python SearchDB.py --subscription No --catdesc News --name Fox --id 10
```

---

## Notes

- You can modify the SQL queries in the `.sql` files to change what data is returned.
- Update the script parameters to filter results as needed.

---

## License

MIT License
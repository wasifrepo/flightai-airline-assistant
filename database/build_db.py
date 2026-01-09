import sqlite3
from pathlib import Path

DB_PATH = Path("database/prices.db")
SEED_PATH = Path("database/seed_prices.sql")


def main():
    sql = SEED_PATH.read_text(encoding="utf-8")
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(sql)

    print(f"Database created/updated at: {DB_PATH}")


if __name__ == "__main__":
    main()

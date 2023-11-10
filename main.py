import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users 
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """
)

conn.commit()


def create_user(name, email):
    cur.execute(
        """
        INSERT INTO users (name, email) VALUES (?, ?)
        """,
        (name, email)
    )
    conn.commit()
    print("User added")


def get_users():
    cur.execute(
        """
        SELECT id, name, email FROM users
        """
    )
    users = cur.fetchall()
    for user in users:
        print(user)


def get_user_by_id(id):
    cur.execute(
        """
        SELECT id, name, email FROM users WHERE id = ?
        """,
        (id,)
    )
    user_by_id = cur.fetchone()
    if user_by_id:
        print(user_by_id)
    else:
        print("User not found")


def update_user(id, name, email):
    cur.execute(
        """
        UPDATE users SET name = ?, email = ? WHERE id = ?
        """,
        (name, email, id)
    )
    conn.commit()
    print("User updated")


def delete_user(id):
    cur.execute(
        """
        DELETE FROM users WHERE id = ?
        """,
        (id)
    )
    conn.commit()
    print("User deleted")

create_user("Noe", "noe@example.com")
create_user("Sem", "sem@example.com")
create_user("Cam", "cam@example.com")
create_user("Jafet", "jafet@example.com")

get_users()
update_user(1, "Noé", "noe@example.com")
get_user_by_id(1)
delete_user("1")
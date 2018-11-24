class SQLQuery:
    createTable = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            name TEXT,
            _hash TEXT NOT NULL,
            _salt TEXT NOT NULL,
            
            UNIQUE (username)
        )
        """

    add = """
        INSERT
        INTO users (username, name, _hash, _salt)
        VALUES (?, ?, ?, ?)
        """

    delete = "DELETE FROM users WHERE user = ?"

    changeName = """
        UPDATE users
        SET name = ?
        WHERE id = ?
        """

    changeHashSalt = """
        UPDATE users
        SET _hash = ?, _salt = ?
        WHERE id = ?
        """
    passwordCheck = "SELECT id FROM users WHERE username = ? AND hash = cHash(?, salt)"

    getUserByUsername = "SELECT id, name FROM users WHERE username = ?"
    getUserById = "SELECT username, name FROM users WHERE id = ?"
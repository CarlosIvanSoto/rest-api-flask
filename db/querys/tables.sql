CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    creation_date DATE DEFAULT (datetime('now')),
    modification_date DATE DEFAULT (datetime('now')),
    completed INTEGER NOT NULL DEFAULT 0
)

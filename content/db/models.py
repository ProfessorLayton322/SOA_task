import sqlalchemy

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("username", sqlalchemy.String(100), unique=True, index=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String()),
    sqlalchemy.Column("email", sqlalchemy.String(100), unique=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("surname", sqlalchemy.String(100)),
    sqlalchemy.Column("birthdate", sqlalchemy.DateTime()),
    sqlalchemy.Column("phone", sqlalchemy.String(15)),
)

sessions = sqlalchemy.Table(
    "sessions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("session", sqlalchemy.String(), index=True),
    sqlalchemy.Column("expires", sqlalchemy.DateTime()),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"))
)

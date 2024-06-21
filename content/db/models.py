import sqlalchemy

metadata = sqlalchemy.MetaData()

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer),
    sqlalchemy.Column("content", sqlalchemy.String(280)),
    sqlalchemy.Column("created", sqlalchemy.DateTime()),
    sqlalchemy.Column("edited", sqlalchemy.DateTime()),
)

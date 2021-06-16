from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = (
    "postgresql://productionuser:k6i9lmW3jb@localhost:5013/production"
)
cnx = create_engine(SQLALCHEMY_DATABASE_URI)

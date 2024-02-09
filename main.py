from sqlalchemy import create_engine
with open('connection.cfg') as f:
    s = f.readlines()
username = (s[0].split(':')[1][0:-1])
password = (s[1].split(':')[1][0:-1])
host = (s[2].split(':')[1][0:-1])

engine = create_engine(
    f"postgresql+psycopg2://postgres:test_db@localhost/test_db",
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)
engine.connect()

print(engine)

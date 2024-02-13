from sqlalchemy import create_engine, text
with open('connection.cfg') as f:
    s = f.readlines()
username = (s[0].split(':')[1][0:-1])
password = (s[1].split(':')[1][0:-1])
host = (s[2].split(':')[1][0:-1])

engine = create_engine(
    f'postgresql+psycopg2://{username}:{password}@localhost/test_db',
    echo=True
)
arg1 = 'name'
with engine.connect() as con:
    res = con.execute(text(f"select {arg1}, point, cup_name from cup"))

for i in res:
    print(f'{i[0]} - {i[1]} - {i[2]}')

print(engine)

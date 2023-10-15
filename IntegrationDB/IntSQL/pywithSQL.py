import sqlalchemy
from sqlalchemy import Column, create_engine, inspect, func
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.sql import select
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name =Column(String)
    fullname = Column(String)
    address = relationship(
        "Address",back_populates="user",cascade="all,delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname}"


class Address(Base):
    __tablename__="address"
    id =Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(100),nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"),nullable=False)

    user = relationship(
        "User",back_populates="address"
    )

    def __repr__(self):
        return f"Address(id={self.id}, email={self.email_address})"


#conexao com banco de dados
engine = create_engine("sqlite://")

#criando as classe como tabelas no banco de dados
Base.metadata.create_all(engine)


inspetor_engine = inspect(engine)

print(inspetor_engine.get_table_names())

with Session(engine) as session:
    reginaldo = User(
        name ='reginaldo',
        fullname='Reginaldo Ferreira',
        address=[Address(
            email_address='regymatrix@gmail.com'
        )]
    )
    eliza = User(
        name='eliza',
        fullname='Elzia Santos',
        address=[Address(
            email_address='eliza@gmail.com'
        ),Address(email_address='eliza@gmail.com')]
    )

    patrick = User(name='patrick', fullname='Patrick fer')

    session.add_all([reginaldo,eliza,patrick])

    session.commit()

stmt = select(User).where(User.name.in_(['reginaldo', 'eliza']))

print(stmt)
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
for address in session.scalars(stmt_address):
     print(address)


print(f"\n Ordem Alfabética")
print(select(User).order_by(User.fullname.desc()))
stmt_orders = select(User).order_by(User.fullname.desc())

for lista in session.scalars(stmt_orders):
    print(lista)

print(f"\n JOIN")
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)

print (stmt_join)
for item in session.scalars(stmt_join):
    print(item)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()

print("Executando Select a partir da Conexão")
for result in results:
    print(result)


print(select(func.count('*')).select_from(User))
stmt_count = select(func.count('*')).select_from(User)

for item in session.scalars(stmt_count):
    print(f"Total: {item}")
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.sql.sqltypes import Date

metadata = MetaData()
Client = Table(
    "mclient", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("regno", Integer, nullable=False),
    Column("serial", String(19)),
    Column("duedate", Date()),
    Column("name", String(70)),
    Column("dbname", String(25)),
    Column("dbport", String(5)),
    Column("localnetwork", String(12)),
    Column("localport", String(5)),
    Column("publicnetwork", String(150)),
    Column("publicport", String(5)),
    Column("addressline1", String(150)),
    Column("city", String(50)),
    Column("stateprov", String(50)),
    Column("zipcode", String(6)),
    Column("delete", String(1)),
)
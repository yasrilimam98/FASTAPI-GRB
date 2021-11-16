from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.sql.sqltypes import Date

metadata = MetaData()
Karyawan = Table(
    "dt_karyawan", metadata,
    Column("id_karyawan", Integer, primary_key=True, index=True),
    Column("nama_karyawan", String(255), nullable=False),
    Column("alamat_karyawan", String(255)),
    Column("ttl_karyawan", Date()),
    Column("telp_karyawan", String(255)),
    Column("email_karyawan", String(255)),
    Column("password", String(255)),
)
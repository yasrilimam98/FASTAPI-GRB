"""create table karyawan

Revision ID: 3d52855b3075
Revises: 
Create Date: 2021-11-16 11:20:01.599671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d52855b3075'
down_revision = None
branch_labels = None
depends_on = None


from faker import Faker

faker = Faker('id_ID')

def upgrade():
    pgw = op.create_table(
        'dt_karyawan',
        sa.Column('id_karyawan', sa.Integer, primary_key=True),
        sa.Column('nama_karyawan', sa.String(255), nullable=False),
        sa.Column('alamat_karyawan', sa.String(255)),
        sa.Column('ttl_karyawan', sa.Date()),
        sa.Column('telp_karyawan', sa.String(255)),
        sa.Column('email_karyawan', sa.String(255), unique=True)
    )
    op.bulk_insert(
        pgw,
        [{'nama_karyawan':faker.name(), 
                 'alamat_karyawan':faker.address(),
                 'ttl_karyawan':faker.date_of_birth(tzinfo=None, minimum_age=21, maximum_age=28),
                 'telp_karyawan':faker.phone_number(),
                 'email_karyawan':faker.email()
                  } for x in range(800)]
    )


def downgrade():
    op.drop_table('dt_karyawan')

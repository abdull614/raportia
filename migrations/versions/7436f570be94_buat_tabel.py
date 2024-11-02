"""Buat Tabel?

Revision ID: 7436f570be94
Revises: 0b72f42e4225
Create Date: 2024-10-30 07:24:47.918765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7436f570be94'
down_revision = '0b72f42e4225'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kehadiran',
    sa.Column('id_kehadiran', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('id_siswa', sa.BigInteger(), nullable=True),
    sa.Column('tanggal', sa.Date(), nullable=False),
    sa.Column('status', sa.Enum('Hadir', 'Sakit', 'Alpa', name='statuskehadiranenum'), nullable=False),
    sa.ForeignKeyConstraint(['id_siswa'], ['siswa.id_siswa'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_kehadiran')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kehadiran')
    # ### end Alembic commands ###
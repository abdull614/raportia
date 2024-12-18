"""membuat table laporan

Revision ID: 0b72f42e4225
Revises: 0bda369d0168
Create Date: 2024-10-22 01:29:21.807007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b72f42e4225'
down_revision = '0bda369d0168'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('laporan',
    sa.Column('id_laporan', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('id_siswa', sa.BigInteger(), nullable=False),
    sa.Column('id_kelas', sa.BigInteger(), nullable=False),
    sa.Column('deskripsi', sa.Text(), nullable=False),
    sa.Column('tanggal', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_kelas'], ['kelas.id_kelas'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_siswa'], ['siswa.id_siswa'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_laporan')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('laporan')
    # ### end Alembic commands ###

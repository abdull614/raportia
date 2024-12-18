"""membuat table guru

Revision ID: bc823e29102e
Revises: 85ee8600c6b6
Create Date: 2024-10-22 01:01:03.587017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc823e29102e'
down_revision = '85ee8600c6b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guru',
    sa.Column('id_guru', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.Column('nip', sa.String(length=20), nullable=False),
    sa.Column('mata_pelajaran', sa.String(length=50), nullable=False),
    sa.Column('no_telp', sa.String(length=13), nullable=False),
    sa.PrimaryKeyConstraint('id_guru')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guru')
    # ### end Alembic commands ###

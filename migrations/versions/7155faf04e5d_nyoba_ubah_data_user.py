"""Nyoba ubah data user

Revision ID: 7155faf04e5d
Revises: 7436f570be94
Create Date: 2024-11-02 18:49:56.991160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7155faf04e5d'
down_revision = '7436f570be94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', mysql.DATETIME(), nullable=True))

    # ### end Alembic commands ###
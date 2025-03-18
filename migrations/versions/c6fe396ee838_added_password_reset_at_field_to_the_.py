"""Added password_reset_at field to the User Model

Revision ID: c6fe396ee838
Revises: 545ba87efc57
Create Date: 2025-03-12 01:05:16.156794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6fe396ee838'
down_revision = '545ba87efc57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_reset_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password_reset_at')

    # ### end Alembic commands ###

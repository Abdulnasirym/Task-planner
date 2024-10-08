"""added start date column attributes

Revision ID: b750e5479e4d
Revises: 74a45d366db7
Create Date: 2024-09-04 14:08:14.828892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b750e5479e4d'
down_revision = '74a45d366db7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###

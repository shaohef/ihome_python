"""add trado_no

Revision ID: 27a82a16dc40
Revises: 86ea7f9ce4b7
Create Date: 2019-06-26 21:15:40.308608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27a82a16dc40'
down_revision = '86ea7f9ce4b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ihome_order', sa.Column('trade_no', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ihome_order', 'trade_no')
    # ### end Alembic commands ###

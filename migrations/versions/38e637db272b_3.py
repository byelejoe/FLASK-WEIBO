"""'3'

Revision ID: 38e637db272b
Revises: ac97432e362a
Create Date: 2018-03-26 14:17:32.800000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38e637db272b'
down_revision = 'ac97432e362a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###

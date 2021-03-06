"""empty message

Revision ID: 1e8f4e8124ef
Revises: 8e17ba06cd55
Create Date: 2022-03-22 11:07:56.509155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e8f4e8124ef'
down_revision = '8e17ba06cd55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    # ### end Alembic commands ###

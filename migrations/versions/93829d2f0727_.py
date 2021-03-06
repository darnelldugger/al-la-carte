"""empty message

Revision ID: 93829d2f0727
Revises: 1f1d179d3efd
Create Date: 2022-04-11 22:53:32.865686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93829d2f0727'
down_revision = '1f1d179d3efd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dish_posts', sa.Column('photo', sa.Text(), nullable=False))
    op.create_unique_constraint(None, 'dish_posts', ['photo'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dish_posts', type_='unique')
    op.drop_column('dish_posts', 'photo')
    # ### end Alembic commands ###

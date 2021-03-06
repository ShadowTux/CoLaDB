"""new shit

Revision ID: 3134c5a61647
Revises: d79d3062900f
Create Date: 2020-03-23 19:23:12.700554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3134c5a61647'
down_revision = 'd79d3062900f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###

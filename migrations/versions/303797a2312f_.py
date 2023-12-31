"""empty message

Revision ID: 303797a2312f
Revises: 845732793c1e
Create Date: 2022-07-07 21:01:31.339910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '303797a2312f'
down_revision = '845732793c1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('like_number', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'profile', ['favorite_games'])
    op.create_unique_constraint(None, 'profile', ['region'])
    op.create_unique_constraint(None, 'profile', ['platform'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'profile', type_='unique')
    op.drop_constraint(None, 'profile', type_='unique')
    op.drop_constraint(None, 'profile', type_='unique')
    op.drop_table('like')
    # ### end Alembic commands ###

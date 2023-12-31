"""empty message

Revision ID: b2060fffa8ad
Revises: 6c18aa8572d0
Create Date: 2023-11-04 17:04:59.885499

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b2060fffa8ad'
down_revision = '6c18aa8572d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('password_reset_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=128), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.drop_table('password_reset')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('password_reset',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('token', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('expiry', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='password_reset_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='password_reset_pkey'),
    sa.UniqueConstraint('token', name='password_reset_token_key')
    )
    op.drop_table('password_reset_token')
    # ### end Alembic commands ###

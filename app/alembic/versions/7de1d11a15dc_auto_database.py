"""auto-database

Revision ID: 7de1d11a15dc
Revises: 
Create Date: 2024-10-28 23:16:39.358784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7de1d11a15dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ToDos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ToDos')
    # ### end Alembic commands ###
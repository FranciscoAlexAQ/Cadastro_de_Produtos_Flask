"""empty message

Revision ID: 6e270b38c8dc
Revises: 
Create Date: 2021-01-11 13:52:15.920462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e270b38c8dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True, not_null=True),
    sa.Column('preco', sa.Integer(), nullable=True, not_null=True),
    sa.Column('estoque_minimo', sa.Integer(), nullable=True, not_null=True),
    sa.Column('saldo_estoque', sa.Integer(), nullable=True, not_null=True),
    sa.Column('observacao', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produtos')
    # ### end Alembic commands ###

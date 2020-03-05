"""empty message

Revision ID: b17b0ced6c3a
Revises: 371db2543f35
Create Date: 2020-03-05 11:25:19.723851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b17b0ced6c3a'
down_revision = '371db2543f35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journal_entry', sa.Column('strength_training', sa.Boolean(), nullable=True))
    op.drop_column('journal_entry', 'title')
    op.drop_column('journal_entry', 'done')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journal_entry', sa.Column('done', sa.BOOLEAN(), nullable=True))
    op.add_column('journal_entry', sa.Column('title', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('journal_entry', 'strength_training')
    # ### end Alembic commands ###
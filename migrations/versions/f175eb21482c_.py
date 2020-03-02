"""empty message

Revision ID: f175eb21482c
Revises: ca0b330ae06c
Create Date: 2020-03-02 20:20:46.538792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f175eb21482c'
down_revision = 'ca0b330ae06c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('journal_entry', 'title')
    op.drop_column('journal_entry', 'done')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journal_entry', sa.Column('done', sa.BOOLEAN(), nullable=True))
    op.add_column('journal_entry', sa.Column('title', sa.VARCHAR(length=140), nullable=True))
    # ### end Alembic commands ###

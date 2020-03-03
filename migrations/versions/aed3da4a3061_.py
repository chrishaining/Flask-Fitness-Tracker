"""empty message

Revision ID: aed3da4a3061
Revises: 5ec6ca985163
Create Date: 2020-03-03 18:03:34.174667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aed3da4a3061'
down_revision = '5ec6ca985163'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_journal_entry_date'), 'journal_entry', ['date'], unique=True)
    op.drop_column('journal_entry', 'done')
    op.drop_column('journal_entry', 'title')
    op.drop_column('journal_entry', 'tai_chi')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journal_entry', sa.Column('tai_chi', sa.BOOLEAN(), nullable=True))
    op.add_column('journal_entry', sa.Column('title', sa.VARCHAR(length=140), nullable=True))
    op.add_column('journal_entry', sa.Column('done', sa.BOOLEAN(), nullable=True))
    op.drop_index(op.f('ix_journal_entry_date'), table_name='journal_entry')
    # ### end Alembic commands ###

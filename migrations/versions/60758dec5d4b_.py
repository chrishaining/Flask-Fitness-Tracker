"""empty message

Revision ID: 60758dec5d4b
Revises: aed3da4a3061
Create Date: 2020-03-04 18:36:31.683811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60758dec5d4b'
down_revision = 'aed3da4a3061'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_journal_entry_date'), 'journal_entry', ['date'], unique=True)
    op.drop_column('journal_entry', 'tai_chi')
    op.drop_column('journal_entry', 'done')
    op.drop_column('journal_entry', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journal_entry', sa.Column('title', sa.VARCHAR(length=140), nullable=True))
    op.add_column('journal_entry', sa.Column('done', sa.BOOLEAN(), nullable=True))
    op.add_column('journal_entry', sa.Column('tai_chi', sa.BOOLEAN(), nullable=True))
    op.drop_index(op.f('ix_journal_entry_date'), table_name='journal_entry')
    # ### end Alembic commands ###

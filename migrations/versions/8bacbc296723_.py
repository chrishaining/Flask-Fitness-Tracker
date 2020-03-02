"""empty message

Revision ID: 8bacbc296723
Revises: f14a4925445b
Create Date: 2020-03-02 20:49:08.084283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bacbc296723'
down_revision = 'f14a4925445b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('journal_entry', 'done')
    op.drop_column('journal_entry', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journal_entry', sa.Column('title', sa.VARCHAR(length=140), nullable=True))
    op.add_column('journal_entry', sa.Column('done', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###

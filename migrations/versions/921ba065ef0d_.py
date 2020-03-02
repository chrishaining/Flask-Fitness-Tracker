"""empty message

Revision ID: 921ba065ef0d
Revises: 7ff9eb24fce4
Create Date: 2020-03-02 20:28:58.544740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '921ba065ef0d'
down_revision = '7ff9eb24fce4'
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

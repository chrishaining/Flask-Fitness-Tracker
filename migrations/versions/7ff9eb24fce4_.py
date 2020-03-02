"""empty message

Revision ID: 7ff9eb24fce4
Revises: b854fc69dd71
Create Date: 2020-03-02 20:26:04.302082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ff9eb24fce4'
down_revision = 'b854fc69dd71'
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

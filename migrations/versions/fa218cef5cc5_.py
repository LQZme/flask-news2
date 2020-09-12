"""empty message

Revision ID: fa218cef5cc5
Revises: fbd7c8384c14
Create Date: 2020-09-10 17:00:41.267812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa218cef5cc5'
down_revision = 'fbd7c8384c14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('passwd', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('passwd', 'user', ['passwd'], unique=True)
    # ### end Alembic commands ###
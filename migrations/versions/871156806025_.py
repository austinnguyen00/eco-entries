"""empty message

Revision ID: 871156806025
Revises: b5b05b5b10c9
Create Date: 2021-05-15 08:26:29.442116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '871156806025'
down_revision = 'b5b05b5b10c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('completed_quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attempt_score', sa.Integer(), nullable=True))
        batch_op.drop_column('quiz_score')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('completed_quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quiz_score', sa.INTEGER(), nullable=True))
        batch_op.drop_column('attempt_score')

    # ### end Alembic commands ###
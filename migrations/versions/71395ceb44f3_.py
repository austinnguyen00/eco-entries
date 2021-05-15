"""empty message

Revision ID: 71395ceb44f3
Revises: 50bcfe5da4ac
Create Date: 2021-05-15 10:34:05.270006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71395ceb44f3'
down_revision = '50bcfe5da4ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('completed_quiz', schema=None) as batch_op:
        batch_op.drop_column('attempt_score')

    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quiz_maxscore', sa.Integer(), nullable=True))
        batch_op.drop_column('quizscore')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quizscore', sa.INTEGER(), nullable=True))
        batch_op.drop_column('quiz_maxscore')

    with op.batch_alter_table('completed_quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attempt_score', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
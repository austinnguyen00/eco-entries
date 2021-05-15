"""empty message

Revision ID: 4bff725cba71
Revises: af74ac1988a7
Create Date: 2021-05-15 13:38:22.028713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bff725cba71'
down_revision = 'af74ac1988a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quiz_scoreoutofhundred', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_quiz_quizname')
        batch_op.create_index(batch_op.f('ix_quiz_quizname'), ['quizname'], unique=False)
        batch_op.drop_column('quiz_maxscore')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quiz_maxscore', sa.INTEGER(), nullable=True))
        batch_op.drop_index(batch_op.f('ix_quiz_quizname'))
        batch_op.create_index('ix_quiz_quizname', ['quizname'], unique=1)
        batch_op.drop_column('quiz_scoreoutofhundred')

    # ### end Alembic commands ###
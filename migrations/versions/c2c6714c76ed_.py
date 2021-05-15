"""empty message

Revision ID: c2c6714c76ed
Revises: 5e9d525de9b7
Create Date: 2021-05-15 13:13:59.890946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2c6714c76ed'
down_revision = '5e9d525de9b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quiz_attemptscore', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_quiz_quizname')
        batch_op.create_index(batch_op.f('ix_quiz_quizname'), ['quizname'], unique=False)
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_quiz_quizname'))
        batch_op.create_index('ix_quiz_quizname', ['quizname'], unique=1)
        batch_op.drop_column('user_id')
        batch_op.drop_column('quiz_attemptscore')

    # ### end Alembic commands ###
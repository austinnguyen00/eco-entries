"""empty message

Revision ID: 3da664300e0f
Revises: f27f76359d46
Create Date: 2021-05-15 06:38:27.516479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3da664300e0f'
down_revision = 'f27f76359d46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('completed_quiz',
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_table('attempted_quiz')
    with op.batch_alter_table('enrolled_course', schema=None) as batch_op:
        batch_op.drop_column('course_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enrolled_course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('course_name', sa.INTEGER(), nullable=True))

    op.create_table('attempted_quiz',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('quiz_name', sa.INTEGER(), nullable=True),
    sa.Column('quiz_score', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_name'], ['quiz.quizname'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_table('completed_quiz')
    # ### end Alembic commands ###
"""empty message

Revision ID: e9cefd29e7fb
Revises: b41b365b164f
Create Date: 2021-05-15 13:17:27.847334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9cefd29e7fb'
down_revision = 'b41b365b164f'
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
    op.drop_table('_alembic_tmp_quiz')
    op.drop_table('_alembic_tmp_course')
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.drop_index('ix_course_timestamp')
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DATETIME(), nullable=True))
        batch_op.create_index('ix_course_timestamp', ['timestamp'], unique=False)

    op.create_table('_alembic_tmp_course',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('coursename', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('_alembic_tmp_quiz',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('quiz_maxscore', sa.INTEGER(), nullable=True),
    sa.Column('quizname', sa.VARCHAR(length=128), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('completed_quiz')
    # ### end Alembic commands ###
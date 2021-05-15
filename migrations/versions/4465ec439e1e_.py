"""empty message

Revision ID: 4465ec439e1e
Revises: f4922773defa
Create Date: 2021-05-15 06:03:50.608337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4465ec439e1e'
down_revision = 'f4922773defa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'timestamp')
    op.add_column('enrolled_course', sa.Column('course_name', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'enrolled_course', type_='foreignkey')
    op.create_foreign_key(None, 'enrolled_course', 'course', ['course_name'], ['coursename'])
    op.drop_column('enrolled_course', 'course_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('enrolled_course', sa.Column('course_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'enrolled_course', type_='foreignkey')
    op.create_foreign_key(None, 'enrolled_course', 'course', ['course_id'], ['id'])
    op.drop_column('enrolled_course', 'course_name')
    op.add_column('course', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###
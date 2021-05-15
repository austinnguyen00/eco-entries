"""empty message

Revision ID: 24fdb8729c7c
Revises: e01e2d282aa5
Create Date: 2021-05-15 06:22:21.244333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24fdb8729c7c'
down_revision = 'e01e2d282aa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'enrolled_course', type_='foreignkey')
    op.create_foreign_key(None, 'enrolled_course', 'course', ['course_name'], ['coursename'])
    op.drop_column('enrolled_course', 'course_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('enrolled_course', sa.Column('course_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'enrolled_course', type_='foreignkey')
    op.create_foreign_key(None, 'enrolled_course', 'course', ['course_id'], ['id'])
    # ### end Alembic commands ###
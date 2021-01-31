"""empty message

Revision ID: df21879ca783
Revises: 
Create Date: 2020-12-19 15:48:55.819511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df21879ca783'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Login_email'), 'Login', ['email'], unique=True)
    op.create_table('institution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login_id', sa.Integer(), nullable=True),
    sa.Column('kind', sa.String(length=64), nullable=False),
    sa.Column('scanner_id', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['login_id'], ['Login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_institution_scanner_id'), 'institution', ['scanner_id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login_id', sa.Integer(), nullable=True),
    sa.Column('contact1', sa.BigInteger(), nullable=False),
    sa.Column('contact2', sa.BigInteger(), nullable=False),
    sa.Column('contact3', sa.BigInteger(), nullable=False),
    sa.Column('contact4', sa.BigInteger(), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('group', sa.String(length=20), nullable=False),
    sa.Column('tagid', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['login_id'], ['Login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_index(op.f('ix_institution_scanner_id'), table_name='institution')
    op.drop_table('institution')
    op.drop_index(op.f('ix_Login_email'), table_name='Login')
    op.drop_table('Login')
    # ### end Alembic commands ###

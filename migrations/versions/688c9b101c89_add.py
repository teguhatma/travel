"""add

Revision ID: 688c9b101c89
Revises: 
Create Date: 2019-03-18 21:13:22.973836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '688c9b101c89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Deskripsi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('telp', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Layanan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('filename_images', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename_images'),
    sa.UniqueConstraint('title')
    )
    op.create_table('kategori',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.create_table('Products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('filename_images', sa.String(length=64), nullable=True),
    sa.Column('kategori_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['kategori_id'], ['kategori.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename_images'),
    sa.UniqueConstraint('title')
    )
    op.create_table('kontak',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('messages', sa.String(length=120), nullable=True),
    sa.Column('telp', sa.String(length=15), nullable=True),
    sa.Column('kategori_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['kategori_id'], ['kategori.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_kontak_email'), 'kontak', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_kontak_email'), table_name='kontak')
    op.drop_table('kontak')
    op.drop_table('Products')
    op.drop_table('kategori')
    op.drop_table('Layanan')
    op.drop_table('Deskripsi')
    # ### end Alembic commands ###
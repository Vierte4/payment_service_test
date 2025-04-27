from alembic import op
import sqlalchemy as sa

revision = '695c1fb895b9'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('transaction_id', sa.String(length=36), nullable=False),
        sa.Column('merchant_id', sa.Integer(), nullable=False),
        sa.Column('amount', sa.Numeric(12, 2), nullable=False),
        sa.Column('currency', sa.String(length=3), nullable=False),
        sa.Column('card_token', sa.String(length=255), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint('transaction_id', name='uq_transaction_transaction_id')
    )

def downgrade():
    op.drop_table('transactions')
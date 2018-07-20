"""empty message

Revision ID: 5aaeafd07224
Revises:
Create Date: 2018-07-05 21:03:07.048351+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5aaeafd07224'
down_revision = None
branch_labels = None
depends_on = None


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leagues')
    op.drop_table('user_badge')
    op.drop_table('badge')
    op.drop_table('hackathon_snapshot')
    op.drop_table('hackathon_participant')
    op.drop_table('hackathon')
    op.drop_table('game_participant')
    op.drop_table('game_bot_stat')
    op.drop_table('game_view_stat')
    op.drop_table('game_stat')
    op.drop_table('game')
    op.drop_table('bot_history')
    op.drop_table('bot')
    op.drop_table('challenge_participant')
    op.drop_table('challenge')
    op.drop_table('user_tier_history')
    op.drop_table('user_notification')
    op.drop_table('user')
    op.drop_table('organization_email_domain')
    op.drop_table('organization')
    op.drop_table('halite_1_user')
    sa.Enum(name='halite_1_user_level').drop(op.get_bind())
    sa.Enum(name='organization_kind').drop(op.get_bind())
    sa.Enum(name='user_player_level').drop(op.get_bind())
    sa.Enum(name='challenge_status').drop(op.get_bind())
    sa.Enum(name='bot_compile_status').drop(op.get_bind())
    sa.Enum(name='user_notification_mood').drop(op.get_bind())
    # ### end Alembic commands ###


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('halite_1_user',
                    sa.Column('userID', sa.Integer(), nullable=False),
                    sa.Column('oauthID', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('oauthProvider', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('username', sa.String(length=32), nullable=False),
                    sa.Column('email', sa.String(length=64), nullable=True),
                    sa.Column('isRunning', sa.Boolean(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('compileStatus', sa.Boolean(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('organization', sa.String(length=64), nullable=False),
                    sa.Column('language', sa.String(length=16), nullable=True),
                    sa.Column('mu', sa.Float(), server_default=sa.text("'25'"), nullable=False),
                    sa.Column('sigma', sa.Float(), server_default=sa.text("'8.333'"), nullable=False),
                    sa.Column('rank', sa.Float(), autoincrement=False, nullable=True),
                    sa.Column('numSubmissions', sa.Integer(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('numGames', sa.Integer(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('creationTime', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
                    sa.Column('updateTime', sa.TIMESTAMP(), nullable=True),
                    sa.Column('onEmailList', sa.Boolean(), server_default=sa.text("'1'"), autoincrement=False, nullable=False),
                    sa.Column('githubEmail', sa.String(length=64), nullable=True),
                    sa.Column('verificationCode', sa.String(length=64), nullable=True),
                    sa.Column('isEmailGood', sa.Boolean(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('level', sa.Enum('High School', 'Undergraduate', 'Graduate', 'Professional', name='halite_1_user_level'), server_default=sa.text("'Professional'"), nullable=False),
                    sa.PrimaryKeyConstraint('userID'),
    )

    op.create_table('organization',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('organization_name', sa.Unicode(length=64), nullable=False),
                    sa.Column('kind', sa.Enum('High School', 'University', 'Professional School', 'Company', 'Other', name='organization_kind'), server_default=sa.text("'Other'"), nullable=False),
                    sa.Column('verification_code', sa.String(length=32), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('organization_email_domain',
                    sa.Column('organization_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('domain', sa.Unicode(length=255), nullable=False),
                    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], name='organization_email_domain_ibfk_1'),
                    sa.PrimaryKeyConstraint('organization_id', 'domain'),
    )


    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('oauth_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('oauth_provider', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('username', sa.Unicode(length=40), nullable=False),
                    sa.Column('email', sa.Unicode(length=320), nullable=True),
                    sa.Column('github_email', sa.Unicode(length=320), nullable=True),
                    sa.Column('verification_code', sa.String(length=64), nullable=True),
                    sa.Column('is_active', sa.Boolean(), server_default=sa.text("'1'"), autoincrement=False, nullable=False),
                    sa.Column('on_email_list', sa.Boolean(), server_default=sa.text("'1'"), autoincrement=False, nullable=False),
                    sa.Column('is_email_good', sa.Boolean(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('player_level', sa.Enum('High School', 'University', 'Professional', name='user_player_level'), server_default=sa.text("'Professional'"), nullable=False),
                    sa.Column('organization_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('country_code', sa.String(length=3), nullable=True),
                    sa.Column('country_subdivision_code', sa.String(length=10), nullable=True),
                    sa.Column('creation_time', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
                    sa.Column('update_time', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('api_key_hash', sa.String(length=255), nullable=True),
                    sa.Column('is_admin', sa.Boolean(), server_default=sa.text("'0'"), autoincrement=False, nullable=True),
                    sa.Column('is_gpu_enabled', sa.Boolean(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], name='user_ibfk_1'),
                    sa.PrimaryKeyConstraint('id'),
    )

    op.create_table('challenge',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
                    sa.Column('finished', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('num_games', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('status', sa.Enum('created', 'playing_game', 'finished', name='challenge_status'), server_default=sa.text("'created'"), nullable=False),
                    sa.Column('most_recent_game_task', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('issuer', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('winner', sa.Integer(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['issuer'], ['user.id'], name='challenge_issuer_fk', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['winner'], ['user.id'], name='challenge_winner_fk', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('challenge_participant',
                    sa.Column('challenge_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('points', sa.Integer(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['challenge_id'], ['challenge.id'], name='challenge_participant_fk', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='challenge_participant_ibfk_2', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('challenge_id', 'user_id'),
    )

    op.create_table('bot',
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('compile_status', sa.Enum('Uploaded', 'InProgress', 'Successful', 'Failed', 'Disabled', name='bot_compile_status'), nullable=False),
                    sa.Column('compile_start', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.Column('language', sa.Unicode(length=64), nullable=True),
                    sa.Column('version_number', sa.Integer(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('games_played', sa.Integer(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('mu', sa.Float(), server_default=sa.text("'25'"), nullable=False),
                    sa.Column('sigma', sa.Float(), server_default=sa.text("'8.333'"), nullable=False),
                    sa.Column('score', sa.Float(), server_default=sa.text("'0'"), nullable=False),
                    sa.Column('creation_time', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
                    sa.Column('update_time', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
                    sa.Column('timeout_sent', sa.Boolean(), server_default=sa.text("'0'"), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='bot_ibfk_2', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'id'),
    )
    op.create_table('bot_history',
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('bot_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('version_number', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('last_rank', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('last_score', sa.Float(), nullable=False),
                    sa.Column('last_num_players', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('last_games_played', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('language', sa.Unicode(length=64), nullable=False),
                    sa.Column('when_retired', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
                    sa.ForeignKeyConstraint(['user_id', 'bot_id'], ['bot.user_id', 'bot.id'], name='bot_history_ibfk_4', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='bot_history_ibfk_3', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'bot_id', 'version_number'),
    )

    op.create_table('game',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('replay_name', sa.String(length=128), nullable=False),
                    sa.Column('map_width', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('map_height', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('map_seed', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('map_generator', sa.String(length=128), nullable=False),
                    sa.Column('time_played', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
                    sa.Column('replay_bucket', sa.Integer(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.Column('challenge_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['challenge_id'], ['challenge.id'], name='game_challenge_fk', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('game_stat',
                    sa.Column('game_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('turns_total', sa.Integer(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['game_id'], ['game.id'], name='game_stat_ibfk_1', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('game_id'),
    )
    op.create_table('game_view_stat',
                    sa.Column('game_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('views_total', sa.Integer(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['game_id'], ['game.id'], name='game_view_stat_ibfk_1', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('game_id'),
    )
    op.create_table('game_bot_stat',
                    sa.Column('game_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('bot_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['game_id'], ['game.id'], name='game_bot_stat_ibfk_1', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id', 'bot_id'], ['bot.user_id', 'bot.id'], name='fkcompid'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fkuserid'),
                    sa.PrimaryKeyConstraint('game_id', 'user_id', 'bot_id'),
    )
    op.create_table('game_participant',
                    sa.Column('game_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('bot_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('version_number', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('log_name', sa.String(length=256), nullable=True),
                    sa.Column('rank', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('player_index', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('timed_out', sa.Boolean(), autoincrement=False, nullable=False),
                    sa.Column('mu', sa.Float(), nullable=True),
                    sa.Column('sigma', sa.Float(), nullable=True),
                    sa.Column('leaderboard_rank', sa.Integer(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['game_id'], ['game.id'], name='game_participant_ibfk_4', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id', 'bot_id'], ['bot.user_id', 'bot.id'], name='game_participant_ibfk_3'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='game_participant_ibfk_2'),
                    sa.PrimaryKeyConstraint('game_id', 'user_id', 'bot_id'),
    )


    op.create_table('hackathon',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.Unicode(length=256), nullable=False),
                    sa.Column('description', sa.Unicode(length=4096), nullable=False),
                    sa.Column('start_date', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('end_date', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('verification_code', sa.String(length=32), nullable=False),
                    sa.Column('organization_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('location', sa.Unicode(length=256), nullable=True),
                    sa.Column('thumbnail', sa.String(length=512), nullable=True),
                    sa.Column('is_open', sa.Boolean(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], name='hackathon_ibfk_1'),
                    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('user_tier_history',
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('tier', sa.String(length=256), nullable=False),
                    sa.Column('last_in_tier', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
                    sa.Column('total_time_in_tier', sa.Integer(), server_default=sa.text("'0'"), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_tier_history_ibfk_2', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'tier'),
    )
    op.create_table('hackathon_snapshot',
                    sa.Column('hackathon_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('bot_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('games_played', sa.Integer(), server_default=sa.text("'0'"), autoincrement=False, nullable=True),
                    sa.Column('score', sa.Float(), nullable=False),
                    sa.Column('mu', sa.Float(), nullable=False),
                    sa.Column('sigma', sa.Float(), nullable=False),
                    sa.Column('version_number', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('language', sa.Unicode(length=64), nullable=True),
                    sa.ForeignKeyConstraint(['hackathon_id'], ['hackathon.id'], name='hackathon_snapshot_ibfk_6', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id', 'bot_id'], ['bot.user_id', 'bot.id'], name='hackathon_snapshot_ibfk_5', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='hackathon_snapshot_ibfk_4', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('hackathon_id', 'user_id', 'bot_id'),
    )
    op.create_table('leagues',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('category', sa.Unicode(length=45), nullable=False),
                    sa.Column('name', sa.Unicode(length=45), nullable=False),
                    sa.Column('description', sa.Unicode(length=1024), nullable=False),
                    sa.Column('query', sa.Unicode(length=1024), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('user_notification',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('title', sa.Unicode(length=64), nullable=False),
                    sa.Column('body', sa.Unicode(length=2048), nullable=False),
                    sa.Column('mood', sa.Enum('error', 'neutral', 'success', name='user_notification_mood'), server_default=sa.text("'neutral'"), nullable=False),
                    sa.Column('creation_time', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_notification_ibfk_2', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
    )

    op.create_table('hackathon_participant',
                    sa.Column('hackathon_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['hackathon_id'], ['hackathon.id'], name='hackathon_participant_ibfk_4', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='hackathon_participant_ibfk_3', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('hackathon_id', 'user_id'),
    )

    op.create_table('badge',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('name', sa.Unicode(length=256), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('user_badge',
                    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('badge_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('is_enabled', sa.Boolean(), server_default=sa.sql.True_(), autoincrement=False, nullable=False),
                    sa.Column('creation_time', sa.TIMESTAMP(timezone=True), server_default=sa.func.current_timestamp(), nullable=True),
                    sa.Column('update_time', sa.TIMESTAMP(timezone=True), nullable=True),
                    sa.ForeignKeyConstraint(['badge_id'], ['badge.id'], name='user_badge_ibfk_2', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_badge_ibfk_1', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'badge_id'),
    )
    # ### end Alembic commands ###

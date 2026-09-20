id_cols = ['id', 'match_id', 'index']  # not features
categorical_cols = ['type', 'play_pattern', 'position', 'team', 'player', 'pass_recipient', 'pass_assisted_shot_id', 'foul_committed_card',
                    'shot_key_pass_id', 'goalkeeper_position', 'bad_behaviour_card', 'outcome', 'action_type',
                    'technique', 'body_part']
numeric_cols = ['timestamp','minute', 'second', 'millisecond', 'duration', 'location_x', 'location_y', 'end_location_x', 'end_location_y', 'period',
                'pass_length', 'pass_angle', 'pass_height']
boolean_cols = [column for column, dtype in playing_events_df.schema.items() if dtype == pl.Boolean]
list_cols = ['related_events', 'shot_freeze_frame']  # variable-length, e.g. freeze frames, tactics lineup

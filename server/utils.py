
import json
from websockets.asyncio.server import broadcast

# this check if the move is possible or legal in nature
def cheack_move_legality(session, player_id, board_pos_row, board_pos_col, command):
    state = list(session.playerlist)[player_id].is_possible_move(board_pos_row, board_pos_col, command)
    return state # todo

def broadcase_move(sktlst, str):
    broadcast(sktlst, json.dumps({"type": "game_history", "value": str}))

def send_error_notification(player_id):
    print('send error notification to ' + str(player_id))

def check_if_game_over():
    # update self.game_lifetime_state to 'game_over'
    return False # todo

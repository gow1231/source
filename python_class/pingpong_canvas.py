def winnerval(self, winner):
    if winner == self.player:
        return 1
    elif winner == EMPTY:
        return 0.5
    elif winner == DRAW:
        return 0
    else:
        return self.lossval


def episode_over(self, winner):
    if winner == DRAW:
        print('Game over! It was a draw.')
    else:
        print('Game over! Winner: Player {0}'.format(winner))

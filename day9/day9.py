class Marble:
    def __init__(self, value, previous: 'Marble' = None, next: 'Marble' = None):
        self.value = value
        self.previous = self
        self.next = self

    def insert_before(self, marble: 'Marble'):
        marble.previous = self.previous
        marble.next = self
        self.previous = marble
        marble.previous.next = marble

    def pop(self):
        self.previous.next = self.next
        self.next.previous = self.previous
        return self.value

    def print(self, stop_at=None):
        if stop_at == self.value:
            print()
        else:
            print(self.value, end=' ')
            if stop_at is None:
                stop_at = self.value
            self.next.print(stop_at)


def high_score(player_count, last_marble_value):
    marble = Marble(0)
    current_marble = marble
    player = 1
    scores = [0] * player_count
    for marble_number in range(1, last_marble_value + 1):
        #marble.print()
        player += 1
        if player > player_count:
            player = 1

        if not marble_number % 23 == 0:
            marble_to_insert_before = current_marble.next.next
            current_marble = Marble(marble_number)
            marble_to_insert_before.insert_before(current_marble)
        else:
            scores[player - 1] += marble_number
            marble_to_remove = current_marble.previous.previous.previous. \
                previous.previous.previous.previous
            current_marble = marble_to_remove.next
            scores[player - 1] += marble_to_remove.pop()
        # if marble_number % 100000 == 0:
        #     print(marble_number)
    return max(scores)


print(high_score(464, 71730))
print(high_score(464, 7173000))

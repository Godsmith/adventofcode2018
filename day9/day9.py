def high_score(player_count, last_marble_value):
    marbles = [0]
    current_index = 0
    player = 1
    scores = [0] * player_count
    for marble_number in range(1, last_marble_value + 1):
        player += 1
        if player > player_count:
            player = 1

        if not marble_number % 23 == 0:
            index_to_insert_before = (current_index + 2) % len(marbles)
            marbles.insert(index_to_insert_before, marble_number)
            current_index = index_to_insert_before
        else:
            scores[player - 1] += marble_number
            index_to_remove = (current_index - 7) % len(marbles)
            scores[player - 1] += marbles.pop(index_to_remove)
            current_index = index_to_remove % len(marbles)
    return max(scores)


print(high_score(464, 71730))

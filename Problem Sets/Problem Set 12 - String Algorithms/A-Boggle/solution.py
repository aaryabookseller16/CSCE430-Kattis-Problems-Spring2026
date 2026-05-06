import sys
from array import array

tokens = sys.stdin.buffer.read().split()
if not tokens:
    sys.exit(0)

# just the usual boggle score table
score_table = array("B", [0, 0, 0, 1, 1, 2, 3, 5, 11])

pos = 0
dictionary_size = int(tokens[pos])
pos += 1

words = []
word_lengths = array("B")
word_scores = array("B")

# this is a compact trie so python dict overhead does not blow up
head = array("i", [-1])
terminal = array("i", [-1])
edge_to = array("i")
edge_next = array("i")
edge_char = bytearray()

for _ in range(dictionary_size):
    word = tokens[pos]
    pos += 1

    if len(word) > 8:
        continue

    word_index = len(words)
    words.append(word)
    word_lengths.append(len(word))
    word_scores.append(score_table[len(word)])

    node = 0
    for letter in word:
        code = letter - 65
        edge = head[node]

        while edge != -1 and edge_char[edge] != code:
            edge = edge_next[edge]

        if edge == -1:
            child = len(head)
            head.append(-1)
            terminal.append(-1)
            edge_char.append(code)
            edge_to.append(child)
            edge_next.append(head[node])
            head[node] = len(edge_to) - 1
            node = child
        else:
            node = edge_to[edge]

    terminal[node] = word_index

board_count = int(tokens[pos])
pos += 1

neighbors = []
for row in range(4):
    for col in range(4):
        current = []
        for d_row in (-1, 0, 1):
            next_row = row + d_row
            if next_row < 0 or next_row >= 4:
                continue
            for d_col in (-1, 0, 1):
                next_col = col + d_col
                if d_row == 0 and d_col == 0:
                    continue
                if next_col < 0 or next_col >= 4:
                    continue
                current.append(next_row * 4 + next_col)
        neighbors.append(tuple(current))

root_child = array("i", [-1]) * 26
edge = head[0]
while edge != -1:
    root_child[edge_char[edge]] = edge_to[edge]
    edge = edge_next[edge]

seen = array("I", [0]) * len(words)
transition_cache = {}
output = []
board_mark = 0

for _ in range(board_count):
    board_mark += 1

    cells = [0] * 16
    cell_index = 0
    for _ in range(4):
        row = tokens[pos]
        pos += 1
        cells[cell_index] = row[0] - 65
        cells[cell_index + 1] = row[1] - 65
        cells[cell_index + 2] = row[2] - 65
        cells[cell_index + 3] = row[3] - 65
        cell_index += 4

    score = 0
    found = 0
    best_word = b""
    best_len = -1

    for start in range(16):
        start_node = root_child[cells[start]]
        if start_node == -1:
            continue

        stack_cells = [start]
        stack_nodes = [start_node]
        stack_masks = [1 << start]
        stack_depths = [1]

        while stack_nodes:
            cell = stack_cells.pop()
            node = stack_nodes.pop()
            mask = stack_masks.pop()
            depth = stack_depths.pop()

            word_index = terminal[node]
            if word_index != -1 and seen[word_index] != board_mark:
                seen[word_index] = board_mark
                score += word_scores[word_index]
                found += 1

                word_len = word_lengths[word_index]
                if word_len > best_len or (word_len == best_len and words[word_index] < best_word):
                    best_word = words[word_index]
                    best_len = word_len

            if depth == 8:
                continue

            for next_cell in neighbors[cell]:
                bit = 1 << next_cell
                if mask & bit:
                    continue

                next_code = cells[next_cell]
                key = (node << 5) | next_code
                child = transition_cache.get(key, -2)

                if child == -2:
                    child = -1
                    edge = head[node]
                    while edge != -1:
                        if edge_char[edge] == next_code:
                            child = edge_to[edge]
                            break
                        edge = edge_next[edge]
                    transition_cache[key] = child

                if child != -1:
                    stack_cells.append(next_cell)
                    stack_nodes.append(child)
                    stack_masks.append(mask | bit)
                    stack_depths.append(depth + 1)

    output.append(str(score).encode() + b" " + best_word + b" " + str(found).encode())

sys.stdout.buffer.write(b"\n".join(output))

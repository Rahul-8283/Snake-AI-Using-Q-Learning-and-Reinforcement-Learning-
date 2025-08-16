# # # import curses
# # # import random

# # # def main(stdscr):
# # #     curses.curs_set(0)  # hide cursor
# # #     stdscr.nodelay(1)   # non-blocking input
# # #     stdscr.timeout(100) # refresh every 100ms

# # #     sh, sw = stdscr.getmaxyx()
# # #     w = curses.newwin(sh, sw, 0, 0)
# # #     w.keypad(1)

# # #     # initial snake position and body
# # #     snk_x = sw // 4
# # #     snk_y = sh // 2
# # #     snake = [
# # #         [snk_y, snk_x],
# # #         [snk_y, snk_x - 1],
# # #         [snk_y, snk_x - 2]
# # #     ]

# # #     food = [sh // 2, sw // 2]
# # #     w.addch(food[0], food[1], curses.ACS_PI)

# # #     key = curses.KEY_RIGHT

# # #     while True:
# # #         next_key = w.getch()
# # #         key = key if next_key == -1 else next_key

# # #         # calculate new head
# # #         head = [snake[0][0], snake[0][1]]
# # #         if key == curses.KEY_DOWN:
# # #             head[0] += 1
# # #         if key == curses.KEY_UP:
# # #             head[0] -= 1
# # #         if key == curses.KEY_LEFT:
# # #             head[1] -= 1
# # #         if key == curses.KEY_RIGHT:
# # #             head[1] += 1

# # #         snake.insert(0, head)

# # #         # check if snake hit border or itself
# # #         if (
# # #             head[0] in [0, sh] or
# # #             head[1] in [0, sw] or
# # #             head in snake[1:]
# # #         ):
# # #             curses.endwin()
# # #             quit()

# # #         # check if snake ate food
# # #         if head == food:
# # #             food = None
# # #             while food is None:
# # #                 nf = [
# # #                     random.randint(1, sh-2),
# # #                     random.randint(1, sw-2)
# # #                 ]
# # #                 food = nf if nf not in snake else None
# # #             w.addch(food[0], food[1], curses.ACS_PI)
# # #         else:
# # #             tail = snake.pop()
# # #             w.addch(tail[0], tail[1], ' ')

# # #         w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

# # # curses.wrapper(main)

# # # - - - - - - - - - - - -  - - - - - - - - - - - - - - ------ - -- - - - - -


# # import curses
# # import random
# # import time

# # def main(stdscr):
# #     # Setup
# #     curses.curs_set(0)           # Hide cursor
# #     stdscr.nodelay(0)            # Wait for input initially
# #     stdscr.keypad(1)
# #     sh, sw = stdscr.getmaxyx()   # Screen height and width

# #     # Create window for game with border
# #     w = curses.newwin(sh, sw, 0, 0)
# #     w.keypad(1)
# #     w.timeout(150)               # Snake speed (ms per move)

# #     # Welcome screen
# #     w.clear()
# #     w.border()
# #     msg = "Press ENTER to Start"
# #     w.addstr(sh//2, (sw - len(msg))//2, msg)
# #     while True:
# #         key = w.getch()
# #         if key == 10:   # Enter key
# #             break

# #     # Initial snake setup
# #     snk_x = sw // 4
# #     snk_y = sh // 2
# #     snake = [
# #         [snk_y, snk_x],
# #         [snk_y, snk_x - 1],
# #         [snk_y, snk_x - 2]
# #     ]

# #     food = [sh // 2, sw // 2]
# #     w.addch(food[0], food[1], curses.ACS_PI)

# #     key = curses.KEY_RIGHT   # initial direction

# #     # Game loop
# #     while True:
# #         next_key = w.getch()
# #         if next_key != -1:
# #             key = next_key   # change direction only if pressed

# #         # Move snake head automatically
# #         head = [snake[0][0], snake[0][1]]
# #         if key == curses.KEY_DOWN:
# #             head[0] += 1
# #         if key == curses.KEY_UP:
# #             head[0] -= 1
# #         if key == curses.KEY_LEFT:
# #             head[1] -= 1
# #         if key == curses.KEY_RIGHT:
# #             head[1] += 1

# #         snake.insert(0, head)

# #         # Check for collision with border or itself
# #         if (head[0] in [0, sh-1] or
# #             head[1] in [0, sw-1] or
# #             head in snake[1:]):
# #             w.clear()
# #             w.border()
# #             msg = " GAME OVER! Press Q to quit "
# #             w.addstr(sh//2, (sw - len(msg))//2, msg)
# #             while True:
# #                 key = w.getch()
# #                 if key in [ord('q'), ord('Q')]:
# #                     return

# #         # Snake eats food
# #         if head == food:
# #             food = None
# #             while food is None:
# #                 nf = [
# #                     random.randint(1, sh-2),
# #                     random.randint(1, sw-2)
# #                 ]
# #                 food = nf if nf not in snake else None
# #             w.addch(food[0], food[1], curses.ACS_PI)
# #         else:
# #             # Move forward (remove tail)
# #             tail = snake.pop()
# #             w.addch(tail[0], tail[1], ' ')

# #         # Draw snake head
# #         w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

# # curses.wrapper(main)

# # # - - - - - - - - - - - -  - - - - - - - - - - - - - - ------ - -- - - - - -


# import curses
# import random

# def main(stdscr):
#     # Setup
#     curses.curs_set(0)           # Hide cursor
#     stdscr.nodelay(0)            # Wait for input initially
#     stdscr.keypad(1)
#     sh, sw = stdscr.getmaxyx()   # Screen height and width

#     # Create game window
#     w = curses.newwin(sh, sw, 0, 0)
#     w.keypad(1)
#     w.timeout(150)               # Snake speed (ms per move)

#     # --- Welcome screen ---
#     w.clear()
#     w.border()
#     msg = "Press ENTER to Start"
#     w.addstr(sh//2, (sw - len(msg))//2, msg)
#     while True:
#         key = w.getch()
#         if key == 10:   # Enter key
#             break

#     # Clear screen and draw fresh border
#     w.clear()
#     w.border()

#     # Initial snake setup
#     snk_x = sw // 4
#     snk_y = sh // 2
#     snake = [
#         [snk_y, snk_x],
#         [snk_y, snk_x - 1],
#         [snk_y, snk_x - 2]
#     ]

#     food = [sh // 2, sw // 2]
#     w.addch(food[0], food[1], curses.ACS_PI)

#     key = curses.KEY_RIGHT   # initial direction

#     # Game loop
#     while True:
#         next_key = w.getch()

#         # --- Handle direction changes safely ---
#         if next_key != -1:
#             if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
#                 if (key == curses.KEY_RIGHT and next_key != curses.KEY_LEFT) or \
#                    (key == curses.KEY_LEFT and next_key != curses.KEY_RIGHT) or \
#                    (key == curses.KEY_UP and next_key != curses.KEY_DOWN) or \
#                    (key == curses.KEY_DOWN and next_key != curses.KEY_UP):
#                     key = next_key

#         # Move snake head automatically
#         head = [snake[0][0], snake[0][1]]
#         if key == curses.KEY_DOWN:
#             head[0] += 1
#         if key == curses.KEY_UP:
#             head[0] -= 1
#         if key == curses.KEY_LEFT:
#             head[1] -= 1
#         if key == curses.KEY_RIGHT:
#             head[1] += 1

#         snake.insert(0, head)

#         # Check for collision with border or itself
#         if (head[0] in [0, sh-1] or
#             head[1] in [0, sw-1] or
#             head in snake[1:]):
#             w.clear()
#             w.border()
#             msg = " GAME OVER! Press Q to quit "
#             w.addstr(sh//2, (sw - len(msg))//2, msg)
#             while True:
#                 key = w.getch()
#                 if key in [ord('q'), ord('Q')]:
#                     return

#         # Snake eats food
#         if head == food:
#             food = None
#             while food is None:
#                 nf = [
#                     random.randint(1, sh-2),
#                     random.randint(1, sw-2)
#                 ]
#                 food = nf if nf not in snake else None
#             w.addch(food[0], food[1], curses.ACS_PI)
#         else:
#             # Move forward (remove tail)
#             tail = snake.pop()
#             w.addch(tail[0], tail[1], ' ')

#         # Redraw border (so tail erasing doesn’t wipe it)
#         w.border()

#         # Draw snake head
#         w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

# curses.wrapper(main)


# # - - - - - - - - - - - -  - - - - - - - - - - - - - - ------ - -- - - - - - Restart

import curses
import random

def start_game(w, sh, sw):
    # Initial snake setup
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT   # initial direction

    while True:
        next_key = w.getch()

        # --- Handle direction changes safely ---
        if next_key != -1:
            if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
                if (key == curses.KEY_RIGHT and next_key != curses.KEY_LEFT) or \
                   (key == curses.KEY_LEFT and next_key != curses.KEY_RIGHT) or \
                   (key == curses.KEY_UP and next_key != curses.KEY_DOWN) or \
                   (key == curses.KEY_DOWN and next_key != curses.KEY_UP):
                    key = next_key

        # Move snake head automatically
        head = [snake[0][0], snake[0][1]]
        if key == curses.KEY_DOWN:
            head[0] += 1
        if key == curses.KEY_UP:
            head[0] -= 1
        if key == curses.KEY_LEFT:
            head[1] -= 1
        if key == curses.KEY_RIGHT:
            head[1] += 1

        snake.insert(0, head)

        # Check for collision with border or itself
        if (head[0] in [0, sh-1] or
            head[1] in [0, sw-1] or
            head in snake[1:]):
            return False  # lost the game

        # Snake eats food
        if head == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh-2),
                    random.randint(1, sw-2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Move forward (remove tail)
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Redraw border (so tail erasing doesn’t wipe it)
        w.border()

        # Draw snake head
        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


def main(stdscr):
    # Setup
    curses.curs_set(0)           # Hide cursor
    stdscr.nodelay(0)            # Wait for input initially
    stdscr.keypad(1)
    sh, sw = stdscr.getmaxyx()   # Screen height and width

    # Create game window
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(150)               # Snake speed (ms per move)

    while True:
        # --- Welcome screen ---
        w.clear()
        w.border()
        msg = "Press ENTER to Start"
        w.addstr(sh//2, (sw - len(msg))//2, msg)
        while True:
            key = w.getch()
            if key == 10:   # Enter key
                break

        # Clear screen and draw fresh border
        w.clear()
        w.border()

        # Run game
        alive = start_game(w, sh, sw)

        # --- Game Over screen ---
        w.clear()
        w.border()
        msg = " GAME OVER! Press R to Restart or Q to Quit "
        w.addstr(sh//2, (sw - len(msg))//2, msg)

        while True:
            key = w.getch()
            if key in [ord('q'), ord('Q')]:
                return
            elif key in [ord('r'), ord('R')]:
                break  # restart loop

curses.wrapper(main)

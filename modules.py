import curses

def select_option(options):
    def main(stdscr):
        stdscr.clear()
        cursor_x = 0

        while True:
            # Display options
            for i, option in enumerate(options):
                x = 0
                y = i
                if i == cursor_x:
                    stdscr.addstr(y, x, f"> {option} <")  # Highlight selected option
                else:
                    stdscr.addstr(y, x, f"  {option}  ")

            stdscr.refresh()

            key = stdscr.getch()

            # Move cursor up or down
            if key == curses.KEY_UP and cursor_x > 0:
                cursor_x -= 1
            elif key == curses.KEY_DOWN and cursor_x < len(options) - 1:
                cursor_x += 1
            elif key == ord('\n'):  # Enter key to select
                break  # Exit the loop

        return cursor_x  # Return the index of the selected option

    return curses.wrapper(main)


def select_option_add(options, note:str):
    def main(stdscr):
        stdscr.clear()
        cursor_x = 0

        while True:
            if note != "":
                stdscr.addstr(0,0,note)
            # Display options
            for i, option in enumerate(options):
                x = 0
                if note != "":
                    y = i+1
                else:
                    y = i
                if i == cursor_x:
                    stdscr.addstr(y, x, f"> {option} <")  # Highlight selected option
                else:
                    stdscr.addstr(y, x, f"  {option}  ")

            stdscr.refresh()

            key = stdscr.getch()

            # Move cursor up or down
            if key == curses.KEY_UP and cursor_x > 0:
                cursor_x -= 1
            elif key == curses.KEY_DOWN and cursor_x < len(options) - 1:
                cursor_x += 1
            elif key == ord('\n'):  # Enter key to select
                break  # Exit the loop

        return cursor_x  # Return the index of the selected option

    return curses.wrapper(main)
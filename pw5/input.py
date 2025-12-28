import curses


def get_input(stdscr, y, x, prompt):
    curses.echo()
    stdscr.addstr(y, x, prompt)
    stdscr.refresh()


    input_bytes= stdscr.getstr(y, x +len(prompt))

    return input_bytes.decode('utf-8')



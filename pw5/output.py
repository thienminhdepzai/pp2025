import curses
import os

def print_menu(stdscr, selected_row_idx, menu_items):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu_items):
        x=w//2 - len(row)//2
        y=h//2 - len (menu_items)//2 + idx

        if idx == selected_row_idx:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y,x , row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def show_message_box (stdscr, title, lines):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(0, 0, f"---{title}---")
    stdscr.attron(curses.A_BOLD)

    for i, line in enumerate(lines):
        if i+2 <h:
            stdscr.addstr(i+2, 0, str(line))
    
    msg = "Press any key to return"
    stdscr.addstr(h-2, 0, msg, curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()

def save_student_to_txt(students):
    f = open("student.txt", "w", encoding="utf-8")

    for s in students:
        f.write(f"{s.id}|{s.name}|{s.dod} \n")

    f.close()

def save_course_to_txt(courses):
    f = open("courses.txt","w",encoding="utf-8")

    for c in courses:
        f.write(f"{c.id}|{c.name}|{c.credits} \n")

    f.close

def save_mark_to_txt(students):
    f= open("mark.txt","w", encoding="utf-8")

    for s in students:
        for course_name, score, credit in s.mark:
            f.write(f"{course_name}|{s.id}|{score} \n")

    f.close()



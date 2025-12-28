import curses
from curses import wrapper

from domain import Student, Course, Markmanager

from input import (
    get_input
    )

from output import (
    show_message_box, 
    print_menu, 
    save_course_to_txt, 
    save_mark_to_txt, 
    save_student_to_txt
    )

from utils.compress import compress_data 

from utils.load import (
    extract_all_data, 
    load_data_course, 
    load_data_student
)



def main(stdscr):
    stdscr.keypad(True)
    mm = Markmanager()
    

    menu_items = [
        "1: input student",
        "2: input course",
        "3: input mark of the course",
        "4: show students",
        "5: show courses",
        "6: calculate student GPA ",
        "7: Show all student GPA ",
        "8: exit"
    ]

    curses.curs_set(0)
    current_row = 0
    selection= None
    while True:
        print_menu(stdscr, current_row, menu_items)

        key = stdscr.getch()

        if key== curses.KEY_UP and current_row >0:
            current_row-=1
        elif key == curses.KEY_DOWN and current_row<len(menu_items) - 1:
            current_row+=1
        elif key in (curses.KEY_ENTER, 10, 17):
            selection = current_row
        elif 49 <= key <= 48 + len(menu_items):   
            selection = key - 49
        
        if selection is not None:
            stdscr.addstr(0, 0, f"you chose: {menu_items[selection]}")
            stdscr.clrtoeol()
            stdscr.refresh()
            stdscr.getch()

        if selection == 0:
            mm.input_student(stdscr)
        elif selection == 1:
            mm.input_courses(stdscr)
        elif selection == 2:
            mm.input_marks_for_course(stdscr)
        elif selection == 3:
            mm.show_student(stdscr)
        elif selection == 4:
            mm.show_course(stdscr)
        elif selection == 5:
            mm.calculate_GPA(stdscr)
        elif selection == 6:
            mm.show_list_GPA(stdscr)
        elif selection == 7:
            save_student_to_txt(Student)
            save_course_to_txt(Course)
            save_mark_to_txt(Student)

            compress_data()
            break
        selection = None 
        
if __name__ == '__main__': 
    extract_all_data()
    wrapper(main)


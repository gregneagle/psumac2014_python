def question(question_number):
    if question_number == 1:
        return "What is your name?"
    elif question_number == 2:
        return "What is your quest?"
    elif question_number == 3:
        return "What is your favorite color?"
    else:
        return "Ahhhhhhh"

print question(1)

print question(3)


def header(text, level):
    open_tag = "<h" + str(level) + ">"
    close_tag = "</h" + str(level) + ">"
    return open_tag + text + close_tag

print header("My Great Title", 1)

print header("My Subtitle", 2)


def header(text, level=1):
    open_tag = "<h" + str(level) + ">"
    close_tag = "</h" + str(level) + ">"
    return open_tag + text + close_tag

print header("My Great Title")


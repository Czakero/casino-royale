def question_about_playing():

    question = True

    while question:

        answer = input("Do you want to play again?").upper()

        if answer == "YES":
            question = False

            return True

        elif answer == "NO":
            question = False

            return False

        else:
            question = True
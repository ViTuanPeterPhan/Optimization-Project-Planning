"""Job Optimization Integration Program"""


__author__ = "ViTuan Phan"


# I intended to create a CPM network to solve for the optimum setup
# of a project so that the minimum number of workers are hired and the
# minimum number of work days will be used.

# I credit professor Osheroff's COP 1500 course for teaching me how to code
# in Python 3. More so than the course materials, professor Osheroff taught
# me to be a tinkerer of the code, and coupled with my general mathematics
# education background, I was able to produce this program. If some portions
# of the program seem inefficient or 'wonky' as some would describe it,
# it is due to the tinkering process arriving at a solution organically,
# rather than simply looking up a clean solution to the problem.

# In the 'optimization' function, I utilized the code from the site below:
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# List comprehension allowed me to pull from my text file specific values
# depending on user input.

# This program has two PEP8 style errors not corrected. They are the
# try/except commands being too broad and the while loop redundant boolean
# check, even though the while loop usually assumes this portion of code.


def misc_3(input_list):
    """misc_n() are functions which allow me to satisfy project
    requirements. This function counts the number of spaces between strings
    from the user input (from misc_1). It does not count the actual
    instances of the space key, it just counts the number of items-1 in the
    input_list.
    input_list - list consisting of strings of text"""
    if len(input_list) == 1:
        print("\nYou didn't include any spaces in your input! ")
    elif len(input_list) == 2:
        print("\nYou included 1 space in your input! ")
    elif 2 < len(input_list) <= 10:  # and key term!
        print("\nYou included " + str(
            len(input_list) - 1) + " spaces in your input! ")


def misc_2(user_input):
    """misc_n() are functions which allow me to satisfy project
    requirements. This function analyzes the user_input, recieved from
    misc_1, and separates the input into separate strings at each of the
    spaces."""
    # If the user didn't enter anything or if they entered only spaces, then
    # they will get error printouts and the series of functions will loop back
    # to the requirements menu function.
    if len(user_input) < 0 or len(user_input) == 0:  # or key term!
        print("Oops! You didn't enter anything! That won't work. ")
    elif user_input.isspace():
        print("Oops! You only entered spaces! That won't work. ")
    # If the user input was acceptable, then they'll have the option to copy
    # the string three times, showing the string multiplication operator in
    # proper use.
    else:
        print("Your parameter was " + str(user_input) + "! ")
        user_input_list = list(user_input.strip().split())
        triple_it = input(
            "type 'three's company too' to triple every first phrase, bit, "
            "or chunk of your input! ")
        if triple_it == "three's company too":
            triple_input_list = []
            for x in range(0, len(user_input_list)):
                triple_input_list.append((" " + user_input_list[
                    x] + " ") * 3)  # string multiplication operator here.
            print(triple_input_list)
        else:
            print("\nNo problem, three's a crowd anyways. ")
            parameters = user_input_list
            misc_3(parameters)


def misc_1():
    """misc_n() are functions which allow me to satisfy project
    requirements. This function assigns a user input to the variable
    'parameters' and sends it to the function misc_2."""
    print("Let's pass along some inputs as parameters to other functions! ")
    parameters = input("Type whatever you want and press enter! ")
    misc_2(parameters)
    print("\nThanks for playing! Returning to the requirements menu. ")


def calculator_startup():
    """This functions runs before calculator(), so the 'available math
    operations' list doesn't display multiple times."""
    print(
        "The calculator is a set of functions that perform basic operations "
        "as well as check truth values of equality statements. ")
    print(
        "\nAvailable mathematical operations: \n (+) Addition \n (-) "
        "Subtraction \n (*) Multiplication \n (/) Division \n (%) Modulus "
        "\n(**) Exponentiation \n(//) Floor Division ")
    print(
        "\n (=) Equality \n(!=) Inequality \n (<) Less Than \n (>) Greater "
        "Than \n(<=) Less Than or Equal To \n(>=) Greater Than or Equal To ")
    calculator()


def calculator():
    """This function is exactly what you would think it is: a set of functions
    that perform basic operations and check truth values of equality
    statements."""
    check_another = True
    while check_another == True:
        user_input = input(
            "\nEnter a mathematical expression in the form a \u2605 b, "
            "\nwhere a and b are numbers and \u2605 is a mathematical "
            "operator. ")
        # The statement below takes the user's input and separates it into two
        # variables and an operator. Each statement within the try/except
        # section looks first for what operator was inputted, by checking if
        # the operator appears in the user_input_list list. Then it assigns
        # the numerical values to the variables 'a' and 'b'. Try/except
        # clause is such that the variables 'a' and 'b' are numerical.
        user_input_list = list(user_input.strip().split())
        try:
            if '+' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("Your chosen operation is addition. ")
                equals = a + b
                print(user_input, "=", equals)
            elif '-' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("Your chosen operation is subtraction. ")
                equals = a - b
                print(user_input, "=", equals)
            elif '*' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("Your chosen operation is multiplication. ")
                equals = a * b
                print(user_input, "=", equals)
            elif '/' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("Your chosen operation is division. ")
                if b == 0:
                    print(
                        "Sorry, you cannot divide by zero. \nOperation "
                        "terminated. ")
                else:
                    equals = a / b
                    print(user_input, "=", equals)
            elif '**' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("Your chosen operation is exponentiation. ")
                equals = a ** b
                print(user_input, "=", equals)
            elif '//' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("Your chosen operation is floor division. ")
                equals = a // b
                print(user_input, "=", equals)
            elif '%' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("Your chosen operation is modulus. ")
                equals = a % b
                print(user_input, "=", equals)
            elif '=' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("You've chosen to check equality. ")
                if not a == b:
                    print(user_input, "is not a true expression. ")
                elif a == b:
                    print(user_input, "is a true expression. ")
            elif '!=' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("You've chosen to check equality. ")
                if a != b:
                    print(user_input, "is a true expression. ")
                else:
                    print(user_input, "is not a true expression. ")
            elif '>' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("You've chosen to check equality. ")
                if a > b:
                    print(user_input, "is a true expression. ")
                else:
                    print(user_input, "is not a true expression. ")
            elif '<' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("You've chosen to check equality. ")
                if a < b:
                    print(user_input, "is a true expression. ")
                else:
                    print(user_input, "is not a true expression. ")
            elif '>=' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("You've chosen to check equality. ")
                if a >= b:
                    print(user_input, "is a true expression. ")
                else:
                    print(user_input, "is not a true expression. ")
            elif '<=' in user_input_list:
                a = float(user_input_list[0])
                b = float(user_input_list[2])
                print("You've chosen to check equality. ")
                if a <= b:
                    print(user_input, "is a true expression. ")
                else:
                    print(user_input, "is not a true expression. ")
            else:
                print(
                    "Sorry, that does not fit this function's input "
                    "requirements. \nOperation terminated. ")
            continue_calc = input(
                "\nEnter '0' to perform another operation, or anything else "
                "to return to the requirements menu. ")
            if continue_calc == "0":
                check_another = False
        except:
            print("\nError in your selection input. Please try again. ")
    print("Returning to the requirements menu! ")


def requirements():
    """This is a submenu that houses the remaining requirements not used in
    my program. It exists to suffice the integration project requirements."""
    run = True
    while run == True:
        print(
            "\nThis submenu houses the remaining requirements that were not "
            "used in my program! ")
        print("Available options: \n1. Calculator. \n2. Miscellaneous. \n\n0."
              " Main Menu. ")
        select_option = input("\nWhich option would you like to utilize? ")
        if select_option == "1":
            calculator_startup()
        elif select_option == "2":
            misc_1()
        elif select_option == "0":
            run = False
            print("Returning to the main menu. ")
        else:
            print("\nError in your selection input. Please try again. ")


def optimize():
    """This function allows the user to calculate optimal job durations
    based on whether different tasks can be completed at the same time or
    not. This is the first step towards a proper CPM network."""
    # The function starts by opening the justData.txt file for reading,
    # and prints the number of jobs currently listed in the project. the
    # num_jobs statement scales the number of lines to the number of jobs,
    # as in text file, each job takes up three lines of information and one
    # spacing line.
    data_list = open('justData.txt')
    num_jobs = int(len(data_list.readlines()) / 4)
    print("\nThere are " + str(num_jobs) + " jobs listed in the project, "
                                           "currently. ")

    # The following chunk of statements counts the number of jobs in the
    # project text file currently and prints a list of every job in the
    # project, along with it's project name, without the number of days and
    # workers corresponding to the job. We use justData.txt here instead of
    # jobData.txt, as it made it easier to read lines of only integers. I
    # understand in the real world, I would only make one text file
    # containing user data and write code to better read the data.
    data_list = [x[:-1] for x in open('justData.txt').readlines()]
    counter = 0
    # Each 'x' in the for loop below goes through and reads every 1st line
    # of a four line chunk from the text file, as those lines contain each job
    # name.
    for x in data_list[0::4]:
        counter += 1
        print("Job " + str(counter) + ". " + str(x))

    # Day and worker values are every 2nd and 3rd line of a four line chunk,
    # as those lines contain the corresponding values. The following chunk
    # of code computes the total number of days and workers required for job
    # completion, prior to any optimization occuring.
    day_values = data_list[1::4]
    worker_values = data_list[2::4]
    total_days = 0
    total_workers = 0
    for x in day_values:
        total_days += int(x)
    for x in worker_values:
        total_workers += int(x)
    print("\nYour project will require at least", str(total_days),
          "days and at least", str(total_workers),
          "workers in total to complete without any optimizations. ")

    check_another = "0"
    while check_another == "0":
        # The input below splits the user input into separate elements and
        # builds a list called 'overlap'. The input should be integer
        # values. Admittedly, this section is not as robust as other
        # functions, as time constraints and that users should only input
        # job numbers (integers) shouldn't result in issues.
        overlap = list(input(
            "\nEnter job numbers that can be completed at the same time, "
            "separated by commas: ").strip().split(','))

        # The following chunk of code will take the jobs that can overlap,
        # check which of those jobs' required days is the largest, and only
        # adds that value to the rest of the required days to compute the
        # total job time duration.
        overlap_day_values = []
        for x in overlap:
            overlap_day_values.append(data_list[1 + ((int(x) - 1) * 4)])

        nonoverlap_day_values = [x for x in day_values if
                                 x not in overlap_day_values]

        for i in range(0, len(nonoverlap_day_values)):
            nonoverlap_day_values[i] = int(nonoverlap_day_values[i])
        for i in range(0, len(overlap_day_values)):
            overlap_day_values[i] = int(overlap_day_values[i])

        max_total_overlap_day = int(max(overlap_day_values))

        new_total_days = max_total_overlap_day + sum(nonoverlap_day_values)

        print("\nYour project will now require at least", str(new_total_days),
              "days and at least", str(total_workers),
              "workers in total to complete. ")
        check_another = input(
            "\nEnter '0' to check another configuration, or anything else to "
            "return to the main menu. ")
    print("Returning to the main menu! ")


def job_view_startup():
    """This function is called at the when users select the job view option
    from the main menu. It only displays an introduction message and then
    calls the job_view() function."""
    data_list = open('jobData.txt')
    num_jobs = int(len(data_list.readlines()) / 4)
    print("There are " + str(num_jobs) + " jobs listed in the project, "
                                         "currently. ")
    job_view()


def job_view():
    """This function allows the user to read the data currently inputted in
    the project file. It opens the jobData.txt file, prints a list of the
    current jobs in the file, and prompts the user to input a job number."""
    # The while loop evaluates the 'view_another' variable. While
    # 'view_another' equals 'True', the user can choose jobs to view from
    # their text files.
    view_another = True
    while view_another == True:
        try:
            # The chunk of code below opens the jobData.txt file, tells the
            # user how many jobs are stored the project currently, allows
            # the user to input options between 1 and the number of jobs,
            # where the function will print the job information previously
            # stored in the text file.
            # The following two statements opens the jobData.txt file and
            # assigns the lines of the text file as the variable value.
            job_data_list = open('jobData.txt')
            read = job_data_list.readlines()

            # The statement below prompts the user to pick a job they'd like
            # to see, by inputting a job number.
            job_selection = int(input("Enter job number you'd like to see: "))

            # The following statements scale the user input into a number
            # that aligns with the number of jobs in the text file. In the
            # text file, each job takes up three lines of information and one
            # spacing line. These scaling statements are used in the
            # upcoming if statement.
            job_index = 4 * (job_selection - 1)
            data_list = open('jobData.txt')
            num_jobs = int(len(data_list.readlines()) / 4)

            # The if statement below checks if there exists a job
            # corresponding to the user input for job_selection. If there
            # isn't a job within the range that exists, a statement will be
            # printed telling the user of such and then the while loop
            # repeats the job_selection prompt again.
            if job_index <= -1 or job_selection > num_jobs:
                print("There is not currently a job number " + str(
                    job_selection) + ". \n\nThere are " + str(
                    num_jobs) + " jobs listed in the project, currently. ")
            # If the user's job_selection input is within the correct bounds,
            # then a statement will print that displays that job's name,
            # duration of job, and number of workers the job will require,
            # as noted by the user earlier in their project.
            else:
                print(
                    str(job_selection) + ". " + str(read[job_index]) + "   " +
                    str(read[job_index + 1]) + "   " +
                    str(read[job_index + 2]))
                return_prompt = input(
                    "Enter '0' to view another job, or anything else to "
                    "return to the main menu. ")
                if return_prompt != "0":
                    view_another = False
        except:
            print("Error in your input, please try again. ")
    print("Returning to the main menu! ")


def job_collect():
    """This function adds jobs to the data text files. If needed, it will
    create new files but if project files already exist, it will append new
    data inputs into the project."""
    print("Now adding jobs to the list. ")
    # The while loop evaluates the 'add_data' variable. While 'add_data'
    # equals 'True', the user can input jobs into their text files.
    add_data = True
    while add_data == True:
        print("\nPlease enter job name, duration, and number of workers. ")
        try:
            # Users are prompted to input a name for their job, the number
            # of days their job will take, and the number of works their job
            # requires. The input statements are all grouped and executed
            # before the write statements to ensure that all parts of the
            # job are collected (without error) before the program appends
            # anything into the text files.
            job_name = input("What is the name of the job? ")
            job_duration = int(input(
                "How long will this job take to complete (in days)? (Please "
                "enter a whole number) "))
            job_workers = int(input(
                "What is the minimum number of workers this job requires to "
                "complete? (Please enter a whole number) "))

            # Below the function inputs data into two similar .txt files.
            # jobData.txt includes text for each job, while justData includes
            # integers only apart from the job names. This was intentionally
            # done to simplify my workflow for the purposes of the integration
            # project. In the real world, I would not duplicate project files.
            # We use the option 'a' in the open() statement to append the
            # existing files.
            in_file = open("jobData.txt", 'a')
            in_file.write("Job name: " + job_name)
            in_file.write("\nDuration of job: " + str(job_duration) + " days")
            in_file.write("\nNumber of workers: "
                          + str(job_workers) + " workers")
            in_file.write("\n\n")
            in_file.close()

            in_file = open("justData.txt", 'a')
            in_file.write(job_name)
            in_file.write("\n" + str(job_duration))
            in_file.write("\n" + str(job_workers))
            in_file.write("\n\n")
            in_file.close()

            print("Job information has been collected. ")

            return_prompt = input(
                "\nEnter '0' to input another job, or anything else to "
                "return to the main menu. ")
            if return_prompt != "0":
                add_data = False
            # If the user inputs anything above in the incorrect format,
            # the except clause below will display a generic error message
            # and the loop will allow the user to try again.
        except:
            print("Your input was not in the correct format. Please try "
                  "again. ")
    print("\nDone! All data was saved in the file 'jobData.txt' and "
          "'justData.txt. Returning to the main menu! ")


def reset_list():
    """This function is how the program starts a new job. The program
    creates two new text files: jobData.txt and justData.txt which are accessed
    and edited in the other options of the program. We use the 'w' option
    for the open() command to overwrite existing files in the project
    folder."""
    print("Are you sure you want to start a new job list? \nThis will erase "
          "all current list data! ")
    warning = input("\nEnter 'y' to confirm, or anything else to go back to "
                    "the main menu. ")
    if warning == "y":
        print("\nAll previous data has been erased. Starting new job list. ")
        in_file = open("jobData.txt", 'w')
        in_file.close()
        in_file = open("justData.txt", 'w')
        in_file.close()
        job_collect()
    else:
        print("Returning to the main menu! ")


def menu():
    """This function is a menu that allows the user to call the different
    functions."""
    # The while loop evaluates the boolean value of 'run'. While 'run'
    # equals 'True', it allows the user to keep calling functions until
    # they're done with the program. When they're done, they should input
    # option '0', and input something other than 'y' to end the program.
    run = True
    while run == True:
        print(
            "\nMain Menu: \n1. Start a new project. \n2. Add jobs to existing "
            "list. \n3. View jobs currently in list. \n4. Optimize project. "
            "\n\n5. Other COP 1500 requirements. \n\n0. End Program. ")
        select_option = input("\nWhich option would you like to utilize? ")
        if select_option == "1":
            reset_list()
        elif select_option == "2":
            job_collect()
        elif select_option == "3":
            job_view_startup()
        elif select_option == "4":
            optimize()
        elif select_option == "5":
            requirements()
        elif select_option == "0":
            run = False
        # If the user inputs something other than the numbers 0-5, they will
        # be prompted to try again.
        else:
            print("\nError in your selection input. Please try again. ")


def main():
    """This function runs at the startup of the program. It displays an
    introduction message and then calls the menu() function."""
    print("Welcome to the job optimization program.",
          "Designed by ViTuan Phan.",
          "This is the final iteration of this project.", sep="\n\n",
          end="\n\n")
    menu()


if __name__ == "__main__":
    main()

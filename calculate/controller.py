from calculate.view import View
from calculate.operators import Operators


class Controller:
    def __init__(self):
        self.operator = Operators()
        self.result = None

    def run(self):
        """
            Run the principal Menu and the user can choice
            which operation he would like to use.
        """
        View.print_menu()
        is_running = True
        while is_running:
            input_message = "Enter your choice"
            user_input = View.get_user_input(input_message)
            if self._is_input_valid(user_input):
                self._operations(user_input)
                View.print_menu()
            is_running = self._is_not_quit(user_input)
        View.end_message()

    def _is_input_valid(self, user_input):
        """
            Checks if the input corresponds to a possibility of operations.

            :param user_input: User input enter in the method run().
            :return: Return True if the input corresponds to a possibility of operations
                     otherwise it return False.
        """
        return user_input in ["1", "2", "3", "4"]

    def _operations(self, user_input):
        """
            Calls the function corresponding with the operation ask by the user and
            get the user operation by an input.

            :param user_input: User input enter in the method run().
        """
        input_message = "Enter the expression to calculate"
        operation = View.get_user_input(input_message)

        if user_input == "1":
            self.result = self.operator.addition(operation)
        elif user_input == "2":
            self.result = self.operator.subtraction(operation)
        elif user_input == "3":
            self.result = self.operator.multiplication(operation)
        elif user_input == "4":
            self.result = self.operator.division(operation)

        View.print_result(operation, self.result)
        View.continue_message()

    def _is_not_quit(self, user_input):
        """
            Checks if the user ask for stop the script thanks to the input enter
            in the method run().

            :param user_input: User input enter in the method run().
            :return: True if the user ask for exit the script.
        """
        return user_input != "5"

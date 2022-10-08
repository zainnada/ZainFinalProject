
class Constants:
    # Employment Type
    FULL_TYPE = "FULL"
    PART_TYPE = "PART"

    # Book Status
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    # Orders status
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"
    # ACTIVE = "ACTIVE" // redundant constant


class Utils:

    @staticmethod
    def empty_checker(*user_input: str):
        for item in user_input:
            if item.isspace() or item == "":
                return True
        return False

    @staticmethod
    def digit_checker(*user_input: str):
        for item in user_input:
            if item.isdigit():
                return True


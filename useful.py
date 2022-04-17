class Useful:
    def format_name(first, last):
        """Take first and last name as input
        and returns formatted as TitleCase"""
        formatted_first = first.title()
        formatted_last = last.title()
        return formatted_first, formatted_last

    def reverse(item):
        """Reverse a string, list, or tuple"""
        return item[::-1]
    
    def dpi_off():
            # FULL CREDIT to
        # https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis
        # for the DPI-Awareness code block!
        #################################################
        import ctypes
        # Query DPI Awareness (Windows 10 and 8)
        awareness = ctypes.c_int()
        errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
        print(awareness.value)

        # Set DPI Awareness  (Windows 10 and 8)
        errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        # the argument is the awareness level, which can be 0, 1 or 2:
        # for 1-to-1 pixel control I seem to need it to be non-zero (I'm using level 2)

        # Set DPI Awareness  (Windows 7 and Vista)
        success = ctypes.windll.user32.SetProcessDPIAware()
        #################################################

    def string_to_list(string):
        """Take a string as input and return a list of the
        constituent contents.  Ex: 'ScaerieTale' returns
        ['S', 'c', 'a', 'e', 'r', 'i', 'e', 'T', 'a', 'l', 'e'] ♥"""
        return [letter for letter in string]

from Game import *

try:
    pass
    Game()
except Exception as e:
    print("\n\n----------OOPS!----------\n"
          "The Game crashed because:\n")
    print(e)
    print("\nPlease create an issue on Github with the error information.\n"
          "Thank You!\n\n")
    input("Press Enter to exit")
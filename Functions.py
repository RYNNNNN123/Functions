def shutdown(user_input):
    if user_input == "Yes":
        print("shutting down")
    elif user_input.lower() == "no":
        print("abort shut down")
    else:
        print("sorry.")


choice = input("Do you want to shut down? ")
shutdown(choice)
print("Are you a superfan of 'Stranger Things' or a fake fan?")
print()
print("Answer these questions to find out.")

# Check if someone likes Eleven
eleven = input("Does someone know telekinesis?(yes/no) ")
if eleven.lower() == "yes":
    print("Great! You're on the right track!")
    likes_eleven = input("Who knows telekinesis?(character name) ")
    if likes_eleven.lower() == "eleven":
        print("You're definitely a superfan!")
    else:
        print("Hmm, you're missing out on an awesome character!")
else:
    print("Oh no, you're not a superfan!")

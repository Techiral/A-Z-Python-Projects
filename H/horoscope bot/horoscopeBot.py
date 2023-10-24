import random

# Dictionary of zodiac signs and their date ranges
zodiac_signs = {
    "Aries": "March 21 - April 19",
    "Taurus": "April 20 - May 20",
    "Gemini": "May 21 - June 20",
    "Cancer": "June 21 - July 22",
    "Leo": "July 23 - August 22",
    "Virgo": "August 23 - September 22",
    "Libra": "September 23 - October 22",
    "Scorpio": "October 23 - November 21",
    "Sagittarius": "November 22 - December 21",
    "Capricorn": "December 22 - January 19",
    "Aquarius": "January 20 - February 18",
    "Pisces": "February 19 - March 20"
}

# Function to get a random horoscope message
def get_random_horoscope():
    horoscopes = [
        "Today is a day for new opportunities and adventures!",
        "You may face challenges, but your determination will help you overcome them.",
        "Your creative energy is at its peak today. Use it wisely.",
        "Stay open to new friendships. You might meet someone special.",
        "Focus on your health and well-being today.",
    ]
    return random.choice(horoscopes)

# Main function for the HoroscopeBot
def horoscope_bot():
    print("Welcome to the HoroscopeBot!")
    while True:
        user_input = input("Enter your zodiac sign (or 'quit' to exit): ").capitalize()
        if user_input == "Quit":
            print("Goodbye!")
            break
        if user_input in zodiac_signs:
            print(f"Your zodiac sign is {user_input}.")
            print(f"Date Range: {zodiac_signs[user_input]}")
            horoscope = get_random_horoscope()
            print("Horoscope: " + horoscope)
        else:
            print("Invalid zodiac sign. Please enter a valid zodiac sign.")

# Run the HoroscopeBot
horoscope_bot()

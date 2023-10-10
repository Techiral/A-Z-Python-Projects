import pyjokes
  
# using get_joke() to generate a single joke
#language is english
#category is neutral
print("Which type of joke you want to hear:-")
print("neutral")
print("twister")
print("all")
s=str(input("Enter the category:- "))
My_joke = pyjokes.get_joke(language="en", category=s)
  
print(My_joke)
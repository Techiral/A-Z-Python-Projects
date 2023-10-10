import pyjokes
  
# using get_joke() to generate a single joke
#language is english
print("Categories:- ")
print("neutral")
print("twister")
print("all")
s=str(input("Type your categories:- "))
My_joke = pyjokes.get_joke(language="en", category=s)
  
print(My_joke)
planet = {
    'mercury' : " Mercury is the closest planet to the Sun and is known for its extreme temperature variations. It has a thin atmosphere and a heavily cratered surface.",
    'Venus' :"Venus is often called Earth's sister planet because of its similar size and composition. However, it has a thick, toxic atmosphere that traps heat, making it the hottest planet in our solar system.",
    'earth' : "Earth is the only known planet to support life. It has a diverse ecosystem, with a range of climates and environments, including oceans, mountains, and deserts.",
    'mars' : "Often called the Red Planet due to its reddish appearance, Mars has a thin atmosphere and is the focus of human exploration for its potential to host future colonies.",
    'jupiter' : "Jupiter is the largest planet in the solar system, with a strong magnetic field and a turbulent atmosphere filled with swirling clouds, including the famous Great Red Spot.",
    'saturn' : "Saturn is known for its stunning ring system, composed of icy particles. It's a gas giant with a complex system of moons.",
    'uranus' : " Uranus is a gas giant with a unique feature—it rotates on its side. It has a blue-green appearance and a system of rings.",
    'Neptune' : "Neptune is the farthest planet from the Sun and is known for its deep blue color. It has powerful storms, including the Great Dark Spot, and a family of moons."
}
name = input("Name of the planet: ").lower()
if name in  planet:
    print(planet[name])
else:
    print("Invalid Planet name.")

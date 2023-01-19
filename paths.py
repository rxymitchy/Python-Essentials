from pathlib import Path
#Absolute path - start from root path
#Relative path - start from current
#Linux - forward slash

# path = Path("practice")
# print(path.mkdir())

# path = Path("eccomerce")
# print(path.mkdir())

# path = Path("eccomerce")
# print(path.rmdir())

path = Path()
for file in (path.glob('*.py')):#gets all python files in the curent directory
    print(file)
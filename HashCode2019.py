

liste = [["a_example.txt", "a.out"],
         ["b_lovely_landscapes.txt", "b.out"],
         ["c_memorable_moments.txt", "c.out"],
         ["d_pet_pictures.txt", "d.out"],
         ["e_shiny_selfies.txt", "e.out"]]

nb = 0

def create_all_horizontal


class Photo():
    def __init__(self, orientation, nb_tag, tags):
        self.orientation = orientation
        self.nb_tag = nb_tag
        self.tags = tags
        self.parents

file = open(liste[nb][0], 'r')

N = int(str(file.readline()))
print(N)

all_photos = []

for i in range(N):
    try:
        a, b, *x = map(str, file.readline().split(" "))
        x[-1] = x[-1].replace("\n", "")
        all_photos.append(Photo(a, b, x))
    except Exception as e:
        print(e)

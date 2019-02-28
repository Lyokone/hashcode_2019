

liste = [["a_example.txt", "a.out"],
         ["b_lovely_landscapes.txt", "b.out"],
         ["c_memorable_moments.txt", "c.out"],
         ["d_pet_pictures.txt", "d.out"],
         ["e_shiny_selfies.txt", "e.out"]]

nb = 0
global_id = 0

def create_all_horizontal_photos(list_photo):
    res = []
    for i in range(len(list_photo)):
        for j in range(i,len(list_photo)):
            if i != j:
                new_tags = list_photo[i].tags + list_photo[j].tags
                new_tags = list(set(new_tags))
                res.append(Photo(global_id, "H", len(new_tags), new_tags, [
                           list_photo[i].id, list_photo[j].id]))
                global_id += 1
    return res

class Photo():
    def __init__(self, id, orientation, nb_tag, tags, parents=[]):
        self.id = id
        self.orientation = orientation
        self.nb_tag = nb_tag
        self.tags = tags
        self.parents = parents


    def __repr__(self):
        return str(self.tags)

file = open(liste[nb][0], 'r')

N = int(str(file.readline()))
print(N)

all_photos_horizontal = []
all_photos_vertical = []

for i in range(N):
    try:
        a, b, *x = map(str, file.readline().split(" "))
        x[-1] = x[-1].replace("\n", "")

        p = Photo(i, a, b, x)
        if p.orientation == "V":
            all_photos_vertical.append(p)
        else:
            all_photos_horizontal.append(p)

    except Exception as e:
        print(e)

    global_id += 1

print(create_all_horizontal_photos(all_photos_vertical))

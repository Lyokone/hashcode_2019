

liste = [["a_example.txt", "a.out"],
         ["b_lovely_landscapes.txt", "b.out"],
         ["c_memorable_moments.txt", "c.out"],
         ["d_pet_pictures.txt", "d.out"],
         ["e_shiny_selfies.txt", "e.out"]]

nb = 2
global_id = 0

def create_all_horizontal_photos(list_photo):
    global global_id
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

all_photos_horizontal.extend(create_all_horizontal_photos(all_photos_vertical))
#print(all_photos_horizontal)


def calculate_score(photo1, photo2):
    total1 = 0
    for x in photo1.tags:
        if x in photo2.tags:
            total1 += 1

    total2 = len(set(photo1.tags) - set(photo2.tags))
    total3 = len(set(photo2.tags) - set(photo1.tags))

    return min(total1, total2, total3)



def find_the_best(list_photo):
    current_photo = list_photo[0]

    score_max = 0
    photo_max = None

    if len(current_photo.parents) > 0:
        res = [current_photo.parents]
    else:
        res = [[current_photo.id]]


    list_photo.remove(current_photo)
    print("start", current_photo)

    start_len = len(list_photo)
    while len(list_photo) > 0:
        print(str((start_len-len(list_photo))/start_len * 100) + "%")
        for photo in list_photo:
            if photo != current_photo:
                score = calculate_score(photo, current_photo)
                if score > score_max:
                    #print("new max", photo)
                    score_max = score
                    photo_max = photo

        #print(photo_max.id, photo_max.tags, "choosed", "score:", score_max)


        for photo in list_photo:
            if photo != current_photo and photo != photo_max:
                if photo_max.id in photo.parents:
                    list_photo.remove(photo)

        #print("current",list_photo, current_photo)
        list_photo.remove(photo_max)
        current_photo = photo_max

        if len(current_photo.parents) > 0:
            res.append(current_photo.parents)
        else:
            res.append([current_photo.id])


        #print("after", list_photo, current_photo)

        score_max = 0
        photo_max = None

    return res


res = find_the_best(all_photos_horizontal)

ff = open(liste[nb][1], 'w')
ff.write(str(len(res)) + "\n")
for x in res:
    print(x)
    for y in x:
        ff.write(str(y) + " ")

    ff.write("\n")

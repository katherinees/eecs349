import numpy as np
import json
import pprint

# Question 5
def cosine_similarity(a, b):
    return float(np.dot(a, b.T) / (np.linalg.norm(a) * np.linalg.norm(b)))

# Question 6
with open('PS4/homework4/cnn_dataset.json') as json_data:
    d = json.load(json_data)
    pix_mj1 = np.array(d['pixel_rep']['mj1'])
    pix_mj2 = np.array(d['pixel_rep']['mj2'])
    pix_cat = np.array(d['pixel_rep']['cat'])
    vgg_mj1 = np.array(d['vgg_rep']['mj1'])
    vgg_mj2 = np.array(d['vgg_rep']['mj2'])
    vgg_cat = np.array(d['vgg_rep']['cat'])
    print('sim pix_mj1, pix_mj2', cosine_similarity(pix_mj1, pix_mj2))
    print('sim pix_mj1, pix_cat', cosine_similarity(pix_mj1, pix_cat))
    print('sim pix_mj2, pix_cat', cosine_similarity(pix_mj2, pix_cat))
    print('sim vgg_mj1, vgg_mj2', cosine_similarity(vgg_mj1, vgg_mj2))
    print('sim vgg_mj1, vgg_cat', cosine_similarity(vgg_mj1, vgg_cat))
    print('sim vgg_mj2, vgg_cat', cosine_similarity(vgg_mj2, vgg_cat))

# Question 8
# (I changed appropriate variables and reran to do the pixel captions
# and vgg captions separately)
with open('PS4/homework4/dataset.json') as json_data:
    f = open('vgg.txt', 'w')
    dataset = json.load(json_data)
    vgg_rep = np.load('PS4/homework4/vgg_rep.npy')
    pix_rep = np.load('PS4/homework4/pixel_rep.npy')
    train_indices = []
    for t in dataset['train']:
        train_indices.append(dataset['images'].index(t))

    for x in dataset['test']:
        testindex = dataset['images'].index(x)
        best_so_far = train_indices[0]
        best_cos = -1
        for ex in train_indices:
            this_cos = cosine_similarity(vgg_rep[testindex], vgg_rep[ex])
            if this_cos > best_cos:
                best_cos = this_cos
                best_so_far = ex
        best_match_im_name = dataset['images'][best_so_far]
        caption = dataset['captions'][best_match_im_name]
        print(x, best_match_im_name, caption)
        f.write(caption)
        f.write('\n')

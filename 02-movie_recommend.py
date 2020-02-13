import numpy as np
import pandas as pd

movies = pd.read_csv('movies_ratings.csv')

# take out unique genres
genres = []
for i in range(len(movies['genre'])):
    genre = movies['genre'][i].split(',')
    for j in range(len(genre)):
        genres.append(genre[j])
genres = np.unique(genres)
genres = genres[2:]


def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    score = len(s1.intersection(s2)) / len(s1.union(s2))
    return score


def scores(user_movies):
    Scores = []
    for i in range(len(genres)):
        m_list = []
        for j in range(len(movies['genre'])):
            genre = movies['genre'][j].split(',')
            for k in range(len(genre)):
                if genre[k] == genres[i]:
                    m_list.append(movies['name'][j])
    #         print(m_list)
        score = jaccard_similarity(user_movies,m_list)
        Scores.append(score)
    genre_index = np.argmax(Scores)
    max_genre = genres[genre_index]
    return max_genre, Scores


def genre(max_genre):
    rec_mov = []
    mov_rate = []
    for j in range(len(movies['genre'])):
        genre = movies['genre'][j].split(',')
#         print(genre)
        for k in range(len(genre)):
            if genre[k] == max_genre:
                rec_mov.append(movies['name'][j])
                mov_rate.append(movies['rating'][j])
    mov_rates = np.array(np.argsort(mov_rate))
    rate_index = np.array(mov_rates[-10:])
    movie_names = []
    for i in range(len(rate_index)):
        mov_index = rate_index[-i]
        movie_names.append(rec_mov[mov_index])
    return movie_names


def result(Scores, max_genre):
    genre_score = []
    for i in range(18):
        genre_score.append(genres[i])
        genre_score.append(Scores[i])
    print("Scores :- ")
    for i in range(0,len(genre_score),2):
        print("   ",genre_score[i]," = ",genre_score[i+1])
    print("Preferred Genre :", max_genre)
    print("Suggested Movies :-")
    for i in range(10):
        print("   ",i+1,".",genre(max_genre)[i])


user_movies = ["She's the One","Time to Kill","American Buffalo","Rendezvous in Paris (Rendez-vous de Paris","Alaska","Fled",
               "Kazaam","Bewegte Mann","Magic Hunter","Larger Than Life","Boy Called Hate","Power 98","Two Deaths",
               "Sorority House Massacre", "Sorority House Massacre II", "Bamboozled", "Bootmen", "Digimon: The Movie", "Get Carter",
               "Get Carter", "Meet the Parents", "Requiem for a Dream", "Tigerland", "Two Family House", "Contender", "Home for the Holidays",
               "Postino", "Confessional", "Indian in the Cupboard", "Eye for an Eye", "Mr. Holland's Opus", "Drop Zone", "Destiny Turns on the Radio",
               "Don't Be a Menace to South Central While Drinking Your Juice in the Hood", "Two if by Sea", "Bio-Dome","Wild Bill", "Browning Version",
               "Bushwhacked", "Burnt By the Sun (Utomlyonnye solntsem)", "Before the Rain (Pred dozhdot)", "Before Sunrise" ,"Billy Madison",
               "Babysitter", "Boys on the Side", "Cure", "Castle Freak", "Circle of Friends", "Clerks", "Don Juan DeMarco", "Disclosure",
               "Dream Man", "Very Brady Sequel","Stefano Quantestorie","Death in the Garden (Mort en ce jardin","Crude Oasis", "Sudden Death",
               "GoldenEye", "American President", "Dracula: Dead and Loving It ", "Balto ", "Nixon ", "Cutthroat Island ", "Casino",
               "Sense and Sensibility ", "Four Rooms ", "Ace Ventura: When Nature Calls ", "Money Train", "Get Shorty", "Copycat ",
               "Assassins ", "Powder ", "Leaving Las Vegas ", "Othello", "Now and Then", "Persuasion ", "City of Lost Children",
               "Shanghai Triad (Yao a yao yao dao waipo qiao)", "Dangerous Minds", "Twelve Monkeys", "Wings of Courage", "Babe ",
               "Carrington", "Dead Man Walking", "Across the Sea of Time", "It Takes Two", "Clueless", "Cry", "Richard III", "Dead Presidents",
               "Restoration", "Mortal Kombat", "To Die For", "How to Make an American Quilt", "Seven (Se7en)", "Pocahontas", "When Night Is Falling",
               "Usual Suspects", "Guardian Angel", "Mighty Aphrodite", "Lamerica", "Big Green", "Georgia", "Kids of the Round Table","Dancer in the Dark",
               "Best in Show", "Beautiful", "Barenaked in America", "Broken Hearts Club", "Girlfight", "Remember the Titans", "Hellraiser",
               "Hellbound: Hellraiser II", "Hellraiser III: Hell on Earth", "Faraway", "Beach Party", "Bikini Beach", "Return of the Fly",
               "Pajama Party", "Stranger Than Paradise", "Voyage to the Bottom of the Sea", "Fantastic Voyage", "Abbott and Costello Meet Frankenstein",
               "Bank Dick", "Creature From the Black Lagoon", "Giant Gila Monster", "Invisible Man", "Killer Shrews", "Kronos", "Kronos",
               "Phantom of the Opera", "Runaway", "Slumber Party Massacre", "Slumber Party Massacre II", "Slumber Party Massacre III"]

max_genre, Scores = scores(user_movies)
result(Scores, max_genre)

import requests
import pandas as pd

# Rate limit of 40 req/s as curteousy, with needless bulk flagged
# Access Token is linked to Dallin's account. USE RESPONSIBLY

# Additionally, TMBD requires attribution for their data. 
## This will mean extra effort to make sure any data or vis attributes them
## correctly or we may face legal action.

# TMBD has a 6 month limit of cached data. This means that 6 months
## after obtaining the data we must either delete it or refresh our requests.
## Another term makes it appear that also applies to our analyses.

# Lastly, we must use the TMDB logo to identify our use of TMDB, the TMDB APIs, 
## or TMDB Content. So a logo needs to be downloaded and placed alongside vis we produce



root = "https://api.themoviedb.org/3"
opt = "/search/movie?query=2020" 
furl = root + opt
# options include /search/movie?query=... for text based searches
# /discover/... filters by definable values like year released, etc
# /find/... can use an external ID like IMDB ID to find connected values
# /movie/... for exact ID
# "movie/343611" 

# 2000+ or last 20 yrs
# 1950-1999 comparison

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTg5YjZkNTE2YWVlZGU4MmI2ZGNmYWY1M2U3NmM2OCIsIm5iZiI6MTc5NDY2ODUyMC44NDUsInN1YiI6IjZhZjg3N2U4MjIwM2U1OTg4ZDMyOTJhYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HADi9PAJcKoFG20_bpptWHSiCXuxohmFpQ48n3XDnFw"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(furl, headers=headers)
movielist2020 = response.json()["results"]
# create dictionaries for this first set
# 3 big dictionaries: popularity, details, and genre
pop_2020 = {}
all_genres = set()
movIDs = set()

for entry in movielist2020:
    movID = entry["id"]

    if not movID in movIDs:
        movIDs.add(movID)

        poster = f"{root}{entry["poster_path"]}"
        name = entry["original_title"]
        lang = entry["original_language"]
        date = entry["release_date"]
        pop = entry["popularity"]
        score = entry["vote_average"]
        genres = entry["genre_ids"]

        pop_2020[movID] = {
            "Title": name,
            "Language": lang,
            "Date": date,
            "Genres": genres,
            "Poster_URL": poster,
            "TMDB_PopScore": pop,
            "TMDB_ViewerRating": score
        }


# Now details dictionary
det_2020 = {}

for i in movIDs:
    opt = f"/movie/{i}"
    rep = requests.get(furl, headers=headers)
    curr_mov = rep.json()
    # store the following in details
    # i for id
    # title for the name
    # runtime for time in minutes
    # revenue for profit calc
    # budget for profit calc
    # origin_country for Location of Release
    # production_companies - unpack list into companies dict, save only list of names for details
    # status - create boolean for Released vs Unreleased
    continue




## One scetion pulls the id, pop score, and other relevant data and holds it in a data frame
## Next section loops through each id to pull new data into a different data frame
## Then practice joining the two together as a raw dataset.

# test successful. Got response back for movie/id_term

# Good tags to look at:
## adult (bool)
## title (str)
## revenue (int)
## budget (int)
## popularity (float) (see their methodology)
## vote_count (int)
## vote_average (float) (see their methodology)
## genres (id= int, name= str)
## production_companies -> name (str)
## release_date (date, YYYY-MM-DD)
## runtime (int, in minutes)
## spoken_languages -> name (str)
## original_language -> (str)
## origin_country (str list)
## poster_path (str, needs origin url to merge with) 

# Look for the results field for search arrays, then request the individual movie id
# For movie documentation
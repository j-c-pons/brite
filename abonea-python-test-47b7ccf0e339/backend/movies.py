from google.cloud import ndb
import requests

omdb_api_key= f'f9707c80'

class MovieFetcher():

    @classmethod
    def fetch_movies(cls):
        ancestor_key = ndb.Key("BriteGroup", "movies")
        query = Movie.query(ancestor=ancestor_key)

        #if not list(query.fetch(limit=1)):
            # Fetch 100 movies from OMDB API
            #for _ in range(100):
                #movie_data = get_movie_data()
                #save_movie_to_datastore(movie_data)

        #print(query)
        # entity = cls(
        #     parent=user.key,
        #     email=email,
        # )
        # entity.put()
        # return entity

    @classmethod
    def get_movie_data():
        random_title = "movie"  # Modify this to get specific types of movies
        url = f"http://www.omdbapi.com/?t={random_title}&apikey={omdb_api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    #@classmethod
    def test(self):
        print("data")
        #ancestor_key = ndb.Key("BriteGroup", "movies")

        # entity = Movie( 
        #     #parent = ancestor_key,
        #     title="test"
        # )
        # entity.put()
        query = Movie.query()
        names = [c.test for c in query]
        print(names)
    
class Movie(ndb.Model):
    #created = ndb.DateTimeProperty(indexed=False)
    title = ndb.StringProperty(indexed=True)
    #phone = ndb.StringProperty(indexed=True)
    #normalized_name = ndb.ComputedProperty(lambda self: self.name and self.name.lower(), indexed=True)

if __name__ == '__main__':
    client = ndb.Client()
    with client.context():
        omdb_fetcher = MovieFetcher()
        #omdb_fetcher.fetch_movies()
        omdb_fetcher.test()
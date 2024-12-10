import db_creation
import db_creation.importBelong
import db_creation.importBook
import db_creation.importFav
import db_creation.importGenres
import db_creation.importRating
import db_creation.importUser
import db_creation.importVisu

db_creation.importBook.addBooks()
db_creation.importGenres.add_genres()
db_creation.importUser.add_users()
db_creation.importRating.add_ratimgs()
db_creation.importVisu.add_visuals()
db_creation.importBelong.add_belongs()
db_creation.importFav.add_fav()
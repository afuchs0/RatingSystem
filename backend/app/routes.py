from flask import jsonify, request
from app import app  # Import the app instance created in __init__.py
from flask_cors import CORS, cross_origin

# Example book data (in-memory)
books = [
    {
        "id": 2767052,
        "title": "The Hunger Games",
        "series": "The Hunger Games #1",
        "author": "Suzanne Collins",
        "description": "WINNING MEANS FAME AND FORTUNE.LOSING MEANS CERTAIN DEATH.THE HUNGER GAMES HAVE BEGUN. . . .In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and once girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV.Sixteen-year-old Katniss Everdeen regards it as a death sentence when she steps forward to take her sister's place in the Games. But Katniss has been close to dead before\u2014and survival, for her, is second nature. Without really meaning to, she becomes a contender. But if she is to win, she will have to start making choices that weight survival against humanity and life against love.",
        "language": "English",
        "isbn": "9780439023481",
        "genres": 
            ['Young Adult',
            'Fiction',
            'Dystopia',
            'Fantasy',
            'Science Fiction',
            'Romance',
            'Adventure',
            'Teen',
            'Post Apocalyptic',
            'Action'
        ],
        "pages": 374,
        "awards": 
            ['Locus Award Nominee for Best Young Adult Book (2009)',
            'Georgia Peach Book Award (2009)',
            'Buxtehuder Bulle (2009)',
            'Golden Duck Award for Young Adult (Hal Clement Award) (2009)',
            '\Grand Prix de lImaginaire Nominee for Roman jeunesse \u00e9tranger (2010)\',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2012)',
            '\West Australian Young Readers Book Award (WAYRBA) for Older Readers (2010)\',
            '\Red House Childrens Book Award for Older Readers & Overall (2010)\',
            'South Carolina Book Award for Junior and Young Adult Book (2011)',
            'Charlotte Award (2010)',
            'Colorado Blue Spruce Young Adult Book Award (2010)',
            'Teen Buckeye Book Award (2009)',
            '\Pennsylvania Young Readers Choice Award for Young Adults (2010)\',
            'Rhode Island Teen Book Award (2010)',
            '\Dorothy Canfield Fisher Childrens Book Award (2010)\',
            'Evergreen Teen Book Award (2011)',
            'Soaring Eagle Book Award (2009)',
            'Milwaukee County Teen Book Award Nominee (2010)',
            'Sakura Medal for Middle School Book (2010)',
            'Michigan Library Association Thumbs Up! Award (2009)',
            'Florida Teens Read (2009)',
            'Deutscher Jugendliteraturpreis for Preis der Jugendjury (2010)',
            'Iowa High School Book Award (2011)',
            'New Mexico Land of Enchantment Award for Young Adult (2011)',
            'Eliot Rosewater Indiana High School Book Award (2010)',
            'The Inky Awards for Silver Inky (2009)',
            'California Young Readers Medal for Young Adult (2011)',
            'Lincoln Award (2011)',
            'Kinderboekwinkelprijs (2010)',
            'Missouri Truman Readers Award (2011)',
            'CYBILS Award for Young Adult Fantasy & Science Fiction (2008)',
            'Literaturpreis der Jury der jungen Leser for Jugendbuch (2010)',
            'The Inky Awards Shortlist for Silver Inky (2009)',
            'Prix Et-lisez-moi (2011)',
            'Missouri Gateway Readers Award (2011)',
            'Oklahoma Sequoyah Award for High School and Intermediate (2011)',
            'Premio El Templo de las Mil Puertas for Mejor novela extranjera perteneciente a saga (2009)',
            '\Rebecca Caudill Young Readers Book Award (2011)\',
            'LovelyBooks Leserpreis for Fantasy (2009)',
            'LovelyBooks Leserpreis for Bestes Cover/Umschlag (2009)',
            'Premi Protagonista Jove for Categoria 13-14 anys (2010)'
        
        ],
        "likedPercent": 96.0,
        "price": 5.09
    },
    {
        "id": 2,
        "title": "Harry Potter and the Order of the Phoenix",
        "series": "Harry Potter #5",
        "author": "J.K. Rowling, Mary GrandPr\u00e9 (Illustrator)",
        "description": "There is a door at the end of a silent corridor. And it\u2019s haunting Harry Pottter\u2019s dreams. Why else would he be waking in the middle of the night, screaming in terror?Harry has a lot on his mind for this, his fifth year at Hogwarts: a Defense Against the Dark Arts teacher with a personality like poisoned honey; a big surprise on the Gryffindor Quidditch team; and the looming terror of the Ordinary Wizarding Level exams. But all these things pale next to the growing threat of He-Who-Must-Not-Be-Named - a threat that neither the magical government nor the authorities at Hogwarts can stop.As the grasp of darkness tightens, Harry must discover the true depth and strength of his friends, the importance of boundless loyalty, and the shocking price of unbearable sacrifice.His fate depends on them all.",
        "language": "English",
        "isbn": "9780439358071",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Magic',
            'Childrens',
            'Adventure',
            'Audiobook',
            'Middle Grade',
            'Classics',
            'Science Fiction Fantasy'
        
        ],
        "pages": 870,
        "awards": 
            ['Bram Stoker Award for Works for Young Readers (2003)',
            'Anthony Award for Young Adult (2004)',
            '\Mythopoeic Fantasy Award for Childrens Literature (2008)\',
            'Audie Award for Audiobook of the Year (2004)',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2004)',
            'Colorado Blue Spruce Young Adult Book Award (2006)',
            'Golden Archer Award for Middle/Junior High (2005)',
            'Deutscher Jugendliteraturpreis Nominee for Preis der Jugendjury (2004)',
            'Carnegie Medal Nominee (2003)'
        
        ],
        "likedPercent": 98.0,
        "price": 7.38
    },
    {
        "id": 2657,
        "title": "To Kill a Mockingbird",
        "series": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "description": "The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it, To Kill A Mockingbird became both an instant bestseller and a critical success when it was first published in 1960. It went on to win the Pulitzer Prize in 1961 and was later made into an Academy Award-winning film, also a classic.Compassionate, dramatic, and deeply moving, To Kill A Mockingbird takes readers to the roots of human behavior - to innocence and experience, kindness and cruelty, love and hatred, humor and pathos. Now with over 18 million copies in print and translated into forty languages, this regional story by a young Alabama woman claims universal appeal. Harper Lee always considered her book to be a simple love story. Today it is regarded as a masterpiece of American literature.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'School',
            'Literature',
            'Young Adult',
            'Historical',
            'Novels',
            'Read For School',
            'High School'
        
        ],
        "pages": 324,
        "awards": 
            ['Pulitzer Prize for Fiction (1961)',
            'Audie Award for Classic (2007)',
            'National Book Award Finalist for Fiction (1961)',
            'Alabama Author Award for Fiction (1961)'
        
        ],
        "likedPercent": 95.0,
        "price": 13.857813917678968
    },
    {
        "id": 1885,
        "title": "Pride and Prejudice",
        "series": "",
        "author": "Jane Austen, Anna Quindlen (Introduction)",
        "description": "Alternate cover edition of ISBN 9780679783268Since its immediate success in 1813, Pride and Prejudice has remained one of the most popular novels in the English language. Jane Austen called this brilliant work \"her own darling child\" and its vivacious heroine, Elizabeth Bennet, \"as delightful a creature as ever appeared in print.\" The romantic clash between the opinionated Elizabeth and her proud beau, Mr. Darcy, is a splendid performance of civilized sparring. And Jane Austen's radiant wit sparkles as her characters dance a delicate quadrille of flirtation and intrigue, making this book the most superb comedy of manners of Regency England.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Romance',
            'Historical Fiction',
            'Literature',
            'Historical',
            'Novels',
            'Historical Romance',
            'Classic Literature',
            'Adult'
        
        ],
        "pages": 279,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 1.0174518353800541
    },
    {
        "id": 41865,
        "title": "Twilight",
        "series": "The Twilight Saga #1",
        "author": "Stephenie Meyer",
        "description": "About three things I was absolutely positive.\r\n\r\nFirst, Edward was a vampire.\r\n\r\nSecond, there was a part of him\u2014and I didn't know how dominant that part might be\u2014that thirsted for my blood.\r\n\r\nAnd third, I was unconditionally and irrevocably in love with him.\r\n\r\nDeeply seductive and extraordinarily suspenseful, Twilight is a love story with bite.",
        "language": "English",
        "isbn": "9780316015844",
        "genres": 
            ['Young Adult',
            'Fantasy',
            'Romance',
            'Vampires',
            'Fiction',
            'Paranormal',
            'Paranormal Romance',
            'Supernatural',
            'Teen',
            'Urban Fantasy'
        
        ],
        "pages": 501,
        "awards": 
            ['Georgia Peach Book Award (2007)',
            'Buxtehuder Bulle (2006)',
            'Kentucky Bluegrass Award for 9-12 (2007)',
            'Prijs van de Kinder- en Jeugdjury Vlaanderen (2008)',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2009)',
            '\West Australian Young Readers Book Award (WAYRBA) for Older Readers (2008)\',
            'Garden State Book Award for Fiction (Grades 9-12) (2008)',
            'South Carolina Book Award for Young Adult Book Award (2008)',
            'Grand Canyon Reader Award for Teen Book (2008)',
            'Maryland Black-Eyed Susan Book Award for High School (2008)',
            'Golden Sower Award for Young Adult (2009)',
            '\Nevada Young Readers Award for Young Adult Category  (2007)\',
            '\The Flume: New Hampshire Teen Readers Choice Award (2007)\',
            '\Pennsylvania Young Readers Choice Award for Young Adult (2009)\',
            'Rhode Island Teen Book Award (2007)',
            'Evergreen Teen Book Award (2008)',
            'Michigan Library Association Thumbs Up! Award Nominee (2006)',
            'Teen Read Award Nominee for Best All-Time-Fave (2010)',
            'Deutscher Jugendliteraturpreis Nominee for Preis der Jugendjury (2007)',
            'Iowa High School Book Award (2008)',
            'Eliot Rosewater Indiana High School Book Award (2008)',
            'Lincoln Award (2008)',
            'Literaturpreis der Jury der jungen Leser for Cover (2007)',
            'Prix Et-lisez-moi (2008)',
            'Missouri Gateway Readers Award (2008)'
        
        ],
        "likedPercent": 78.0,
        "price": 2.1
    },
    {
        "id": 19063,
        "title": "The Book Thief",
        "series": "",
        "author": "Markus Zusak (Goodreads Author)",
        "description": "Librarian's note: An alternate cover edition can be found hereIt is 1939. Nazi Germany. The country is holding its breath. Death has never been busier, and will be busier still.By her brother's graveside, Liesel's life is changed when she picks up a single object, partially hidden in the snow. It is The Gravedigger's Handbook, left behind there by accident, and it is her first act of book thievery. So begins a love affair with books and words, as Liesel, with the help of her accordian-playing foster father, learns to read. Soon she is stealing books from Nazi book-burnings, the mayor's wife's library, wherever there are books to be found.But these are dangerous times. When Liesel's foster family hides a Jew in their basement, Liesel's world is both opened up, and closed down.In superbly crafted writing that burns with intensity, award-winning author Markus Zusak has given us one of the most enduring stories of our time.(Note: this title was not published as YA fiction)",
        "language": "English",
        "isbn": "9780375831003",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Young Adult',
            'Historical',
            'Classics',
            'War',
            'Holocaust',
            'World War II',
            'Books About Books',
            'Audiobook'
        
        ],
        "pages": 552,
        "awards": 
            ['National Jewish Book Award for Children\u2019s and Young Adult Literature (2006)',
            '\Book Sense Book of the Year Award for Childrens Literature (2007)\',
            'Buxtehuder Bulle (2008)',
            'Sydney Taylor Book Award for Teen Readers (2007)',
            'Prijs van de Kinder- en Jeugdjury Vlaanderen (2009)',
            'Michael L. Printz Award Nominee (2007)',
            'Exclusive Books Boeke Prize (2007)',
            'Rhode Island Teen Book Award Nominee (2008)',
            'The Quill Award Nominee for Young Adult/Teen (2006)',
            'Zilveren Zoen (2008)',
            'Teen Read Award Nominee for Best All-Time-Fave (2010)',
            'Deutscher Jugendliteraturpreis for Preis der Jugendjury (2009)',
            'Association of Jewish Libraries for Teen Book Award (2006)',
            'Lincoln Award Nominee (2010)',
            'Australian Book Industry Award (ABIA) Nominee for Literary Fiction (2008)',
            'Kathleen Mitchell Award',
            'Ena Noel Award (2008)',
            'Literaturpreis der Jury der jungen Leser for Jugendbuch (2009)',
            'LovelyBooks Leserpreis for Allgemeine Literatur (2009)',
            'Margaret A. Edwards Award (2014)'
        
        ],
        "likedPercent": 96.0,
        "price": 3.8
    },
    {
        "id": 170448,
        "title": "Animal Farm",
        "series": "",
        "author": "George Orwell, Russell Baker (Preface), C.M. Woodhouse (Introduction)",
        "description": "Librarian's note: There is an Alternate Cover Edition for this edition of this book here.A farm is taken over by its overworked, mistreated animals. With flaming idealism and stirring slogans, they set out to create a paradise of progress, justice, and equality. Thus the stage is set for one of the most telling satiric fables ever penned \u2013a razor-edged fairy tale for grown-ups that records the evolution from revolution against tyranny to a totalitarianism just as terrible. When Animal Farm was first published, Stalinist Russia was seen as its target. Today it is devastatingly clear that wherever and whenever freedom is attacked, under whatever banner, the cutting clarity and savage comedy of George Orwell\u2019s masterpiece have a meaning and message still ferociously fresh.",
        "language": "English",
        "isbn": "9780451526342",
        "genres": 
            ['Classics',
            'Fiction',
            'Dystopia',
            'Fantasy',
            'Literature',
            'Politics',
            'School',
            'Science Fiction',
            'Novels',
            'Read For School'
        
        ],
        "pages": 141,
        "awards": 
            ['Prometheus Hall of Fame Award (2011)',
            'Retro Hugo Award for Best Novella (1996)'
        
        ],
        "likedPercent": 91.0,
        "price": 4.42
    },
    {
        "id": 11127,
        "title": "The Chronicles of Narnia",
        "series": "The Chronicles of Narnia (Publication Order) #1\u20137",
        "author": "C.S. Lewis, Pauline Baynes (Illustrator)",
        "description": "Journeys to the end of the world, fantastic creatures, and epic battles between good and evil\u2014what more could any reader ask for in one book? The book that has it all is The Lion, the Witch and the Wardrobe, written in 1949 by Clive Staples Lewis. But Lewis did not stop there. Six more books followed, and together they became known as The Chronicles of Narnia.For the past fifty years, The Chronicles of Narnia have transcended the fantasy genre to become part of the canon of classic literature. Each of the seven books is a masterpiece, drawing the reader into a land where magic meets reality, and the result is a fictional world whose scope has fascinated generations.This edition presents all seven books\u2014unabridged\u2014in one impressive volume. The books are presented here in chronlogical order, each chapter graced with an illustration by the original artist, Pauline Baynes. Deceptively simple and direct, The Chronicles of Narnia continue to captivate fans with adventures, characters, and truths that speak to readers of all ages, even fifty years after they were first published.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Classics',
            'Fiction',
            'Young Adult',
            'Childrens',
            'Christian',
            'Adventure',
            'Science Fiction Fantasy',
            'Middle Grade',
            'Christian Fiction'
        
        ],
        "pages": 767,
        "awards": 
           [''
        
        ],
        "likedPercent": 96.0,
        "price": 19.979171069738783
    },
    {
        "id": 304,
        "title": "J.R.R. Tolkien 4-Book Boxed Set: The Hobbit and The Lord of the Rings",
        "series": "The Lord of the Rings #0-3",
        "author": "J.R.R. Tolkien",
        "description": "This four-volume, boxed set contains J.R.R. Tolkien's epic masterworks The Hobbit and the three volumes of The Lord of the Rings (The Fellowship of the Ring, The Two Towers, and The Return of the King).In The Hobbit, Bilbo Baggins is whisked away from his comfortable, unambitious life in Hobbiton by the wizard Gandalf and a company of dwarves. He finds himself caught up in a plot to raid the treasure hoard of Smaug the Magnificent, a large and very dangerous dragon.The Lord of the Rings tells of the great quest undertaken by Frodo Baggins and the Fellowship of the Ring: Gandalf the wizard; the hobbits Merry, Pippin, and Sam; Gimli the dwarf; Legolas the elf; Boromir of Gondor; and a tall, mysterious stranger called Strider. J.R.R. Tolkien's three volume masterpiece is at once a classic myth and a modern fairy tale\u2014a story of high and heroic adventure set in the unforgettable landscape of Middle-earth",
        "language": "English",
        "isbn": "9780345538376",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Classics',
            'Adventure',
            'Science Fiction Fantasy',
            'Epic Fantasy',
            'High Fantasy',
            'Young Adult',
            'Literature',
            'Magic'
        
        ],
        "pages": 1728,
        "awards": 
            [''
        
        ],
        "likedPercent": 98.0,
        "price": 21.15
    },
    {
        "id": 18405,
        "title": "Gone with the Wind",
        "series": "",
        "author": "Margaret Mitchell",
        "description": "Scarlett O'Hara, the beautiful, spoiled daughter of a well-to-do Georgia plantation owner, must use every means at her disposal to claw her way out of the poverty she finds herself in after Sherman's March to the Sea.",
        "language": "English",
        "isbn": "9780446675536",
        "genres": 
            ['Classics',
            'Historical Fiction',
            'Fiction',
            'Romance',
            'Historical',
            'War',
            'Literature',
            'Civil War',
            'Historical Romance',
            'Novels'
        
        ],
        "pages": 1037,
        "awards": 
            ['Pulitzer Prize for Novel (1937)',
            'National Book Award for Novel (1936)'
        
        ],
        "likedPercent": 94.0,
        "price": 5.58
    },
    {
        "id": 11870085,
        "title": "The Fault in Our Stars",
        "series": "",
        "author": "John Green (Goodreads Author)",
        "description": "Despite the tumor-shrinking medical miracle that has bought her a few years, Hazel has never been anything but terminal, her final chapter inscribed upon diagnosis. But when a gorgeous plot twist named Augustus Waters suddenly appears at Cancer Kid Support Group, Hazel's story is about to be completely rewritten.Insightful, bold, irreverent, and raw, The Fault in Our Stars is award-winning author John Green's most ambitious and heartbreaking work yet, brilliantly exploring the funny, thrilling, and tragic business of being alive and in love.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Young Adult',
            'Romance',
            'Fiction',
            'Contemporary',
            'Realistic Fiction',
            'Teen',
            'Coming Of Age',
            'Drama',
            'Novels',
            'Love'
        
        ],
        "pages": 313,
        "awards": 
            ['Georgia Peach Book Award (2013)',
            'Buxtehuder Bulle (2012)',
            'Odyssey Award (2013)',
            'Audie Award for Teens (2013)',
            '\West Australian Young Readers Book Award (WAYRBA) for Older Readers (2013)\',
            '\Pennsylvania Young Readers Choice Award for Young Adults (2013)\',
            'Rhode Island Teen Book Award (2014)',
            'Evergreen Teen Book Award (2015)',
            'Soaring Eagle Book Award (2014)',
            'Milwaukee County Teen Book Award (2013)',
            'Indies Choice Book Award for Young Adult (2013)',
            'Deutscher Jugendliteraturpreis for Preis der Jugendjury (2013)',
            'Amelia Elizabeth Walden Award (2013)',
            'Dioraphte Jongerenliteratuurprijs for vertaald boek en publieksprijs (2013)',
            'The Inky Awards for Silver Inky (2012)',
            'California Young Readers Medal for Young Adult (2015)',
            'Lincoln Award (2014)',
            'Luisterboek Award (2015)',
            'Goodreads Choice Award for Young Adult Fiction (2012) and Nominee for Best of the Best  (2018)',
            'Green Mountain Book Award (2014)',
            'The Inky Awards Shortlist for Silver Inky (2012)',
            '\Louisiana Teen Readers Choice (2015)\',
            'Missouri Gateway Readers Award (2015)',
            'Oklahoma Sequoyah Award for High School (2015)',
            'Alabama Author Award for Young Adult (2013)',
            'Premio El Templo de las Mil Puertas for Mejor novela extranjera independiente (2012)',
            'FAB Award Nominee (2014)',
            'Premi Protagonista Jove for Categoria 15-16 anys (2013)'
        
        ],
        "likedPercent": 93.0,
        "price": 10.387028063221452
    },
    {
        "id": 386162,
        "title": "The Hitchhiker's Guide to the Galaxy",
        "series": "The Hitchhiker's Guide to the Galaxy #1",
        "author": "Douglas Adams",
        "description": "Seconds before the Earth is demolished to make way for a galactic freeway, Arthur Dent is plucked off the planet by his friend Ford Prefect, a researcher for the revised edition of The Hitchhiker's Guide to the Galaxy who, for the last fifteen years, has been posing as an out-of-work actor.Together this dynamic pair begin a journey through space aided by quotes from The Hitchhiker's Guide (\"A towel is about the most massively useful thing an interstellar hitchhiker can have\") and a galaxy-full of fellow travelers: Zaphod Beeblebrox\u2014the two-headed, three-armed ex-hippie and totally out-to-lunch president of the galaxy; Trillian, Zaphod's girlfriend (formally Tricia McMillan), whom Arthur tried to pick up at a cocktail party once upon a time zone; Marvin, a paranoid, brilliant, and chronically depressed robot; Veet Voojagig, a former graduate student who is obsessed with the disappearance of all the ballpoint pens he bought over the years.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Science Fiction',
            'Fiction',
            'Humor',
            'Fantasy',
            'Classics',
            'Comedy',
            'Science Fiction Fantasy',
            'Audiobook',
            'Adventure',
            'Novels'
        
        ],
        "pages": 193,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 16.21038817514787
    },
    {
        "id": 370493,
        "title": "The Giving Tree",
        "series": "",
        "author": "Shel Silverstein",
        "description": "\"Once there was a tree...and she loved a little boy.\"So begins a story of unforgettable perception, beautifully written and illustrated by the gifted and versatile Shel Silverstein.Every day the boy would come to the tree to eat her apples, swing from her branches, or slide down her trunk...and the tree was happy. But as the boy grew older he began to want more from the tree, and the tree gave and gave and gave.This is a tender story, touched with sadness, aglow with consolation. Shel Silverstein has created a moving parable for readers of all ages that offers an affecting interpretation of the gift of giving and a serene acceptance of another's capacity to love in return.",
        "language": "English",
        "isbn": "9780060256654",
        "genres": 
            ['Childrens',
            'Picture Books',
            'Classics',
            'Fiction',
            'Poetry',
            'Young Adult',
            'Fantasy',
            'Juvenile',
            'Kids',
            'Short Stories'
        
        ],
        "pages": 64,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 4.87
    },
    {
        "id": 6185,
        "title": "Wuthering Heights",
        "series": "",
        "author": "Emily Bront\u00eb, Richard J. Dunn (Editor), David Timson (Narrator), Charlotte Bront\u00eb (Commentary), Robert Heindel (Illustrator)",
        "description": "You can find the redesigned cover of this edition HERE.This best-selling Norton Critical Edition is based on the 1847 first edition of the novel. For the Fourth Edition, the editor has collated the 1847 text with several modern editions and has corrected a number of variants, including accidentals. The text is accompanied by entirely new explanatory annotations.New to the fourth Edition are twelve of Emily Bronte's letters regarding the publication of the 1847 edition of Wuthering Heights as well as the evolution of the 1850 edition, prose and poetry selections by the author, four reviews of the novel, and poetry selections by the author, four reviews of the novel, and Edward Chitham's insightful and informative chronology of the creative process behind the beloved work.Five major critical interpretations of Wuthering Heights are included, three of them new to the Fourth Edition. A Stuart Daley considers the importance of chronology in the novel. J. Hillis Miller examines Wuthering Heights's problems of genre and critical reputation. Sandra M. Gilbert assesses the role of Victorian Christianity plays in the novel, while Martha Nussbaum traces the novel's romanticism. Finally, Lin Haire-Sargeant scrutinizes the role of Heathcliff in film adaptations of Wuthering Heights. A Chronology and updated Selected Bibliography are also included.",
        "language": "English",
        "isbn": "9780393978896",
        "genres": 
            ['Classics',
            'Fiction',
            'Romance',
            'Gothic',
            'Literature',
            'Historical Fiction',
            '19th Century',
            'Novels',
            'Classic Literature',
            'Historical'
        
        ],
        "pages": 464,
        "awards": 
            [''
      
        ],
        "likedPercent": 88.0,
        "price": 2.73
    },
    {
        "id": 968,
        "title": "The Da Vinci Code",
        "series": "Robert Langdon #2",
        "author": "Dan Brown (Goodreads Author)",
        "description": "ISBN 9780307277671 moved to this edition.While in Paris, Harvard symbologist Robert Langdon is awakened by a phone call in the dead of the night. The elderly curator of the Louvre has been murdered inside the museum, his body covered in baffling symbols. As Langdon and gifted French cryptologist Sophie Neveu sort through the bizarre riddles, they are stunned to discover a trail of clues hidden in the works of Leonardo da Vinci\u2014clues visible for all to see and yet ingeniously disguised by the painter.Even more startling, the late curator was involved in the Priory of Sion\u2014a secret society whose members included Sir Isaac Newton, Victor Hugo, and Da Vinci\u2014and he guarded a breathtaking historical secret. Unless Langdon and Neveu can decipher the labyrinthine puzzle\u2014while avoiding the faceless adversary who shadows their every move\u2014the explosive, ancient truth will be lost forever.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Mystery',
            'Thriller',
            'Suspense',
            'Mystery Thriller',
            'Historical Fiction',
            'Adventure',
            'Novels',
            'Crime',
            'Adult'
        
        ],
        "pages": 489,
        "awards": 
            ['British Book Award for Book of the Year (2005)',
            'Book Sense Book of the Year Award for Adult Fiction (2004)',
            '\Humos Gouden Bladwijzer (2004)\',
            'Zilveren Vingerafdruk (2004)',
            '\The Flume: New Hampshire Teen Readers Choice Award (2006)\',
            'Teen Buckeye Book Award (2005)',
            'Iowa High School Book Award (2006)',
            'Puddly Award for Fiction (2007)',
            'Missouri Gateway Readers Award for Adult (2006)'
        
        ],
        "likedPercent": 89.0,
        "price": 3.777097288253707
    },
    {
        "id": 929,
        "title": "Memoirs of a Geisha",
        "series": "",
        "author": "Arthur Golden",
        "description": "A literary sensation and runaway bestseller, this brilliant debut novel presents with seamless authenticity and exquisite lyricism the true confessions of one of Japan's most celebrated geisha.In Memoirs of a Geisha, we enter a world where appearances are paramount; where a girl's virginity is auctioned to the highest bidder; where women are trained to beguile the most powerful men; and where love is scorned as illusion. It is a unique and triumphant work of fiction - at once romantic, erotic, suspenseful - and completely unforgettable.",
        "language": "English",
        "isbn": "9781400096893",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Romance',
            'Historical',
            'Classics',
            'Japan',
            'Adult',
            'Novels',
            'Asia',
            'Adult Fiction'
        
        ],
        "pages": 503,
        "awards": 
            [''
        
        ],
        "likedPercent": 95.0,
        "price": 2.76
    },
    {
        "id": 5297,
        "title": "The Picture of Dorian Gray",
        "series": "",
        "author": "Oscar Wilde, Jeffrey Eugenides (Introduction)",
        "description": "Written in his distinctively dazzling manner, Oscar Wilde\u2019s story of a fashionable young man who sells his soul for eternal youth and beauty is the author\u2019s most popular work. The tale of Dorian Gray\u2019s moral disintegration caused a scandal when it \ufb01rst appeared in 1890, but though Wilde was attacked for the novel\u2019s corrupting in\ufb02uence, he responded that there is, in fact, \u201ca terrible moral in Dorian Gray.\u201d Just a few years later, the book and the aesthetic/moral dilemma it presented became issues in the trials occasioned by Wilde\u2019s homosexual liaisons, which resulted in his imprisonment. Of Dorian Gray\u2019s relationship to autobiography, Wilde noted in a letter, \u201cBasil Hallward is what I think I am: Lord Henry what the world thinks me: Dorian what I would like to be\u2014in other ages, perhaps.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Horror',
            'Fantasy',
            'Literature',
            'Gothic',
            'Novels',
            '19th Century',
            'LGBT',
            'Classic Literature'
        
        ],
        "pages": 272,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 12.032483266360758
    },
    {
        "id": 24213,
        "title": "Alice's Adventures in Wonderland & Through the Looking-Glass",
        "series": "Alice's Adventures in Wonderland #1-2",
        "author": "Lewis Carroll, John Tenniel (Illustrator), Martin Gardner (Introduction)",
        "description": "\"I can't explain myself, I'm afraid, sir,\" said Alice, \"Because I'm not myself, you see.\"When Alice sees a white rabbit take a watch out of its waistcoat pocket she decides to follow it, and a sequence of most unusual events is set in motion. This mini book contains the entire topsy-turvy stories of Alice's Adventures in Wonderland and Through the Looking-Glass, accompanied by practical notes and Martina Pelouso's memorable full-colour illustrations.",
        "language": "English",
        "isbn": "9780451527745",
        "genres": 
            ['Classics',
            'Fantasy',
            'Fiction',
            'Childrens',
            'Young Adult',
            'Literature',
            'Adventure',
            'Novels',
            '19th Century',
            'British Literature'
        
        ],
        "pages": 239,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 3.07
    },
    {
        "id": 10210,
        "title": "Jane Eyre",
        "series": "",
        "author": "Charlotte Bront\u00eb, Michael Mason (Editor), Barnett Freedman (Illustrator)",
        "description": "Orphaned as a child, Jane has felt an outcast her whole young life. Her courage is tested once again when she arrives at Thornfield Hall, where she has been hired by the brooding, proud Edward Rochester to care for his ward Ad\u00e8le. Jane finds herself drawn to his troubled yet kind spirit. She falls in love. Hard. But there is a terrifying secret inside the gloomy, forbidding Thornfield Hall. Is Rochester hiding from Jane? Will Jane be left heartbroken and exiled once again?",
        "language": "English",
        "isbn": "9780142437209",
        "genres": 
            ['Classics',
            'Fiction',
            'Romance',
            'Historical Fiction',
            'Literature',
            'Gothic',
            'Historical',
            '19th Century',
            'School',
            'Classic Literature'
        
        ],
        "pages": 532,
        "awards": 
           [''
        
        ],
        "likedPercent": 93.0,
        "price": 5.46
    },
    {
        "id": 24280,
        "title": "Les Mis\u00e9rables",
        "series": "",
        "author": "Victor Hugo, Lee Fahnestock (Translator), Norman MacAfee (Translator)",
        "description": "Introducing one of the most famous characters in literature, Jean Valjean\u2014the noble peasant imprisoned for stealing a loaf of bread\u2014Les Mis\u00e9rables ranks among the greatest novels of all time. In it, Victor Hugo takes readers deep into the Parisian underworld, immerses them in a battle between good and evil, and carries them to the barricades during the uprising of 1832 with a breathtaking realism that is unsurpassed in modern prose. Within his dramatic story are themes that capture the intellect and the emotions: crime and punishment, the relentless persecution of Valjean by Inspector Javert, the desperation of the prostitute Fantine, the amorality of the rogue Th\u00e9nardier, and the universal desire to escape the prisons of our own minds. Les Mis\u00e9rables gave Victor Hugo a canvas upon which he portrayed his criticism of the French political and judicial systems, but the portrait that resulted is larger than life, epic in scope\u2014an extravagant spectacle that dazzles the senses even as it touches the heart.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'Literature',
            'France',
            'Historical',
            'Novels',
            'French Literature',
            'Romance',
            'Classic Literature'
        
        ],
        "pages": 1463,
        "awards": 
            [''
        
        ],
        "likedPercent": 93.0,
        "price": 5.630427891218754
    },
    {
        "id": 13079982451,
        "title": "Fahrenheit 451",
        "series": "",
        "author": "Ray Bradbury",
        "description": "Guy Montag is a fireman. In his world, where television rules and literature is on the brink of extinction, firemen start fires rather than put them out. His job is to destroy the most illegal of commodities, the printed book, along with the houses in which they are hidden.Montag never questions the destruction and ruin his actions produce, returning each day to his bland life and wife, Mildred, who spends all day with her television 'family'. But then he meets an eccentric young neighbor, Clarisse, who introduces him to a past where people did not live in fear and to a present where one sees the world through the ideas in books instead of the mindless chatter of television.When Mildred attempts suicide and Clarisse suddenly disappears, Montag begins to question everything he has ever known.",
        "language": "English",
        "isbn": "B0064CPN7I",
        "genres": 
            ['Classics',
            'Fiction',
            'Science Fiction',
            'Dystopia',
            'School',
            'Literature',
            'Novels',
            'Fantasy',
            'Adult',
            'Science Fiction Fantasy'
        
        ],
        "pages": 194,
        "awards": 
            ['Prometheus Hall of Fame Award (1984)',
            'Geffen Award for Best Translated SF Book (2002)',
            'California Book Award for Fiction (Silver) (1953)',
            'Retro Hugo Award for Best Novel (2004)'
        
        ],
        "likedPercent": 92.0,
        "price": 13.055604259387607
    },
    {
        "id": 13335037,
        "title": "Divergent",
        "series": "Divergent #1",
        "author": "Veronica Roth (Goodreads Author)",
        "description": "In Beatrice Prior's dystopian Chicago world, society is divided into five factions, each dedicated to the cultivation of a particular virtue\u2014Candor (the honest), Abnegation (the selfless), Dauntless (the brave), Amity (the peaceful), and Erudite (the intelligent). On an appointed day of every year, all sixteen-year-olds must select the faction to which they will devote the rest of their lives. For Beatrice, the decision is between staying with her family and being who she really is\u2014she can't have both. So she makes a choice that surprises everyone, including herself.During the highly competitive initiation that follows, Beatrice renames herself Tris and struggles alongside her fellow initiates to live out the choice they have made. Together they must undergo extreme physical tests of endurance and intense psychological simulations, some with devastating consequences. As initiation transforms them all, Tris must determine who her friends really are\u2014and where, exactly, a romance with a sometimes fascinating, sometimes exasperating boy fits into the life she's chosen. But Tris also has a secret, one she's kept hidden from everyone because she's been warned it can mean death. And as she discovers unrest and growing conflict that threaten to unravel her seemingly perfect society, she also learns that her secret might help her save those she loves . . . or it might destroy her.",
        "language": "English",
        "isbn": "9780062024039",
        "genres": 
            ['Young Adult',
            'Dystopia',
            'Fiction',
            'Fantasy',
            'Science Fiction',
            'Romance',
            'Adventure',
            'Teen',
            'Post Apocalyptic',
            'Action'
        
        ],
        "pages": 487,
        "awards": 
            ['Georgia Peach Book Award (2012)',
            'South Carolina Book Award for Young Adult (2014)',
            'Rhode Island Teen Book Award (2013)',
            'Evergreen Teen Book Award (2014)',
            'Soaring Eagle Book Award (2012)',
            'Milwaukee County Teen Book Award Nominee (2012)',
            '\Childrens Choice Book Award Nominee for Teen Choice Book of the Year (2012)\',
            'Sakura Medal',
            'New Mexico Land of Enchantment Award for Young Adult (2014)',
            'Eliot Rosewater Indiana High School Book Award (2014)',
            'California Young Readers Medal for Young Adult (2014)',
            'Lincoln Award Nominee (2014)',
            'DABWAHA Romance Tournament for Best Young Adult Romance (2012)',
            'Goodreads Choice Award for Favorite Book and for Young Adult Fantasy & Science Fiction and Nominee for Goodreads Author (2011)',
            'Green Mountain Book Award (2013)',
            'The Magnolia Award for 6-8 (2014)',
            '\Louisiana Teen Readers Choice (2014)\',
            'Missouri Gateway Readers Award (2014)',
            'Oklahoma Sequoyah Award for High Schol (2014)',
            'Premio El Templo de las Mil Puertas Nominee for Mejor novela extranjera perteneciente a saga (2011)'
        
        ],
        "likedPercent": 94.0,
        "price": 0.88
    },
    {
        "id": 7624,
        "title": "Lord of the Flies",
        "series": "",
        "author": "William Golding",
        "description": "At the dawn of the next world war, a plane crashes on an uncharted island, stranding a group of schoolboys. At first, with no adult supervision, their freedom is something to celebrate; this far from civilization the boys can do anything they want. Anything. They attempt to forge their own society, failing, however, in the face of terror, sin and evil. And as order collapses, as strange howls echo in the night, as terror begins its reign, the hope of adventure seems as far from reality as the hope of being rescued. Labeled a parable, an allegory, a myth, a morality tale, a parody, a political treatise, even a vision of the apocalypse, Lord of the Flies is perhaps our most memorable novel about \u201cthe end of innocence, the darkness of man\u2019s heart.\u201d",
        "language": "English",
        "isbn": "9780140283334",
        "genres": 
            ['Classics',
            'Fiction',
            'Young Adult',
            'School',
            'Literature',
            'Dystopia',
            'Read For School',
            'Novels',
            'High School',
            'Adventure'
        
        ],
        "pages": 182,
        "awards": 
            [''
        
        ],
        "likedPercent": 86.0,
        "price": 1.89
    },
    {
        "id": 18135,
        "title": "Romeo and Juliet",
        "series": "",
        "author": "William Shakespeare, Paul Werstine (Editor), Barbara A. Mowat (Editor), Paavo Emil Cajander (Translator)",
        "description": "In Romeo and Juliet, Shakespeare creates a violent world, in which two young people fall in love. It is not simply that their families disapprove; the Montagues and the Capulets are engaged in a blood feud.In this death-filled setting, the movement from love at first sight to the lovers\u2019 final union in death seems almost inevitable. And yet, this play set in an extraordinary world has become the quintessential story of young love. In part because of its exquisite language, it is easy to respond as if it were about all young lovers.",
        "language": "English",
        "isbn": "9780743477116",
        "genres": 
            ['Classics',
            'Plays',
            'Fiction',
            'Romance',
            'School',
            'Drama',
            'Read For School',
            'Literature',
            'High School',
            'Poetry'
        
        ],
        "pages": 301,
        "awards": 
            [''
        
        ],
        "likedPercent": 87.0,
        "price": 6.79
    },
    {
        "id": 18144590,
        "title": "The Alchemist",
        "series": "",
        "author": "Paulo Coelho (Goodreads Author), Alan R. Clarke (Translator), James Noel Smith (Illustrator)",
        "description": "Paulo Coelho's enchanting novel has inspired a devoted following around the world. This story, dazzling in its powerful simplicity and soul-stirring wisdom, is about an Andalusian shepherd boy named Santiago who travels from his homeland in Spain to the Egyptian desert in search of a treasure buried near the Pyramids. Along the way he meets a Gypsy woman, a man who calls himself king, and an alchemist, all of whom point Santiago in the direction of his quest. No one knows what the treasure is, or if Santiago will be able to surmount the obstacles in his path. But what starts out as a journey to find worldly goods turns into a discovery of the treasure found within. Lush, evocative, and deeply humane, the story of Santiago is an eternal testament to the transforming power of our dreams and the importance of listening to our hearts.Illustration: Jim Tierney",
        "language": "English",
        "isbn": "9780062315007",
        "genres": 
            ['Fiction',
            'Classics',
            'Fantasy',
            'Philosophy',
            'Novels',
            'Spirituality',
            'Literature',
            'Self Help',
            'Inspirational',
            'Adventure'
        
        ],
        "pages": 182,
        "awards": 
            ['NBDB National Book Award Nominee for Translation (2015)',
            'Grand Prix des lectrices de Elle for roman (1995)',
            'Premio Grinzane Cavour for Narrativa Straniera (1996)',
            'Corine Internationaler Buchpreis for Belletristik (2002)'
        
        ],
        "likedPercent": 87.0,
        "price": 13.22
    },
    {
        "id": 7144,
        "title": "Crime and Punishment",
        "series": "",
        "author": "Fyodor Dostoyevsky, David McDuff (Translator)",
        "description": "Raskolnikov, a destitute and desperate former student, wanders through the slums of St Petersburg and commits a random murder without remorse or regret. He imagines himself to be a great man, a Napoleon: acting for a higher purpose beyond conventional moral law. But as he embarks on a dangerous game of cat and mouse with a suspicious police investigator, Raskolnikov is pursued by the growing voice of his conscience and finds the noose of his own guilt tightening around his neck. Only Sonya, a downtrodden prostitute, can offer the chance of redemption.",
        "language": "English",
        "isbn": "9780143058144",
        "genres": 
            ['Classics',
            'Fiction',
            'Russia',
            'Literature',
            'Russian Literature',
            'Novels',
            'Philosophy',
            'Crime',
            '19th Century',
            'School'
        
        ],
        "pages": 671,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 18.85
    },
    {
        "id": 22628,
        "title": "The Perks of Being a Wallflower",
        "series": "",
        "author": "Stephen Chbosky",
        "description": "standing on the fringes of life...offers a unique perspective. But there comes a time to seewhat it looks like from the dance floor.This haunting novel about the dilemma of passivity vs. passion marks the stunning debut of a provocative new voice in contemporary fiction: The Perks of Being A WALLFLOWERThis is the story of what it's like to grow up in high school. More intimate than a diary, Charlie's letters are singular and unique, hilarious and devastating. We may not know where he lives. We may not know to whom he is writing. All we know is the world he shares. Caught between trying to live his life and trying to run from it puts him on a strange course through uncharted territory. The world of first dates and mixed tapes, family dramas and new friends. The world of sex, drugs, and The Rocky Horror Picture Show, when all one requires is that the perfect song on that perfect drive to feel infinite.Through Charlie, Stephen Chbosky has created a deeply affecting coming-of-age story, a powerful novel that will spirit you back to those wild and poignant roller coaster days known as growing up.(back cover)",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Young Adult',
            'Fiction',
            'Contemporary',
            'Coming Of Age',
            'Romance',
            'Realistic Fiction',
            'LGBT',
            'Classics',
            'Mental Health',
            'Teen'
        
        ],
        "pages": 213,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 1.1254775271249502
    },
    {
        "id": 4671,
        "title": "The Great Gatsby",
        "series": "",
        "author": "F. Scott Fitzgerald, Francis Scott Fitzgerald",
        "description": "Alternate Cover Edition ISBN: 0743273567 (ISBN13: 9780743273565)The Great Gatsby, F. Scott Fitzgerald's third book, stands as the supreme achievement of his career. This exemplary novel of the Jazz Age has been acclaimed by generations of readers. The story is of the fabulously wealthy Jay Gatsby and his new love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted \"gin was the national drink and sex the national obsession,\" it is an exquisitely crafted tale of America in the 1920s.The Great Gatsby is one of the great classics of twentieth-century literature.(back cover)",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'School',
            'Literature',
            'Historical Fiction',
            'Romance',
            'Novels',
            'Read For School',
            'High School',
            'American'
        
        ],
        "pages": 200,
        "awards": 
            ['Grammy Award Nominee for Best Spoken Word Album (2003)'
        
        ],
        "likedPercent": 90.0,
        "price": 13.237929348548695
    },
    {
        "id": 256683,
        "title": "City of Bones",
        "series": "The Mortal Instruments #1",
        "author": "Cassandra Clare (Goodreads Author)",
        "description": "When fifteen-year-old Clary Fray heads out to the Pandemonium Club in New York City, she hardly expects to witness a murder\u2015 much less a murder committed by three teenagers covered with strange tattoos and brandishing bizarre weapons. Then the body disappears into thin air. It's hard to call the police when the murderers are invisible to everyone else and when there is nothing\u2015not even a smear of blood\u2015to show that a boy has died. Or was he a boy?This is Clary's first meeting with the Shadowhunters, warriors dedicated to ridding the earth of demons. It's also her first encounter with Jace, a Shadowhunter who looks a little like an angel and acts a lot like a jerk. Within twenty-four hours Clary is pulled into Jace's world with a vengeance when her mother disappears and Clary herself is attacked by a demon. But why would demons be interested in ordinary mundanes like Clary and her mother? And how did Clary suddenly get the Sight? The Shadowhunters would like to know...",
        "language": "English",
        "isbn": "9781416914280",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Paranormal',
            'Romance',
            'Urban Fantasy',
            'Fiction',
            'Vampires',
            'Supernatural',
            'Angels',
            'Magic'
        
        ],
        "pages": 485,
        "awards": 
            ['Locus Award Nominee for Best First Novel (2008)',
            'Georgia Peach Book Award Nominee for Honor book (2009)',
            'South Carolina Book Award Nominee for Young Adult Book Award (2010)',
            '\Pacific Northwest Library Association Young Readers Choice Award (2010)\',
            'Lincoln Award (2010)'
        
        ],
        "likedPercent": 92.0,
        "price": 6.29
    },
    {
        "id": 375802,
        "title": "Ender's Game",
        "series": "Ender's Saga #1",
        "author": "Orson Scott Card, Stefan Rudnicki (Narrator), Harlan Ellison (Narrator)",
        "description": "Andrew \"Ender\" Wiggin thinks he is playing computer simulated war games; he is, in fact, engaged in something far more desperate. The result of genetic experimentation, Ender may be the military genius Earth desperately needs in a war against an alien enemy seeking to destroy all human life. The only way to find out is to throw Ender into ever harsher training, to chip away and find the diamond inside, or destroy him utterly. Ender Wiggin is six years old when it begins. He will grow up fast.But Ender is not the only result of the experiment. The war with the Buggers has been raging for a hundred years, and the quest for the perfect general has been underway almost as long. Ender's two older siblings, Peter and Valentine, are every bit as unusual as he is, but in very different ways. While Peter was too uncontrollably violent, Valentine very nearly lacks the capability for violence altogether. Neither was found suitable for the military's purpose. But they are driven by their jealousy of Ender, and by their inbred drive for power. Peter seeks to control the political process, to become a ruler. Valentine's abilities turn more toward the subtle control of the beliefs of commoner and elite alike, through powerfully convincing essays. Hiding their youth and identities behind the anonymity of the computer networks, these two begin working together to shape the destiny of Earth-an Earth that has no future at all if their brother Ender fails.Source: hatrack.com",
        "language": "English",
        "isbn": "9780812550702",
        "genres": 
            ['Science Fiction',
            'Fiction',
            'Young Adult',
            'Fantasy',
            'Classics',
            'Science Fiction Fantasy',
            'Dystopia',
            'War',
            'Audiobook',
            'Adventure'
        
        ],
        "pages": 324,
        "awards": 
            ['Hugo Award for Best Novel (1986)',
            'Nebula Award for Best Novel (1985)',
            'N\u00e9bula (1985)',
            'Margaret A. Edwards Award (2008)'
        
        ],
        "likedPercent": 95.0,
        "price": 4.6
    },
    {
        "id": 4667024,
        "title": "The Help",
        "series": "",
        "author": "Kathryn Stockett (Goodreads Author)",
        "description": "Librarian's note: An alternate cover edition can be found hereThree ordinary women are about to take one extraordinary step.Twenty-two-year-old Skeeter has just returned home after graduating from Ole Miss. She may have a degree, but it is 1962, Mississippi, and her mother will not be happy till Skeeter has a ring on her finger. Skeeter would normally find solace with her beloved maid Constantine, the woman who raised her, but Constantine has disappeared and no one will tell Skeeter where she has gone.Aibileen is a black maid, a wise, regal woman raising her seventeenth white child. Something has shifted inside her after the loss of her own son, who died while his bosses looked the other way. She is devoted to the little girl she looks after, though she knows both their hearts may be broken.Minny, Aibileen's best friend, is short, fat, and perhaps the sassiest woman in Mississippi. She can cook like nobody's business, but she can't mind her tongue, so she's lost yet another job. Minny finally finds a position working for someone too new to town to know her reputation. But her new boss has secrets of her own.Seemingly as different from one another as can be, these women will nonetheless come together for a clandestine project that will put them all at risk. And why? Because they are suffocating within the lines that define their town and their times. And sometimes lines are made to be crossed.In pitch-perfect voices, Kathryn Stockett creates three extraordinary women whose determination to start a movement of their own forever changes a town, and the way women, mothers, daughters, caregivers, friends, view one another. A deeply moving novel filled with poignancy, humor, and hope, The Help is a timeless and universal story about the lines we abide by, and the ones we don't. (jacket flap)",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Historical',
            'Adult',
            'Adult Fiction',
            'Contemporary',
            'Audiobook',
            'Classics',
            'Chick Lit',
            'Book Club'
        
        ],
        "pages": 451,
        "awards": 
            ['Orange Prize Nominee for Fiction Longlist (2010)',
            'Audie Award for Fiction (2010)',
            'Exclusive Books Boeke Prize (2009)',
            'SIBA Book Award for Fiction (2010)',
            'Indies Choice Book Award for Adult Debut (2010)',
            'Puddly Award for Fiction (2011)',
            'Lincoln Award Nominee (2013)',
            'Grand Prix des lectrices de Elle for roman (2011)',
            'Goodreads Choice Award for Fiction (2009) and Nominee for Best of the Best  (2018)',
            'Townsend Prize for Fiction (2010)'
        
        ],
        "likedPercent": 98.0,
        "price": 9.751134286849856
    },
    {
        "id": 8127,
        "title": "Anne of Green Gables",
        "series": "Anne of Green Gables #1",
        "author": "L.M. Montgomery",
        "description": "As soon as Anne Shirley arrives at the snug white farmhouse called Green Gables, she is sure she wants to stay forever . . . but will the Cuthberts send her back to to the orphanage? Anne knows she's not what they expected\u2014a skinny girl with fiery red hair and a temper to match. If only she can convince them to let her stay, she'll try very hard not to keep rushing headlong into scrapes and blurting out the first thing that comes to her mind. Anne is not like anyone else, the Cuthberts agree; she is special\u2014a girl with an enormous imagination. This orphan girl dreams of the day when she can call herself Anne of Green Gables.",
        "language": "English",
        "isbn": "9780451528827",
        "genres": 
            ['Classics',
            'Fiction',
            'Young Adult',
            'Childrens',
            'Historical Fiction',
            'Middle Grade',
            'Historical',
            'Audiobook',
            'Canada',
            'Coming Of Age'
        
        ],
        "pages": 320,
        "awards": 
            [''
        
        ],
        "likedPercent": 95.0,
        "price": 6.07
    },
    {
        "id": 3,
        "title": "Harry Potter and the Sorcerer's Stone",
        "series": "Harry Potter #1",
        "author": "J.K. Rowling, Mary GrandPr\u00e9 (Illustrator)",
        "description": "Harry Potter's life is miserable. His parents are dead and he's stuck with his heartless relatives, who force him to live in a tiny closet under the stairs. But his fortune changes when he receives a letter that tells him the truth about himself: he's a wizard. A mysterious visitor rescues him from his relatives and takes him to his new home, Hogwarts School of Witchcraft and Wizardry.After a lifetime of bottling up his magical powers, Harry finally feels like a normal kid. But even within the Wizarding community, he is special. He is the boy who lived: the only person to have ever survived a killing curse inflicted by the evil Lord Voldemort, who launched a brutal takeover of the Wizarding world, only to vanish after failing to kill Harry.Though Harry's first year at Hogwarts is the best of his life, not everything is perfect. There is a dangerous secret object hidden within the castle walls, and Harry believes it's his responsibility to prevent it from falling into evil hands. But doing so will bring him into contact with forces more terrifying than he ever could have imagined.Full of sympathetic characters, wildly imaginative situations, and countless exciting details, the first installment in the series assembles an unforgettable magical world and sets the stage for many high-stakes adventures to come.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Young Adult',
            'Magic',
            'Childrens',
            'Middle Grade',
            'Adventure',
            'Classics',
            'Audiobook',
            'Science Fiction Fantasy'
        
        ],
        "pages": 309,
        "awards": 
            ['\Mythopoeic Fantasy Award for Childrens Literature (2008)\',
            '\British Book Award for Childrens Book of the Year (1998)\',
            'Prijs van de Nederlandse Kinderjury for 6-9 jaar en 10-12 jaar (2002)',
            'American Booksellers Book Of The Year  Award for Children (1999)',
            'Audie Award (2000)',
            '\West Australian Young Readers Book Award (WAYRBA) for Younger Readers (2000)\',
            'South Carolina Book Award for Junior Book Award (2001)',
            'Grand Canyon Reader Award for Teen Book (2000)',
            'Charlotte Award (2000)',
            'Nene Award (2000)',
            '\Massachusetts Childrens Book Award (2000)\',
            'Colorado Blue Spruce Young Adult Book Award (2001)',
            'Blue Hen Book Award for Chapter Book (2001)',
            '\Nevada Young Readers Award for Young Reader Category (2000)\',
            'Golden Archer Award for Middle/Junior High (2000)',
            'Indian Paintbrush Book Award (2000)',
            'Hotze de Roosprijs (2002)',
            'Nestl\u00e9 Smarties Book Prize for 9\u201311 years (1997)',
            'Eliot Rosewater Indiana High School Book Award (2001)',
            'Kinderboekwinkelprijs (1999)',
            'Parenting Book of the Year Award (1998)',
            'North East Teenage Book Award (1999)',
            '\Specsavers National Book Award for Childrens Book of the Year (1998)\',
            'Washington State Sasquatch Award (2000)',
            'Literaturpreis der Jury der jungen Leser for Kinderbuch (1999)',
            'Carnegie Medal Nominee (1997)',
            '\Rebecca Caudill Young Readers Book Award (2001)\',
            'Premi Protagonista Jove for Categoria 12-13 anys (2000)'
        
        ],
        "likedPercent": 96.0,
        "price": 17.89732528529731
    },
    {
        "id": 157993,
        "title": "The Little Prince",
        "series": "",
        "author": "Antoine de Saint-Exup\u00e9ry, Richard Howard (Translator), Ivan Minatti (Translator), Nguy\u1ec5n Th\u00e0nh V\u0169 (Illustrator)",
        "description": "A PBS Great American Read Top 100 PickFew stories are as widely read and as universally cherished by children and adults alike as The Little Prince. Richard Howard's translation of the beloved classic beautifully reflects Saint-Exup\u00e9ry's unique and gifted style. Howard, an acclaimed poet and one of the preeminent translators of our time, has excelled in bringing the English text as close as possible to the French, in language, style, and most important, spirit. The artwork in this edition has been restored to match in detail and in color Saint-Exup\u00e9ry's original artwork. Combining Richard Howard's translation with restored original art, this definitive English-language edition of The Little Prince will capture the hearts of readers of all ages.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Fantasy',
            'Childrens',
            'France',
            'Young Adult',
            'Philosophy',
            'Literature',
            'French Literature',
            'Middle Grade'
        
        ],
        "pages": 93,
        "awards": 
            ['Retro Hugo Award for Best Novella (2019)'
        
        ],
        "likedPercent": 95.0,
        "price": 10.123109679200526
    },
    {
        "id": 24178,
        "title": "Charlotte's Web",
        "series": "",
        "author": "E.B. White, Garth Williams (Illustrator), Rosemary Wells (Illustrations)",
        "description": "This beloved book by E. B. White, author of Stuart Little and The Trumpet of the Swan, is a classic of children's literature that is \"just about perfect.\" This high-quality paperback features vibrant illustrations colorized by Rosemary Wells!Some Pig. Humble. Radiant. These are the words in Charlotte's Web, high up in Zuckerman's barn. Charlotte's spiderweb tells of her feelings for a little pig named Wilbur, who simply wants a friend. They also express the love of a girl named Fern, who saved Wilbur's life when he was born the runt of his litter.E. B. White's Newbery Honor Book is a tender novel of friendship, love, life, and death that will continue to be enjoyed by generations to come. This edition contains newly color illustrations by Garth Williams, the acclaimed illustrator of E. B. White's Stuart Little and Laura Ingalls Wilder's Little House series, among many other books.",
        "language": "English",
        "isbn": "9780064410939",
        "genres": 
            ['Classics',
            'Childrens',
            'Fiction',
            'Young Adult',
            'Fantasy',
            'Animals',
            'Middle Grade',
            'Juvenile',
            'School',
            'Chapter Books'
        
        ],
        "pages": 184,
        "awards": 
            ['Newbery Medal Nominee (1953)',
            '\George C. Stone Center for Childrens Books Recognition of Merit Award (1970)\',
            'Audie Award Nominee for Audiobook of the Year and Middle Grade (2020)',
            '\Massachusetts Childrens Book Award (1984)\',
            'Laura Ingalls Wilder Award (1970)'
        
        ],
        "likedPercent": 94.0,
        "price": 6.15
    },
    {
        "id": 890,
        "title": "Of Mice and Men",
        "series": "",
        "author": "John Steinbeck",
        "description": "The compelling story of two outsiders striving to find their place in an unforgiving world. Drifters in search of work, George and his simple-minded friend Lennie have nothing in the world except each other and a dream -- a dream that one day they will have some land of their own. Eventually they find work on a ranch in California\u2019s Salinas Valley, but their hopes are doomed as Lennie, struggling against extreme cruelty, misunderstanding and feelings of jealousy, becomes a victim of his own strength. Tackling universal themes such as the friendship of a shared vision, and giving voice to America\u2019s lonely and dispossessed, Of Mice and Men has proved one of Steinbeck\u2019s most popular works, achieving success as a novel, a Broadway play and three acclaimed films.",
        "language": "English",
        "isbn": "9780142000670",
        "genres": 
            ['Classics',
            'Fiction',
            'School',
            'Historical Fiction',
            'Literature',
            'Read For School',
            'Novels',
            'High School',
            'American',
            'Classic Literature'
        
        ],
        "pages": 103,
        "awards": 
            ['\New York Drama Critics Circle Award for Best American Play (1938)\'
        
        ],
        "likedPercent": 90.0,
        "price": 5.75
    },
    {
        "id": 18619684,
        "title": "The Time Traveler's Wife",
        "series": "",
        "author": "Audrey Niffenegger (Goodreads Author)",
        "description": "A funny, often poignant tale of boy meets girl with a twist: what if one of them couldn't stop slipping in and out of time? Highly original and imaginative, this debut novel raises questions about life, love, and the effects of time on relationships.Audrey Niffenegger\u2019s innovative debut, The Time Traveler\u2019s Wife, is the story of Clare, a beautiful art student, and Henry, an adventuresome librarian, who have known each other since Clare was six and Henry was thirty-six, and were married when Clare was twenty-three and Henry thirty-one. Impossible but true, because Henry is one of the first people diagnosed with Chrono-Displacement Disorder: periodically his genetic clock resets and he finds himself misplaced in time, pulled to moments of emotional gravity in his life, past and future. His disappearances are spontaneous, his experiences unpredictable, alternately harrowing and amusing. The Time Traveler\u2019s Wife depicts the effects of time travel on Henry and Clare\u2019s marriage and their passionate love for each other as the story unfolds from both points of view. Clare and Henry attempt to live normal lives, pursuing familiar goals\u2014steady jobs, good friends, children of their own. All of this is threatened by something they can neither prevent nor control, making their story intensely moving and entirely unforgettable.",
        "language": "English",
        "isbn": "9781939126016",
        "genres": 
            ['Fiction',
            'Romance',
            'Fantasy',
            'Time Travel',
            'Science Fiction',
            'Contemporary',
            'Adult',
            'Chick Lit',
            'Adult Fiction',
            'Magical Realism'
        
        ],
        "pages": 500,
        "awards": 
            ['Arthur C. Clarke Award Nominee (2005)',
            'Orange Prize Nominee for Fiction Longlist (2004)',
            'British Book Award (2006)',
            'John W. Campbell Memorial Award Nominee for Best Science Fiction Novel (2005)',
            'Exclusive Books Boeke Prize (2005)',
            'ALA Alex Award (2004)'
        
        ],
        "likedPercent": 91.0,
        "price": 4.881548487077044
    },
    {
        "id": 17245,
        "title": "Dracula",
        "series": "Dracula #1",
        "author": "Bram Stoker, Nina Auerbach (Editor), David J. Skal (Editor)",
        "description": "You can find an alternative cover edition for this ISBN here and here.A rich selection of background and source materials is provided in three areas: Contexts includes probable inspirations for Dracula in the earlier works of James Malcolm Rymer and Emily Gerard. Also included are a discussion of Stoker's working notes for the novel and \"Dracula's Guest,\" the original opening chapter to Dracula. Reviews and Reactions reprints five early reviews of the novel. \"Dramatic and Film Variations\" focuses on theater and film adaptations of Dracula, two indications of the novel's unwavering appeal. David J. Skal, Gregory A. Waller, and Nina Auerbach offer their varied perspectives. Checklists of both dramatic and film adaptations are included.Criticism collects seven theoretical interpretations of Dracula by Phyllis A. Roth, Carol A. Senf, Franco Moretti, Christopher Craft, Bram Dijkstra, Stephen D. Arata, and Talia Schaffer.A Chronology and a Selected Bibliography are included.",
        "language": "English",
        "isbn": "9780393970128",
        "genres": 
            ['Classics',
            'Horror',
            'Fiction',
            'Fantasy',
            'Vampires',
            'Gothic',
            'Paranormal',
            'Literature',
            'Audiobook',
            'Supernatural'
        
        ],
        "pages": 488,
        "awards": 
            [''
        
        ],
        "likedPercent": 93.0,
        "price": 4.55
    },
    {
        "id": 5129,
        "title": "Brave New World",
        "series": "",
        "author": "Aldous Huxley",
        "description": "Brave New World is a dystopian novel by English author Aldous Huxley, written in 1931 and published in 1932. Largely set in a futuristic World State, inhabited by genetically modified citizens and an intelligence-based social hierarchy, the novel anticipates huge scientific advancements in reproductive technology, sleep-learning, psychological manipulation and classical conditioning that are combined to make a dystopian society which is challenged by only a single individual: the story's protagonist.",
        "language": "English",
        "isbn": "9780060929879",
        "genres": 
            ['Classics',
            'Fiction',
            'Science Fiction',
            'Dystopia',
            'Literature',
            'Novels',
            'School',
            'Fantasy',
            'Philosophy',
            'Science Fiction Fantasy'
        
        ],
        "pages": 288,
        "awards": 
            [''
        
        ],
        "likedPercent": 92.0,
        "price": 3.78
    },
    {
        "id": 320,
        "title": "One Hundred Years of Solitude",
        "series": "",
        "author": "Gabriel Garc\u00eda M\u00e1rquez, Gregory Rabassa (Translator)",
        "description": "The brilliant, bestselling, landmark novel that tells the story of the Buendia family, and chronicles the irreconcilable conflict between the desire for solitude and the need for love\u2014in rich, imaginative prose that has come to define an entire genre known as \"magical realism.\"",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Classics',
            'Magical Realism',
            'Literature',
            'Novels',
            'Fantasy',
            'Historical Fiction',
            'Spanish Literature',
            'Literary Fiction',
            'Latin American'
        
        ],
        "pages": 417,
        "awards": 
            ['Premio Internacional de Novela R\u00f3mulo Gallegos (1972)',
            'Prix du Meilleur Livre \u00c9tranger for Roman (1969)'
        
        ],
        "likedPercent": 90.0,
        "price": 9.500977153898924
    },
    {
        "id": 5107,
        "title": "The Catcher in the Rye",
        "series": "",
        "author": "J.D. Salinger",
        "description": "The hero-narrator of The Catcher in the Rye is an ancient child of sixteen, a native New Yorker named Holden Caulfield. Through circumstances that tend to preclude adult, secondhand description, he leaves his prep school in Pennsylvania and goes underground in New York City for three days. The boy himself is at once too simple and too complex for us to make any final comment about him or his story. Perhaps the safest thing we can say about Holden is that he was born in the world not just strongly attracted to beauty but, almost, hopelessly impaled on it. There are many voices in this novel: children's voices, adult voices, underground voices-but Holden's voice is the most eloquent of all. Transcending his own vernacular, yet remaining marvelously faithful to it, he issues a perfectly articulated cry of mixed pain and pleasure. However, like most lovers and clowns and poets of the higher orders, he keeps most of the pain to, and for, himself. The pleasure he gives away, or sets aside, with all his heart. It is there for the reader who can handle it to keep. J.D. Salinger's classic novel of teenage angst and rebellion was first published in 1951. The novel was included on Time's 2005 list of the 100 best English-language novels written since 1923. It was named by Modern Library and its readers as one of the 100 best English-language novels of the 20th century. It has been frequently challenged in the court for its liberal use of profanity and portrayal of sexuality and in the 1950's and 60's it was the novel that every teenage boy wants to read.",
        "language": "English",
        "isbn": "9780316769174",
        "genres": 
            ['Classics',
            'Fiction',
            'Young Adult',
            'Literature',
            'School',
            'Novels',
            'Coming Of Age',
            'American',
            'High School',
            'Read For School'
        
        ],
        "pages": 277,
        "awards": 
            ['Teen Read Award Nominee for Best All-Time-Fave (2010)',
            'National Book Award Finalist for Fiction (1952)'
        
        ],
        "likedPercent": 86.0,
        "price": 2.6
    },
    {
        "id": 21787,
        "title": "The Princess Bride",
        "series": "",
        "author": "William Goldman",
        "description": "What happens when the most beautiful girl in the world marries the handsomest prince of all time and he turns out to be...well...a lot less than the man of her dreams?As a boy, William Goldman claims, he loved to hear his father read the S. Morgenstern classic, The Princess Bride. But as a grown-up he discovered that the boring parts were left out of good old Dad's recitation, and only the \"good parts\" reached his ears.Now Goldman does Dad one better. He's reconstructed the \"Good Parts Version\" to delight wise kids and wide-eyed grownups everywhere.What's it about? Fencing. Fighting. True Love. Strong Hate. Harsh Revenge. A Few Giants. Lots of Bad Men. Lots of Good Men. Five or Six Beautiful Women. Beasties Monstrous and Gentle. Some Swell Escapes and Captures. Death, Lies, Truth, Miracles, and a Little Sex.In short, it's about everything.",
        "language": "English",
        "isbn": "9780345418265",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Classics',
            'Romance',
            'Humor',
            'Young Adult',
            'Adventure',
            'Science Fiction Fantasy',
            'Comedy',
            'Fairy Tales'
        
        ],
        "pages": 456,
        "awards": 
            [''
        
        ],
        "likedPercent": 95.0,
        "price": 6.23
    },
    {
        "id": 28187,
        "title": "The Lightning Thief",
        "series": "Percy Jackson and the Olympians #1",
        "author": "Rick Riordan (Goodreads Author)",
        "description": "Alternate cover for this ISBN can be found herePercy Jackson is a good kid, but he can't seem to focus on his schoolwork or control his temper. And lately, being away at boarding school is only getting worse - Percy could have sworn his pre-algebra teacher turned into a monster and tried to kill him. When Percy's mom finds out, she knows it's time that he knew the truth about where he came from, and that he go to the one place he'll be safe. She sends Percy to Camp Half Blood, a summer camp for demigods (on Long Island), where he learns that the father he never knew is Poseidon, God of the Sea. Soon a mystery unfolds and together with his friends\u2014one a satyr and the other the demigod daughter of Athena - Percy sets out on a quest across the United States to reach the gates of the Underworld (located in a recording studio in Hollywood) and prevent a catastrophic war between the gods.",
        "language": "English",
        "isbn": "9780786838653",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Mythology',
            'Fiction',
            'Middle Grade',
            'Adventure',
            'Childrens',
            'Urban Fantasy',
            'Greek Mythology',
            'Magic'
        
        ],
        "pages": 375,
        "awards": 
            ['\Young Readers Choice Award (2008)\',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2011)',
            'South Carolina Book Award for Junior Book Award (2008)',
            'Grand Canyon Reader Award for Tween Book (2008)',
            'Nene Award (2008)',
            '\Massachusetts Childrens Book Award (2008)\',
            '\Pennsylvania Young Readers Choice Award for Grades 6-8 (2008)\',
            'Rhode Island Teen Book Award Nominee (2007)',
            'Sunshine State Young Readers Award for Grades 6-8 (2007)',
            '\Pacific Northwest Library Association Young Readers Choice Award for Intermediate (2008)\',
            'Iowa Teen Award (2009)',
            'Lincoln Award Nominee (2009)',
            'Oklahoma Sequoyah Award for YA (2008)',
            '\Rebecca Caudill Young Readers Book Award (2009)\'
        
        ],
        "likedPercent": 95.0,
        "price": 1.79
    },
    {
        "id": 2998,
        "title": "The Secret Garden",
        "series": "",
        "author": "Frances Hodgson Burnett",
        "description": "\"One of the most delightful and enduring classics of children's literature, The Secret Garden by Victorian author Frances Hodgson Burnett has remained a firm favorite with children the world over ever since it made its first appearance. Initially published as a serial story in 1910 in The American Magazine, it was brought out in novel form in 1911.  The plot centers round Mary Lennox, a young English girl who returns to England from India, having suffered the immense trauma by losing both her parents in a cholera epidemic. However, her memories of her parents are not pleasant, as they were a selfish, neglectful and pleasure-seeking couple. Mary is given to the care of her uncle Archibald Craven, whom she has never met. She travels to his home, Misselthwaite Manor located in the gloomy Yorkshire, a vast change from the sunny and warm climate she was used to. When she arrives, she is a rude, stubborn and given to stormy temper tantrums. However, her nature undergoes a gradual transformation when she learns of the tragedies that have befallen her strict and disciplinarian uncle whom she earlier feared and despised. Once when he's away from home, Mary discovers a charming walled garden which is always kept locked. The mystery deepens when she hears sounds of sobbing from somewhere within her uncle's vast mansion. The kindly servants ignore her queries or pretend they haven't heard, spiking Mary's curiosity.  The Secret Garden appeals to both young and old alike. It has wonderful elements of mystery, spirituality, charming characters and an authentic rendering of childhood emotions and experiences. Commonsense, truth and kindness, compassion and a belief in the essential goodness of human beings lie at the heart of this unforgettable story. It is the best known of Frances Hodgson Burnett's works, though most of us have definitely heard of, if not read, her other novel Little Lord Fauntleroy.  The book has been adapted extensively on stage, film and television and translated into all the world's major languages. In 1991, a Japanese anime version was launched for television in Japan. It remains a popular and beloved story of a child's journey into maturity, and a must-read for every child, parent, teacher and anyone who would enjoy this fascinating glimpse of childhood. One of the most delightful and enduring classics of children's literature, The Secret Garden by Victorian author Frances Hodgson Burnett has remained a firm favorite with children the world over ever since it made its first appearance. Initially published as a serial story in 1910 in The American Magazine, it was brought out in novel form in 1911.\" ",
        "language": "English",
        "isbn": "9780517189603",
        "genres": 
            ['Classics',
            'Fiction',
            'Childrens',
            'Young Adult',
            'Historical Fiction',
            'Middle Grade',
            'Literature',
            'Fantasy',
            'Historical',
            'Audiobook'
        
        ],
        "pages": 331,
        "awards": 
            ['Lewis Carroll Shelf Award (1958)'
        
        ],
        "likedPercent": 95.0,
        "price": 3.33
    },
    {
        "id": 128029,
        "title": "A Thousand Splendid Suns",
        "series": "",
        "author": "Khaled Hosseini (Goodreads Author)",
        "description": "A Thousand Splendid Suns is a breathtaking story set against the volatile events of Afghanistan's last thirty years\u2014from the Soviet invasion to the reign of the Taliban to post-Taliban rebuilding\u2014that puts the violence, fear, hope, and faith of this country in intimate, human terms. It is a tale of two generations of characters brought jarringly together by the tragic sweep of war, where personal lives\u2014the struggle to survive, raise a family, find happiness\u2014are inextricable from the history playing out around them.Propelled by the same storytelling instinct that made The Kite Runner a beloved classic, A Thousand Splendid Suns is at once a remarkable chronicle of three decades of Afghan history and a deeply moving account of family and friendship. It is a striking, heart-wrenching novel of an unforgiving time, an unlikely friendship, and an indestructible love\u2014a stunning accomplishment.--front flap",
        "language": "English",
        "isbn": "9781594489501",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Contemporary',
            'Novels',
            'Historical',
            'War',
            'Adult Fiction',
            'Adult',
            'Drama',
            'Literature'
        
        ],
        "pages": 372,
        "awards": 
            ['British Book Award for Best Read of the Year (2008)',
            'Book Sense Book of the Year Award for Adult Fiction (2008)',
            'California Book Award for Fiction (Silver) (2007)',
            'Exclusive Books Boeke Prize Nominee (2007)',
            'Lincoln Award Nominee (2011)'
        
        ],
        "likedPercent": 97.0,
        "price": 1.16
    },
    {
        "id": 33574273,
        "title": "A Wrinkle in Time",
        "series": "Time Quintet #1",
        "author": "Madeleine L'Engle",
        "description": "It was a dark and stormy night.Out of this wild night, a strange visitor comes to the Murry house and beckons Meg, her brother Charles Wallace, and their friend Calvin O'Keefe on a most dangerous and extraordinary adventure\u2014one that will threaten their lives and our universe.Winner of the 1963 Newbery Medal, A Wrinkle in Time is the first book in Madeleine L'Engle's classic Time Quintet.",
        "language": "English",
        "isbn": "9781250153272",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Classics',
            'Young Adult',
            'Science Fiction',
            'Childrens',
            'Middle Grade',
            'Time Travel',
            'Adventure',
            'Science Fiction Fantasy'
        
        ],
        "pages": 218,
        "awards": 
            ['Newbery Medal (1963)',
            '\Dorothy Canfield Fisher Childrens Book Award Nominee (1964)\',
            'Oklahoma Sequoyah Award (1965)',
            'Margaret A. Edwards Award (1998)'
        
        ],
        "likedPercent": 91.0,
        "price": 4.8
    },
    {
        "id": 13496,
        "title": "A Game of Thrones",
        "series": "A Song of Ice and Fire #1",
        "author": "George R.R. Martin",
        "description": "Here is the first volume in George R. R. Martin\u2019s magnificent cycle of novels that includes A Clash of Kings and A Storm of Swords. As a whole, this series comprises a genuine masterpiece of modern fantasy, bringing together the best the genre has to offer. Magic, mystery, intrigue, romance, and adventure fill these pages and transport us to a world unlike any we have ever experienced. Already hailed as a classic, George R. R. Martin\u2019s stunning series is destined to stand as one of the great achievements of imaginative fiction.A GAME OF THRONESLong ago, in a time forgotten, a preternatural event threw the seasons out of balance. In a land where summers can last decades and winters a lifetime, trouble is brewing. The cold is returning, and in the frozen wastes to the north of Winterfell, sinister and supernatural forces are massing beyond the kingdom\u2019s protective Wall. At the center of the conflict lie the Starks of Winterfell, a family as harsh and unyielding as the land they were born to. Sweeping from a land of brutal cold to a distant summertime kingdom of epicurean plenty, here is a tale of lords and ladies, soldiers and sorcerers, assassins and bastards, who come together in a time of grim omens.Here an enigmatic band of warriors bear swords of no human metal; a tribe of fierce wildlings carry men off into madness; a cruel young dragon prince barters his sister to win back his throne; and a determined woman undertakes the most treacherous of journeys. Amid plots and counterplots, tragedy and betrayal, victory and terror, the fate of the Starks, their allies, and their enemies hangs perilously in the balance, as each endeavors to win that deadliest of conflicts: the game of thrones.source: georgerrmartin.com",
        "language": "English",
        "isbn": "9780553588484",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Epic Fantasy',
            'Adult',
            'Science Fiction Fantasy',
            'High Fantasy',
            'Adventure',
            'Dragons',
            'Audiobook',
            'Epic'
        
        ],
        "pages": 835,
        "awards": 
            ['Nebula Award Nominee for Best Novel (1997)',
            'Locus Award for Best Fantasy Novel (1997)',
            'World Fantasy Award Nominee for Best Novel (1997)',
            'Premio Ignotus for Novela extranjera (2003)'
        
        ],
        "likedPercent": 96.0,
        "price": 4.01
    },
    {
        "id": 2956,
        "title": "The Adventures of Huckleberry Finn",
        "series": "Adventures of Tom and Huck #2",
        "author": "Mark Twain, Guy Cardwell (Notes), John Seelye (Introduction), Walter Trier (Ilustrator)",
        "description": "A nineteenth-century boy from a Mississippi River town recounts his adventures as he travels down the river with a runaway slave, encountering a family involved in a feud, two scoundrels pretending to be royalty, and Tom Sawyer's aunt who mistakes him for Tom.",
        "language": "English",
        "isbn": "9780142437179",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'Literature',
            'Young Adult',
            'Adventure',
            'School',
            'Novels',
            'Read For School',
            'American'
        
        ],
        "pages": 327,
        "awards": 
            [''
        
        ],
        "likedPercent": 90.0,
        "price": 6.99
    },
    {
        "id": 12232938,
        "title": "The Lovely Bones",
        "series": "",
        "author": "Alice Sebold",
        "description": "\"My name was Salmon, like the fish; first name, Susie. I was fourteen when I was murdered on December 6, 1973.\"So begins the story of Susie Salmon, who is adjusting to her new home in heaven, a place that is not at all what she expected, even as she is watching life on earth continue without her -- her friends trading rumors about her disappearance, her killer trying to cover his tracks, her grief-stricken family unraveling. Out of unspeakable tragedy and loss, The Lovely Bones succeeds, miraculously, in building a tale filled with hope, humor, suspense, even joy.",
        "language": "English",
        "isbn": "9780316166683",
        "genres": 
            ['Fiction',
            'Mystery',
            'Young Adult',
            'Contemporary',
            'Fantasy',
            'Crime',
            'Adult',
            'Adult Fiction',
            'Drama',
            'Novels'
        
        ],
        "pages": 372,
        "awards": 
            ['Bram Stoker Award for Best First Novel (2002)',
            'Orange Prize Nominee for Fiction Longlist (2003)',
            'British Book Award for Best Read of the Year (2004)',
            'Book Sense Book of the Year Award for Adult Fiction (2003)',
            'California Book Award for First Fiction (Silver) (2002)',
            'South Carolina Book Award for Young Adult Book Award (2005)',
            'Chicago Tribune Heartland Prize for Fiction (2002)',
            'Iowa High School Book Award (2005)',
            'Puddly Award for Fiction (2003)',
            'Eliot Rosewater Indiana High School Book Award (2005)',
            'Lincoln Award Nominee (2005)',
            'Missouri Gateway Readers Award (2005)'
        
        ],
        "likedPercent": 89.0,
        "price": 1.91
    },
    {
        "id": 231804,
        "title": "The Outsiders",
        "series": "",
        "author": "S.E. Hinton (Goodreads Author)",
        "description": "The Outsiders is about two weeks in the life of a 14-year-old boy. The novel tells the story of Ponyboy Curtis and his struggles with right and wrong in a society in which he believes that he is an outsider. According to Ponyboy, there are two kinds of people in the world: greasers and socs. A soc (short for \"social\") has money, can get away with just about anything, and has an attitude longer than a limousine. A greaser, on the other hand, always lives on the outside and needs to watch his back. Ponyboy is a greaser, and he's always been proud of it, even willing to rumble against a gang of socs for the sake of his fellow greasers--until one terrible night when his friend Johnny kills a soc. The murder gets under Ponyboy's skin, causing his bifurcated world to crumble and teaching him that pain feels the same whether a soc or a greaser.Librarian note: This record is for one of the three editions published with different covers and with ISBN 0-140-38572-X / 978-0-14-038572-4. The records are for the 1988 cover (this record), the 1995 cover, and the 2008 cover which is also the current in-print cover.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Young Adult',
            'Fiction',
            'School',
            'Realistic Fiction',
            'Read For School',
            'Coming Of Age',
            'Historical Fiction',
            'Contemporary',
            'Teen'
        
        ],
        "pages": 192,
        "awards": 
            ['Books I Loved Best Yearly (BILBY) Awards for Secondary  (1991)',
            'Margaret A. Edwards Award (1988)'
        
        ],
        "likedPercent": 94.0,
        "price": 10.679956521544781
    },
    {
        "id": 19543,
        "title": "Where the Wild Things Are",
        "series": "",
        "author": "Maurice Sendak",
        "description": "Max, a wild and naughty boy, is sent to bed without his supper by his exhausted mother. In his room, he imagines sailing far away to a land of Wild Things. Instead of eating him, the Wild Things make Max their king.",
        "language": "English",
        "isbn": "9780099408390",
        "genres": 
            ['Childrens',
            'Picture Books',
            'Fiction',
            'Classics',
            'Fantasy',
            'Adventure',
            'Young Adult',
            'Animals',
            'Kids',
            'Monsters'
        
        ],
        "pages": 37,
        "awards": 
            ['Caldecott Medal (1964)',
            'Lewis Carroll Shelf Award',
            'Indies Choice Book Award for Picture Book Hall of Fame (2009)'
        
        ],
        "likedPercent": 93.0,
        "price": 3.67
    },
    {
        "id": 23772,
        "title": "Green Eggs and Ham",
        "series": "",
        "author": "Dr. Seuss",
        "description": "\u201cDo you like green eggs and ham?\u201d asks Sam-I-am in this Beginner Book by Dr. Seuss. In a house or with a mouse? In a boat or with a goat? On a train or in a tree? Sam keeps asking persistently. With unmistakable characters and signature rhymes, Dr. Seuss\u2019s beloved favorite has cemented its place as a children\u2019s classic. In this most famous of cumulative tales, the list of places to enjoy green eggs and ham, and friends to enjoy them with, gets longer and longer. Follow Sam-I-am as he insists that this unusual treat is indeed a delectable snack to be savored everywhere and in every way. Originally created by Dr. Seuss, Beginner Books encourage children to read all by themselves, with simple words and illustrations that give clues to their meaning.",
        "language": "English",
        "isbn": "9780394800165",
        "genres": 
            ['Childrens',
            'Picture Books',
            'Classics',
            'Fiction',
            'Poetry',
            'Fantasy',
            'Humor',
            'Kids',
            'Food',
            'Young Adult'
        
        ],
        "pages": 62,
        "awards": 
            [''
        
        ],
        "likedPercent": 95.0,
        "price": 2.98
    },
    {
        "id": 1381,
        "title": "The Odyssey",
        "series": "",
        "author": "Homer, Robert Fagles (Translator), Bernard Knox (Introduction)",
        "description": "Sing to me of the man, Muse, the man of twists and turnsdriven time and again off course, once he had plunderedthe hallowed heights of Troy.So begins Robert Fagles' magnificent translation of the Odyssey, which Jasper Griffin in The New York Times Review of Books hails as \"a distinguished achievement.\"If the Iliad is the world's greatest war epic, then the Odyssey is literature's grandest evocation of everyman's journey though life. Odysseus' reliance on his wit and wiliness for survival in his encounters with divine and natural forces, during his ten-year voyage home to Ithaca after the Trojan War, is at once a timeless human story and an individual test of moral endurance. In the myths and legends that are retold here, Fagles has captured the energy and poetry of Homer's original in a bold, contemporary idiom, and given us an Odyssey to read aloud, to savor, and to treasure for its sheer lyrical mastery.Renowned classicist Bernard Knox's superb Introduction and textual commentary provide new insights and background information for the general reader and scholar alike, intensifying the strength of Fagles' translation.This is an Odyssey to delight both the classicist and the public at large, and to captivate a new generation of Homer's students.--Robert Fagles, winner of the PEN/Ralph Manheim Medal for Translation and a 1996 Academy Award in Literature from the American Academy of Arts and Letters, presents us with Homer's best-loved and most accessible poem in a stunning new modern-verse translation.",
        "language": "English",
        "isbn": "9780143039952",
        "genres": 
            ['Classics',
            'Fiction',
            'Poetry',
            'Mythology',
            'Fantasy',
            'School',
            'Literature',
            'Adventure',
            'Read For School',
            'Historical Fiction'
        
        ],
        "pages": 541,
        "awards": 
            [''
        
        ],
        "likedPercent": 87.0,
        "price": 3.65
    },
    {
        "id": 4214,
        "title": "Life of Pi",
        "series": "",
        "author": "Yann Martel",
        "description": "Life of Pi is a fantasy adventure novel by Yann Martel published in 2001. The protagonist, Piscine Molitor \"Pi\" Patel, a Tamil boy from Pondicherry, explores issues of spirituality and practicality from an early age. He survives 227 days after a shipwreck while stranded on a boat in the Pacific Ocean with a Bengal tiger named Richard Parker.",
        "language": "English",
        "isbn": "9780770430078",
        "genres": 
            ['Fiction',
            'Fantasy',
            'Classics',
            'Adventure',
            'Contemporary',
            'Novels',
            'Literature',
            'Magical Realism',
            'India',
            'Philosophy'
        
        ],
        "pages": 460,
        "awards": 
            ['Booker Prize (2002)',
            'Bollinger Everyman Wodehouse Prize Nominee for Comic Fiction (2003)',
            'Exclusive Books Boeke Prize (2003)',
            '\Governor Generals Literary Awards / Prix litt\u00e9raires du Gouverneur g\u00e9n\u00e9ral Nominee for Fiction (2001)\',
            'Lincoln Award Nominee (2005)',
            'Deutscher B\u00fccherpreis for Belletristik (2004)',
            'CBC Canada Reads Nominee (2003)',
            'Luisterboek Award Nominee (2015)',
            '\QWF (Quebec Writers Federation) Award for Paragraphe Hugh MacLennan Prize for Fiction (2001)\',
            'Asian/Pacific American Award for Literature for Adult Fiction (2003)'
        
        ],
        "likedPercent": 90.0,
        "price": 2.86
    },
    {
        "id": 1953,
        "title": "A Tale of Two Cities",
        "series": "",
        "author": "Charles Dickens, Richard Maxwell (Editor/Introduction)",
        "description": "After eighteen years as a political prisoner in the Bastille, the ageing Doctor Manette is finally released and reunited with his daughter in England. There the lives of two very different men, Charles Darnay, an exiled French aristocrat, and Sydney Carton, a disreputable but brilliant English lawyer, become enmeshed through their love for Lucie Manette. From the tranquil roads of London, they are drawn against their will to the vengeful, bloodstained streets of Paris at the height of the Reign of Terror, and they soon fall under the lethal shadow of La Guillotine.",
        "language": "English",
        "isbn": "9780141439600",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'Literature',
            'Historical',
            'Novels',
            'School',
            'Classic Literature',
            '19th Century',
            'British Literature'
        
        ],
        "pages": 489,
        "awards": 
            [''
        
        ],
        "likedPercent": 88.0,
        "price": 1.12
    },
    {
        "id": 43641,
        "title": "Water for Elephants",
        "series": "",
        "author": "Sara Gruen (Goodreads Author)",
        "description": "Winner of the 2007 BookBrowse Award for Most Popular Book.An atmospheric, gritty, and compelling novel of star-crossed lovers, set in the circus world circa 1932, by the bestselling author of Riding Lessons. When Jacob Jankowski, recently orphaned and suddenly adrift, jumps onto a passing train, he enters a world of freaks, drifters, and misfits, a second-rate circus struggling to survive during the Great Depression, making one-night stands in town after endless town. A veterinary student who almost earned his degree, Jacob is put in charge of caring for the circus menagerie. It is there that he meets Marlena, the beautiful young star of the equestrian act, who is married to August, the charismatic but twisted animal trainer. He also meets Rosie, an elephant who seems untrainable until he discovers a way to reach her. Beautifully written, Water for Elephants is illuminated by a wonderful sense of time and place. It tells a story of a love between two people that overcomes incredible odds in a world in which even love is a luxury that few can afford.",
        "language": "English",
        "isbn": "9781565125605",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Romance',
            'Historical',
            'Adult',
            'Adult Fiction',
            'Contemporary',
            'Book Club',
            'Novels',
            'Animals'
        
        ],
        "pages": 335,
        "awards": 
            ['Book Sense Book of the Year Award for Adult Fiction (2007)',
            'ALA Alex Award (2007)',
            'The Quill Award Nominee for General Fiction (2006)',
            'LovelyBooks Leserpreis Nominee for Allgemeine Literatur (2009)'
        
        ],
        "likedPercent": 94.0,
        "price": 3.46
    },
    {
        "id": 7604,
        "title": "Lolita",
        "series": "",
        "author": "Vladimir Nabokov, Craig Raine (Afterword)",
        "description": "Humbert Humbert - scholar, aesthete and romantic - has fallen completely and utterly in love with Lolita Haze, his landlady's gum-snapping, silky skinned twelve-year-old daughter. Reluctantly agreeing to marry Mrs Haze just to be close to Lolita, Humbert suffers greatly in the pursuit of romance; but when Lo herself starts looking for attention elsewhere, he will carry her off on a desperate cross-country misadventure, all in the name of Love. Hilarious, flamboyant, heart-breaking and full of ingenious word play, Lolita is an immaculate, unforgettable masterpiece of obsession, delusion and lust.",
        "language": "English",
        "isbn": "B00IIAQY3Q",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Novels',
            'Russia',
            'Romance',
            'Russian Literature',
            'Literary Fiction',
            '20th Century',
            'Adult'
        
        ],
        "pages": 331,
        "awards": 
            ['National Book Award Finalist for Fiction (1959)'
        
        ],
        "likedPercent": 89.0,
        "price": 17.492737400594745
    },
    {
        "id": 4981,
        "title": "Slaughterhouse-Five",
        "series": "",
        "author": "Kurt Vonnegut Jr.",
        "description": "Selected by the Modern Library as one of the 100 best novels of all time, Slaughterhouse-Five, an American classic, is one of the world's great antiwar books. Centering on the infamous firebombing of Dresden, Billy Pilgrim's odyssey through time reflects the mythic journey of our own fractured lives as we search for meaning in what we fear most.",
        "language": "English",
        "isbn": "9780385333849",
        "genres": 
            ['Classics',
            'Fiction',
            'Science Fiction',
            'War',
            'Historical Fiction',
            'Literature',
            'Novels',
            'Time Travel',
            'American',
            'Fantasy'
        
        ],
        "pages": 275,
        "awards": 
            ['Hugo Award Nominee for Best SF Novel (1970)',
            'Nebula Award Nominee for Best Novel (1969)',
            'National Book Award Finalist for Fiction (1970)',
            '\Chicago Publishers Award (1970)\'
        
        ],
        "likedPercent": 92.0,
        "price": 8.5
    },
    {
        "id": 35031085,
        "title": "Frankenstein: The 1818 Text",
        "series": "",
        "author": "Mary Wollstonecraft Shelley, Charlotte Gordon (Goodreads Author) (Introduction)",
        "description": "Mary Shelley's seminal novel of the scientist whose creation becomes a monsterThis edition is the original 1818 text, which preserves the hard-hitting and politically charged aspects of Shelley's original writing, as well as her unflinching wit and strong female voice. This edition also includes a new introduction and suggestions for further reading by author and Shelley expert Charlotte Gordon, literary excerpts and reviews selected by Gordon and a chronology and essay by preeminent Shelley scholar Charles E. Robinson.",
        "language": "English",
        "isbn": "9780143131847",
        "genres": 
            ['Classics',
            'Fiction',
            'Horror',
            'Science Fiction',
            'Gothic',
            'Fantasy',
            'School',
            'Literature',
            'Novels',
            '19th Century'
        
        ],
        "pages": 288,
        "awards": 
            [''
        
        ],
        "likedPercent": 89.0,
        "price": 8.75
    },
    {
        "id": 77203,
        "title": "The Kite Runner",
        "series": "",
        "author": "Khaled Hosseini (Goodreads Author), Berliani M. Nugrahani (Translator)",
        "description": "The unforgettable, heartbreaking story of the unlikely friendship between a wealthy boy and the son of his father\u2019s servant, The Kite Runner is a beautifully crafted novel set in a country that is in the process of being destroyed. It is about the power of reading, the price of betrayal, and the possibility of redemption; and an exploration of the power of fathers over sons\u2014their love, their sacrifices, their lies.A sweeping story of family, love, and friendship told against the devastating backdrop of the history of Afghanistan over the last thirty years, The Kite Runner is an unusual and powerful novel that has become a beloved, one-of-a-kind classic.--khaledhosseini.com",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Contemporary',
            'Classics',
            'Novels',
            'Historical',
            'Literature',
            'Adult',
            'Adult Fiction',
            'Drama'
        
        ],
        "pages": 371,
        "awards": 
            ['Borders Original Voices Award for Fiction (2003)',
            '\Humos Gouden Bladwijzer (2008)\',
            'Exclusive Books Boeke Prize (2004)',
            'ALA Alex Award (2004)',
            'Puddly Award for Fiction (2006)',
            'Lincoln Award Nominee (2006)',
            'Prix des libraires du Qu\u00e9bec for Laur\u00e9ats hors Qu\u00e9bec (2006)',
            'LovelyBooks Leserpreis Nominee for Allgemeine Literatur (2009)'
        
        ],
        "likedPercent": 95.0,
        "price": 19.815418470227197
    },
    {
        "id": 38447,
        "title": "The Handmaid's Tale",
        "series": "The Handmaid's Tale #1",
        "author": "Margaret Atwood (Goodreads Author)",
        "description": "Offred is a Handmaid in the Republic of Gilead. She may leave the home of the Commander and his wife once a day to walk to food markets whose signs are now pictures instead of words because women are no longer allowed to read. She must lie on her back once a month and pray that the Commander makes her pregnant, because in an age of declining births, Offred and the other Handmaids are valued only if their ovaries are viable. Offred can remember the years before, when she lived and made love with her husband, Luke; when she played with and protected her daughter; when she had a job, money of her own, and access to knowledge. But all of that is gone now . . . Funny, unexpected, horrifying, and altogether convincing, The Handmaid's Tale is at once scathing satire, dire warning, and tour de force.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Classics',
            'Dystopia',
            'Science Fiction',
            'Feminism',
            'Fantasy',
            'Adult',
            'Audiobook',
            'Literature',
            'Novels'
        "
        ],
        "pages": 314,
        "awards": 
            ['Booker Prize Nominee (1986)',
            'Nebula Award Nominee for Best Novel (1986)',
            'Locus Award Nominee for Best SF Novel (1987)',
            'Arthur C. Clarke Award (1987)',
            'Audie Award for Fiction (2013)',
            'Los Angeles Times Book Prize for Fiction (1986)',
            'Prometheus Award Nominee for Best Novel (1987)',
            'James Tiptree Jr. Award Nominee for Retrospective (1995)',
            '\Governor Generals Literary Awards / Prix litt\u00e9raires du Gouverneur g\u00e9n\u00e9ral for Fiction (1985)\',
            'SF Chronicle Award Nominee for Novel (1987)',
            '\Commonwealth Writers Prize Nominee for Best Book in Caribbean and Canada (1987)\',
            'CBC Canada Reads Nominee (2002)',
            'Met\u0173 verstin\u0117 knyga Nominee (2012)'
        
        ],
        "likedPercent": 93.0,
        "price": 10.916560580424179
    },
    {
        "id": 3636,
        "title": "The Giver",
        "series": "The Giver #1",
        "author": "Lois Lowry (Goodreads Author)",
        "description": "Twelve-year-old Jonas lives in a seemingly ideal world. Not until he is given his life assignment as the Receiver does he begin to understand the dark secrets behind this fragile community.",
        "language": "English",
        "isbn": "9780385732550",
        "genres": 
            ['Young Adult',
            'Fiction',
            'Classics',
            'Dystopia',
            'Science Fiction',
            'Fantasy',
            'School',
            'Childrens',
            'Middle Grade',
            'Read For School'
        
        ],
        "pages": 208,
        "awards": 
            ['Newbery Medal (1994)',
            '\Mythopoeic Fantasy Award Nominee for Childrens Literature (1994)\',
            'Golden Duck Award for Young Adult (Hal Clement Award) (1994)',
            'Garden State Book Award for Teen Fiction Grades 6-8 (1996)',
            '\Buckeye Childrens Book Award for Grade 6-8 (1997)\',
            'Grand Canyon Reader Award for Teen Book (1995)',
            'Maryland Black-Eyed Susan Book Award for Grade 6-9 (1995)',
            'Golden Sower Award for Young Adult (1995)',
            '\Pennsylvania Young Readers Choice Award for Grades 3-8 (1995)\',
            'Soaring Eagle Book Award Nominee (1996)',
            '\Pacific Northwest Library Association Young Readers Choice Award for Senior (1996)\',
            'Boston Globe-Horn Book Award Nominee for Fiction (1993)',
            'New Mexico Land of Enchantment Award (1997)',
            'Eliot Rosewater Indiana High School Book Award (1997)',
            '\William Allen White Childrens Book Award (1996)\',
            'Wyoming Indian Paintbrush Nominee (1996)',
            '\NSK Neustadt Prize for Childrens Literature Nominee (2013)\',
            'Oklahoma Sequoyah Award for YA (1996)',
            '\Rebecca Caudill Young Readers Book Award (1996)\',
            'Hea Lasteraamat (2010)',
            'Premi Protagonista Jove for Categoria 13-14 anys (2016)',
            'Margaret A. Edwards Award (2007)'
        
        ],
        "likedPercent": 94.0,
        "price": 7.15
    },
    {
        "id": 16866822,
        "title": "Catch-22",
        "series": "Catch-22 #1",
        "author": "Joseph Heller",
        "description": "The novel is set during World War II, from 1942 to 1944. It mainly follows the life of Captain John Yossarian, a U.S. Army Air Forces B-25 bombardier. Most of the events in the book occur while the fictional 256th Squadron is based on the island of Pianosa, in the Mediterranean Sea, west of Italy. The novel looks into the experiences of Yossarian and the other airmen in the camp, who attempt to maintain their sanity while fulfilling their service requirements so that they may return home.",
        "language": "English",
        "isbn": "9780684833392",
        "genres": 
        ['Classics',
            'Fiction',
            'War',
            'Historical Fiction',
            'Humor',
            'Literature',
            'Novels',
            'Unfinished',
            'American',
            'Historical'
        
        ],
        "pages": 453,
        "awards": 
        ['National Book Award Finalist for Fiction (1962)'
        
        ],
        "likedPercent": 90.0,
        "price": 3.32
    },
    {
        "id": 44767458,
        "title": "Dune",
        "series": "Dune #1",
        "author": "Frank Herbert",
        "description": "Set on the desert planet Arrakis, Dune is the story of the boy Paul Atreides, heir to a noble family tasked with ruling an inhospitable world where the only thing of value is the \u201cspice\u201d melange, a drug capable of extending life and enhancing consciousness. Coveted across the known universe, melange is a prize worth killing for...When House Atreides is betrayed, the destruction of Paul\u2019s family will set the boy on a journey toward a destiny greater than he could ever have imagined. And as he evolves into the mysterious man known as Muad\u2019Dib, he will bring to fruition humankind\u2019s most ancient and unattainable dream.",
        "language": "English",
        "isbn": "9780593099322",
        "genres": 
            ['Science Fiction',
            'Fiction',
            'Fantasy',
            'Classics',
            'Science Fiction Fantasy',
            'Space Opera',
            'Audiobook',
            'Novels',
            'Adventure',
            'Adult'
        
        ],
        "pages": 661,
        "awards": 
        ['Hugo Award for Best Novel (1966)',
            'Nebula Award for Best Novel (1965)',
            'Seiun Award \u661f\u96f2\u8cde for Best Foreign Novel (1974)'
        
        ],
        "likedPercent": 94.0,
        "price": 29.34
    },
    {
        "id": 5043,
        "title": "The Pillars of the Earth",
        "series": "Kingsbridge #1",
        "author": "Ken Follett (Goodreads Author)",
        "description": "Ken Follett is known worldwide as the master of split-second suspense, but his most beloved and bestselling book tells the magnificent tale of a twelfth-century monk driven to do the seemingly impossible: build the greatest Gothic cathedral the world has ever known.Everything readers expect from Follett is here: intrigue, fast-paced action, and passionate romance. But what makes The Pillars of the Earth extraordinary is the time the twelfth century; the place feudal England; and the subject the building of a glorious cathedral. Follett has re-created the crude, flamboyant England of the Middle Ages in every detail. The vast forests, the walled towns, the castles, and the monasteries become a familiar landscape. Against this richly imagined and intricately interwoven backdrop, filled with the ravages of war and the rhythms of daily life, the master storyteller draws the reader irresistibly into the intertwined lives of his characters into their dreams, their labors, and their loves: Tom, the master builder; Aliena, the ravishingly beautiful noblewoman; Philip, the prior of Kingsbridge; Jack, the artist in stone; and Ellen, the woman of the forest who casts a terrifying curse. From humble stonemason to imperious monarch, each character is brought vividly to life.The building of the cathedral, with the almost eerie artistry of the unschooled stonemasons, is the center of the drama. Around the site of the construction, Follett weaves a story of betrayal, revenge, and love, which begins with the public hanging of an innocent man and ends with the humiliation of a king.For the Movie tie-in edition with the same ISBN go to this Alternate Cover Edition",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
        ['Historical Fiction',
            'Fiction',
            'Historical',
            'Fantasy',
            'Classics',
            'Medieval',
            'Audiobook',
            'British Literature',
            'Novels',
            'Adult'
        
        ],
        "pages": 976,
        "awards": 
            [''
        
        ],
        "likedPercent": 95.0,
        "price": 5.3634039517705805
    },
    {
        "id": 149267,
        "title": "The Stand",
        "series": "",
        "author": "Stephen King (Goodreads Author), Bernie Wrightson (Illustrator)",
        "description": "This is the way the world ends: with a nanosecond of computer error in a Defense Department laboratory and a million casual contacts that form the links in a chain letter of death. And here is the bleak new world of the day after: a world stripped of its institutions and emptied of 99 percent of its people. A world in which a handful of panicky survivors choose sides -- or are chosen.",
        "language": "English",
        "isbn": "9780385199575",
        "genres": 
        ['Horror',
            'Fiction',
            'Fantasy',
            'Science Fiction',
            'Post Apocalyptic',
            'Thriller',
            'Dystopia',
            'Apocalyptic',
            'Audiobook',
            'Classics'
        
        ],
        "pages": 1153,
        "awards": 
        ['Locus Award Nominee for Best SF Novel (1979)',
            'World Fantasy Award Nominee for Best Novel (1979)',
            'Gandalf Award Nominee (1979)',
            'Balrog Award Nominee for Best Novel (1979) (1980)'
        
        ],
        "likedPercent": 96.0,
        "price": 8.38
    },
    {
        "id": 3590,
        "title": "The Adventures of Sherlock Holmes",
        "series": "Sherlock Holmes #3",
        "author": "Arthur Conan Doyle",
        "description": "The Adventures of Sherlock Holmes is the series of short stories that made the fortunes of the Strand magazine, in which they were first published, and won immense popularity for Sherlock Holmes and Dr Watson. The detective is at the height of his powers and the volume is full of famous cases, including 'The Red-Headed League', 'The Blue Carbuncle', and 'The Speckled Band'. Although Holmes gained a reputation for infallibility, Conan Doyle showed his own realism and feminism by having the great detective defeated by Irene Adler - the woman - in the very first story, 'A Scandal in Bohemia'. The editor of this volume, Richard Lancelyn Green is editor of The Uncollected Sherlock Holmes and The Further Adventures of Sherlock Holmes. With John Michael Gibson, he compiled the Soho Series Bibliography of A. Conan Doyle.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
        ['Classics',
            'Mystery',
            'Fiction',
            'Short Stories',
            'Crime',
            'Detective',
            'Literature',
            'Mystery Thriller',
            'Adventure',
            'Audiobook'
        
        ],
        "pages": 389,
        "awards": 
        [''
        
        ],
        "likedPercent": 98.0,
        "price": 18.473430156621575
    },
    {
        "id": 76620,
        "title": "Watership Down",
        "series": "Watership Down #1",
        "author": "Richard Adams",
        "description": "Librarian's note: See alternate cover edition of ISBN13 9780380395866 here.Set in England's Downs, a once idyllic rural landscape, this stirring tale of adventure, courage and survival follows a band of very special creatures on their flight from the intrusion of man and the certain destruction of their home. Led by a stouthearted pair of friends, they journey forth from their native Sandleford Warren through the harrowing trials posed by predators and adversaries, to a mysterious promised land and a more perfect society.",
        "language": "English",
        "isbn": "9780380395866",
        "genres": 
        ['Classics',
            'Fiction',
            'Fantasy',
            'Young Adult',
            'Animals',
            'Childrens',
            'Adventure',
            'Literature',
            'Novels',
            'Audiobook'
        
        ],
        "pages": 478,
        "awards": 
        ['Mythopoeic Fantasy Award Nominee (1975)',
            '\Guardian Childrens Fiction Prize (1973)\',
            'Audie Award Nominee for Best Male Narrator (2020)',
            'Boston Globe-Horn Book Award (1975)',
            'California Young Readers Medal for Young Adult (1977)',
            'Carnegie Medal (1972)'
        
        ],
        "likedPercent": 91.0,
        "price": 5.25
    },
    {
        "id": 2623,
        "title": "Great Expectations",
        "series": "",
        "author": "Charles Dickens, \u03a0\u03b1\u03c5\u03bb\u03af\u03bd\u03b1 \u03a0\u03b1\u03bc\u03c0\u03bf\u03cd\u03b4\u03b7 (Translator), Marisa Sestino (Translator)",
        "description": "'In what may be Dickens's best novel, humble, orphaned Pip is apprenticed to the dirty work of the forge but dares to dream of becoming a gentleman \u2014 and one day, under sudden and enigmatic circumstances, he finds himself in possession of \"great expectations.\" In this gripping tale of crime and guilt, revenge and reward, the compelling characters include Magwitch, the fearful and fearsome convict; Estella, whose beauty is excelled only by her haughtiness; and the embittered Miss Havisham, an eccentric jilted bride",
        "language": "English",
        "isbn": "9780192833594",
        "genres": 
        ['Classics',
            'Fiction',
            'Literature',
            'Historical Fiction',
            'School',
            'Novels',
            '19th Century',
            'Classic Literature',
            'British Literature',
            'Victorian'
        
        ],
        "pages": 505,
        "awards": 
        ['Audie Award for Classic (2010)',
            '\u041f\u0440\u0435\u043c\u0456\u044f \u0456\u043c\u0435\u043d\u0456 \u041c\u0430\u043a\u0441\u0438\u043c\u0430 \u0420\u0438\u043b\u044c\u0441\u044c\u043a\u043e\u0433\u043e (1993)'
        
        ],
        "likedPercent": 87.0,
        "price": 0.85
    },
    {
        "id": 1934,
        "title": "Little Women",
        "series": "Little Women #1",
        "author": "Louisa May Alcott",
        "description": "Generations of readers young and old, male and female, have fallen in love with the March sisters of Louisa May Alcott\u2019s most popular and enduring novel, Little Women. Here are talented tomboy and author-to-be Jo, tragically frail Beth, beautiful Meg, and romantic, spoiled Amy, united in their devotion to each other and their struggles to survive in New England during the Civil War.It is no secret that Alcott based Little Women on her own early life. While her father, the freethinking reformer and abolitionist Bronson Alcott, hobnobbed with such eminent male authors as Emerson, Thoreau, and Hawthorne, Louisa supported herself and her sisters with \"woman\u2019s work,\u201d including sewing, doing laundry, and acting as a domestic servant. But she soon discovered she could make more money writing. Little Women brought her lasting fame and fortune, and far from being the \"girl\u2019s book\u201d her publisher requested, it explores such timeless themes as love and death, war and peace, the conflict between personal ambition and family responsibilities, and the clash of cultures between Europe and America.",
        "language": "English",
        "isbn": "9780451529305",
        "genres": 
        ['Classics',
            'Fiction',
            'Historical Fiction',
            'Young Adult',
            'Romance',
            'Historical',
            'Literature',
            'Childrens',
            'Classic Literature',
            'Novels'
        
        ],
        "pages": 449,
        "awards": 
            [''
        
        ],
        "likedPercent": 93.0,
        "price": 5.51
    },
    {
        "id": 6514,
        "title": "The Bell Jar",
        "series": "",
        "author": "Sylvia Plath",
        "description": "The Bell Jar chronicles the crack-up of Esther Greenwood: brilliant, beautiful, enormously talented, and successful, but slowly going under\u2014maybe for the last time. Sylvia Plath masterfully draws the reader into Esther's breakdown with such intensity that Esther's insanity becomes completely real and even rational, as probable and accessible an experience as going to the movies. Such deep penetration into the dark and harrowing corners of the psyche is an extraordinary accomplishment and has made The Bell Jar a haunting American classic.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Feminism',
            'Mental Health',
            'Psychology',
            'Mental Illness',
            'Literature',
            'Novels',
            'Poetry',
            'Adult'
        "
        ],
        "pages": 294,
        "awards": 
            [''
        
        ],
        "likedPercent": 93.0,
        "price": 2.521782990399913
    },
    {
        "id": 136251,
        "title": "Harry Potter and the Deathly Hallows",
        "series": "Harry Potter #7",
        "author": "J.K. Rowling",
        "description": "Harry Potter is leaving Privet Drive for the last time. But as he climbs into the sidecar of Hagrid\u2019s motorbike and they take to the skies, he knows Lord Voldemort and the Death Eaters will not be far behind.The protective charm that has kept him safe until now is broken. But the Dark Lord is breathing fear into everything he loves. And he knows he can\u2019t keep hiding.To stop Voldemort, Harry knows he must find the remaining Horcruxes and destroy them.He will have to face his enemy in one final battle.--jkrowling.com",
        "language": "English",
        "isbn": "9780545010221",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Magic',
            'Childrens',
            'Adventure',
            'Audiobook',
            'Middle Grade',
            'Classics',
            'Science Fiction Fantasy'
        
        ],
        "pages": 759,
        "awards": 
            ['Locus Award Nominee for Best Young Adult Novel (2008)',
            'Odyssey Award Nominee (2008)',
            'Audie Award (2008)',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2008)',
            'Teen Read Award Nominee for Best All-Time-Fave (2010)',
            'Puddly Award for Fiction (2008)',
            'Andre Norton Award (2007)',
            'Carnegie Medal Nominee (2008)'
        
        ],
        "likedPercent": 98.0,
        "price": 2.85
    },
    {
        "id": 332613,
        "title": "One Flew Over the Cuckoo's Nest",
        "series": "",
        "author": "Ken Kesey",
        "description": "Tyrannical Nurse Ratched rules her ward in an Oregon State mental hospital with a strict and unbending routine, unopposed by her patients, who remain cowed by mind-numbing medication and the threat of electric shock therapy. But her regime is disrupted by the arrival of McMurphy \u2013 the swaggering, fun-loving trickster with a devilish grin who resolves to oppose her rules on behalf of his fellow inmates. His struggle is seen through the eyes of Chief Bromden, a seemingly mute half-Indian patient who understands McMurphy's heroic attempt to do battle with the powers that keep them imprisoned. Ken Kesey's extraordinary first novel is an exuberant, ribald and devastatingly honest portrayal of the boundaries between sanity and madness.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Psychology',
            'Novels',
            'School',
            'Mental Health',
            'American',
            'Mental Illness',
            'Contemporary'
        
        ],
        "pages": 325,
        "awards": 
            [''
        
        ],
        "likedPercent": 96.0,
        "price": 9.536902304978538
    },
    {
        "id": 15823480,
        "title": "Anna Karenina",
        "series": "",
        "author": "Leo Tolstoy, Aylmer Maude (Translator), Lev Tolstoi, Louise Maude (Translator), George Gibian (Preface)",
        "description": "Acclaimed by many as the world's greatest novel, Anna Karenina provides a vast panorama of contemporary life in Russia and of humanity in general. In it Tolstoy uses his intense imaginative insight to create some of the most memorable characters in all of literature. Anna is a sophisticated woman who abandons her empty existence as the wife of Karenin and turns to Count Vronsky to fulfil her passionate nature - with tragic consequences. Levin is a reflection of Tolstoy himself, often expressing the author's own views and convictions.Throughout, Tolstoy points no moral, merely inviting us not to judge but to watch. As Rosemary Edmonds comments, 'He leaves the shifting patterns of the kaleidoscope to bring home the meaning of the brooding words following the title, 'Vengeance is mine, and I will repay.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Romance',
            'Russia',
            'Historical Fiction',
            'Literature',
            'Russian Literature',
            'Novels',
            '19th Century',
            'Classic Literature'
        
        ],
        "pages": 964,
        "awards": 
            ['PEN Translation Prize for Richard Pevear & Larissa Volokhonsky (2002)'
        
        ],
        "likedPercent": 92.0,
        "price": 13.575342766462185
    },
    {
        "id": 10964,
        "title": "Outlander",
        "series": "Outlander #1",
        "author": "Diana Gabaldon (Goodreads Author)",
        "description": "The year is 1945. Claire Randall, a former combat nurse, is just back from the war and reunited with her husband on a second honeymoon when she walks through a standing stone in one of the ancient circles that dot the British Isles. Suddenly she is a Sassenach\u2014an \u201coutlander\u201d\u2014in a Scotland torn by war and raiding border clans in the year of Our Lord...1743. Hurled back in time by forces she cannot understand, Claire is catapulted into the intrigues of lairds and spies that may threaten her life, and shatter her heart. For here James Fraser, a gallant young Scots warrior, shows her a love so absolute that Claire becomes a woman torn between fidelity and desire\u2014and between two vastly different men in two irreconcilable lives.",
        "language": "English",
        "isbn": "9780440242949",
        "genres": 
            ['Historical Fiction',
            'Romance',
            'Fantasy',
            'Fiction',
            'Time Travel',
            'Historical',
            'Historical Romance',
            'Adult',
            'Audiobook',
            'Scotland'
        
        ],
        "pages": 850,
        "awards": 
            ['RITA Award by Romance Writers of America for Best Romance of 1991 & nominee for Best First Book & nominee for Single Title Historical Romance (1992)',
            'Puddly Award for Romance (2001)'
        
        ],
        "likedPercent": 92.0,
        "price": 5.98
    },
    {
        "id": 10917,
        "title": "My Sister's Keeper",
        "series": "",
        "author": "Jodi Picoult (Goodreads Author)",
        "description": "Anna is not sick, but she might as well be. By age thirteen, she has undergone countless surgeries, transfusions, and shots so that her older sister, Kate, can somehow fight the leukemia that has plagued her since childhood. The product of preimplantation genetic diagnosis, Anna was conceived as a bone marrow match for Kate\u2014a life and a role that she has never challenged... until now. Like most teenagers, Anna is beginning to question who she truly is. But unlike most teenagers, she has always been defined in terms of her sister\u2014and so Anna makes a decision that for most would be unthinkable, a decision that will tear her family apart and have perhaps fatal consequences for the sister she loves.A provocative novel that raises some important ethical issues, My Sister's Keeper is the story of one family's struggle for survival at all human costs and a stunning parable for all time.",
        "language": "English",
        "isbn": "9780743454537",
        "genres": 
            ['Fiction',
            'Contemporary',
            'Chick Lit',
            'Young Adult',
            'Drama',
            'Adult',
            'Adult Fiction',
            'Realistic Fiction',
            'Family',
            'Novels'
        
        ],
        "pages": 423,
        "awards": 
            ['Audie Award for Multi-Voiced Performance (2005)',
            '\Pennsylvania Young Readers Choice Award for Young Adults (2007)\',
            'ALA Alex Award (2005)',
            'Lincoln Award (2006)',
            'Green Mountain Book Award (2007)',
            'Missouri Gateway Readers Award Nominee (2007)'
        
        ],
        "likedPercent": 94.0,
        "price": 2.76
    },
    {
        "id": 39988,
        "title": "Matilda",
        "series": "",
        "author": "Roald Dahl, Quentin Blake (Illustrator)",
        "description": "Matilda is a little girl who is far too good to be true. At age five-and-a-half she's knocking off double-digit multiplication problems and blitz-reading Dickens. Even more remarkably, her classmates love her even though she's a super-nerd and the teacher's pet. But everything is not perfect in Matilda's world. For starters she has two of the most idiotic, self-centered parents who ever lived. Then there's the large, busty nightmare of a school principal, Miss (\"The\") Trunchbull, a former hammer-throwing champion who flings children at will and is approximately as sympathetic as a bulldozer. Fortunately for Matilda, she has the inner resources to deal with such annoyances: astonishing intelligence, saintly patience, and an innate predilection for revenge.She warms up with some practical jokes aimed at her hapless parents, but the true test comes when she rallies in defense of her teacher, the sweet Miss Honey, against the diabolical Trunchbull. There is never any doubt that Matilda will carry the day. Even so, this wonderful story is far from predictable. Roald Dahl, while keeping the plot moving imaginatively, also has an unerring ear for emotional truth. The reader cares about Matilda because in addition to all her other gifts, she has real feelings.",
        "language": "English",
        "isbn": "9780141301068",
        "genres": 
            ['Childrens',
            'Fiction',
            'Classics',
            'Fantasy',
            'Young Adult',
            'Middle Grade',
            'Humor',
            'Audiobook',
            'Magic',
            'Juvenile'
        
        ],
        "pages": 240,
        "awards": 
            ['Odyssey Award Nominee (2014)',
            'Prijs van de Nederlandse Kinderjury for 10-12 jaar en 13-16 jaar (1989)',
            '\Audie Award for Childrens Titles Ages 8-12 (2014)\',
            'Books I Loved Best Yearly (BILBY) Awards for Read Aloud (1990)',
            'Younger Readers (1997) (1990)',
            '\West Australian Young Readers Book Award (WAYRBA) for Younger Readers (1989)\',
            '\Blue Peter Book Award for Voters Award - Book that Made Me Laugh the Loudest (2000)\',
            '\Red House Childrens Book Award (1989)\',
            'Maryland Black-Eyed Susan Book Award for Book Award (1992)',
            '\Massachusetts Childrens Book Award (1992)\',
            '\Nevada Young Readers Award for Intermediate Category  (1992)\',
            '\Beehive Book Award for Childrens Fiction (1991)\',
            'Indian Paintbrush Book Award (1991)',
            'Bluestem Book Award Nominee (2016)',
            '\Virginia Readers Choice for Elementary (1990)\',
            '\Rebecca Caudill Young Readers Book Award (1991)\'
        
        ],
        "likedPercent": 97.0,
        "price": 6.01
    },
    {
        "id": 3263607,
        "title": "The Fellowship of the Ring",
        "series": "The Lord of the Rings #1",
        "author": "J.R.R. Tolkien",
        "description": "One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkeness bind themIn ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, The Dark Lord, forged the One Ring, filling it with his own power so that he could rule all others. But the One Ring was taken from him, and though he sought it throughout Middle-earth, it remained lost to him. After many ages it fell into the hands of Bilbo Baggins, as told in The Hobbit.In a sleepy village in the Shire, young Frodo Baggins finds himself faced with an immense task, as his elderly cousin Bilbo entrusts the Ring to his care. Frodo must leave his home and make a perilous journey across Middle-earth to the Cracks of Doom, there to destroy the Ring and foil the Dark Lord in his evil purpose.",
        "language": "English",
        "isbn": "9780345015339",
        "genres": 
            ['Classics',
            'Adventure',
            'Science Fiction Fantasy',
            'High Fantasy',
            'Epic Fantasy',
            'Young Adult',
            'Novels',
            'Magic',
            'Literature',
            'Audiobook'
        
        ],
        "pages": 527,
        "awards": 
            ['Publieksprijs voor het Nederlandse Boek Nominee (2002)'
        
        ],
        "likedPercent": 95.0,
        "price": 8.194453148637619
    },
    {
        "id": 2429135,
        "title": "The Girl with the Dragon Tattoo",
        "series": "Millennium #1",
        "author": "Stieg Larsson, Reg Keeland (Translator)",
        "description": "Harriet Vanger, a scion of one of Sweden\u2019s wealthiest families disappeared over forty years ago. All these years later, her aged uncle continues to seek the truth. He hires Mikael Blomkvist, a crusading journalist recently trapped by a libel conviction, to investigate. He is aided by the pierced and tattooed punk prodigy Lisbeth Salander. Together they tap into a vein of unfathomable iniquity and astonishing corruption.An international publishing sensation, Stieg Larsson\u2019s The Girl with the Dragon Tattoo combines murder mystery, family saga, love story, and financial intrigue into one satisfyingly complex and entertainingly atmospheric novel.Alternate Cover Edition ISBN 0307269752 (ISBN13: 9780307269751)",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Mystery',
            'Suspense',
            'Contemporary',
            'Adult',
            'Adult Fiction',
            'Sweden',
            'Thriller',
            'Audiobook',
            'Crime'
        
        ],
        "pages": 465,
        "awards": 
            ['Barry Award for Mystery/Crime Novel Of The Decade (2010)',
            'Macavity Award for Best First Mystery Novel (2009)',
            'Anthony Award for Best First Novel (2009)',
            'Glass Key Award (2006)',
            'CWA International Dagger Nominee (2008)',
            'Galaxy British Book Awards for Crime Thriller of the Year (2009)',
            'Exclusive Books Boeke Prize (2008)',
            'Strand Critics Award  Nominee for Best First Novel (2008)'
        
        ],
        "likedPercent": 93.0,
        "price": 10.861639305485207
    },
    {
        "id": 17899948,
        "title": "Rebecca",
        "series": "",
        "author": "Daphne du Maurier",
        "description": "Last night I dreamt I went to Manderley again . . .The novel begins in Monte Carlo, where our heroine is swept off her feet by the dashing widower Maxim de Winter and his sudden proposal of marriage. Orphaned and working as a lady's maid, she can barely believe her luck. It is only when they arrive at his massive country estate that she realizes how large a shadow his late wife will cast over their lives--presenting her with a lingering evil that threatens to destroy their marriage from beyond the grave.",
        "language": "English",
        "isbn": "9780316323703",
        "genres": 
            ['Classics',
            'Fiction',
            'Mystery',
            'Romance',
            'Gothic',
            'Historical Fiction',
            'Thriller',
            'Suspense',
            'Mystery Thriller',
            'Adult'
        
        ],
        "pages": 449,
        "awards": 
            ['National Book Award for Fiction (1938)',
            'Anthony Award for Best Novel of the Century (2000)'
        
        ],
        "likedPercent": 96.0,
        "price": 2.4136644272253425
    },
    {
        "id": 409614271984,
        "title": "1984",
        "series": "",
        "author": "George Orwell",
        "description": "Among the seminal texts of the 20th century, Nineteen Eighty-Four is a rare work that grows more haunting as its futuristic purgatory becomes more real. Published in 1949, the book offers political satirist George Orwell's nightmarish vision of a totalitarian, bureaucratic world and one poor stiff's attempt to find individuality. The brilliance of the novel is Orwell's prescience of modern life\u2014the ubiquity of television, the distortion of the language\u2014and his ability to construct such a thorough version of hell. Required reading for students since it was published, it ranks among the most terrifying novels ever written.",
        "language": "English",
        "isbn": "B003JTHWKU",
        "genres": 
            ['Classics',
            'Fiction',
            'Science Fiction',
            'Dystopia',
            'Literature',
            'Novels',
            'Politics',
            'School',
            'Fantasy',
            'Adult'
        
        ],
        "pages": 237,
        "awards": 
            ['Prometheus Hall of Fame Award (1984)',
            'Locus Award Nominee for All-Time Best Science Fiction Novel (1987)'
        
        ],
        "likedPercent": 94.0,
        "price": 7.65442179843546
    },
    {
        "id": 52892857,
        "title": "The Color Purple",
        "series": "The Color Purple Collection #1",
        "author": "Alice Walker",
        "description": "Winner of the Pulitzer Prize and the National Book Award. Alice Walker's iconic modern classic is now a Penguin Book.A powerful cultural touchstone of modern American literature, The Color Purple depicts the lives of African American women in early twentieth-century rural Georgia. Separated as girls, sisters Celie and Nettie sustain their loyalty to and hope in each other across time, distance and silence. Through a series of letters spanning twenty years, first from Celie to God, then the sisters to each other despite the unknown, the novel draws readers into its rich and memorable portrayals of Celie, Nettie, Shug Avery and Sofia and their experience. The Color Purple broke the silence around domestic and sexual abuse, narrating the lives of women through their pain and struggle, companionship and growth, resilience and bravery. Deeply compassionate and beautifully imagined, Alice Walker's epic carries readers on a spirit-affirming journey towards redemption and love.",
        "language": "English",
        "isbn": "9780143135692",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'Feminism',
            'Historical',
            'LGBT',
            'African American',
            'Literature',
            'Novels',
            'Adult'
        
        ],
        "pages": 304,
        "awards": 
            ['Pulitzer Prize for Fiction (1983)',
            'National Book Award for Fiction (Hardcover) (1983)',
            'National Book Critics Circle Award Nominee for Fiction (1982)',
            'Townsend Prize for Fiction (1984)'
        
        ],
        "likedPercent": 95.0,
        "price": 13.75
    },
    {
        "id": 14891,
        "title": "A Tree Grows in Brooklyn",
        "series": "",
        "author": "Betty Smith",
        "description": "The beloved American classic about a young girl's coming-of-age at the turn of the century, Betty Smith's A Tree Grows in Brooklyn is a poignant and moving tale filled with compassion and cruelty, laughter and heartache, crowded with life and people and incident. The story of young, sensitive, and idealistic Francie Nolan and her bittersweet formative years in the slums of Williamsburg has enchanted and inspired millions of readers for more than sixty years. By turns overwhelming, sublime, heartbreaking, and uplifting, the daily experiences of the unforgettable Nolans are raw with honesty and tenderly threaded with family connectedness -- in a work of literary art that brilliantly captures a unique time and place as well as incredibly rich moments of universal experience.",
        "language": "English",
        "isbn": "9780061120077",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'Young Adult',
            'Coming Of Age',
            'Historical',
            'Literature',
            'New York',
            'Novels',
            'Book Club'
        
        ],
        "pages": 496,
        "awards": 
            ['Audie Award for Classic (2002)'
        
        ],
        "likedPercent": 96.0,
        "price": 5.01
    },
    {
        "id": 41817486,
        "title": "A Clockwork Orange",
        "series": "",
        "author": "Anthony Burgess",
        "description": "In Anthony Burgess's influential nightmare vision of the future, criminals take over after dark. Teen gang leader Alex narrates in fantastically inventive slang that echoes the violent intensity of youth rebelling against society. Dazzling and transgressive, A Clockwork Orange is a frightening fable about good and evil and the meaning of human freedom. This edition includes the controversial last chapter not published in the first edition, and Burgess\u2019s introduction, \u201cA Clockwork Orange Resucked.\u201d",
        "language": "English",
        "isbn": "9780393341768",
        "genres": 
            ['Classics',
            'Fiction',
            'Science Fiction',
            'Dystopia',
            'Literature',
            'Novels',
            'Horror',
            'Thriller',
            'Crime',
            'Modern Classics'
        
        ],
        "pages": 240,
        "awards": 
            ['Prometheus Hall of Fame Award (2008)'
        
        ],
        "likedPercent": 92.0,
        "price": 13.05
    },
    {
        "id": 6288,
        "title": "The Road",
        "series": "",
        "author": "Cormac McCarthy",
        "description": "A searing, postapocalyptic novel destined to become Cormac McCarthy\u2019s masterpiece.A father and his son walk alone through burned America. Nothing moves in the ravaged landscape save the ash on the wind. It is cold enough to crack stones, and when the snow falls it is gray. The sky is dark. Their destination is the coast, although they don\u2019t know what, if anything, awaits them there. They have nothing; just a pistol to defend themselves against the lawless bands that stalk the road, the clothes they are wearing, a cart of scavenged food\u2014and each other.The Road is the profoundly moving story of a journey. It boldly imagines a future in which no hope remains, but in which the father and his son, \u201ceach the other\u2019s world entire,\u201d are sustained by love. Awesome in the totality of its vision, it is an unflinching meditation on the worst and the best that we are capable of: ultimate destructiveness, desperate tenacity, and the tenderness that keeps two people alive in the face of total devastation.",
        "language": "English",
        "isbn": "9780307265432",
        "genres": 
            ['Fiction',
            'Science Fiction',
            'Dystopia',
            'Post Apocalyptic',
            'Classics',
            'Horror',
            'Literature',
            'Novels',
            'Apocalyptic',
            'Contemporary'
        
        ],
        "pages": 241,
        "awards": 
            ['Pulitzer Prize for Fiction (2007)',
            'Locus Award Nominee for Best SF Novel (2007)',
            'James Tait Black Memorial Prize for Fiction (2006)',
            'The Quill Award for General Fiction (2007)',
            'Puddly Award for Fiction (2010)',
            'National Book Critics Circle Award Nominee for Fiction (2006)',
            'Believer Book Award (2006)',
            'T\u00e4htivaeltaja Award (2009)',
            'Cena Akademie SFFH for Kniha roku (Book of the Year) (2008)',
            'Prix des libraires du Qu\u00e9bec for Laur\u00e9ats hors Qu\u00e9bec (2009)',
            'International Dublin Literary Award Nominee (2008)',
            'The Rooster -- The Morning News Tournament of Books (2007)'
        
        ],
        "likedPercent": 90.0,
        "price": 6.83
    },
    {
        "id": 4934,
        "title": "The Brothers Karamazov",
        "series": "The Brothers Karamazov #1-4",
        "author": "Fyodor Dostoyevsky, Fyodor Dostoyevsky, Richard Pevear (Translator), Larissa Volokhonsky (Translator)",
        "description": "The Brothers Karamazov is a murder mystery, a courtroom drama, and an exploration of erotic rivalry in a series of triangular love affairs involving the \u201cwicked and sentimental\u201d Fyodor Pavlovich Karamazov and his three sons\u2015the impulsive and sensual Dmitri; the coldly rational Ivan; and the healthy, red-cheeked young novice Alyosha. Through the gripping events of their story, Dostoevsky portrays the whole of Russian life, is social and spiritual striving, in what was both the golden age and a tragic turning point in Russian culture.This award-winning translation by Richard Pevear and Larissa Volokhonsky remains true to the verbalinventiveness of Dostoevsky\u2019s prose, preserving the multiple voices, the humor, and the surprising modernity of the original. It is an achievement worthy of Dostoevsky\u2019s last and greatest novel.",
        "language": "English",
        "isbn": "9780374528379",
        "genres": 
            ['Classics',
            'Fiction',
            'Russia',
            'Literature',
            'Russian Literature',
            'Philosophy',
            'Novels',
            '19th Century',
            'Classic Literature',
            'Religion'
        
        ],
        "pages": 796,
        "awards": 
            [''
        
        ],
        "likedPercent": 95.0,
        "price": 5.51
    },
    {
        "id": 252577,
        "title": "Angela's Ashes",
        "series": "Frank McCourt #1",
        "author": "Frank McCourt",
        "description": "Imbued on every page with Frank McCourt's astounding humor and compassion. This is a glorious book that bears all the marks of a classic.\"When I look back on my childhood I wonder how I managed to survive at all. It was, of course, a miserable childhood: the happy childhood is hardly worth your while. Worse than the ordinary miserable childhood is the miserable Irish childhood, and worse yet is the miserable Irish Catholic childhood.\" So begins the Pulitzer Prize winning memoir of Frank McCourt, born in Depression-era Brooklyn to recent Irish immigrants and raised in the slums of Limerick, Ireland. Frank's mother, Angela, has no money to feed the children since Frank's father, Malachy, rarely works, and when he does he drinks his wages. Yet Malachy-- exasperating, irresponsible and beguiling-- does nurture in Frank an appetite for the one thing he can provide: a story. Frank lives for his father's tales of Cuchulain, who saved Ireland, and of the Angel on the Seventh Step, who brings his mother babies. Perhaps it is story that accounts for Frank's survival. Wearing rags for diapers, begging a pig's head for Christmas dinner and gathering coal from the roadside to light a fire, Frank endures poverty, near-starvation and the casual cruelty of relatives and neighbors--yet lives to tell his tale with eloquence, exuberance and remarkable forgiveness. Angela's Ashes, imbued on every page with Frank McCourt's astounding humor and compassion, is a glorious book that bears all the marks of a classic.",
        "language": "English",
        "isbn": "9780007205233",
        "genres": 
            ['Nonfiction',
            'Memoir',
            'Biography',
            'Classics',
            'Ireland',
            'Autobiography',
            'Biography Memoir',
            'History',
            'Irish Literature',
            'Historical'
        
        ],
        "pages": 452,
        "awards": 
            ['Pulitzer Prize for Biography or Autobiography (1997)',
            'American Booksellers Book Of The Year  Award for Adult Trade (1997)',
            'Audie Award for Nonfiction',
            'Abridged (1997)',
            'Los Angeles Times Book Prize for Biography (1996)',
            'Exclusive Books Boeke Prize (1997)',
            'National Book Critics Circle Award for Biography/Autobiography (1996)'
        
        ],
        "likedPercent": 94.0,
        "price": 2.76
    },
    {
        "id": 345627,
        "title": "Vampire Academy",
        "series": "Vampire Academy #1",
        "author": "Richelle Mead (Goodreads Author)",
        "description": "ONLY A TRUE BEST FRIEND CAN PROTECT YOU FROM YOUR IMMORTAL ENEMIES...Lissa Dragomir is a Moroi princess: a mortal vampire with a rare gift for harnessing the earth's magic. She must be protected at all times from Strigoi; the fiercest vampires - the ones who never die. The powerful blend of human and vampire blood that flows through Rose Hathaway, Lissa's best friend, makes her a dhampir. Rose is dedicated to a dangerous life of protecting Lissa from the Strigoi, who are hell-bent on making Lissa one of them.After two years of freedom, Rose and Lissa are caught and dragged back to St. Vladimir's Academy, a school for vampire royalty and their guardians-to-be, hidden in the deep forests of Montana. But inside the iron gates, life is even more fraught with danger... and the Strigoi are always close by.Rose and Lissa must navigate their dangerous world, confront the temptations of forbidden love, and never once let their guard down, lest the evil undead make Lissa one of them forever...",
        "language": "English",
        "isbn": "9781595141743",
        "genres": 
            ['Young Adult',
            'Fantasy',
            'Vampires',
            'Paranormal',
            'Romance',
            'Urban Fantasy',
            'Fiction',
            'Supernatural',
            'Paranormal Romance',
            'Magic'
        
        ],
        "pages": 332,
        "awards": 
            [''
        
        ],
        "likedPercent": 92.0,
        "price": 3.33
    },
    {
        "id": 52036,
        "title": "Siddhartha",
        "series": "",
        "author": "Hermann Hesse, Hilda Rosner (Translator)",
        "description": "Herman Hesse's classic novel has delighted, inspired, and influenced generations of readers, writers, and thinkers. In this story of a wealthy Indian Brahmin who casts off a life of privilege to seek spiritual fulfillment. Hesse synthesizes disparate philosophies--Eastern religions, Jungian archetypes, Western individualism--into a unique vision of life as expressed through one man's search for true meaning.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Philosophy',
            'Religion',
            'Spirituality',
            'Literature',
            'Buddhism',
            'German Literature',
            'Novels',
            'Historical Fiction'
        
        ],
        "pages": 152,
        "awards": 
            [''
        
        ],
        "likedPercent": 92.0,
        "price": 2.760548901002766
    },
    {
        "id": 7244,
        "title": "The Poisonwood Bible",
        "series": "",
        "author": "Barbara Kingsolver",
        "description": "The Poisonwood Bible is a story told by the wife and four daughters of Nathan Price, a fierce, evangelical Baptist who takes his family and mission to the Belgian Congo in 1959. They carry with them everything they believe they will need from home, but soon find that all of it -- from garden seeds to Scripture -- is calamitously transformed on African soil. What follows is a suspenseful epic of one family's tragic undoing and remarkable reconstruction over the course of three decades in postcolonial Africa.",
        "language": "English",
        "isbn": "9780060786502",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Africa',
            'Classics',
            'Historical',
            'Literary Fiction',
            'Literature',
            'Novels',
            'Religion',
            'Adult Fiction'
        
        ],
        "pages": 546,
        "awards": 
            ['Pulitzer Prize Nominee for Fiction (1999)',
            'Orange Prize Nominee for Fiction Shortlist (1999)',
            'Book Sense Book of the Year Award for Adult (2000)',
            'PEN/Faulkner Award for Fiction Nominee (1999)',
            'Independent Publisher Book Award (IPPY) for Audio Fiction - Unabridged (1999)',
            'Exclusive Books Boeke Prize (2000)',
            'Puddly Award for Novel (2001)',
            'International Dublin Literary Award Nominee (2000)'
        
        ],
        "likedPercent": 91.0,
        "price": 4.12
    },
    {
        "id": 119322,
        "title": "The Golden Compass",
        "series": "His Dark Materials #1",
        "author": "Philip Pullman",
        "description": "Lyra is rushing to the cold, far North, where witch clans and armored bears rule. North, where the Gobblers take the children they steal--including her friend Roger. North, where her fearsome uncle Asriel is trying to build a bridge to a parallel world.Can one small girl make a difference in such great and terrible endeavors? This is Lyra: a savage, a schemer, a liar, and as fierce and true a champion as Roger or Asriel could want--but what Lyra doesn't know is that to help one of them will be to betray the other.",
        "language": "English",
        "isbn": "9780679879244",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Childrens',
            'Adventure',
            'Science Fiction',
            'Science Fiction Fantasy',
            'Steampunk',
            'Middle Grade',
            'Audiobook'
        
        ],
        "pages": 399,
        "awards": 
            ['\Guardian Childrens Fiction Prize (1996)\',
            '\Audie Award for Childrens Titles (2000)\',
            'Lincoln Award Nominee (2005)',
            'Carnegie Medal (1995)'
        
        ],
        "likedPercent": 91.0,
        "price": 1.61
    },
    {
        "id": 3836,
        "title": "Don Quixote",
        "series": "",
        "author": "Miguel de Cervantes Saavedra, John Rutherford (Translator), Roberto Gonz\u00e1lez Echevarr\u00eda (Introduction)",
        "description": "Don Quixote has become so entranced by reading chivalric romances that he determines to become a knight-errant himself. In the company of his faithful squire, Sancho Panza, his exploits blossom in all sorts of wonderful ways. While Quixote's fancy often leads him astray\u2014he tilts at windmills, imagining them to be giants\u2014Sancho acquires cunning and a certain sagacity. Sane madman and wise fool, they roam the world together, and together they have haunted readers' imaginations for nearly four hundred years.With its experimental form and literary playfulness, Don Quixote has been generally recognized as the first modern novel. The book has been enormously influential on a host of writers, from Fielding and Sterne to Flaubert, Dickens, Melville, and Faulkner, who reread it once a year, \"just as some people read the Bible.\"",
        "language": "English",
        "isbn": "9780142437230",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Spanish Literature',
            'Adventure',
            'Novels',
            'Historical Fiction',
            'Spain',
            'Humor',
            'Classic Literature'
        
        ],
        "pages": 1023,
        "awards": 
            ['Will Eisner Comic Industry Awards Nominee for Best Adaptation from Another Medium & Best Humor Publication (2014)',
            '\u0392\u03c1\u03b1\u03b2\u03b5\u03af\u03bf \u039b\u03bf\u03b3\u03bf\u03c4\u03b5\u03c7\u03bd\u03b9\u03ba\u03ae\u03c2 \u039c\u03b5\u03c4\u03ac\u03c6\u03c1\u03b1\u03c3\u03b7\u03c2 \u0395\u039a\u0395\u039c\u0395\u039b for \u0399\u03c3\u03c0\u03b1\u03bd\u03cc\u03c6\u03c9\u03bd\u03b7 \u039b\u03bf\u03b3\u03bf\u03c4\u03b5\u03c7\u03bd\u03af\u03b1 (2010)',
            'Premio de traducci\u00f3n literaria Valle Incl\u00e1n for John Rutherford (2002)'
        
        ],
        "likedPercent": 90.0,
        "price": 9.04
    },
    {
        "id": 662,
        "title": "Atlas Shrugged",
        "series": "",
        "author": "Ayn Rand, Leonard Peikoff (Goodreads Author) (Introduction)",
        "description": "This is the story of a man who said that he would stop the motor of the world and did. Was he a destroyer or the greatest of liberators?Why did he have to fight his battle, not against his enemies, but against those who needed him most, and his hardest battle against the woman he loved? What is the world\u2019s motor \u2014 and the motive power of every man? You will know the answer to these questions when you discover the reason behind the baffling events that play havoc with the lives of the characters in this story. Tremendous in its scope, this novel presents an astounding panorama of human life \u2014 from the productive genius who becomes a worthless playboy \u2014 to the great steel industrialist who does not know that he is working for his own destruction \u2014 to the philosopher who becomes a pirate \u2014 to the composer who gives up his career on the night of his triumph \u2014 to the woman who runs a transcontinental railroad \u2014 to the lowest track worker in her Terminal tunnels. You must be prepared, when you read this novel, to check every premise at the root of your convictions.This is a mystery story, not about the murder \u2014 and rebirth \u2014 of man\u2019s spirit. It is a philosophical revolution, told in the form of an action thriller of violent events, a ruthlessly brilliant plot structure and an irresistible suspense. Do you say this is impossible? Well, that is the first of your premises to check.",
        "language": "English",
        "isbn": "9780452011878",
        "genres": 
            ['Classics',
            'Philosophy',
            'Literature',
            'Politics',
            'Science Fiction',
            'Dystopia',
            'Economics',
            'Novels',
            'Audiobook',
            'Fiction'
        
        ],
        "pages": 1168,
        "awards": 
            ['Prometheus Hall of Fame Award (1983)',
            'National Book Award Finalist for Fiction (1958)'
        
        ],
        "likedPercent": 80.0,
        "price": 4.41
    },
    {
        "id": 5,
        "title": "Harry Potter and the Prisoner of Azkaban",
        "series": "Harry Potter #3",
        "author": "J.K. Rowling, Mary GrandPr\u00e9 (Illustrator)",
        "description": "Harry Potter's third year at Hogwarts is full of new dangers. A convicted murderer, Sirius Black, has broken out of Azkaban prison, and it seems he's after Harry. Now Hogwarts is being patrolled by the dementors, the Azkaban guards who are hunting Sirius. But Harry can't imagine that Sirius or, for that matter, the evil Lord Voldemort could be more frightening than the dementors themselves, who have the terrible power to fill anyone they come across with aching loneliness and despair. Meanwhile, life continues as usual at Hogwarts. A top-of-the-line broom takes Harry's success at Quidditch, the sport of the Wizarding world, to new heights. A cute fourth-year student catches his eye. And he becomes close with the new Defense of the Dark Arts teacher, who was a childhood friend of his father. Yet despite the relative safety of life at Hogwarts and the best efforts of the dementors, the threat of Sirius Black grows ever closer. But if Harry has learned anything from his education in wizardry, it is that things are often not what they seem. Tragic revelations, heartwarming surprises, and high-stakes magical adventures await the boy wizard in this funny and poignant third installment of the beloved series.--scholastic.com",
        "language": "English",
        "isbn": "9780439655484",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Magic',
            'Childrens',
            'Adventure',
            'Middle Grade',
            'Audiobook',
            'Classics',
            'Science Fiction Fantasy'
        
        ],
        "pages": 435,
        "awards": 
            ['Bram Stoker Award for Best Work for Young Readers (1999)',
            'Hugo Award Nominee for Best Novel (2000)',
            'Locus Award for Best Fantasy Novel (2000)',
            '\Whitbread Award for Childrens Book of the Year (1999)\',
            '\Mythopoeic Fantasy Award for Childrens Literature (2008)\',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2005)',
            'Colorado Blue Spruce Young Adult Book Award (2004)',
            'Maine Student Book Award (2001)',
            'Golden Archer Award for Intermediate (2001)',
            'Indian Paintbrush Book Award (2004)',
            'Soaring Eagle Book Award (2002)',
            'Hotze de Roosprijs (2001)',
            'Nestl\u00e9 Smarties Book Prize for 9\u201311 years (1999)'
        
        ],
        "likedPercent": 99.0,
        "price": 5.94
    },
    {
        "id": 2165,
        "title": "The Old Man and the Sea",
        "series": "",
        "author": "Ernest Hemingway",
        "description": "Librarian's note: An alternate cover edition can be found hereThis short novel, already a modern classic, is the superbly told, tragic story of a Cuban fisherman in the Gulf Stream and the giant Marlin he kills and loses \u2014 specifically referred to in the citation accompanying the author's Nobel Prize for literature in 1954.",
        "language": "English",
        "isbn": "9780684830490",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Novels',
            'American',
            'School',
            'Adventure',
            'Classic Literature',
            'Literary Fiction',
            '20th Century'
        
        ],
        "pages": 96,
        "awards": 
            ['Pulitzer Prize for Fiction (1953)',
            'Premio Bancarella (1953)',
            'National Book Award Finalist for Fiction (1953)'
        
        ],
        "likedPercent": 87.0,
        "price": 15.63
    },
    {
        "id": 33648131,
        "title": "The Notebook",
        "series": "The Notebook #1",
        "author": "Nicholas Sparks (Goodreads Author)",
        "description": "Set amid the austere beauty of the North Carolina coast begins the story of Noah Calhoun, a rural Southerner recently returned from the Second World War. Noah is restoring a plantation home to its former glory, and he is haunted by images of the beautiful girl he met fourteen years earlier, a girl he loved like no other. Unable to find her, yet unwilling to forget the summer they spent together, Noah is content to live with only memories...until she unexpectedly returns to his town to see him once again.Like a puzzle within a puzzle, the story of Noah and Allie is just the beginning. As it unfolds, their tale miraculously becomes something different, with much higher stakes. The result is a deeply moving portrait of love itself, the tender moments and the fundamental changes that affect us all. It is a story of miracles and emotions that will stay with you forever.",
        "language": "English",
        "isbn": "B000Q67J66",
        "genres": 
            ['Romance',
            'Fiction',
            'Chick Lit',
            'Contemporary',
            'Adult',
            'Adult Fiction',
            'Contemporary Romance',
            'Love',
            'Drama',
            'Classics'
        
        ],
        "pages": 227,
        "awards": 
            [''
        
        ],
        "likedPercent": 91.0,
        "price": 13.820938055274484
    },
    {
        "id": 99107,
        "title": "Winnie-the-Pooh",
        "series": "Winnie-the-Pooh #1",
        "author": "A.A. Milne, Ernest H. Shepard (Illustrator)",
        "description": "The adventures of Christopher Robin and his friends in which Pooh Bear uses a balloon to get honey, Piglet meets a Heffalump, and Eeyore has a birthday.",
        "language": "English",
        "isbn": "9780525467564",
        "genres": 
            ['Classics',
            'Childrens',
            'Fiction',
            'Fantasy',
            'Animals',
            'Picture Books',
            'Young Adult',
            'Audiobook',
            'Middle Grade',
            'Juvenile'
        
        ],
        "pages": 145,
        "awards": 
            [''
        
        ],
        "likedPercent": 96.0,
        "price": 5.3
    },
    {
        "id": 23919,
        "title": "The Complete Stories and Poems",
        "series": "",
        "author": "Edgar Allan Poe",
        "description": "This single volume brings together all of Poe's stories and poems, and illuminates the diverse and multifaceted genius of one of the greatest and most influential figures in American literary history.",
        "language": "English",
        "isbn": "9780385074070",
        "genres": 
            ['Classics',
            'Poetry',
            'Horror',
            'Fiction',
            'Short Stories',
            'Mystery',
            'Gothic',
            'Literature',
            'Fantasy',
            'Classic Literature'
        
        ],
        "pages": 821,
        "awards": 
            [''
        
        ],
        "likedPercent": 97.0,
        "price": 5.27
    },
    {
        "id": 43763,
        "title": "Interview with the Vampire",
        "series": "The Vampire Chronicles #1",
        "author": "Anne Rice",
        "description": "This is the story of Louis, as told in his own words, of his journey through mortal and immortal life. Louis recounts how he became a vampire at the hands of the radiant and sinister Lestat and how he became indoctrinated, unwillingly, into the vampire way of life. His story ebbs and flows through the streets of New Orleans, defining crucial moments such as his discovery of the exquisite lost young child Claudia, wanting not to hurt but to comfort her with the last breaths of humanity he has inside. Yet, he makes Claudia a vampire, trapping her womanly passion, will, and intelligence inside the body of a small child. Louis and Claudia form a seemingly unbreakable alliance and even \"settle down\" for a while in the opulent French Quarter. Louis remembers Claudia's struggle to understand herself and the hatred they both have for Lestat that sends them halfway across the world to seek others of their kind. Louis and Claudia are desperate to find somewhere they belong, to find others who understand, and someone who knows what and why they are.Louis and Claudia travel Europe, eventually coming to Paris and the ragingly successful Theatre des Vampires--a theatre of vampires pretending to be mortals pretending to be vampires. Here they meet the magnetic and ethereal Armand, who brings them into a whole society of vampires. But Louis and Claudia find that finding others like themselves provides no easy answers and in fact presents dangers they scarcely imagined.Originally begun as a short story, the book took off as Anne wrote it, spinning the tragic and triumphant life experiences of a soul. As well as the struggles of its characters, Interview captures the political and social changes of two continents. The novel also introduces Lestat, Anne's most enduring character, a heady mixture of attraction and revulsion. The book, full of lush description, centers on the themes of immortality, change, loss, sexuality, and power.source: annerice.com",
        "language": "English",
        "isbn": "9780345476876",
        "genres": 
            ['Horror',
            'Fantasy',
            'Fiction',
            'Vampires',
            'Paranormal',
            'Supernatural',
            'Classics',
            'Gothic',
            'Urban Fantasy',
            'Historical Fiction'
        
        ],
        "pages": 342,
        "awards": 
            ['British Fantasy Award Nominee for Best Novel (1977)'
        
        ],
        "likedPercent": 93.0,
        "price": 2.66
    },
    {
        "id": 4473,
        "title": "A Prayer for Owen Meany",
        "series": "",
        "author": "John Irving (Goodreads Author)",
        "description": "Eleven-year-old Owen Meany, playing in a Little League baseball game in Gravesend, New Hampshire, hits a foul ball and kills his best friend's mother. Owen doesn't believe in accidents; he believes he is God's instrument. What happens to Owen after that 1953 foul is both extraordinary and terrifying. At moments a comic, self-deluded victim, but in the end the principal, tragic actor in a divine plan, Owen Meany is the most heartbreaking hero John Irving has yet created.",
        "language": "English",
        "isbn": "9780552135399",
        "genres": 
            ['Fiction',
            'Classics',
            'Contemporary',
            'Literature',
            'Literary Fiction',
            'Novels',
            'Historical Fiction',
            'Adult Fiction',
            'Coming Of Age',
            'American'
        
        ],
        "pages": 637,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 2.86
    },
    {
        "id": 153747,
        "title": "Moby-Dick or, the Whale",
        "series": "",
        "author": "Herman Melville, Andrew Delbanco (Introduction), Tom Quirk (Notes), Rockwell Kent (Illustrator)",
        "description": "\"It is the horrible texture of a fabric that should be woven of ships' cables and hawsers. A Polar wind blows through it, and birds of prey hover over it.\" So Melville wrote of his masterpiece, one of the greatest works of imagination in literary history. In part, Moby-Dick is the story of an eerily compelling madman pursuing an unholy war against a creature as vast and dangerous and unknowable as the sea itself. But more than just a novel of adventure, more than an encyclopaedia of whaling lore and legend, the book can be seen as part of its author's lifelong meditation on America. Written with wonderfully redemptive humour, Moby-Dick is also a profound inquiry into character, faith, and the nature of perception.This edition of Moby-Dick, which reproduces the definitive text of the novel, includes invaluable explanatory notes, along with maps, illustrations, and a glossary of nautical terms.",
        "language": "English",
        "isbn": "9780142437247",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Adventure',
            'Novels',
            'Historical Fiction',
            'American',
            'Classic Literature',
            '19th Century',
            'Unfinished'
        
        ],
        "pages": 654,
        "awards": 
            ['Audie Award for Solo Narration - Male (2006)',
            '\u041f\u0440\u0435\u043c\u0456\u044f \u0456\u043c\u0435\u043d\u0456 \u041c\u0430\u043a\u0441\u0438\u043c\u0430 \u0420\u0438\u043b\u044c\u0441\u044c\u043a\u043e\u0433\u043e (1991)'
        
        ],
        "likedPercent": 79.0,
        "price": 1.87
    },
    {
        "id": 4989,
        "title": "The Red Tent",
        "series": "",
        "author": "Anita Diamant (Goodreads Author)",
        "description": "Her name is Dinah. In the Bible, her life is only hinted at in a brief and violent detour within the more familiar chapters of the Book of Genesis that are about her father, Jacob, and his dozen sons. Told in Dinah's voice, this novel reveals the traditions and turmoils of ancient womanhood\u2014the world of the red tent. It begins with the story of her mothers\u2014Leah, Rachel, Zilpah, and Bilhah\u2014the four wives of Jacob. They love Dinah and give her gifts that sustain her through a hard-working youth, a calling to midwifery, and a new home in a foreign land. Dinah's story reaches out from a remarkable period of early history and creates an intimate connection with the past. Deeply affecting, The Red Tent combines rich storytelling with a valuable achievement in modern fiction: a new view of biblical women's society.",
        "language": "English",
        "isbn": "9780312353766",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Historical',
            'Religion',
            'Book Club',
            'Feminism',
            'Adult',
            'Adult Fiction',
            'Womens',
            'Novels'
        
        ],
        "pages": 324,
        "awards": 
            ['Book Sense Book of the Year Award for Adult Fiction (2001)',
            '\Boston Authors Club Award (1998)\'
        
        ],
        "likedPercent": 94.0,
        "price": 5.26
    },
    {
        "id": 37435,
        "title": "The Secret Life of Bees",
        "series": "",
        "author": "Sue Monk Kidd (Goodreads Author)",
        "description": "Set in South Carolina in 1964, The Secret Life of Bees tells the story of Lily Owens, whose life has been shaped around the blurred memory of the afternoon her mother was killed. When Lily's fierce-hearted black \"stand-in mother,\" Rosaleen, insults three of the deepest racists in town, Lily decides to spring them both free. They escape to Tiburon, South Carolina--a town that holds the secret to her mother's past. Taken in by an eccentric trio of black beekeeping sisters, Lily is introduced to their mesmerizing world of bees and honey, and the Black Madonna. This is a remarkable novel about divine female power, a story women will share and pass on to their daughters for years to come.",
        "language": "English",
        "isbn": "9780142001745",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Young Adult',
            'Classics',
            'Adult Fiction',
            'Historical',
            'Contemporary',
            'Adult',
            'Coming Of Age',
            'Chick Lit'
        
        ],
        "pages": 302,
        "awards": 
            ['Orange Prize Nominee for Fiction Longlist (2002)',
            'Book Sense Book of the Year Award for Paperback (2004)',
            'Lincoln Award Nominee (2005)',
            'Missouri Gateway Readers Award Nominee (2005)',
            'LovelyBooks Leserpreis Nominee for Allgemeine Literatur (2009)'
        
        ],
        "likedPercent": 94.0,
        "price": 3.5
    },
    {
        "id": 6,
        "title": "Harry Potter and the Goblet of Fire",
        "series": "Harry Potter #4",
        "author": "J.K. Rowling, Mary GrandPr\u00e9 (Illustrator)",
        "description": "Harry Potter is midway through his training as a wizard and his coming of age. Harry wants to get away from the pernicious Dursleys and go to the International Quidditch Cup with Hermione, Ron, and the Weasleys. He wants to dream about Cho Chang, his crush (and maybe do more than dream). He wants to find out about the mysterious event that's supposed to take place at Hogwarts this year, an event involving two other rival schools of magic, and a competition that hasn't happened for hundreds of years. He wants to be a normal, fourteen-year-old wizard. But unfortunately for Harry Potter, he's not normal - even by wizarding standards.And in his case, different can be deadly.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Magic',
            'Childrens',
            'Adventure',
            'Audiobook',
            'Middle Grade',
            'Classics',
            'Science Fiction Fantasy'
        
        ],
        "pages": 734,
        "awards": 
            ['Hugo Award for Best Novel (2001)',
            '\Mythopoeic Fantasy Award for Childrens Literature (2008)\',
            'Publieksprijs voor het Nederlandse Boek (2001)',
            'Audie Award for Solo Narration - Male (2001)',
            '\West Australian Young Readers Book Award (WAYRBA) for Younger Readers (2001)\',
            'Golden Archer Award for Middle/Junior High (2002)',
            'Indian Paintbrush Book Award (2002)',
            'Deutscher B\u00fccherpreis for Publikumspreis',
            'Corine Internationaler Buchpreis for Kinder- und Jugendbuch (2001)'
        
        ],
        "likedPercent": 99.0,
        "price": 16.675812360800933
    },
    {
        "id": 7171637,
        "title": "Clockwork Angel",
        "series": "The Infernal Devices #1",
        "author": "Cassandra Clare (Goodreads Author), Rita Sussekind (Translator)",
        "description": "In a time when Shadowhunters are barely winning the fight against the forces of darkness, one battle will change the course of history forever. Welcome to the Infernal Devices trilogy, a stunning and dangerous prequel to the New York Times bestselling Mortal Instruments series.The year is 1878. Tessa Gray descends into London\u2019s dark supernatural underworld in search of her missing brother. She soon discovers that her only allies are the demon-slaying Shadowhunters\u2014including Will and Jem, the mysterious boys she is attracted to. Soon they find themselves up against the Pandemonium Club, a secret organization of vampires, demons, warlocks, and humans. Equipped with a magical army of unstoppable clockwork creatures, the Club is out to rule the British Empire, and only Tessa and her allies can stop them...",
        "language": "English",
        "isbn": "9781416975861",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Paranormal',
            'Romance',
            'Steampunk',
            'Historical Fiction',
            'Fiction',
            'Urban Fantasy',
            'Vampires',
            'Angels'
        
        ],
        "pages": 481,
        "awards": 
            ['RITA Award by Romance Writers of America Nominee for Young Adult Romance (2011)',
            '\Romantic Times Reviewers Choice Award (RT Award) Nominee for Best Young Adult Paranormal/Fantasy Novel (2010)\',
            'The Inky Awards for Silver Inky (2011)',
            'Lincoln Award Nominee (2013)',
            'Goodreads Choice Award Nominee for Young Adult Fantasy and for Favorite Book and for Goodreads Author (2010)',
            'The Inky Awards Shortlist for Silver Inky (2011)',
            'Oklahoma Sequoyah Award for High School (2013)',
            'Premio El Templo de las Mil Puertas for Mejor novela extranjera perteneciente a saga (2010)'
        
        ],
        "likedPercent": 95.0,
        "price": 4.62
    },
    {
        "id": 1,
        "title": "Harry Potter and the Half-Blood Prince",
        "series": "Harry Potter #6",
        "author": "J.K. Rowling",
        "description": "The war against Voldemort is not going well; even Muggle governments are noticing. Ron scans the obituary pages of the Daily Prophet, looking for familiar names. Dumbledore is absent from Hogwarts for long stretches of time, and the Order of the Phoenix has already suffered losses.And yet . . .As in all wars, life goes on. The Weasley twins expand their business. Sixth-year students learn to Apparate - and lose a few eyebrows in the process. Teenagers flirt and fight and fall in love. Classes are never straightforward, through Harry receives some extraordinary help from the mysterious Half-Blood Prince.So it's the home front that takes center stage in the multilayered sixth installment of the story of Harry Potter. Here at Hogwarts, Harry will search for the full and complete story of the boy who became Lord Voldemort - and thereby find what may be his only vulnerability.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Magic',
            'Childrens',
            'Adventure',
            'Audiobook',
            'Middle Grade',
            'Classics',
            'Science Fiction Fantasy'
        
        ],
        "pages": 652,
        "awards": 
            ['Locus Award Nominee for Best Young Adult Novel (2006)',
            'Audie Award for Audiobook of the Year (2006)',
            'British Book of the Year (2006)'
        
        ],
        "likedPercent": 98.0,
        "price": 16.964713007300993
    },
    {
        "id": 16299,
        "title": "And Then There Were None",
        "series": "",
        "author": "Agatha Christie",
        "description": "First, there were ten\u2014a curious assortment of strangers summoned as weekend guests to a little private island off the coast of Devon. Their host, an eccentric millionaire unknown to all of them, is nowhere to be found. All that the guests have in common is a wicked past they're unwilling to reveal\u2014and a secret that will seal their fate. For each has been marked for murder. A famous nursery rhyme is framed and hung in every room of the mansion:\"Ten little boys went out to dine; One choked his little self and then there were nine. Nine little boys sat up very late; One overslept himself and then there were eight. Eight little boys traveling in Devon; One said he'd stay there then there were seven. Seven little boys chopping up sticks; One chopped himself in half and then there were six. Six little boys playing with a hive; A bumblebee stung one and then there were five. Five little boys going in for law; One got in Chancery and then there were four. Four little boys going out to sea; A red herring swallowed one and then there were three. Three little boys walking in the zoo; A big bear hugged one and then there were two. Two little boys sitting in the sun; One got frizzled up and then there was one. One little boy left all alone; He went out and hanged himself and then there were none.\"When they realize that murders are occurring as described in the rhyme, terror mounts. One by one they fall prey. Before the weekend is out, there will be none. Who has choreographed this dastardly scheme? And who will be left to tell the tale? Only the dead are above suspicion.",
        "language": "English",
        "isbn": "9780312330873",
        "genres": 
            ['Mystery',
            'Classics',
            'Fiction',
            'Crime',
            'Thriller',
            'Mystery Thriller',
            'Audiobook',
            'Adult',
            'Suspense',
            'Novels'
        
        ],
        "pages": 264,
        "awards": 
            [''
        
        ],
        "likedPercent": 96.0,
        "price": 4.82
    },
    {
        "id": 2187,
        "title": "Middlesex",
        "series": "",
        "author": "Jeffrey Eugenides",
        "description": "Middlesex tells the breathtaking story of Calliope Stephanides, and three generations of the Greek-American Stephanides family, who travel from a tiny village overlooking Mount Olympus in Asia Minor to Prohibition-era Detroit, witnessing its glory days as the Motor City and the race riots of 1967 before moving out to the tree-lined streets of suburban Grosse Pointe, Michigan. To understand why Calliope is not like other girls, she has to uncover a guilty family secret, and the astonishing genetic history that turns Callie into Cal, one of the most audacious and wondrous narrators in contemporary fiction. Lyrical and thrilling, Middlesex is an exhilarating reinvention of the American epic.",
        "language": "English",
        "isbn": "9780312422158",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Contemporary',
            'LGBT',
            'Literary Fiction',
            'Novels',
            'Classics',
            'Literature',
            'Queer',
            'Adult'
        
        ],
        "pages": 529,
        "awards": 
            ['Pulitzer Prize for Fiction (2003)',
            'James Tait Black Memorial Prize Nominee for Fiction (2003)',
            'Ambassador Book Award for Fiction (2003)',
            'Audie Award for Fiction',
            'Unabridged (2003)',
            'National Book Critics Circle Award Nominee for Fiction (2002)'
        
        ],
        "likedPercent": 91.0,
        "price": 3.11
    },
    {
        "id": 49552,
        "title": "The Stranger",
        "series": "",
        "author": "Albert Camus, Matthew Ward (Translator)",
        "description": "Through the story of an ordinary man unwittingly drawn into a senseless murder on an Algerian beach, Camus explored what he termed \"the nakedness of man faced with the absurd.\" First published in English in 1946; now in a new translation by Matthew Ward.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Philosophy',
            'France',
            'Literature',
            'Novels',
            'French Literature',
            'School',
            '20th Century',
            'Literary Fiction'
        
        ],
        "pages": 123,
        "awards": 
            ['PEN Translation Prize for Matthew Ward (1989)'
        
        ],
        "likedPercent": 92.0,
        "price": 8.085209382929865
    },
    {
        "id": 117833,
        "title": "The Master and Margarita",
        "series": "",
        "author": "Mikhail Bulgakov, Katherine Tiernan O'Connor (Translator), Ellendea Proffer (Annotations and Afterword), Diana Lewis Burgin (Translator)",
        "description": "The first complete, annotated English Translation of Mikhail Bulgakov's comic masterpiece.An audacious revision of the stories of Faust and Pontius Pilate, The Master and Margarita is recognized as one of the essential classics of modern Russian literature. The novel's vision of Soviet life in the 1930s is so ferociously accurate that it could not be published during its author's lifetime and appeared only in a censored edition in the 1960s. Its truths are so enduring that its language has become part of the common Russian speech.One hot spring, the devil arrives in Moscow, accompanied by a retinue that includes a beautiful naked witch and an immense talking black cat with a fondness for chess and vodka. The visitors quickly wreak havoc in a city that refuses to believe in either God or Satan. But they also bring peace to two unhappy Muscovites: one is the Master, a writer pilloried for daring to write a novel about Christ and Pontius Pilate; the other is Margarita, who loves the Master so deeply that she is willing literally to go to hell for him. What ensues is a novel of inexhaustible energy, humor, and philosophical depth, a work whose nuances emerge for the first time in Diana Burgin's and Katherine Tiernan O'Connor's splendid English version.(back cover)",
        "language": "English",
        "isbn": "9780679760801",
        "genres": 
            ['Classics',
            'Fiction',
            'Russia',
            'Fantasy',
            'Russian Literature',
            'Magical Realism',
            'Literature',
            'Novels',
            'Historical Fiction',
            '20th Century'
        
        ],
        "pages": 335,
        "awards": 
            [''
        
        ],
        "likedPercent": 94.0,
        "price": 13.56
    },
    {
        "id": 186074,
        "title": "The Name of the Wind",
        "series": "The Kingkiller Chronicle #1",
        "author": "Patrick Rothfuss (Goodreads Author)",
        "description": "Told in Kvothe's own voice, this is the tale of the magically gifted young man who grows to be the most notorious wizard his world has ever seen. The intimate narrative of his childhood in a troupe of traveling players, his years spent as a near-feral orphan in a crime-ridden city, his daringly brazen yet successful bid to enter a legendary school of magic, and his life as a fugitive after the murder of a king form a gripping coming-of-age story unrivaled in recent literature. A high-action story written with a poet's hand, The Name of the Wind is a masterpiece that will transport readers into the body and mind of a wizard.",
        "language": "English",
        "isbn": "9780756404079",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Epic Fantasy',
            'High Fantasy',
            'Magic',
            'Science Fiction Fantasy',
            'Adult',
            'Adventure',
            'Audiobook',
            'Epic'
        
        ],
        "pages": 662,
        "awards": 
            ['Locus Award Nominee for Best First Novel and Best Fantasy Novel (2008)',
            'Compton Crook Award Nominee (2008)',
            '\Grand Prix de lImaginaire Nominee for Roman \u00e9tranger and Traduction (2010)\',
            'ALA Alex Award (2008)',
            'The Quill Award for Science Fiction/Fantasy/Horror (2007)',
            'Sakura Medal for High School Book (2009)',
            'Premio Ignotus Nominee for Mejor novela extranjera (Best Foreign Novel) (2010)',
            'T\u00e4htifantasia Award Nominee (2011)'
        
        ],
        "likedPercent": 96.0,
        "price": 9.36
    },
    {
        "id": 11588,
        "title": "The Shining",
        "series": "The Shining #1",
        "author": "Stephen King (Goodreads Author)",
        "description": "Jack Torrance's new job at the Overlook Hotel is the perfect chance for a fresh start. As the off-season caretaker at the atmospheric old hotel, he'll have plenty of time to spend reconnecting with his family and working on his writing. But as the harsh winter weather sets in, the idyllic location feels ever more remote...and more sinister. And the only one to notice the strange and terrible forces gathering around the Overlook is Danny Torrance, a uniquely gifted five-year-old.",
        "language": "English",
        "isbn": "9780450040184",
        "genres": 
            ['Horror',
            'Fiction',
            'Thriller',
            'Classics',
            'Fantasy',
            'Mystery',
            'Paranormal',
            'Suspense',
            'Novels',
            'Adult'
        
        ],
        "pages": 659,
        "awards": 
            ['Locus Award Nominee for Best Fantasy Novel (1978)',
            'Gandalf Award Nominee (1978)'
        
        ],
        "likedPercent": 95.0,
        "price": 7.59
    },
    {
        "id": 24583,
        "title": "The Adventures of Tom Sawyer",
        "series": "Adventures of Tom and Huck #1",
        "author": "Mark Twain, Guy Cardwell (Annotations), John Seelye (Introduction)",
        "description": "The Adventures of Tom Sawyer revolves around the youthful adventures of the novel's schoolboy protagonist, Thomas Sawyer, whose reputation precedes him for causing mischief and strife. Tom lives with his Aunt Polly, half-brother Sid, and cousin Mary in the quaint town of St. Petersburg, just off the shore of the Mississippi River. St. Petersburg is described as a typical small-town atmosphere where the Christian faith is predominant, the social network is close-knit, and familiarity resides.  Unlike his brother Sid, Tom receives \"lickings\" from his Aunt Polly; ever the mischief-maker, would rather play hooky than attend school and often sneaks out his bedroom window at night to adventure with his friend, Huckleberry Finn \u00ad the town's social outcast. Tom, despite his dread of schooling, is extremely clever and would normally get away with his pranks if Sid were not such a \"tattle-tale.\"  As punishment for skipping school to go swimming, Aunt Polly assigns Tom the chore of whitewashing the fence surrounding the house. In a brilliant scheme, Tom is able to con the neighborhood boys into completing the chore for him, managing to convince them of the joys of whitewashing. At school, Tom is equally as flamboyant, and attracts attention by chasing other boys, yelling, and running around. With his usual antics, Tom attempts to catch the eye of Becky Thatcher, a new girl in town, and persuades her to get \"engaged\" by kissing him. But their romance collapses when she learns Tom has been \"engaged\" previously to Amy Lawrence. Shortly after Becky shuns him, he accompanies Huckleberry Finn to the graveyard at night, where they witness the murder of Dr. Robinson.Excerpt:\"TOM!\" No answer. \"TOM!\" No answer. \"What's gone with that boy, \u00a0I wonder? You TOM!\" No answer. The old lady pulled her spectacles down and looked over them about the room; then she put them up and looked out under them. She seldom or never looked\u00a0through\u00a0them for so small a thing as a boy; they were her state pair, the pride of her heart, and were built for \"style,\" not service\u2014she could have seen through a pair of stove-lids just as well. She looked perplexed for a moment, and then said, not fiercely, but still loud enough for the furniture to hear: \"Well, I lay if I get hold of you I'll\u2014\" She did not finish, for by this time she was bending down and punching under the bed with the broom, and so she needed breath to punctuate the punches with. She resurrected nothing but the cat. \"I never did see the beat of that boy!\"",
        "language": "English",
        "isbn": "9780143039563",
        "genres": 
            ['Classics',
            'Fiction',
            'Adventure',
            'Young Adult',
            'Historical Fiction',
            'Literature',
            'Childrens',
            'School',
            'Novels',
            'American'
        
        ],
        "pages": 244,
        "awards": 
            ['Lewis Carroll Shelf Award (1967)'
        
        ],
        "likedPercent": 92.0,
        "price": 3.36
    },
    {
        "id": 113436,
        "title": "Eragon",
        "series": "The Inheritance Cycle #1",
        "author": "Christopher Paolini (Goodreads Author)",
        "description": "An alternate cover edition for ISBN 9780375826696 can be found here.One boy...One dragon...A world of adventure. When Eragon finds a polished blue stone in the forest, he thinks it is the lucky discovery of a poor farm boy; perhaps it will buy his family meat for the winter. But when the stone brings a dragon hatchling, Eragon soon realizes he has stumbled upon a legacy nearly as old as the Empire itself. Overnight his simple life is shattered, and he is thrust into a perilous new world of destiny, magic, and power. With only an ancient sword and the advice of an old storyteller for guidance, Eragon and the fledgling dragon must navigate the dangerous terrain and dark enemies of an Empire ruled by a king whose evil knows no bounds. Can Eragon take up the mantle of the legendary Dragon Riders? The fate of the Empire may rest in his hands.",
        "language": "English",
        "isbn": "9780375826696",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Dragons',
            'Adventure',
            'Magic',
            'High Fantasy',
            'Science Fiction Fantasy',
            'Young Adult Fantasy',
            'Childrens'
        
        ],
        "pages": 503,
        "awards": 
            ['\Book Sense Book of the Year Award for Childrens Literature (2004)\',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2007)',
            'South Carolina Book Award for Young Adult Book (2006)',
            'Grand Canyon Reader Award for Teen Book (2006)',
            'Nene Award (2006)',
            'Colorado Blue Spruce Young Adult Book Award (2005)',
            '\Pennsylvania Young Readers Choice Award for Grades 6-8 (2005)\',
            'Rhode Island Teen Book Award (2005)',
            'Beehive Book Award for Young Adult Book (2005)',
            'Evergreen Teen Book Award (2006)',
            'Golden Archer Award for Middle/Junior High (2006)',
            'Soaring Eagle Book Award (2005)',
            '\Pacific Northwest Library Association Young Readers Choice Award for Intermediate (2006)\',
            'Iowa Teen Award (2008)',
            'Eliot Rosewater Indiana High School Book Award (2006)',
            'Literaturpreis der Jury der jungen Leser for Kinderbuch (2005)',
            '\Virginia Readers Choice for Middle (2005)\',
            'Missouri Gateway Readers Award for Young Adult (2006)',
            'Oklahoma Sequoyah Award for YA (2006)',
            '\Rebecca Caudill Young Readers Book Award (2006)\'
        
        ],
        "likedPercent": 88.0,
        "price": 2.86
    },
    {
        "id": 6310,
        "title": "Charlie and the Chocolate Factory",
        "series": "Charlie Bucket #1",
        "author": "Roald Dahl, Quentin Blake (Illustrations)",
        "description": "Charlie Bucket's wonderful adventure begins when he finds one of Mr. Willy Wonka's precious Golden Tickets and wins a whole day inside the mysterious chocolate factory. Little does he know the surprises that are in store for him!\r\n(back cover)",
        "language": "English",
        "isbn": "9780142403884",
        "genres": 
            ['Childrens',
            'Fantasy',
            'Fiction',
            'Classics',
            'Young Adult',
            'Middle Grade',
            'Humor',
            'Adventure',
            'Juvenile',
            'Novels'
        
        ],
        "pages": 176,
        "awards": 
            ['Books I Loved Best Yearly (BILBY) Awards for Read Aloud (1992)',
            '\North Dakota Childrens Choice Award (1985)\'
        
        ],
        "likedPercent": 95.0,
        "price": 1.13
    },
    {
        "id": 36576608,
        "title": "Flowers for Algernon",
        "series": "",
        "author": "Daniel Keyes",
        "description": "The story of a mentally disabled man whose experimental quest for intelligence mirrors that of Algernon, an extraordinary lab mouse. In diary entries, Charlie tells how a brain operation increases his IQ and changes his life. As the experimental procedure takes effect, Charlie's intelligence expands until it surpasses that of the doctors who engineered his metamorphosis. The experiment seems to be a scientific breakthrough of paramount importance until Algernon begins his sudden, unexpected deterioration. Will the same happen to Charlie?",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Classics',
            'Science Fiction',
            'Young Adult',
            'Literature',
            'Psychology',
            'School',
            'Novels',
            'Adult',
            'Read For School'
        
        ],
        "pages": 216,
        "awards": 
            ['Hugo Award Nominee for Best Novel (1967)',
            'Nebula Award for Best Novel (tie) (1966)',
            'Locus Award Nominee for All-Time Best Novel (36th in poll) (1975)'
        
        ],
        "likedPercent": 95.0,
        "price": 19.13076217275974
    },
    {
        "id": 70401,
        "title": "On the Road",
        "series": "Duluoz Legend",
        "author": "Jack Kerouac",
        "description": "A quintessential novel of America & the Beat Generation On the Road chronicles Jack Kerouac's years traveling the N. American continent with his friend Neal Cassady, \"a sideburned hero of the snowy West.\" As \"Sal Paradise\" & \"Dean Moriarty,\" the two roam the country in a quest for self-knowledge & experience. Kerouac's love of America, compassion for humanity & sense of language as jazz combine to make On the Road an inspirational work of lasting importance. This classic novel of freedom & longing defined what it meant to be \"Beat\" & has inspired every generation since its initial publication.",
        "language": "English",
        "isbn": "9780140042597",
        "genres": 
            ['Classics',
            'Fiction',
            'Travel',
            'Literature',
            'Novels',
            'American',
            'Adventure',
            '20th Century',
            'Unfinished',
            'Modern Classics'
        
        ],
        "pages": 307,
        "awards": 
            ['Grammy Award Nominee for Best Spoken Word Album (2001)'
        
        ],
        "likedPercent": 83.0,
        "price": 1.91
    },
    {
        "id": 485894,
        "title": "The Metamorphosis",
        "series": "",
        "author": "Franz Kafka, Stanley Corngold (Translator), Mircea Iv\u0103nescu (Translator)",
        "description": "Alternate cover edition of ISBN 0553213695 / 9780553213690\"As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect. He was laying on his hard, as it were armor-plated, back and when he lifted his head a little he could see his domelike brown belly divided into stiff arched segments on top of which the bed quilt could hardly keep in position and was about to slide off completely. His numerous legs, which were pitifully thin compared to the rest of his bulk, waved helplessly before his eyes.\" With it's startling, bizarre, yet surprisingly funny first opening, Kafka begins his masterpiece, The Metamorphosis. It is the story of a young man who, transformed overnight into a giant beetle-like insect, becomes an object of disgrace to his family, an outsider in his own home, a quintessentially alienated man. A harrowing\u2014though absurdly comic\u2014meditation on human feelings of inadequacy, guilt, and isolation, The Metamorphosis has taken its place as one of the most widely read and influential works of twentieth-century fiction. As W.H. Auden wrote, \"Kafka is important to us because his predicament is the predicament of modern man.\"",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Fantasy',
            'Literature',
            'Short Stories',
            'Philosophy',
            'School',
            'German Literature',
            'Horror',
            'Novels'
        
        ],
        "pages": 201,
        "awards": 
            [''
        
        ],
        "likedPercent": 89.0,
        "price": 18.87003339911703
    },
    {
        "id": 99561,
        "title": "Looking for Alaska",
        "series": "",
        "author": "John Green (Goodreads Author)",
        "description": "Before. Miles \u201cPudge\u201d Halter is done with his safe life at home. His whole life has been one big non-event, and his obsession with famous last words has only made him crave \u201cthe Great Perhaps\u201d even more (Francois Rabelais, poet). He heads off to the sometimes crazy and anything-but-boring world of Culver Creek Boarding School, and his life becomes the opposite of safe. Because down the hall is Alaska Young. The gorgeous, clever, funny, sexy, self-destructive, screwed up, and utterly fascinating Alaska Young. She is an event unto herself. She pulls Pudge into her world, launches him into the Great Perhaps, and steals his heart. Then. . . . After. Nothing is ever the same.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Young Adult',
            'Fiction',
            'Contemporary',
            'Romance',
            'Realistic Fiction',
            'Coming Of Age',
            'Teen',
            'Mystery',
            'Young Adult Contemporary',
            'High School'
        
        ],
        "pages": 221,
        "awards": 
            ['Los Angeles Times Book Prize Nominee for Young Adult Fiction (2005)',
            'Michael L. Printz Award (2006)',
            'Rhode Island Teen Book Award Nominee (2007)',
            'Michigan Library Association Thumbs Up! Award Nominee (2006)',
            'Deutscher Jugendliteraturpreis Nominee for Jugendbuch (2008)',
            'The Inky Awards for Silver Inky (2007)',
            'Lincoln Award Nominee (2009)',
            'Bronzener Lufti (2007)',
            'Green Mountain Book Award (2008)',
            'The Inky Awards Shortlist for Silver Inky (2007)',
            'Alabama Author Award for Young Adult (2006)',
            'Premio El Templo de las Mil Puertas Nominee for Mejor novela extranjera independiente (2014)'
        
        ],
        "likedPercent": 91.0,
        "price": 8.902707869630406
    },
    {
        "id": 1232,
        "title": "The Shadow of the Wind",
        "series": "El cementerio de los libros olvidados #1",
        "author": "Carlos Ruiz Zaf\u00f3n, Lucia Graves (Translator)",
        "description": "Barcelona, 1945: A city slowly heals from its war wounds, and Daniel, an antiquarian book dealer's son who mourns the loss of his mother, finds solace in a mysterious book entitled The Shadow of the Wind, by one Julian Carax. But when he sets out to find the author's other works, he makes a shocking discovery: someone has been systematically destroying every copy of every book Carax has written. In fact, Daniel may have the last of Carax's books in existence. Soon Daniel's seemingly innocent quest opens a door into one of Barcelona's darkest secrets--an epic story of murder, madness, and doomed love.--back cover",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Mystery',
            'Fantasy',
            'Books About Books',
            'Historical',
            'Spain',
            'Spanish Literature',
            'Gothic',
            'Magical Realism'
        
        ],
        "pages": 487,
        "awards": 
            ['Barry Award for Best First Novel (2005)',
            'Gumshoe Award Nominee for Best European Crime Novel (2005)',
            'Borders Original Voices Award for Fiction (2004)',
            'Dilys Award Nominee (2005)',
            '\Humos Gouden Bladwijzer (2006)\',
            'Prix du Meilleur Livre \u00c9tranger for Roman (2004)',
            'Prix des libraires du Qu\u00e9bec for Laur\u00e9ats hors Qu\u00e9bec (2005)',
            'One Book One San Diego (2015)',
            'Premi Llibreter de narrativa Nominee (2002)'
        
        ],
        "likedPercent": 95.0,
        "price": 13.92093772527481
    },
    {
        "id": 1618,
        "title": "The Curious Incident of the Dog in the Night-Time",
        "series": "",
        "author": "Mark Haddon",
        "description": "Christopher John Francis Boone knows all the countries of the world and their capitals and every prime number up to 7,057. He relates well to animals but has no understanding of human emotions. He cannot stand to be touched. And he detests the color yellow.Although gifted with a superbly logical brain, for fifteen-year-old Christopher everyday interactions and admonishments have little meaning. He lives on patterns, rules, and a diagram kept in his pocket. Then one day, a neighbor's dog, Wellington, is killed and his carefully constructive universe is threatened. Christopher sets out to solve the murder in the style of his favourite (logical) detective, Sherlock Holmes. What follows makes for a novel that is funny, poignant and fascinating in its portrayal of a person whose curse and blessing are a mind that perceives the world entirely literally.",
        "language": "English",
        "isbn": "9781400032716",
        "genres": 
            ['Fiction',
            'Mystery',
            'Young Adult',
            'Contemporary',
            'Novels',
            'Classics',
            'Psychology',
            'Literature',
            'Realistic Fiction',
            'Adult Fiction'
        
        ],
        "pages": 226,
        "awards": 
            ['Booker Prize Nominee for Longlist (2003)',
            'James Tait Black Memorial Prize Nominee for Fiction (2003)',
            'Whitbread Award for Novel and Book of the Year (2003)',
            '\Guardian Childrens Fiction Prize (2003)\',
            'McKitterick Prize (2004)',
            'Los Angeles Times Book Prize for Art Seidenbaum Award for First Fiction (2003)',
            'Exclusive Books Boeke Prize (2004)',
            'ALA Alex Award (2004)',
            'Zilveren Zoen (2004)',
            'Lincoln Award Nominee (2006)',
            '\Commonwealth Writers Prize for Best First Book Overall (2004)\',
            'North East Teenage Book Award Nominee (2004)',
            'Carnegie Medal Nominee (2003)',
            '\Dolly Gray Childrens Literature Award (2004)\',
            'Premi Protagonista Jove for Categoria 15-16 anys (2006)'
        
        ],
        "likedPercent": 92.0,
        "price": 2.94
    },
    {
        "id": 4948,
        "title": "The Very Hungry Caterpillar",
        "series": "",
        "author": "Eric Carle",
        "description": "THE all-time classic story, from generation to generation, sold somewhere in the world every 30 seconds! Have you shared it with a child or grandchild in your life? One sunny Sunday, the caterpillar was hatched out of a tiny egg. He was very hungry. On Monday, he ate through one apple; on Tuesday, he ate through three plums--and still he was hungry. When full at last, he made a cocoon around himself and went to sleep, to wake up a few weeks later wonderfully transformed into a butterfly!The brilliantly innovative Eric Carle has dramatized the story of one of Nature's commonest yet loveliest marvels, the metamorphosis of the butterfly. This audiobook will delight as well as instruct the very youngest listener.",
        "language": "English",
        "isbn": "9780241003008",
        "genres": 
            ['Picture Books',
            'Childrens',
            'Fiction',
            'Classics',
            'Animals',
            'Food',
            'Counting',
            'Storytime',
            'Kids',
            'Mathematics'
        
        ],
        "pages": 26,
        "awards": 
            ['California Young Readers Medal Nominee for Primary (1976)'
        
        ],
        "likedPercent": 94.0,
        "price": 2.42
    },
    {
        "id": 6900,
        "title": "Tuesdays with Morrie",
        "series": "",
        "author": "Mitch Albom (Goodreads Author)",
        "description": "Maybe it was a grandparent, or a teacher or a colleague. Someone older, patient and wise, who understood you when you were young and searching, and gave you sound advice to help you make your way through it. For Mitch Albom, that person was Morrie Schwartz, his college professor from nearly twenty years ago.Maybe, like Mitch, you lost track of this mentor as you made your way, and the insights faded. Wouldn't you like to see that person again, ask the bigger questions that still haunt you? Mitch Albom had that second chance. He rediscovered Morrie in the last months of the older man's life. Knowing he was dying of ALS - or motor neurone disease - Mitch visited Morrie in his study every Tuesday, just as they used to back in college. Their rekindled relationship turned into one final 'class': lessons in how to live.",
        "language": "English",
        "isbn": "9780751529814",
        "genres": 
            ['Nonfiction',
            'Memoir',
            'Biography',
            'Inspirational',
            'Classics',
            'Philosophy',
            'Self Help',
            'Contemporary',
            'Adult',
            'Biography Memoir'
        
        ],
        "pages": 210,
        "awards": 
            [''
        
        ],
        "likedPercent": 93.0,
        "price": 3.27
    },
    {
        "id": 9717,
        "title": "The Unbearable Lightness of Being",
        "series": "",
        "author": "Milan Kundera, Michael Henry Heim (Translator)",
        "description": "In The Unbearable Lightness of Being, Milan Kundera tells the story of a young woman in love with a man torn between his love for her and his incorrigible womanizing and one of his mistresses and her humbly faithful lover. This magnificent novel juxtaposes geographically distant places, brilliant and playful reflections, and a variety of styles, to take its place as perhaps the major achievement of one of the world\u2019s truly great writers.",
        "language": "English",
        "isbn": "9780571224388",
        "genres": 
            ['Fiction',
            'Classics',
            'Philosophy',
            'Literature',
            'Novels',
            'Czech Literature',
            'Romance',
            'Contemporary',
            'Literary Fiction',
            '20th Century'
        
        ],
        "pages": 320,
        "awards": 
            ['Los Angeles Times Book Prize for Fiction (1984)'
        
        ],
        "likedPercent": 93.0,
        "price": 11.62
    },
    {
        "id": 119073,
        "title": "The Name of the Rose",
        "series": "",
        "author": "Umberto Eco, William Weaver (Translator)",
        "description": "The year is 1327. Benedictines in a wealthy Italian abbey are suspected of heresy, and Brother William of Baskerville arrives to investigate. When his delicate mission is suddenly overshadowed by seven bizarre deaths, Brother William turns detective. His tools are the logic of Aristotle, the theology of Aquinas, the empirical insights of Roger Bacon\u2014all sharpened to a glistening edge by wry humor and a ferocious curiosity. He collects evidence, deciphers secret symbols and coded manuscripts, and digs into the eerie labyrinth of the abbey, where \u201cthe most interesting things happen at night.\u201d",
        "language": "English",
        "isbn": "9780156001311",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Mystery',
            'Classics',
            'Historical',
            'Literature',
            'Crime',
            'Italian Literature',
            'Italy',
            'Novels'
        
        ],
        "pages": 536,
        "awards": 
            ['\u0625\u0645\u0628\u064a\u0631\u062a\u0648',
            'Premio Strega (1981)',
            'Los Angeles Times Book Prize Nominee for Fiction (1983)',
            'Edgar Award Nominee for Best Novel (1984)',
            'PEN Translation Prize for William Weaver (1984)',
            'Premio Anghiari (1981)',
            '\Premio Il Libro dellanno (1981)\',
            'Prix M\u00e9dicis Etranger (1982)',
            '\u3053\u306e\u30df\u30b9\u30c6\u30ea\u30fc\u304c\u3059\u3054\u3044\uff01 for Best Translated Mystery Novel of the Year in Japan (1991)'
        
        ],
        "likedPercent": 93.0,
        "price": 4.07
    },
    {
        "id": 10365,
        "title": "Where the Red Fern Grows",
        "series": "",
        "author": "Wilson Rawls",
        "description": "A loving threesome, they ranged the dark hills and river bottoms of Cherokee country. Old Dan had the brawn. Little Ann had the brains, and Billy had the will to make them into the finest hunting team in the valley. Glory and victory were coming to them, but sadness waited too. Where the Red Fern Grows is an exciting tale of love and adventure you'll never forget.",
        "language": "English",
        "isbn": "9780375806810",
        "genres": 
            ['Classics',
            'Fiction',
            'Young Adult',
            'Childrens',
            'Animals',
            'Historical Fiction',
            'Middle Grade',
            'School',
            'Realistic Fiction',
            'Read For School'
        
        ],
        "pages": 272,
        "awards": 
            ['\Massachusetts Childrens Book Award (1987)\',
            '\North Dakota Childrens Choice Award (1981)\'
        
        ],
        "likedPercent": 93.0,
        "price": 5.4
    },
    {
        "id": 15881,
        "title": "Harry Potter and the Chamber of Secrets",
        "series": "Harry Potter #2",
        "author": "J.K. Rowling, Mary GrandPr\u00e9 (Illustrator)",
        "description": "Ever since Harry Potter had come home for the summer, the Dursleys had been so mean and hideous that all Harry wanted was to get back to the Hogwarts School for Witchcraft and Wizardry. But just as he\u2019s packing his bags, Harry receives a warning from a strange impish creature who says that if Harry returns to Hogwarts, disaster will strike.And strike it does. For in Harry\u2019s second year at Hogwarts, fresh torments and horrors arise, including an outrageously stuck-up new professor and a spirit who haunts the girls\u2019 bathroom. But then the real trouble begins \u2013 someone is turning Hogwarts students to stone. Could it be Draco Malfoy, a more poisonous rival than ever? Could it possible be Hagrid, whose mysterious past is finally told? Or could it be the one everyone at Hogwarts most suspects\u2026 Harry Potter himself!",
        "language": "English",
        "isbn": "9780439064866",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Magic',
            'Childrens',
            'Middle Grade',
            'Adventure',
            'Audiobook',
            'Classics',
            'Science Fiction Fantasy'
        
        ],
        "pages": 341,
        "awards": 
            ['\Mythopoeic Fantasy Award for Childrens Literature (2008)\',
            'British Book Award (1999)',
            'Prijs van de Jonge Jury (2002)',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (2006)',
            'Colorado Blue Spruce Young Adult Book Award (2008)',
            'Golden Archer Award for Middle/Junior High (2008)',
            'Nestl\u00e9 Smarties Book Prize for 9\u201311 years (1998)'
        
        ],
        "likedPercent": 98.0,
        "price": 4.17
    },
    {
        "id": 22034,
        "title": "The Godfather",
        "series": "The Godfather #1",
        "author": "Mario Puzo, Robert Thompson (Introduction), Peter Bart (Afterword)",
        "description": "The Godfather\u2014the epic tale of crime and betrayal that became a global phenomenon.Almost fifty years ago, a classic was born. A searing portrayal of the Mafia underworld, The Godfather introduced readers to the first family of American crime fiction, the Corleones, and their powerful legacy of tradition, blood, and honor. The seduction of power, the pitfalls of greed, and the allegiance to family\u2014these are the themes that have resonated with millions of readers around the world and made The Godfather the definitive novel of the violent subculture that, steeped in intrigue and controversy, remains indelibly etched in our collective consciousness.~penguin.com",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Classics',
            'Crime',
            'Thriller',
            'Historical Fiction',
            'Mystery',
            'Drama',
            'Novels',
            'Literature',
            'American'
        
        ],
        "pages": 448,
        "awards": 
            [''
        
        ],
        "likedPercent": 96.0,
        "price": 2.211876821827123
    },
    {
        "id": 12296,
        "title": "The Scarlet Letter",
        "series": "",
        "author": "Nathaniel Hawthorne, Thomas E. Connolly (Annotations), Nina Baym (Introduction)",
        "description": "Nathaniel Hawthorne's THE SCARLET LETTER reaches to our nation's historical and moral roots for the material of great tragedy. Set in an early New England colony, the novel shows the terrible impact a single, passionate act has on the lives of three members of the community: the defiant Hester Prynne; the fiery, tortured Reverend Dimmesdale; and the obsessed, vengeful Chillingworth.With THE SCARLET LETTER, Hawthorne became the first American novelist to forge from our Puritan heritage a universal classic, a masterful exploration of humanity's unending struggle with sin, guilt and pride.",
        "language": "English",
        "isbn": "9780142437261",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'School',
            'Literature',
            'High School',
            'Read For School',
            'Historical',
            'Classic Literature',
            'American'
        
        ],
        "pages": 279,
        "awards": 
            [''
        
        ],
        "likedPercent": 80.0,
        "price": 1.91
    },
    {
        "id": 168642,
        "title": "In Cold Blood",
        "series": "",
        "author": "Truman Capote",
        "description": "On November 15, 1959, in the small town of Holcomb, Kansas, four members of the Clutter family were savagely murdered by blasts from a shotgun held a few inches from their faces. There was no apparent motive for the crime, and there were almost no clues. As Truman Capote reconstructs the murder and the investigation that led to the capture, trial, and execution of the killers, he generates both mesmerizing suspense and astonishing empathy. At the center of his study are the amoral young killers Perry Smith and Dick Hickcock, who, vividly drawn by Capote, are shown to be reprehensible yet entirely and frighteningly human. In Cold Blood is a seminal work of modern prose, a remarkable synthesis of journalistic skill and powerfully evocative narrative.",
        "language": "English",
        "isbn": "9780679745587",
        "genres": 
            ['Nonfiction',
            'Classics',
            'True Crime',
            'Crime',
            'Mystery',
            'History',
            'Literature',
            'Thriller',
            'American',
            'Biography'
        
        ],
        "pages": 343,
        "awards": 
            ['Edgar Award for Best Fact Crime (1966)'
        
        ],
        "likedPercent": 93.0,
        "price": 6.58
    },
    {
        "id": 36236124,
        "title": "Fight Club",
        "series": "",
        "author": "Chuck Palahniuk (Goodreads Author)",
        "description": "Chuck Palahniuk showed himself to be his generation\u2019s most visionary satirist in this, his first book. Fight Club\u2019s estranged narrator leaves his lackluster job when he comes under the thrall of Tyler Durden, an enigmatic young man who holds secret after-hours boxing matches in the basement of bars. There, two men fight \"as long as they have to.\" This is a gloriously original work that exposes the darkness at the core of our modern world.",
        "language": "English",
        "isbn": "9780393355949",
        "genres": 
            ['Fiction',
            'Contemporary',
            'Classics',
            'Thriller',
            'Novels',
            'Mystery',
            'Adult',
            'Literature',
            'American',
            'Adult Fiction'
        
        ],
        "pages": 218,
        "awards": 
            ['Oregon Book Award for Fiction (1997)'
        
        ],
        "likedPercent": 95.0,
        "price": 10.16
    },
    {
        "id": 3431,
        "title": "The Five People You Meet in Heaven",
        "series": "The Five People You Meet in Heaven #1",
        "author": "Mitch Albom (Goodreads Author)",
        "description": "From the author of the phenomenal #1 New York Times bestseller Tuesdays with Morrie, a novel that explores the unexpected connections of our lives, and the idea that heaven is more than a place; it's an answer. Eddie is a wounded war veteran, an old man who has lived, in his mind, an uninspired life. His job is fixing rides at a seaside amusement park. On his 83rd birthday, a tragic accident kills him as he tries to save a little girl from a falling cart. He awakes in the afterlife, where he learns that heaven is not a destination. It's a place where your life is explained to you by five people, some of whom you knew, others who may have been strangers. One by one, from childhood to soldier to old age, Eddie's five people revisit their connections to him on earth, illuminating the mysteries of his \"meaningless\" life, and revealing the haunting secret behind the eternal question: \"Why was I here?\"",
        "language": "English",
        "isbn": "9781401308582",
        "genres": 
            ['Fiction',
            'Inspirational',
            'Contemporary',
            'Fantasy',
            'Adult',
            'Spirituality',
            'Classics',
            'Adult Fiction',
            'Philosophy',
            'Novels'
        
        ],
        "pages": 196,
        "awards": 
            ['Lincoln Award Nominee (2008)'
        
        ],
        "likedPercent": 91.0,
        "price": 3.57
    },
    {
        "id": 6339664,
        "title": "Hush, Hush",
        "series": "Hush, Hush #1",
        "author": "Becca Fitzpatrick (Goodreads Author)",
        "description": "A SACRED OATHA FALLEN ANGELA FORBIDDEN LOVERomance was not part of Nora Grey's plan. She's never been particularly attracted to the boys at her school, no matter how hard her best friend, Vee, pushes them at her. Not until Patch comes along. With his easy smile and eyes that seem to see inside her, Patch draws Nora to him against her better judgment.But after a series of terrifying encounters, Nora's not sure whom to trust. Patch seems to be everywhere she is and seems to know more about her than her closest friends. She can't decide whether she should fall into his arms or run and hide. And when she tries to seek some answers, she finds herself near a truth that is way more unsettling than anything Patch makes her feel.For she is right in the middle of an ancient battle between the immortal and those that have fallen - and, when it comes to choosing sides, the wrong choice will cost Nora her life.",
        "language": "English",
        "isbn": "9781416989417",
        "genres": 
            ['Young Adult',
            'Fantasy',
            'Romance',
            'Paranormal',
            'Angels',
            'Paranormal Romance',
            'Supernatural',
            'Fiction',
            'Urban Fantasy',
            'Young Adult Fantasy'
        ],
        "pages": 391,
        "awards": 
            ['Goodreads Choice Award Nominee for Young Adult Series (2009)'
        ],
        "likedPercent": 88.0,
        "price": 2.55
    },
    {
        "id": 233093,
        "title": "The Cat in the Hat",
        "series": "The Cat in the Hat #1",
        "author": "Dr. Seuss",
        "description": "Poor Sally and her brother. It's cold and wet and they're stuck in the house with nothing to do . . . until a giant cat in a hat shows up, transforming the dull day into a madcap adventure and almost wrecking the place in the process! Written by Dr. Seuss in 1957 in response to the concern that \"pallid primers [with] abnormally courteous, unnaturally clean boys and girls' were leading to growing illiteracy among children, The Cat in the Hat (the first Random House Beginner Book) changed the way our children learn how to read.Book Details: \r\n   Format: Hardcover \r\n   Publication Date: 3/12/1957 \r\n   Pages: 72 \r\n   Reading Level: Age 3 and Up \r\n ",
        "language": "English",
        "isbn": "9780394800011",
        "genres": 
            ['Childrens',
            'Picture Books',
            'Classics',
            'Fiction',
            'Poetry',
            'Fantasy',
            'Humor',
            'Animals',
            'Kids',
            'Cats'
        ],
        "pages": 61,
        "awards": 
            ['Books I Loved Best Yearly (BILBY) Awards for Early Readers (2004',
            '2012) (2004)'
        ],
        "likedPercent": 93.0,
        "price": 0.85
    },
    {
        "id": 30165203,
        "title": "American Gods",
        "series": "American Gods #1",
        "author": "Neil Gaiman (Goodreads Author)",
        "description": "Days before his release from prison, Shadow's wife, Laura, dies in a mysterious car crash. Numbly, he makes his way back home. On the plane, he encounters the enigmatic Mr Wednesday, who claims to be a refugee from a distant war, a former god and the king of America. Together they embark on a profoundly strange journey across the heart of the USA, whilst all around them a storm of preternatural and epic proportions threatens to break.Scary, gripping and deeply unsettling, American Gods takes a long, hard look into the soul of America. You'll be surprised by what - and who - it finds there...This is the author's preferred text, never before published in the UK, and is about 12,000 words longer than the previous UK edition.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Urban Fantasy',
            'Mythology',
            'Audiobook',
            'Science Fiction',
            'Science Fiction Fantasy',
            'Adult',
            'Contemporary',
            'Novels'
        ],
        "pages": 635,
        "awards": 
            ['Bram Stoker Award for Best Novel (2001)',
            'Hugo Award for Best Novel (2002)',
            'Nebula Award for Best Novel (2002)',
            'Locus Award for Best Fantasy Novel (2002)',
            'International Horror Guild Award Nominee for Best Novel (2001)',
            'World Fantasy Award Nominee for Best Novel (2002)',
            'SFX Award for Best Novel (2002)',
            'Geffen Award (2003)',
            'Mythopoeic Fantasy Award Nominee for Adult Literature (2002)',
            'British Science Fiction Association Award Nominee for Best Novel (2001)',
            '\Grand Prix de lImaginaire Nominee for Roman \u00e9tranger (2003)\',
            'Prix Bob Morane for roman traduit (2003)',
            'British Fantasy Award Nominee for Best Novel (August Derlith Fantasy Award) (2002)'
        ],
        "likedPercent": 93.0,
        "price": 17.36695507656816
    },
    {
        "id": 7126,
        "title": "The Count of Monte Cristo",
        "series": "",
        "author": "Alexandre Dumas, Robin Buss (Translator)",
        "description": "Thrown in prison for a crime he has not committed, Edmond Dantes is confined to the grim fortress of If. There he learns of a great hoard of treasure hidden on the Isle of Monte Cristo and he becomes determined not only to escape, but also to unearth the treasure and use it to plot the destruction of the three men responsible for his incarceration. Dumas\u2019 epic tale of suffering and retribution, inspired by a real-life case of wrongful imprisonment, was a huge popular success when it was first serialized in the 1840s.Robin Buss\u2019s lively English translation is complete and unabridged, and remains faithful to the style of Dumas\u2019s original. This edition includes an introduction, explanatory notes and suggestions for further reading.",
        "language": "English",
        "isbn": "9780140449266",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'Adventure',
            'Literature',
            'France',
            'Historical',
            'Classic Literature',
            'Novels',
            'Romance'
        ],
        "pages": 1276,
        "awards": 
            ['
        "
        ],
        "likedPercent": 95.0,
        "price": 6.13
    },
    {
        "id": 256008,
        "title": "Lonesome Dove",
        "series": "Lonesome Dove #1",
        "author": "Larry McMurtry",
        "description": "A love story, an adventure, and an epic of the frontier, Larry McMurtry\u2019s Pulitzer Prize\u2014 winning classic, Lonesome Dove, the third book in the Lonesome Dove tetralogy, is the grandest novel ever written about the last defiant wilderness of America.Journey to the dusty little Texas town of Lonesome Dove and meet an unforgettable assortment of heroes and outlaws, whores and ladies, Indians and settlers. Richly authentic, beautifully written, always dramatic, Lonesome Dove is a book to make us laugh, weep, dream, and remember.",
        "language": "English",
        "isbn": "9780671683900",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Westerns',
            'Classics',
            'Historical',
            'Adventure',
            'Novels',
            'Literature',
            'Audiobook',
            'American'
        ],
        "pages": 960,
        "awards": 
            ['Pulitzer Prize for Fiction (1986)',
            'PEN/Faulkner Award for Fiction Nominee (1986)',
            'National Book Critics Circle Award Nominee for Fiction (1985)',
            'Spur Award for Best Western Novel (1985)'
        ],
        "likedPercent": 97.0,
        "price": 4.55
    },
    {
        "id": 343,
        "title": "Perfume: The Story of a Murderer",
        "series": "",
        "author": "Patrick S\u00fcskind, John E. Woods (Translator)",
        "description": "An acclaimed bestseller and international sensation, Patrick Suskind's classic novel provokes a terrifying examination of what happens when one man's indulgence in his greatest passion\u2014his sense of smell\u2014leads to murder.In the slums of eighteenth-century France, the infant Jean-Baptiste Grenouille is born with one sublime gift\u2014an absolute sense of smell. As a boy, he lives to decipher the odors of Paris, and apprentices himself to a prominent perfumer who teaches him the ancient art of mixing precious oils and herbs. But Grenouille's genius is such that he is not satisfied to stop there, and he becomes obsessed with capturing the smells of objects such as brass doorknobs and fresh-cut wood. Then one day he catches a hint of a scent that will drive him on an ever-more-terrifying quest to create the \"ultimate perfume\"\u2014the scent of a beautiful young virgin. Told with dazzling narrative brilliance, Perfume is a hauntingly powerful tale of murder and sensual depravity.",
        "language": "English",
        "isbn": "9780140120837",
        "genres": 
            ['Fiction',
            'Classics',
            'Historical Fiction',
            'Horror',
            'Mystery',
            'Thriller',
            'Crime',
            'Historical',
            'German Literature',
            'Novels'
        ],
        "pages": 263,
        "awards": 
            ['World Fantasy Award for Best Novel (1987)',
            'PEN Translation Prize for John E. Woods (1987)'
        ],
        "likedPercent": 92.0,
        "price": 2.6
    },
    {
        "id": 38709,
        "title": "Holes",
        "series": "Holes #1",
        "author": "Louis Sachar (Goodreads Author)",
        "description": "Stanley Yelnats is under a curse. A curse that began with his no-good-dirty-rotten-pig-stealing-great-great-grandfather and has since followed generations of Yelnats. Now Stanley has been unjustly sent to a boys\u2019 detention center, Camp Green Lake, where the boys build character by spending all day, every day digging holes exactly five feet wide and five feet deep. There is no lake at Camp Green Lake. But there are an awful lot of holes.It doesn\u2019t take long for Stanley to realize there\u2019s more than character improvement going on at Camp Green Lake. The boys are digging holes because the warden is looking for something. But what could be buried under a dried-up lake? Stanley tries to dig up the truth in this inventive and darkly humorous tale of crime and punishment\u2014and redemption.",
        "language": "English",
        "isbn": "9780439244190",
        "genres": 
            ['Young Adult',
            'Fiction',
            'Childrens',
            'Middle Grade',
            'Realistic Fiction',
            'Classics',
            'Mystery',
            'Adventure',
            'School',
            'Contemporary'
        ],
        "pages": 233,
        "awards": 
            ['Newbery Medal (1999)',
            '\National Book Award for Young Peoples Literature (1998)\',
            '\West Australian Young Readers Book Award (WAYRBA) for Older Readers (2001)\',
            'Grand Canyon Reader Award for Teen Book (2001)',
            'Nene Award (2001)',
            'Maryland Black-Eyed Susan Book Award for Grade 6-9 (2001)',
            '\Massachusetts Childrens Book Award (2001)\',
            '\Flicker Tale Childrens Book Award (2000)\',
            '\Pennsylvania Young Readers Choice Award for Grades 6-8 (2000)\',
            '\Dorothy Canfield Fisher Childrens Book Award (2000)\',
            'Evergreen Teen Book Award (2001)',
            'Soaring Eagle Book Award (2003)',
            'Sunshine State Young Readers Award for Grades 3-5 and Grades 6-8 (2002)',
            '\Pacific Northwest Library Association Young Readers Choice Award for Junior (2001)\',
            'Zilveren Zoen (2000)',
            'Deutscher Jugendliteraturpreis Nominee for Jugendbuch (2001)',
            'Boston Globe-Horn Book Award for Fiction (1999)',
            'New Mexico Land of Enchantment Award for Young Adult (2001)',
            '\William Allen White Childrens Book Award (2001)\',
            'Oklahoma Sequoyah Award for Children and YA (2001)',
            '\Rebecca Caudill Young Readers Book Award (2002)\',
            'Premi Protagonista Jove for Categoria 14-15 anys (2000)'
        ],
        "likedPercent": 93.0,
        "price": 3.1
    },
    {
        "id": 100915,
        "title": "The Lion, the Witch and the Wardrobe",
        "series": "The Chronicles of Narnia (Publication Order) #1",
        "author": "C.S. Lewis",
        "description": "Narnia...the land beyond the wardrobe door, a secret place frozen in eternal winter, a magical country waiting to be set free.Lucy is the first to find the secret of the wardrobe in the professor's mysterious old house. At first her brothers and sister don't believe her when she tells of her visit to the land of Narnia. But soon Edmund, then Peter and Susan step through the wardrobe themselves. In Narnia they find a country buried under the evil enchantment of the White Witch. When they meet the Lion Aslan, they realize they've been called to a great adventure and bravely join the battle to free Narnia from the Witch's sinister spell.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Classics',
            'Fiction',
            'Young Adult',
            'Childrens',
            'Adventure',
            'Middle Grade',
            'Christian',
            'Magic',
            'Christian Fiction'
        ],
        "pages": 206,
        "awards": 
            ['Lewis Carroll Shelf Award (1962)',
            '\The Keith Barker Millennium Childrens Book Awards Childrens Book of the Century\',
            'Retro Hugo Award Nominee for Best Novel (2001)'
        ],
        "likedPercent": 95.0,
        "price": 13.444484118785581
    },
    {
        "id": 472331,
        "title": "Watchmen",
        "series": "Watchmen #1-12",
        "author": "Alan Moore (Goodreads Author), Dave Gibbons (Illustrator/Letterer), John Higgins (Colorist)",
        "description": "This Hugo Award-winning graphic novel chronicles the fall from grace of a group of super-heroes plagued by all-too-human failings. Along the way, the concept of the super-hero is dissected as the heroes are stalked by an unknown assassin.One of the most influential graphic novels of all time and a perennial best-seller, Watchmen has been studied on college campuses across the nation and is considered a gateway title, leading readers to other graphic novels such as V for Vendetta, Batman: The Dark Knight Returns and The Sandman series.",
        "language": "English",
        "isbn": "9780930289232",
        "genres": 
            ['Graphic Novels',
            'Comics',
            'Fiction',
            'Science Fiction',
            'Fantasy',
            'Graphic Novels Comics',
            'Comic Book',
            'Classics',
            'Superheroes',
            'Dystopia'
        ],
        "pages": 416,
        "awards": 
            ['Hugo Award for Other Forms (1988)',
            'Locus Award for Best Non-Fiction/Art (1988)',
            'Harvey Awards for Best Writer (for Alan Moore)',
            'Best Artist or Penciller (for Dave Gibbons)',
            'Best Continuing or Limited Series',
            'Best Single Issue (\Watchmen #9\)',
            'Best Graphic Album',
            'Best Colorist (for John Higgins) & Special Award for Excellence in Production  (1988)',
            '\Prix du Festival dAngoul\u00eame for Alph-art du meilleur album \u00e9tranger (1989)\',
            'Urhunden Prize for Foreign Album (1992)',
            'Will Eisner Comic Industry Awards for Best Archival Collection/Project\u2013Comic Books (in 2006 awards',
            'for Absolute edition)',
            'Best Finite Series',
            'Best Graphic Album',
            'Best Writer (for Alan Moore)',
            'Best Writer/Artist (single or team) (for Alan Moore & Dave Gibbons) (1988)',
            'IGN Award for Best Collection (2005)'
        ],
        "likedPercent": 96.0,
        "price": 4.85
    },
    {
        "id": 830502,
        "title": "It",
        "series": "",
        "author": "Stephen King (Goodreads Author)",
        "description": "Welcome to Derry, Maine ...It\u2019s a small city, a place as hauntingly familiar as your own hometown. Only in Derry the haunting is real ...They were seven teenagers when they first stumbled upon the horror. Now they are grown-up men and women who have gone out into the big world to gain success and happiness. But none of them can withstand the force that has drawn them back to Derry to face the nightmare without an end, and the evil without a name.",
        "language": "English",
        "isbn": "9780450411434",
        "genres": 
            ['Horror',
            'Fiction',
            'Thriller',
            'Fantasy',
            'Audiobook',
            'Mystery',
            'Adult',
            'Paranormal',
            'Classics',
            'Novels'
        ],
        "pages": 1116,
        "awards": 
            ['Locus Award Nominee for Best Fantasy Novel (1987)',
            'World Fantasy Award Nominee for Best Novel (1987)',
            'Colorado Blue Spruce Young Adult Book Award (1994)',
            'British Fantasy Award for Best Novel (1987)'
        ],
        "likedPercent": 94.0,
        "price": 5.71
    },
    {
        "id": 4556058,
        "title": "The Last Olympian",
        "series": "Percy Jackson and the Olympians #5",
        "author": "Rick Riordan (Goodreads Author)",
        "description": "All year the half-bloods have been preparing for battle against the Titans, knowing the odds of victory are grim. Kronos's army is stronger than ever, and with every god and half-blood he recruits, the evil Titan's power only grows.While the Olympians struggle to contain the rampaging monster Typhon, Kronos begins his advance on New York City, where Mount Olympus stands virtually unguarded. Now it's up to Percy Jackson and an army of young demigods to stop the Lord of Time. In this momentous final book in the New York Times best-selling series, the long-awaited prophecy surrounding Percy's sixteenth birthday unfolds. And as the battle for Western civilization rages on the streets of Manhattan, Percy faces a terrifying suspicion that he may be fighting against his own fate.",
        "language": "English",
        "isbn": "9781423101475",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Mythology',
            'Fiction',
            'Middle Grade',
            'Adventure',
            'Childrens',
            'Greek Mythology',
            'Urban Fantasy',
            'Magic'
        ],
        "pages": 381,
        "awards": 
            ['Soaring Eagle Book Award (2010)',
            'Goodreads Choice Award Nominee for Favorite Book & Young Adult Series (2009)',
            'Carnegie Medal Nominee (2010)',
            'Premio El Templo de las Mil Puertas Nominee for Mejor novela extranjera perteneciente a saga (2010)'
        ],
        "likedPercent": 98.0,
        "price": 7.44
    },
    {
        "id": 114345,
        "title": "The Little House Collection",
        "series": "Little House #1-9",
        "author": "Laura Ingalls Wilder, Garth Williams (Illustrator)",
        "description": "This nine-book paperback box set of the classic series features the classic black-and-white artwork from Garth Williams.The nine books in the timeless Little House series tell the story of Laura\u2019s real childhood as an American pioneer, and are cherished by readers of all generations. They offer a unique glimpse into life on the American frontier, and tell the heartwarming, unforgettable story of a loving family.Little House in the Big WoodsMeet the Ingalls family\u2014Laura, Ma, Pa, Mary, and baby Carrie, who all live in a cozy log cabin in the big woods of Wisconsin in the 1870s. Though many of their neighbors are wolves and panthers and bears, the woods feel like home, thanks to Ma\u2019s homemade cheese and butter and the joyful sounds of Pa\u2019s fiddle.Farmer BoyAs Laura Ingalls is growing up in a little house in Kansas, Almanzo Wilder lives on a big farm in New York. He and his brothers and sisters work hard from dawn to supper to help keep their family farm running. Almanzo wishes for just one thing\u2014his very own horse\u2014but he must prove that he is ready for such a big responsibility.Little House on the PrairieWhen Pa decides to sell the log house in the woods, the family packs up and moves from Wisconsin to Kansas, where Pa builds them their little house on the prairie! Living on the farm is different from living in the woods, but Laura and her family are kept busy and are happy with the promise of their new life on the prairie.On the Banks of Plum CreekThe Ingalls family lives in a sod house beside Plum Creek in Minnesota until Pa builds them a new house made of sawed lumber. The money for the lumber will come from their first wheat crop. But then, just before the wheat is ready to harvest, a strange glittering cloud fills the sky, blocking out the sun. Millions of grasshoppers cover the field and everything on the farm, and by the end of a week, there is no wheat crop left.By the Shores of Silver LakePa Ingalls heads west to the unsettled wilderness of the Dakota Territory. When Ma, Mary, Laura, Carrie, and baby Grace join him, they become the first settlers in the town of De Smet. Pa starts work on the first building of the brand new town, located on the shores of Silver Lake. The Long WinterThe first terrible storm comes to the barren prairie in October. Then it snows almost without stopping until April. With snow piled as high as the rooftops, it\u2019s impossible for trains to deliver supplies, and the townspeople, including Laura and her family, are starving. Young Almanzo Wilder, who has settled in the town, risks his life to save the town.Little Town on the PrairieDe Smet is rejuvenated with the beginning of spring. But in addition to the parties, socials, and \u201cliteraries,\u201d work must continue. Laura spends many hours sewing shirts to help Ma and Pa get enough money to send Mary to a college for the blind. But in the evenings, Laura makes time for a new caller, Almanzo Wilder.These Happy Golden YearsLaura must continue to earn money to keep Mary in her college for the blind, so she gets a job as a teacher. It\u2019s not easy, and for the first time she\u2019s living away from home. But it gets a little better every Friday, when Almanzo picks Laura up to take her back home for the weekend. Though Laura is still young, she and Almanzo are officially courting, and she knows that this is a time for new beginnings.The First Four YearsLaura Ingalls and Almanzo Wilder have just been married! They move to a small prairie homestead to start their lives together. But each year brings new challenges\u2014storms, sickness, fire, and unpaid debts. These first four years call for courage, strength, and a great deal of determination. And through it all, Laura and Almanzo still have their love, which only grows when baby Rose arrives.",
        "language": "English",
        "isbn": "9780060529963",
        "genres": 
            ['Classics',
            'Historical Fiction',
            'Childrens',
            'Fiction',
            'Young Adult',
            'Historical',
            'Middle Grade',
            'Juvenile',
            'Literature',
            'Kids'
        ],
        "pages": 2700,
        "awards": 
            [''
        ],
        "likedPercent": 96.0,
        "price": 11.013002132215131
    },
    {
        "id": 6656,
        "title": "The Divine Comedy",
        "series": "La Divina Commedia #1-3",
        "author": "Dante Alighieri, Allen Mandelbaum (Translator), Eugenio Montale (Introduction)",
        "description": "The Divine Comedy describes Dante's descent into Hell with Virgil as a guide; his ascent of Mount Purgatory and encounter with his dead love, Beatrice; and finally, his arrival in Heaven. Examining questions of faith, desire and enlightenment, the poem is a brilliantly nuanced and moving allegory of human redemption. Dante Alighieri was born in Florence in 1265 and belonged to a noble but impoverished family. His life was divided by political duties and poetry, the most of famous of which was inspired by his meeting with Bice Portinari, whom he called Beatrice,including La Vita Nuova and The Divine Comedy. He died in Ravenna in 1321.",
        "language": "English",
        "isbn": "9780679433132",
        "genres": 
            ['Classics',
            'Poetry',
            'Fiction',
            'Literature',
            'Religion',
            'Philosophy',
            'Fantasy',
            'Italian Literature',
            'Italy',
            'Classic Literature'
        ],
        "pages": 798,
        "awards": 
            ['Pr\u00eamio Jabuti for Tradu\u00e7\u00e3o (2000)',
            'Deutsch-Italienischer \u00dcbersetzerpreis (2013)',
            '\u041f\u0440\u0435\u043c\u0456\u044f \u0456\u043c\u0435\u043d\u0456 \u041c\u0430\u043a\u0441\u0438\u043c\u0430 \u0420\u0438\u043b\u044c\u0441\u044c\u043a\u043e\u0433\u043e (1978)'
        ],
        "likedPercent": 93.0,
        "price": 13.66
    },
    {
        "id": 34268,
        "title": "Peter Pan",
        "series": "",
        "author": "J.M. Barrie, Michael Hague (Illustrator)",
        "description": "Peter Pan by J. M. Barrie Peter Pan, the mischievous boy who refuses to grow up, lands in the Darling's proper middle-class home to look for his shadow. He befriends Wendy, John and Michael and teaches them to fly (with a little help from fairy dust). He and Tinker Bell whisk them off to Never-land where they encounter the Red Indians, the Little Lost Boys, pirates and the dastardly Captain Hook.",
        "language": "English",
        "isbn": "9780805072457",
        "genres": 
            ['Classics',
            'Fantasy',
            'Fiction',
            'Childrens',
            'Adventure',
            'Young Adult',
            'Audiobook',
            'Middle Grade',
            'Fairy Tales',
            'Literature'
        ],
        "pages": 176,
        "awards": 
            [''
        ],
        "likedPercent": 93.0,
        "price": 5.26
    },
    {
        "id": 355697,
        "title": "All Quiet on the Western Front",
        "series": "All Quiet on the Western Front/The Road Back #1",
        "author": "Erich Maria Remarque, Arthur Wesley Wheen (Translator)",
        "description": "One by one the boys begin to fall\u2026\r\n\r\nIn 1914 a room full of German schoolboys, fresh-faced and idealistic, are goaded by their schoolmaster to troop off to the \u2018glorious war\u2019. With the fire and patriotism of youth they sign up. What follows is the moving story of a young \u2018unknown soldier\u2019 experiencing the horror and disillusionment of life in the trenches.",
        "language": "English",
        "isbn": "9780449213940",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'War',
            'Historical',
            'Literature',
            'School',
            'German Literature',
            'World War I',
            'Novels'
        ],
        "pages": 296,
        "awards": 
            ['Luisterboek Award Nominee (2015)'
        ],
        "likedPercent": 91.0,
        "price": 2.32
    },
    {
        "id": 5907,
        "title": "The Hobbit, or There and Back Again",
        "series": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "description": "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.Written for J.R.R. Tolkien\u2019s own children, The Hobbit met with instant critical acclaim when it was first published in 1937. Now recognized as a timeless classic, this introduction to the hobbit Bilbo Baggins, the wizard Gandalf, Gollum, and the spectacular world of Middle-earth recounts of the adventures of a reluctant hero, a powerful and dangerous ring, and the cruel dragon Smaug the Magnificent. The text in this 372-page paperback edition is based on that first published in Great Britain by Collins Modern Classics (1998), and includes a note on the text by Douglas A. Anderson (2001).",
        "language": "English",
        "isbn": "9780618260300",
        "genres": 
            ['Fantasy',
            'Classics',
            'Fiction',
            'Adventure',
            'Young Adult',
            'Science Fiction Fantasy',
            'High Fantasy',
            'Childrens',
            'Epic Fantasy',
            'Novels'
        ],
        "pages": 366,
        "awards": 
            ['Keith Barker Millennium Book Award',
            'Books I Loved Best Yearly (BILBY) Awards for Older Readers (1997)',
            'Mythopoeic Scholarship Award for Inklings Studies (1990)'
        ],
        "likedPercent": 95.0,
        "price": 4.68
    },
    {
        "id": 1423,
        "title": "The Compleat Works of Wllm Shkspr (abridged)",
        "series": "",
        "author": "Reduced Shakespeare Company, Adam Long (Contributor), Daniel Singer (Contributor), Jess Winfield (Editor)",
        "description": "Revised from the rather long original complete works of Shakespeare, this abridged version is written by three Americans, with no qualifications worth speaking of. The playtext is reproduced here with footnotes which will be of no help to anyone and a letter from the authors to the Queen.",
        "language": "English",
        "isbn": "9781557831576",
        "genres": 
            ['Plays',
            'Classics',
            'Humor',
            'Fiction',
            'Drama',
            'Theatre',
            'Comedy',
            'Poetry',
            'Literature',
            'Adult'
        ],
        "pages": 137,
        "awards": 
            [''
        ],
        "likedPercent": 96.0,
        "price": 3.17
    },
    {
        "id": 9712,
        "title": "Love in the Time of Cholera",
        "series": "",
        "author": "Gabriel Garc\u00eda M\u00e1rquez, Edith Grossman (Translator)",
        "description": "In their youth, Florentino Ariza and Fermina Daza fall passionately in love. When Fermina eventually chooses to marry a wealthy, well-born doctor, Florentino is heartbroken, but he is a romantic. As he rises in his business career he whiles away the years in 622 affairs\u2014yet he reserves his heart for Fermina. Her husband dies at last, and Florentino purposefully attends the funeral. Fifty years, nine months, and four days after he first declared his love for Fermina, he will do so again.",
        "language": "English",
        "isbn": "9781400034680",
        "genres": 
            ['Fiction',
            'Classics',
            'Historical Fiction',
            'Romance',
            'Magical Realism',
            'Literature',
            'Novels',
            'Spanish Literature',
            'Literary Fiction',
            'Historical'
        ],
        "pages": 348,
        "awards": 
            ['Audie Award',
            'Los Angeles Times Book Prize for Fiction (1988)'
        ],
        "likedPercent": 90.0,
        "price": 3.36
    },
    {
        "id": 2802316,
        "title": "Shadow Kiss",
        "series": "Vampire Academy #3",
        "author": "Richelle Mead (Goodreads Author)",
        "description": "WHAT IF FOLLOWING HER HEART MEANS ROSE COULD LOSE HER BEST FRIEND FOREVER?Lissa Dragomir is a Moroi princess: a mortal vampire with a rare gift for harnessing the earth's magic. She must be protected at all times from Strigoi; the fiercest vampires - the ones who never die. The powerful blend of human and vampire blood that flows through Rose Hathaway, Lissa's best friend, makes her a Dhampir. Rose is dedicated to a dangerous life of protecting Lissa from the Strigoi, who are hell-bent on making Lissa one of them.Rose knows it is forbidden to love another guardian. Her best friend, Lissa - the last Dragomir princess - must always come first. Unfortunately, when it comes to gorgeous Dimitri Belikov, some rules are meant to be broken...Then a strange darkness begins to grow in Rose's mind, and ghostly shadows warn of a terrible evil drawing nearer to the Academy's iron gates. The immortal undead are closing in, and they want vengeance for the lives Rose has stolen. In a heart-stopping battle to rival her worst nightmares, Rose will have to choose between life, love, and the two people who matter most... but will her choice mean that only one can survive?",
        "language": "English",
        "isbn": "9781595141972",
        "genres": 
            ['Young Adult',
            'Vampires',
            'Fantasy',
            'Paranormal',
            'Romance',
            'Urban Fantasy',
            'Paranormal Romance',
            'Supernatural',
            'Fiction',
            'Magic'
        ],
        "pages": 443,
        "awards": 
            ['Premio El Templo de las Mil Puertas Nominee for Mejor novela extranjera perteneciente a saga (2011)'
        "
        ],
        "likedPercent": 96.0,
        "price": 2.76
    },
    {
        "id": 11735983,
        "title": "Insurgent",
        "series": "Divergent #2",
        "author": "Veronica Roth (Goodreads Author)",
        "description": "One choice can transform you\u2014or it can destroy you. But every choice has consequences, and as unrest surges in the factions all around her, Tris Prior must continue trying to save those she loves\u2014and herself\u2014while grappling with haunting questions of grief and forgiveness, identity and loyalty, politics and love.Tris's initiation day should have been marked by celebration and victory with her chosen faction; instead, the day ended with unspeakable horrors. War now looms as conflict between the factions and their ideologies grows. And in times of war, sides must be chosen, secrets will emerge, and choices will become even more irrevocable\u2014and even more powerful. Transformed by her own decisions but also by haunting grief and guilt, radical new discoveries, and shifting relationships, Tris must fully embrace her Divergence, even if she does not know what she may lose by doing so.New York Times bestselling author Veronica Roth's much-anticipated second book of the dystopian DIVERGENT series is another intoxicating thrill ride of a story, rich with hallmark twists, heartbreaks, romance, and powerful insights about human nature.",
        "language": "English",
        "isbn": "9780007442911",
        "genres": 
            ['Young Adult',
            'Dystopia',
            'Fiction',
            'Fantasy',
            'Science Fiction',
            'Romance',
            'Adventure',
            'Teen',
            'Post Apocalyptic',
            'Action'
        ],
        "pages": 525,
        "awards": 
            ['\Romantic Times Reviewers Choice Award (RT Award) for Young Adult Protagonist (2011)\',
            'Goodreads Choice Award for Young Adult Fantasy and Goodreads Author (2012)'
        ],
        "likedPercent": 93.0,
        "price": 7.16926012017656
    },
    {
        "id": 3412,
        "title": "The Thorn Birds",
        "series": "",
        "author": "Colleen McCullough",
        "description": "Alternate Cover Edition ISBN 0380018179 (ISBN13: 9780380018178)The Thorn Birds is a robust, romantic saga of a singular family, the Clearys. It begins in the early part of this century, when Paddy Cleary moves his wife, Fiona, and their seven children to Drogheda, the vast Australian sheep station owned by his autocratic and childless older sister; and it ends more than half a century later, when the only survivor of the third generation, the brilliant actress Justine O'Neill, sets a course of life and love halfway around the world from her roots.The central figures in this enthralling story are the indomitable Meggie, the only Cleary daughter, and the one man she truly loves, the stunningly handsome and ambitious priest Ralph de Bricassart. Ralph's course moves him a long way indeed, from a remote Outback parish to the halls of the Vatican; and Meggie's except for a brief and miserable marriage elsewhere, is fixed to the Drogheda that is part of her bones - but distance does not dim their feelings though it shapes their lives.Wonderful characters people this book; strong and gentle, Paddy, hiding a private memory; dutiful Fiona, holding back love because it once betrayed her, violent, tormented Frank, and the other hardworking Cleary sons who give the boundless lands of Drogheda the energy and devotion most men save for women; Meggie; Ralph; and Meggie's children, Justine and Dane. And the land itself; stark, relentless in its demands, brilliant in its flowering, prey to gigantic cycles of drought and flood, rich when nature is bountiful, surreal like no other place on earth.(First Edition Jacket)",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Romance',
            'Classics',
            'Australia',
            'Historical',
            'Historical Romance',
            'Novels',
            'Drama',
            'Adult'
        ],
        "pages": 692,
        "awards": 
            [''
        ],
        "likedPercent": 95.0,
        "price": 15.844000238443462
    },
    {
        "id": 35545737,
        "title": "A Walk to Remember",
        "series": "",
        "author": "Nicholas Sparks (Goodreads Author)",
        "description": "There was a time when the world was sweeter...when the women in Beaufort, North Carolina, wore dresses, and the men donned hats...when something happened to a seventeen-year-old boy that would change his life forever. Every April, when the wind blows in from the sea and mingles with the scent of lilacs, Landon Carter remembers his last year at Beaufort High. It was 1958, and Landon had already dated a girl or two. He even swore that he had once been in love. Certainly the last person in town he thought he'd fall for was Jamie Sullivan, the daughter of the town's Baptist minister. A quiet girl who always carried a Bible with her schoolbooks, Jamie seemed content living in a world apart from the other teens. She took care of her widowed father, rescued hurt animals, and helped out at the local orphanage. No boy had ever asked her out. Landon would never have dreamed of it. Then a twist of fate made Jamie his partner for the homecoming dance, and Landon Carter's life would never be the same. Being with Jamie would show him the depths of the human heart and lead him to a decision so stunning it would send him irrevocably on the road to manhood. No other author today touches our emotions more deeply than Nicholas Sparks.Illuminating both the strength and the gossamer fragility of our deepest emotions, his two New York Times bestsellers, The Notebook and Message in a Bottle, have established him as the leading author of today's most cherished love stories. Now, in A Walk to Remember, he tells a truly unforgettable story, one that glimmers with all of his magic, holding us spellbound-and reminding us that in life each of us may find one great love, the kind that changes everything...",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Romance',
            'Fiction',
            'Chick Lit',
            'Contemporary',
            'Young Adult',
            'Adult',
            'Adult Fiction',
            'Drama',
            'Contemporary Romance',
            'Love'
        ],
        "pages": 215,
        "awards": 
            ['Iowa High School Book Award (2004)'
        ],
        "likedPercent": 94.0,
        "price": 10.494822155061065
    },
    {
        "id": 113946,
        "title": "How the Grinch Stole Christmas!",
        "series": "",
        "author": "Dr. Seuss",
        "description": "\"The Grinch hated Christmas! The whole Christmas season!Now, please don't ask why. No one quite knows the reason.\"Dr. Seuss's small-hearted Grinch ranks right up there with Scrooge when it comes to the crankiest, scowling holiday grumps of all time. For 53 years, the Grinch has lived in a cave on the side of a mountain, looming above the Whos in Whoville. The noisy holiday preparations and infernal singing of the happy little citizens below annoy him to no end. The Grinch decides this frivolous merriment must stop. His \"wonderful, awful\" idea is to don a Santa outfit, strap heavy antlers on his poor, quivering dog Max, construct a makeshift sleigh, head down to Whoville, and strip the chafingly cheerful Whos of their Yuletide glee once and for all.Looking quite out of place and very disturbing in his makeshift Santa get-up, the Grinch slithers down chimneys with empty bags and stealing the Whos' presents, their food, even the logs from their humble Who-fires. He takes the ramshackle sleigh to Mt. Crumpit to dump it and waits to hear the sobs of the Whos when they wake up and discover the trappings of Christmas have disappeared. Imagine the Whos' dismay when they discover the evil-doings of Grinch in his anti-Santa guise. But what is that sound? It's not sobbing, but singing! Children simultaneously adore and fear this triumphant, twisted Seussian testimonial to the undaunted cheerfulness of the Whos, the transcendent nature of joy, and of course, the growth potential of a heart that's two sizes too small. This holiday classic is perfect for reading aloud to your favorite little Whos.",
        "language": "English",
        "isbn": "9780007173044",
        "genres": 
            ['Childrens',
            'Picture Books',
            'Christmas',
            'Classics',
            'Fiction',
            'Poetry',
            'Holiday',
            'Fantasy',
            'Humor',
            'Kids'
        ],
        "pages": 64,
        "awards": 
            [''
        ],
        "likedPercent": 95.0,
        "price": 15.223896369876218
    },
    {
        "id": 13,
        "title": "The Ultimate Hitchhiker's Guide to the Galaxy",
        "series": "The Hitchhiker's Guide to the Galaxy #0.5-5",
        "author": "Douglas Adams",
        "description": "At last in paperback in one complete volume, here are the five novels from Douglas Adams's Hitchhiker series. \"The Hitchhiker's Guide to the Galaxy\"Seconds before the Earth is demolished for a galactic freeway, Arthur Dent is saved by Ford Prefect, a researcher for the revised Guide. Together they stick out their thumbs to the stars and begin a wild journey through time and space.\"The Restaurant at the End of the Universe\"Facing annihilation at the hands of warmongers is a curious time to crave tea. It could only happen to the cosmically displaced Arthur Dent and his comrades as they hurtle across the galaxy in a desperate search for a place to eat.\"Life, the Universe and Everything\"The unhappy inhabitants of planet Krikkit are sick of looking at the night sky- so they plan to destroy it. The universe, that is. Now only five individuals can avert Armageddon: mild-mannered Arthur Dent and his stalwart crew.\"So Long, and Thanks for All the Fish\"Back on Earth, Arthur Dent is ready to believe that the past eight years were all just a figment of his stressed-out imagination. But a gift-wrapped fishbowl with a cryptic inscription conspires to thrust him back to reality. So to speak.\"Mostly Harmless\"Just when Arthur Dent makes the terrible mistake of starting to enjoy life, all hell breaks loose. Can he save the Earth from total obliteration? Can he save the Guide from a hostile alien takeover? Can he save his daughter from herself?Also includes the short story \"Young Zaphod Plays It Safe\".",
        "language": "English",
        "isbn": "9780345453747",
        "genres": 
            ['Science Fiction',
            'Fiction',
            'Humor',
            'Fantasy',
            'Classics',
            'Comedy',
            'Science Fiction Fantasy',
            'Adventure',
            'Novels',
            'British Literature'
        ],
        "pages": 815,
        "awards": 
            [''
        ],
        "likedPercent": 96.0,
        "price": 2.76
    },
    {
        "id": 6867,
        "title": "Atonement",
        "series": "",
        "author": "Ian McEwan",
        "description": "Ian McEwan\u2019s symphonic novel of love and war, childhood and class, guilt and forgiveness provides all the satisfaction of a brilliant narrative and the provocation we have come to expect from this master of English prose.On a hot summer day in 1935, thirteen-year-old Briony Tallis witnesses the flirtation between her older sister, Cecilia, and Robbie Turner, the son of a servant. But Briony\u2019s incomplete grasp of adult motives and her precocious imagination bring about a crime that will change all their lives, a crime whose repercussions Atonement follows through the chaos and carnage of World War II and into the close of the twentieth century.",
        "language": "English",
        "isbn": "9780385721790",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Romance',
            'Classics',
            'Historical',
            'War',
            'Literary Fiction',
            'Contemporary',
            'Literature',
            'Novels'
        ],
        "pages": 351,
        "awards": 
            ['Booker Prize Nominee (2001)',
            'James Tait Black Memorial Prize Nominee for Fiction (2001)',
            'Whitbread Award Nominee for Novel (2001)',
            'WH Smith Literary Award (2002)',
            'Los Angeles Times Book Prize for Fiction (2002)',
            'Exclusive Books Boeke Prize (2002)',
            'National Book Critics Circle Award for Fiction (2002)',
            '\Commonwealth Writers Prize for Best Book in South Asia and Europe (2002)\',
            'Deutscher B\u00fccherpreis for Internationale Belletristik (2003)',
            'Premi Llibreter de narrativa Nominee (2003)',
            'International Dublin Literary Award Nominee (2003)'
        ],
        "likedPercent": 90.0,
        "price": 2.86
    },
    {
        "id": 92303,
        "title": "The Importance of Being Earnest",
        "series": "",
        "author": "Oscar Wilde",
        "description": "Oscar Wilde's madcap farce about mistaken identities, secret engagements, and lovers entanglements still delights readers more than a century after its 1895 publication and premiere performance. The rapid-fire wit and eccentric characters of The Importance of Being Earnest have made it a mainstay of the high school curriculum for decades.Cecily Cardew and Gwendolen Fairfax are both in love with the same mythical suitor. Jack Worthing has wooed Gwendolen as Ernest while Algernon has also posed as Ernest to win the heart of Jack's ward, Cecily. When all four arrive at Jack's country home on the same weekend the \"rivals\" to fight for Ernest's undivided attention and the \"Ernests\" to claim their beloveds pandemonium breaks loose. Only a senile nursemaid and an old, discarded hand-bag can save the day!This Prestwick House Literary Touchstone Edition includes a glossary and reader's notes to help the modern reader appreciate Wilde's wry wit and elaborate plot twists.",
        "language": "English",
        "isbn": "9781580495806",
        "genres": 
            ['Classics',
            'Plays',
            'Fiction',
            'Drama',
            'Humor',
            'Literature',
            'School',
            'Comedy',
            'Theatre',
            'Romance'
        ],
        "pages": 76,
        "awards": 
            [''
        ],
        "likedPercent": 96.0,
        "price": 5.26
    },
    {
        "id": 19501,
        "title": "Eat, Pray, Love",
        "series": "",
        "author": "Elizabeth Gilbert (Goodreads Author)",
        "description": "A celebrated writer's irresistible, candid, and eloquent account of her pursuit of worldly pleasure, spiritual devotion, and what she really wanted out of life. Around the time Elizabeth Gilbert turned thirty, she went through an early-onslaught midlife crisis. She had everything an educated, ambitious American woman was supposed to want\u2014a husband, a house, a successful career. But instead of feeling happy and fulfilled, she was consumed with panic, grief, and confusion. She went through a divorce, a crushing depression, another failed love, and the eradication of everything she ever thought she was supposed to be. To recover from all this, Gilbert took a radical step. In order to give herself the time and space to find out who she really was and what she really wanted, she got rid of her belongings, quit her job, and undertook a yearlong journey around the world\u2014all alone. Eat, Pray, Love is the absorbing chronicle of that year. Her aim was to visit three places where she could examine one aspect of her own nature set against the backdrop of a culture that has traditionally done that one thing very well. In Rome, she studied the art of pleasure, learning to speak Italian and gaining the twenty-three happiest pounds of her life. India was for the art of devotion, and with the help of a native guru and a surprisingly wise cowboy from Texas, she embarked on four uninterrupted months of spiritual exploration. In Bali, she studied the art of balance between worldly enjoyment and divine transcendence. She became the pupil of an elderly medicine man and also fell in love the best way\u2014unexpectedly. An intensely articulate and moving memoir of self-discovery, Eat, Pray, Love is about what can happen when you claim responsibility for your own contentment and stop trying to live in imitation of society\u2019s ideals. It is certain to touch anyone who has ever woken up to the unrelenting need for change.",
        "language": "English",
        "isbn": "9780143038412",
        "genres": 
            ['Nonfiction',
            'Memoir',
            'Travel',
            'Biography',
            'Chick Lit',
            'Romance',
            'Spirituality',
            'Contemporary',
            'Biography Memoir',
            'Autobiography'
        ],
        "pages": 368,
        "awards": 
            ['Puddly Award for Nonfiction (2008)'
        ],
        "likedPercent": 81.0,
        "price": 2.86
    },
    {
        "id": 37415,
        "title": "Their Eyes Were Watching God",
        "series": "",
        "author": "Zora Neale Hurston",
        "description": "Fair and long-legged, independent and articulate, Janie Crawford sets out to be her own person -- no mean feat for a black woman in the '30s. Janie's quest for identity takes her through three marriages and into a journey back to her roots.",
        "language": "English",
        "isbn": "9780061120060",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'School',
            'African American',
            'Literature',
            'Novels',
            'Feminism',
            'Read For School',
            'High School'
        ],
        "pages": 219,
        "awards": 
            ['Audie Award for Solo Narration - Female (2001)'
        ],
        "likedPercent": 91.0,
        "price": 14.2
    },
    {
        "id": 7190,
        "title": "The Three Musketeers",
        "series": "The d'Artagnan Romances #1",
        "author": "Alexandre Dumas",
        "description": "Alexandre Dumas\u2019s most famous tale\u2014 and possibly the most famous historical novel of all time\u2014 in a handsome hardcover volume.This swashbuckling epic of chivalry, honor, and derring-do, set in France during the 1620s, is richly populated with romantic heroes, unattainable heroines, kings, queens, cavaliers, and criminals in a whirl of adventure, espionage, conspiracy, murder, vengeance, love, scandal, and suspense. Dumas transforms minor historical figures into larger- than-life characters: the Comte d\u2019Artagnan, an impetuous young man in pursuit of glory; the beguilingly evil seductress \u201cMilady\u201d; the powerful and devious Cardinal Richelieu; the weak King Louis XIII and his unhappy queen\u2014and, of course, the three musketeers themselves, Athos, Porthos, and Aramis, whose motto \u201call for one, one for all\u201d has come to epitomize devoted friendship. With a plot that delivers stolen diamonds, masked balls, purloined letters, and, of course, great bouts of swordplay, The Three Musketeers is eternally entertaining.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'Adventure',
            'France',
            'Literature',
            'Historical',
            'French Literature',
            'Classic Literature',
            'Novels'
        ],
        "pages": 625,
        "awards": 
            [''
        ],
        "likedPercent": 95.0,
        "price": 14.0411979119477
    },
    {
        "id": 236093,
        "title": "The Wonderful Wizard of Oz",
        "series": "Oz #1",
        "author": "L. Frank Baum, W.W. Denslow (Illustrator)",
        "description": "When Dorothy and her little dog Toto are caught in a tornado, they and their Kansas farmhouse are suddenly transported to Oz, where Munchkins live, monkeys fly and Wicked Witches rule. Desperate to return home, and with the Wicked Witch of the West on their trail, Dorothy and Toto - together with new friends the Tin Woodsman, Scarecrow and cowardly Lion - embark on a fantastic quest along the Yellow Brick Road in search of the Emerald City. There they hope to meet the legendary, all-powerful Wizard of Oz, who alone may hold the power to grant their every wish.Just as captivating as it was a hundred years ago, this is a story that all ages will love.",
        "language": "English",
        "isbn": "9780140621679",
        "genres": 
            ['Classics',
            'Fantasy',
            'Fiction',
            'Childrens',
            'Young Adult',
            'Adventure',
            'Audiobook',
            'Middle Grade',
            'Magic',
            'Literature'
        ],
        "pages": 154,
        "awards": 
            ['Lewis Carroll Shelf Award (1968)'
        ],
        "likedPercent": 93.0,
        "price": 1.45
    },
    {
        "id": 2282133,
        "title": "Frostbite",
        "series": "Vampire Academy #2",
        "author": "Richelle Mead (Goodreads Author)",
        "description": "WHEN LOVE AND JEALOUSY COLLIDE ON THE SLOPES, WINTER BREAK TURNS DEADLY...Lissa Dragomir is a Moroi princess: a mortal vampire with a rare gift for harnessing the earth's magic. She must be protected at all times from Strigoi; the fiercest vampires - the ones who never die. The powerful blend of human and vampire blood that flows through Rose Hathaway, Lissa's best friend, makes her a Dhampir. Rose is dedicated to a dangerous life of protecting Lissa from the Strigoi, who are hell-bent on making Lissa one of them.Rose has serious guy trouble. Her gorgeous tutor, Dimitri, has his eye on someone else, her friend Mason has a huge crush on her, and she keeps getting stuck in her best friend Lissa's head while she's making out with her boyfriend, Christian.Then a nearby Strigoi attack puts St. Vladimir's on high alert, and the Academy whisks its students away on a mandatory holiday ski trip. But the glittering winter landscape and posh Idaho resort only provide the illusion of safety. When three students run away to strike back again the deadly Strigoi, Rose must join forces with Christian to rescue them. Only this time, Rose - and her heart - are in more danger than she ever could have imagined...",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Young Adult',
            'Vampires',
            'Fantasy',
            'Paranormal',
            'Romance',
            'Urban Fantasy',
            'Paranormal Romance',
            'Supernatural',
            'Fiction',
            'Magic'
        ],
        "pages": 327,
        "awards": 
            [''
        ],
        "likedPercent": 96.0,
        "price": 17.75931525966488
    },
    {
        "id": 32929,
        "title": "Goodnight Moon",
        "series": "Over the Moon #2",
        "author": "Margaret Wise Brown, Clement Hurd (Illustrator)",
        "description": "In a great green room, tucked away in bed, is a little bunny. \"Goodnight room, goodnight moon.\" And to all the familiar things in the softly lit room -- to the picture of the three little bears sitting on chairs, to the clocks and his socks, to the mittens and the kittens, to everything one by one -- the little bunny says goodnight.In this classic of children's literature, beloved by generations of readers and listeners, the quiet poetry of the words and the gentle, lulling illustrations combine to make a perfect book for the end of the day.",
        "language": "English",
        "isbn": "9780060775858",
        "genres": 
            ['Childrens',
            'Picture Books',
            'Classics',
            'Fiction',
            'Poetry',
            'Kids',
            'Animals',
            'Juvenile',
            'Young Adult',
            'Storytime'
        ],
        "pages": 32,
        "awards": 
            [''
        ],
        "likedPercent": 94.0,
        "price": 5.69
    },
    {
        "id": 7784,
        "title": "The Lorax",
        "series": "",
        "author": "Dr. Seuss",
        "description": "\"UNLESS someone like you...cares a whole awful lot...nothing is going to get better...It's not.\" Long before saving the earth became a global concern, Dr. Seuss, speaking through his character the Lorax, warned against mindless progress and the danger it posed to the earth's natural beauty. His classic cautionary tale is now available in an irresistible mini-edition, perfect for backpack or briefcase, for Arbor Day, Earth Day, and every day.",
        "language": "English",
        "isbn": "9780679889106",
        "genres": 
            ['Childrens',
            'Picture Books',
            'Fiction',
            'Classics',
            'Poetry',
            'Fantasy',
            'Environment',
            'Young Adult',
            'Kids',
            'Juvenile'
        ],
        "pages": 72,
        "awards": 
            ['California Young Readers Medal Nominee for Primary (1976)',
            'Green Prize for Sustainable Literature'
        ],
        "likedPercent": 95.0,
        "price": 41.26
    },
    {
        "id": 12067,
        "title": "Good Omens: The Nice and Accurate Prophecies of Agnes Nutter, Witch",
        "series": "",
        "author": "Terry Pratchett, Neil Gaiman (Goodreads Author)",
        "description": "\u2018Armageddon only happens once, you know. They don\u2019t let you go around again until you get it right.\u2019People have been predicting the end of the world almost from its very beginning, so it\u2019s only natural to be sceptical when a new date is set for Judgement Day. But what if, for once, the predictions are right, and the apocalypse really is due to arrive next Saturday, just after tea?You could spend the time left drowning your sorrows, giving away all your possessions in preparation for the rapture, or laughing it off as (hopefully) just another hoax. Or you could just try to do something about it.It\u2019s a predicament that Aziraphale, a somewhat fussy angel, and Crowley, a fast-living demon now finds themselves in. They\u2019ve been living amongst Earth\u2019s mortals since The Beginning and, truth be told, have grown rather fond of the lifestyle and, in all honesty, are not actually looking forward to the coming Apocalypse.And then there\u2019s the small matter that someone appears to have misplaced the Antichrist\u2026",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Humor',
            'Urban Fantasy',
            'Comedy',
            'Audiobook',
            'Science Fiction Fantasy',
            'Adult',
            'Science Fiction',
            'Supernatural'
        ],
        "pages": 491,
        "awards": 
            ['Locus Award Nominee for Best Fantasy Novel (1991)',
            'World Fantasy Award Nominee for Best Novel (1991)'
        ],
        "likedPercent": 95.0,
        "price": 2.575574479806435
    },
    {
        "id": 5996153,
        "title": "Blood Promise",
        "series": "Vampire Academy #4",
        "author": "Richelle Mead (Goodreads Author)",
        "description": "Bound by love, but sworn to kill...The world thought Dimitri was dead. And to a certain extent, he was. But I hadn't been able to forget a conversation he and I had once had. We'd both agreed that we'd rather be dead - truly dead - than walk the world as Strigoi. It was time to honor our words.Guardian Rose Hathaway's life will never be the same. The recent attack on St. Vladimir's Academy devastated the entire Moroi world. Many are dead. And, for the few victims carried off by Strigoi, their fates are even worse. A rare tattoo now adorns Rose's neck; a mark that says she's killed far too many Strigoi to count.But only one victim matters... Dimitri Belikov. Rose must now choose one of two very different paths: honoring her life's vow to protect Lissa\u2014her best friend and the last surviving Dragomir princess\u2014or, dropping out of the Academy to strike out on her own and hunt down the man she loves. She'll have to go to the ends of the earth to find Dimitri and keep the promise he begged her to make. But the question is, when the time comes, will he want to be saved?Now, with everything at stake\u2014and worlds away from St. Vladimir's and her unguarded, vulnerable, and newly rebellious best friend\u2014can Rose find the strength to destroy Dimitri? Or, will she sacrifice herself for a chance at eternal love?Readers who fell in love with Rose, Lissa, and Dimitri won't want to miss Blood Promise, the much-anticipated, epic fourth novel in Richelle Mead's enthralling Vampire Academy series.",
        "language": "English",
        "isbn": "9781595141989",
        "genres": 
            ['Young Adult',
            'Vampires',
            'Fantasy',
            'Paranormal',
            'Romance',
            'Urban Fantasy',
            'Paranormal Romance',
            'Supernatural',
            'Fiction',
            'Magic'
        ],
        "pages": 503,
        "awards": 
            ['\Childrens Choice Book Award Nominee for Teen Choice Book of the Year (2010)\',
            'Goodreads Choice Award Nominee for Young Adult Series (2009)'
        ],
        "likedPercent": 96.0,
        "price": 3.73
    },
    {
        "id": 32261,
        "title": "Tess of the D'Urbervilles",
        "series": "",
        "author": "Thomas Hardy, Margaret R. Higonnet (Introduction), Maria Grazia Griffini (Translator), Tim Dolin (Notes)",
        "description": "Alternate cover edition of ISBN 9780141439594.When Tess Durbeyfield is driven by family poverty to claim kinship with the wealthy D'Urbervilles and seek a portion of their family fortune, meeting her 'cousin' Alec proves to be her downfall. A very different man, Angel Clare, seems to offer her love and salvation, but Tess must choose whether to reveal her past or remain silent in the hope of a peaceful future.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Romance',
            'Literature',
            'Historical Fiction',
            '19th Century',
            'Victorian',
            'Classic Literature',
            'Novels',
            'British Literature'
        ],
        "pages": 518,
        "awards": 
            [''
        ],
        "likedPercent": 88.0,
        "price": 2.8857671640702645
    },
    {
        "id": 1078,
        "title": "The Good Earth",
        "series": "House of Earth #1",
        "author": "Pearl S. Buck",
        "description": "This tells the poignant tale of a Chinese farmer and his family in old agrarian China. The humble Wang Lung glories in the soil he works, nurturing the land as it nurtures him and his family. Nearby, the nobles of the House of Hwang consider themselves above the land and its workers; but they will soon meet their own downfall.Hard times come upon Wang Lung and his family when flood and drought force them to seek work in the city. The working people riot, breaking into the homes of the rich and forcing them to flee. When Wang Lung shows mercy to one noble and is rewarded, he begins to rise in the world, even as the House of Hwang falls.",
        "language": "English",
        "isbn": "9781416500186",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'China',
            'Literature',
            'Historical',
            'Asia',
            'Novels',
            'School',
            'Classic Literature'
        ],
        "pages": 418,
        "awards": 
            ['Pulitzer Prize for Novel (1932)',
            'William Dean Howells Medal (1935)'
        ],
        "likedPercent": 92.0,
        "price": 5.27
    },
    {
        "id": 4900,
        "title": "Heart of Darkness",
        "series": "",
        "author": "Joseph Conrad, An\u00edbal Fernandes (Translator)",
        "description": "Heart of Darkness, a novel by Joseph Conrad, was originally a three-part series in Blackwood's Magazine in 1899. It is a story within a story, following a character named Charlie Marlow, who recounts his adventure to a group of men onboard an anchored ship. The story told is of his early life as a ferry boat captain. Although his job was to transport ivory downriver, Charlie develops an interest in investing an ivory procurement agent, Kurtz, who is employed by the government. Preceded by his reputation as a brilliant emissary of progress, Kurtz has now established himself as a god among the natives in \u201cone of the darkest places on earth.\u201d Marlow suspects something else of Kurtz: he has gone mad.A reflection on corruptive European colonialism and a journey into the nightmare psyche of one of the corrupted, Heart of Darkness is considered one of the most influential works ever written.",
        "language": "English",
        "isbn": "9781892295491",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Africa',
            'Historical Fiction',
            'School',
            'Novels',
            'Read For School',
            'Adventure',
            'High School'
        ],
        "pages": 188,
        "awards": 
            [''
        ],
        "likedPercent": 78.0,
        "price": 7.19
    },
    {
        "id": 2120932,
        "title": "The Battle of the Labyrinth",
        "series": "Percy Jackson and the Olympians #4",
        "author": "Rick Riordan (Goodreads Author)",
        "description": "Percy Jackson isn't expecting freshman orientation to be any fun. But when a mysterious mortal acquaintance appears at his potential new school, followed by demon cheerleaders, things quickly move from bad to worse.In this fourth installment of the blockbuster series, time is running out as war between the Olympians and the evil Titan lord Kronos draws near. Even the safe haven of Camp Half-Blood grows more vulnerable by the minute as Kronos's army prepares to invade its once impenetrable borders. To stop the invasion, Percy and his demigod friends must set out on a quest through the Labyrinth - a sprawling underground world with stunning surprises at every turn.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Mythology',
            'Fiction',
            'Middle Grade',
            'Adventure',
            'Childrens',
            'Greek Mythology',
            'Urban Fantasy',
            'Magic'
        ],
        "pages": 361,
        "awards": 
            [''
        ],
        "likedPercent": 98.0,
        "price": 7.141149560035879
    },
    {
        "id": 1622,
        "title": "A Midsummer Night's Dream",
        "series": "",
        "author": "William Shakespeare, Paul Werstine (Editor), Barbara A. Mowat (Editor), Catherine Belsey (Contributor)",
        "description": "Shakespeare's intertwined love polygons begin to get complicated from the start--Demetrius and Lysander both want Hermia but she only has eyes for Lysander. Bad news is, Hermia's father wants Demetrius for a son-in-law. On the outside is Helena, whose unreturned love burns hot for Demetrius. Hermia and Lysander plan to flee from the city under cover of darkness but are pursued by an enraged Demetrius (who is himself pursued by an enraptured Helena). In the forest, unbeknownst to the mortals, Oberon and Titania (King and Queen of the faeries) are having a spat over a servant boy. The plot twists up when Oberon's head mischief-maker, Puck, runs loose with a flower which causes people to fall in love with the first thing they see upon waking. Throw in a group of labourers preparing a play for the Duke's wedding (one of whom is given a donkey's head and Titania for a lover by Puck) and the complications become fantastically funny.",
        "language": "English",
        "isbn": "9780743477543",
        "genres": 
            ['Classics',
            'Plays',
            'Fiction',
            'Drama',
            'Fantasy',
            'School',
            'Romance',
            'Literature',
            'Theatre',
            'Poetry'
        ],
        "pages": 240,
        "awards": 
            [''
        ],
        "likedPercent": 93.0,
        "price": 3.0
    },
    {
        "id": 18335634,
        "title": "Clockwork Princess",
        "series": "The Infernal Devices #3",
        "author": "Cassandra Clare (Goodreads Author)",
        "description": "Danger and betrayal, love and loss, secrets and enchantment are woven together in the breathtaking finale to the #1 New York Times bestselling Infernal Devices Trilogy, prequel to the internationally bestselling Mortal Instruments series.THE INFERNAL DEVICES WILL NEVER STOP COMINGA net of shadows begins to tighten around the Shadowhunters of the London Institute. Mortmain plans to use his Infernal Devices, an army of pitiless automatons, to destroy the Shadowhunters. He needs only one last item to complete his plan: he needs Tessa Gray.Charlotte Branwell, head of the London Institute, is desperate to find Mortmain before he strikes. But when Mortmain abducts Tessa, the boys who lay equal claim to her heart, Jem and Will, will do anything to save her. For though Tessa and Jem are now engaged, Will is as much in love with her as ever.As those who love Tessa rally to rescue her from Mortmain\u2019s clutches, Tessa realizes that the only person who can save her is herself. But can a single girl, even one who can command the power of angels, face down an entire army?Danger and betrayal, secrets and enchantment, and the tangled threads of love and loss intertwine as the Shadowhunters are pushed to the very brink of destruction in the breathtaking conclusion to the Infernal Devices trilogy.",
        "language": "English",
        "isbn": "9781406321340",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Romance',
            'Paranormal',
            'Steampunk',
            'Historical Fiction',
            'Urban Fantasy',
            'Angels',
            'Fiction',
            'Historical'
        ],
        "pages": 567,
        "awards": 
            ['Goodreads Choice Award Nominee for Young Adult Fantasy & Science Fiction (2013)'
        ],
        "likedPercent": 97.0,
        "price": 4.0
    },
    {
        "id": 2547,
        "title": "The Prophet",
        "series": "",
        "author": "Kahlil Gibran",
        "description": "Kahlil Gibran\u2019s masterpiece, The Prophet, is one of the most beloved classics of our time. Published in 1923, it has been translated into more than twenty languages, and the American editions alone have sold more than nine million copies.The Prophet is a collection of poetic essays that are philosophical, spiritual, and, above all, inspirational. Gibran\u2019s musings are divided into twenty-eight chapters covering such sprawling topics as love, marriage, children, giving, eating and drinking, work, joy and sorrow, housing, clothes, buying and selling, crime and punishment, laws, freedom, reason and passion, pain, self-knowledge, teaching, friendship, talking, time, good and evil, prayer, pleasure, beauty, religion, and death.",
        "language": "English",
        "isbn": "9780001000391",
        "genres": 
            ['Poetry',
            'Philosophy',
            'Classics',
            'Fiction',
            'Spirituality',
            'Religion',
            'Literature',
            'Inspirational',
            'Self Help',
            'Novels'
        ],
        "pages": 127,
        "awards": 
            [''
        ],
        "likedPercent": 94.0,
        "price": 5.8
    },
    {
        "id": 40605251,
        "title": "The Mists of Avalon",
        "series": "Avalon #1",
        "author": "Marion Zimmer Bradley",
        "description": "Here is the magical legend of King Arthur, vividly retold through the eyes and lives of the women who wielded power from behind the throne. A spellbinding novel, an extraordinary literary achievement, THE MISTS OF AVALON will stay with you for a long time to come....",
        "language": "English",
        "isbn": "B000FC1JCQ",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Historical Fiction',
            'Arthurian',
            'Mythology',
            'Science Fiction Fantasy',
            'Historical',
            'Classics',
            'Romance',
            'Magic'
        ],
        "pages": 1009,
        "awards": 
            ['Locus Award for Best Fantasy Novel (1984)'
        ],
        "likedPercent": 93.0,
        "price": 6.259513883088901
    },
    {
        "id": 561456,
        "title": "The Titan's Curse",
        "series": "Percy Jackson and the Olympians #3",
        "author": "Rick Riordan (Goodreads Author)",
        "description": "It's not everyday you find yourself in combat with a half-lion, half-human.\r\n\r\nBut when you're the son of a Greek god, it happens. And now my friend Annabeth is missing, a goddess is in chains and only five half-blood heroes can join the quest to defeat the doomsday monster.\r\n\r\nOh, and guess what? The Oracle has predicted that not all of us will survive...",
        "language": "English",
        "isbn": "9780141382890",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Mythology',
            'Fiction',
            'Middle Grade',
            'Adventure',
            'Childrens',
            'Greek Mythology',
            'Urban Fantasy',
            'Magic'
        ],
        "pages": 320,
        "awards": 
            ['Premio El Templo de las Mil Puertas Nominee for Mejor novela extranjera perteneciente a saga (2009)'
        ],
        "likedPercent": 98.0,
        "price": 3.43
    },
    {
        "id": 28186,
        "title": "The Sea of Monsters",
        "series": "Percy Jackson and the Olympians #2",
        "author": "Rick Riordan (Goodreads Author)",
        "description": "The heroic son of Poseidon makes an action-packed comeback in the second must-read installment of Rick Riordan's amazing young readers series. Starring Percy Jackson, a \"half blood\" whose mother is human and whose father is the God of the Sea, Riordan's series combines cliffhanger adventure and Greek mythology lessons that results in true page-turners that get better with each installment.In this episode, The Sea of Monsters, Percy sets out to retrieve the Golden Fleece before his summer camp is destroyed, surpassing the first book's drama and setting the stage for more thrills to come.",
        "language": "English",
        "isbn": "9780786856862",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Mythology',
            'Fiction',
            'Middle Grade',
            'Adventure',
            'Childrens',
            'Urban Fantasy',
            'Greek Mythology',
            'Magic'
        ],
        "pages": 279,
        "awards": 
            [''
        ],
        "likedPercent": 97.0,
        "price": 1.91
    },
    {
        "id": 7763,
        "title": "The Joy Luck Club",
        "series": "",
        "author": "Amy Tan (Goodreads Author)",
        "description": "Four mothers, four daughters, four families, whose histories shift with the four winds depending on who's telling the stories. In 1949, four Chinese women, recent immigrants to San Francisco, meet weekly to play mahjong and tell stories of what they left behind in China. United in loss and new hope for their daughters' futures, they call themselves the Joy Luck Club. Their daughters, who have never heard these stories, think their mothers' advice is irrelevant to their modern American lives \u2013 until their own inner crises reveal how much they've unknowingly inherited of their mothers' pasts. With wit and sensitivity, Amy Tan examines the sometimes painful, often tender, and always deep connection between mothers and daughters. As each woman reveals her secrets, trying to unravel the truth about her life, the strings become more tangled, more entwined. Mothers boast or despair over daughters, and daughters roll their eyes even as they feel the inextricable tightening of their matriarchal ties. Tan is an astute storyteller, enticing readers to immerse themselves into these lives of complexity and mystery.",
        "language": "English",
        "isbn": "9780143038092",
        "genres": 
            ['Fiction',
            'Historical Fiction',
            'Classics',
            'China',
            'Contemporary',
            'Adult Fiction',
            'Adult',
            'Literature',
            'Asia',
            'Novels'
        ],
        "pages": 288,
        "awards": 
            ['California Book Award for Fiction (Gold) (1989)',
            'Los Angeles Times Book Prize Nominee for Fiction (1989)',
            'Northern California Book Awards for Fiction (1989)',
            'National Book Critics Circle Award Nominee for Fiction (1989)',
            'National Book Award Finalist for Fiction (1989)'
        ],
        "likedPercent": 92.0,
        "price": 4.74
    },
    {
        "id": 13023,
        "title": "Alice in Wonderland",
        "series": "",
        "author": "Jane Carruth (Adapted By), Lewis Carroll (Original Story By), Rene Cloke (Illustrator)",
        "description": "\r\n  This is an adaptation. For the editions of the original book, see here\r\n.Alice's Adventures in Wonderland (commonly shortened to Alice in Wonderland) is an 1865 novel written by English mathematician Charles Lutwidge Dodgson under the pseudonym Lewis Carroll. It tells of a girl named Alice falling through a rabbit hole into a fantasy world populated by peculiar, anthropomorphic creatures. The tale plays with logic, giving the story lasting popularity with adults as well as with children. It is considered to be one of the best examples of the literary nonsense genre. Its narrative course and structure, characters and imagery have been enormously influential in both popular culture and literature, especially in the fantasy genre.",
        "language": "English",
        "isbn": "9780517223628",
        "genres": 
            ['Classics',
            'Fantasy',
            'Fiction',
            'Childrens',
            'Young Adult',
            'Adventure',
            'Literature',
            'Novels',
            'Classic Literature',
            'Middle Grade'
        ],
        "pages": 92,
        "awards": 
            ['Kate Greenaway Medal (1988)',
            'Kurt Maschler Award (1999)'
        ],
        "likedPercent": 92.0,
        "price": 5.26
    },
    {
        "id": 1852,
        "title": "The Call of the Wild",
        "series": "",
        "author": "Jack London, Avi (Introduction)",
        "description": "First published in 1903, The Call of the Wild is regarded as Jack London's masterpiece. Based on London's experiences as a gold prospector in the Canadian wilderness and his ideas about nature and the struggle for existence, The Call of the Wild is a tale about unbreakable spirit and the fight for survival in the frozen Alaskan Klondike.",
        "language": "English",
        "isbn": "9780439227148",
        "genres": 
            ['Classics',
            'Fiction',
            'Adventure',
            'Young Adult',
            'Animals',
            'Historical Fiction',
            'Literature',
            'School',
            'Childrens',
            'Novels'
        ],
        "pages": 172,
        "awards": 
            [''
        ],
        "likedPercent": 91.0,
        "price": 5.38
    },
    {
        "id": 71728,
        "title": "Jonathan Livingston Seagull",
        "series": "",
        "author": "Richard Bach (Goodreads Author), Russell Munson (Photographer)",
        "description": "This is a story for people who follow their hearts and make their own rules...people who get special pleasure out of doing something well, even if only for themselves...people who know there's more to this living than meets the eye: they\u2019ll be right there with Jonathan, flying higher and faster than ever they dreamed.Jonathan Livingston Seagull is no ordinary bird. He believes it is every gull's right to fly, to reach the ultimate freedom of challenge and discovery, finding his greatest reward in teaching younger gulls the joy of flight and the power of dreams. The special 20th anniversary release of this spiritual classic!",
        "language": "English",
        "isbn": "9780743278904",
        "genres": 
            ['Fiction',
            'Classics',
            'Philosophy',
            'Fantasy',
            'Spirituality',
            'Inspirational',
            'Self Help',
            'Literature',
            'Novels',
            'Animals'
        ],
        "pages": 112,
        "awards": 
            ['Nene Award (1974)'
        ],
        "likedPercent": 88.0,
        "price": 4.55
    },
    {
        "id": 2175,
        "title": "Madame Bovary",
        "series": "",
        "author": "Gustave Flaubert, Mark Overstall (Contributor), Paul De Man (Editor), Malcolm Bowie (Introduction), Margaret Mauldon (Translator)",
        "description": "'Oh, why, dear God, did I marry him?'Emma Bovary is beautiful and bored, trapped in her marriage to a mediocre doctor and stifled by the banality of provincial life. An ardent devourer of sentimental novels, she longs for passion and seeks escape in fantasies of high romance, in voracious spending and, eventually, in adultery. But even her affairs bring her disappointment, and when real life continues to fail to live up to her romantic expectations, the consequences are devastating. Flaubert's erotically charged and psychologically acute portrayal of Emma Bovary caused a moral outcry on its publication in 1857. It was deemed so lifelike that many women claimed they were the model for his heroine; but Flaubert insisted: 'Madame Bovary, c'est moi.'This modern translation by Flaubert's biographer, Geoffrey Wall, retains all the delicacy and precision of the French original. The edition also contains a preface by the novelist Mich\u00e8le Roberts.",
        "language": "French",
        "isbn": "9780192840394",
        "genres": 
            ['Classics',
            'Fiction',
            'France',
            'Literature',
            'French Literature',
            'Romance',
            '19th Century',
            'Novels',
            'Historical Fiction',
            'Classic Literature'
        ],
        "pages": 329,
        "awards": 
            [''
        ],
        "likedPercent": 87.0,
        "price": 1.45
    },
    {
        "id": 378,
        "title": "The Phantom Tollbooth",
        "series": "",
        "author": "Norton Juster, Jules Feiffer (Illustrator)",
        "description": "Librarian's Note: For an alternate cover edition of the same ISBN, click here.Hailed as \u201ca classic. . . . humorous, full of warmth and real invention\u201d (The New Yorker), this beloved story -first published more than fifty years ago- introduces readers to Milo and his adventures in the Lands Beyond. For Milo, everything\u2019s a bore. When a tollbooth mysteriously appears in his room, he drives through only because he\u2019s got nothing better to do. But on the other side, things seem different. Milo visits the Island of Conclusions (you get there by jumping), learns about time from a ticking watchdog named Tock, and even embarks on a quest to rescue Rhyme and Reason! Somewhere along the way, Milo realizes something astonishing. Life is far from dull. In fact, it\u2019s exciting beyond his wildest dreams. . . .",
        "language": "English",
        "isbn": "9780394820378",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Childrens',
            'Classics',
            'Young Adult',
            'Middle Grade',
            'Adventure',
            'Humor',
            'Science Fiction Fantasy',
            'Juvenile'
        ],
        "pages": 256,
        "awards": 
            [''
        ],
        "likedPercent": 94.0,
        "price": 5.79
    },
    {
        "id": 40940121,
        "title": "Bridge to Terabithia",
        "series": "",
        "author": "Katherine Paterson",
        "description": "Jess Aarons' greatest ambition is to be the fastest runner in his grade. He's been practicing all summer and can't wait to see his classmates' faces when he beats them all. But on the first day of school, a new girl boldly crosses over to the boys' side and outruns everyone.That's not a very promising beginning for a friendship, but Jess and Leslie Burke become inseparable. Together they create Terabithia, a magical kingdom in the woods where the two of them reign as king and queen, and their imaginations set the only limits.",
        "language": "English",
        "isbn": "B001UFP6JY",
        "genres": 
            ['Young Adult',
            'Fiction',
            'Classics',
            'Childrens',
            'Fantasy',
            'Middle Grade',
            'Realistic Fiction',
            'School',
            'Juvenile',
            'Contemporary'
        ],
        "pages": 190,
        "awards": 
            ['Newbery Medal (1978)',
            'Lewis Carroll Shelf Award (1978)',
            'Zilveren Griffel (1983)',
            '\Dorothy Canfield Fisher Childrens Book Award Nominee (1979)\',
            'California Young Readers Medal Nominee for Middle School/Junior High (1980)'
        ],
        "likedPercent": 92.0,
        "price": 9.278812427895108
    },
    {
        "id": 7938275,
        "title": "The Hunger Games Trilogy Boxset",
        "series": "The Hunger Games #1-3",
        "author": "Suzanne Collins, Guillaume Fournier (Translator), Pilar Ram\u00edrez Tello (Goodreads Author) (Translator), Hanna H\u00f6rl (Illustrator), Sylke Hachmeister (Translator), Peter Kl\u00f6ss (Translator)",
        "description": "The extraordinary, ground breaking New York Times bestsellers The Hunger Games and Catching Fire, along with the third book in The Hunger Games trilogy by Suzanne Collins, Mockingjay, are available for the first time ever in a beautiful boxset edition. Stunning, gripping, and powerful. The trilogy is now complete!",
        "language": "English",
        "isbn": "9780545265355",
        "genres": 
            ['Young Adult',
            'Fiction',
            'Fantasy',
            'Dystopia',
            'Science Fiction',
            'Romance',
            'Adventure',
            'Teen',
            'Action',
            'Novels'
        ],
        "pages": 1155,
        "awards": 
            ['Audie Award for Excellence in Design (2016)'
        ],
        "likedPercent": 98.0,
        "price": 4.09
    },
    {
        "id": 191139,
        "title": "Oh, the Places You'll Go!",
        "series": "",
        "author": "Dr. Seuss",
        "description": "For out-starting upstarts of all ages, here is a wonderfully wise and blessedly brief graduation speech from the one and only Dr. Seuss. In his inimitable, humorous verse and pictures, he addresses the Great Balancing Act (life itself, and the ups and downs it presents) while encouraging us to find the success that lies within us.\r\n  \r\n  And will you succeed?Yes! You will indeed!(98 and \u00be percent guaranteed.)\r\n  \r\nA modern classic, Oh, the Places You'll Go! was first published one year before Dr. Seuss's death at the age of eighty-seven. In a mere fifty-six pages, Dr, Seuss managed to impart a lifetime of wisdom. It is the perfect send-off for children starting out in the maze of life, be they nursery school grads or newly-minted PhD's. Everyone will find it inspired good fun.",
        "language": "English",
        "isbn": "9780679805274",
        "genres": 
            ['Childrens',
            'Picture Books',
            'Fiction',
            'Classics',
            'Poetry',
            'Fantasy',
            'Young Adult',
            'Inspirational',
            'Kids',
            'Humor'
        ],
        "pages": 44,
        "awards": 
            [''
        ],
        "likedPercent": 95.0,
        "price": 5.01
    },
    {
        "id": 5060378,
        "title": "The Girl Who Played with Fire",
        "series": "Millennium #2",
        "author": "Stieg Larsson, Reg Keeland (Translator)",
        "description": "Part blistering espionage thriller, part riveting police procedural, and part piercing expos\u00e9 on social injustice, The Girl Who Played with Fire is a masterful, endlessly satisfying novel. \u00a0Mikael Blomkvist, crusading publisher of the magazine Millennium, has decided to run a story that will expose an extensive sex trafficking operation. On the eve of its publication, the two reporters responsible for the article are murdered, and the fingerprints found on the murder weapon belong to his friend, the troubled genius hacker Lisbeth Salander. Blomkvist, convinced of Salander\u2019s innocence, plunges into an investigation. Meanwhile, Salander herself is drawn into a murderous game of cat and mouse, which forces her to face her dark past.From the Trade Paperback edition.",
        "language": "English",
        "isbn": "9780307269980",
        "genres": 
            ['Fiction',
            'Mystery',
            'Thriller',
            'Crime',
            'Mystery Thriller',
            'Suspense',
            'Contemporary',
            'Sweden',
            'Adult',
            'Audiobook'
        ],
        "pages": 503,
        "awards": 
            ['Anthony Award Nominee for Best Novel (2010)',
            'Dilys Award Nominee (2010)',
            'CWA International Dagger Nominee (2009)',
            'Svenska Deckarakademins pris f\u00f6r b\u00e4sta svenska kriminalroman (2006)',
            'Goodreads Choice Award for Mystery/Thriller (2009)'
        ],
        "likedPercent": 97.0,
        "price": 3.25
    },
    {
        "id": 6186357,
        "title": "The Maze Runner",
        "series": "The Maze Runner #1",
        "author": "James Dashner (Goodreads Author)",
        "description": "There are alternate cover editions for this ASIN here and here.If you ain\u2019t scared, you ain\u2019t human. When Thomas wakes up in the lift, the only thing he can remember is his name. He\u2019s surrounded by strangers\u2014boys whose memories are also gone. Nice to meet ya, shank. Welcome to the Glade. Outside the towering stone walls that surround the Glade is a limitless, ever-changing maze. It\u2019s the only way out\u2014and no one\u2019s ever made it through alive. Everything is going to change. Then a girl arrives. The first girl ever. And the message she delivers is terrifying. Remember. Survive. Run.",
        "language": "English",
        "isbn": "9780385737944",
        "genres": 
            ['Young Adult',
            'Dystopia',
            'Science Fiction',
            'Fiction',
            'Fantasy',
            'Adventure',
            'Post Apocalyptic',
            'Mystery',
            'Teen',
            'Audiobook'

        ],
        "pages": 384,
        "awards": 
            ['Georgia Peach Book Award (2011)',
            'Utah Book Award Nominee for Young Adults (2009)',
            '\Romantic Times Reviewers Choice Award (RT Award) Nominee for Best Young Adult Paranormal/Fantasy Novel  (2009)\',
            'Charlotte Award (2012)',
            '\Pennsylvania Young Readers Choice Award Nominee (2011)\',
            'Evergreen Teen Book Award (2012)',
            'Milwaukee County Teen Book Award Nominee (2011)',
            'Lincoln Award (2012)',
            'Missouri Truman Readers Award (2012)'
        
        ],
        "likedPercent": 92.0,
        "price": 3.17
    },
    {
        "id": 27712,
        "title": "The Neverending Story",
        "series": "",
        "author": "Michael Ende, Ralph Manheim (Translator), Roswitha Quadflieg (Illustrator)",
        "description": "This epic work of the imagination has captured the hearts of millions of readers worldwide since it was first published more than a decade ago. Its special story within a story is an irresistible invitation for readers to become part of the book itself. And now this modern classic and bibliophile's dream is available in hardcover again.The story begins with a lonely boy named Bastian and the strange book that draws him into the beautiful but doomed world of Fantastica. Only a human can save this enchanted place by giving its ruler, the Childlike Empress, a new name. But the journey to her tower leads through lands of dragons, giants, monsters, and magic and once Bastian begins his quest, he may never return. As he is drawn deeper into Fantastica, he must find the courage to face unspeakable foes and the mysteries of his own heart. Readers, too, can travel to the wondrous, unforgettable world of Fantastica if they will just turn the page...--front flap",
        "language": "English",
        "isbn": "9780525457589",
        "genres": 
            ['Fantasy',
            'Classics',
            'Fiction',
            'Young Adult',
            'Childrens',
            'Adventure',
            'German Literature',
            'Middle Grade',
            'Science Fiction Fantasy',
            'Books About Books'
        ],
        "pages": 396,
        "awards": 
            ['Buxtehuder Bulle (1979)',
            'Zilveren Griffel (1983)',
            'Preis der Leseratten des ZDF (1980)'
        
        ],
        "likedPercent": 94.0,
        "price": 7.54
    },
    {
        "id": 18254,
        "title": "Oliver Twist",
        "series": "",
        "author": "Charles Dickens, Philip Horne (Introduction), Gerald Dickens (Narrator), \u67e5\u5c14\u65af\u00b7\u72c4\u66f4\u65af, \u5434\u5029\u5353 (Translator)",
        "description": "A gripping portrayal of London's dark criminal underbelly, published in Penguin Classics with an introduction by Philip Horne.The story of Oliver Twist - orphaned, and set upon by evil and adversity from his first breath - shocked readers when it was published. After running away from the workhouse and pompous beadle Mr Bumble, Oliver finds himself lured into a den of thieves peopled by vivid and memorable characters - the Artful Dodger, vicious burglar Bill Sikes, his dog Bull's Eye, and prostitute Nancy, all watched over by cunning master-thief Fagin. Combining elements of Gothic Romance, the Newgate Novel and popular melodrama, Dickens created an entirely new kind of fiction, scathing in its indictment of a cruel society, and pervaded by an unforgettable sense of threat and mystery.This Penguin Classics edition of Oliver Twist is the first critical edition to faithfully reproduce the text as its earliest readers would have encountered it from its serialisation in Bentley's Miscellany, and includes an introduction by Philip Horne, a glossary of Victorian thieves' slang, a chronology of Dickens's life, a map of contemporary London and all of George Cruikshank's original illustrations.For more than seventy years, Penguin has been the leading publisher of classic literature in the English-speaking world. With more than 1,700 titles, Penguin Classics represents a global bookshelf of the best works throughout history and across genres and disciplines. Readers trust the series to provide authoritative texts enhanced by introductions and notes by distinguished scholars and contemporary authors, as well as up-to-date translations by award-winning translators.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'Literature',
            'Novels',
            '19th Century',
            'Classic Literature',
            'British Literature',
            'Victorian',
            'Historical'
        
        ],
        "pages": 608,
        "awards": 
            ['CityRead London (2012)'
        
        ],
        "likedPercent": 92.0,
        "price": 11.877147438670043
    },
    {
        "id": 338798,
        "title": "Ulysses",
        "series": "",
        "author": "James Joyce, Morris L. Ernst (Foreword), John M. Woolsey (Foreword)",
        "description": "Loosely based on the Odyssey, this landmark of modern literature follows ordinary Dubliners in 1904. Capturing a single day in the life of Dubliner Leopold Bloom, his friends Buck Mulligan and Stephen Dedalus, his wife Molly, and a scintillating cast of supporting characters, Joyce pushes Celtic lyricism and vulgarity to splendid extremes. Captivating experimental techniques range from interior monologues to exuberant wordplay and earthy humor. A major achievement in 20th century literature.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Novels',
            'Ireland',
            'Irish Literature',
            'Unfinished',
            '20th Century',
            'Literary Fiction',
            'Banned Books'
        
        ],
        "pages": 783,
        "awards": 
            ['\u041d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u043d\u0430 \u043d\u0430\u0433\u0440\u0430\u0434\u0430 \u201e\u0425\u0440\u0438\u0441\u0442\u043e \u0413. \u0414\u0430\u043d\u043e\u0432\u201c for \u041f\u0440\u0435\u0432\u043e\u0434\u043d\u0430 \u0445\u0443\u0434\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u0430 \u043b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430 (2004)'
        
        ],
        "likedPercent": 82.0,
        "price": 8.69953052147681
    },
    {
        "id": 295,
        "title": "Treasure Island",
        "series": "",
        "author": "Robert Louis Stevenson, David W. Whitehead (Introduction), Richard S. Hartmetz (Goodreads Author) (Editor)",
        "description": "\"For sheer storytelling delight and pure adventure, Treasure Island has never been surpassed. From the moment young Jim Hawkins first encounters the sinister Blind Pew at the Admiral Benbow Inn until the climactic battle for treasure on a tropic isle, the novel creates scenes and characters that have fired the imaginations of generations of readers. Written by a superb prose stylist, a master of both action and atmosphere, the story centers upon the conflict between good and evil - but in this case a particularly engaging form of evil. It is the villainy of that most ambiguous rogue Long John Silver that sets the tempo of this tale of treachery, greed, and daring. Designed to forever kindle a dream of high romance and distant horizons, Treasure Island is, in the words of G. K. Chesterton, 'the realization of an ideal, that which is promised in its provocative and beckoning map; a vision not only of white skeletons but also green palm trees and sapphire seas.' G. S. Fraser terms it 'an utterly original book' and goes on to write: 'There will always be a place for stories like Treasure Island that can keep boys and old men happy.'",
        "language": "English",
        "isbn": "9780753453803",
        "genres": 
            ['Classics',
            'Fiction',
            'Adventure',
            'Young Adult',
            'Historical Fiction',
            'Childrens',
            'Literature',
            'Pirates',
            'Fantasy',
            'Novels'
        
        ],
        "pages": 311,
        "awards": 
            ['Odyssey Award Nominee (2008)',
            'Pr\u00eamio Jabuti Nominee for Adapta\u00e7\u00e3o (2017)',
            'Audie Award for Classic (2008)'
        
        ],
        "likedPercent": 92.0,
        "price": 5.6
    },
    {
        "id": 10818853,
        "title": "Fifty Shades of Grey",
        "series": "Fifty Shades #1",
        "author": "E.L. James (Goodreads Author)",
        "description": "When literature student Anastasia Steele goes to interview young entrepreneur Christian Grey, she encounters a man who is beautiful, brilliant, and intimidating. The unworldly, innocent Ana is startled to realize she wants this man and, despite his enigmatic reserve, finds she is desperate to get close to him. Unable to resist Ana\u2019s quiet beauty, wit, and independent spirit, Grey admits he wants her, too\u2014but on his own terms.\u00a0Shocked yet thrilled by Grey\u2019s singular erotic tastes, Ana hesitates. For all the trappings of success\u2014his multinational businesses, his vast wealth, his loving family\u2014Grey is a man tormented by demons and consumed by the need to control. When the couple embarks on a daring, passionately physical affair, Ana discovers Christian Grey\u2019s secrets and explores her own dark desires.Erotic, amusing, and deeply moving, the Fifty Shades Trilogy is a tale that will obsess you, possess you, and stay with you forever.This book is intended for mature audiences.",
        "language": "English",
        "isbn": "9781612130293",
        "genres": 
            ['Romance',
            'Fiction',
            'Erotica',
            'Adult',
            'BDSM',
            'Contemporary',
            'Chick Lit',
            'Contemporary Romance',
            'Erotic Romance',
            'Adult Fiction'
        
        ],
        "pages": 356,
        "awards": 
            ['All About Romance (AAR) Annual Reader Poll for Best Erotic Romance (tie) (2012)',
            'Australian Book Industry Award (ABIA) for International Book (2013)',
            'Goodreads Choice Award Nominee for Romance (2011)'
        
        ],
        "likedPercent": 78.0,
        "price": 1.8892102637450119
    },
    {
        "id": 40611463,
        "title": "The Clan of the Cave Bear",
        "series": "Earth's Children #1",
        "author": "Jean M. Auel",
        "description": "This novel of awesome beauty and power is a moving saga about people, relationships, and the boundaries of love. Through Jean M. Auel's magnificent storytelling we are taken back to the dawn of modern humans, and with a girl named Ayla we are swept up in the harsh and beautiful Ice Age world they shared with the ones who called themselves the Clan of the Cave Bear. A natural disaster leaves the young girl wandering alone in an unfamiliar and dangerous land until she is found by a woman of the Clan, people very different from her own kind. To them, blond, blue-eyed Ayla looks peculiar and ugly--she is one of the Others, those who have moved into their ancient homeland; but Iza cannot leave the girl to die and takes her with them. Iza and Creb, the old Mog-ur, grow to love her, and as Ayla learns the ways of the Clan and Iza's way of healing, most come to accept her. But the brutal and proud youth who is destined to become their next leader sees her differences as a threat to his authority. He develops a deep and abiding hatred for the strange girl of the Others who lives in their midst, and is determined to get his revenge.",
        "language": "English",
        "isbn": "B00466HQ2Y",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Fantasy',
            'Historical',
            'Classics',
            'Romance',
            'Adventure',
            'Prehistoric',
            'Adult',
            'Novels'
        
        ],
        "pages": 516,
        "awards": 
            ['National Book Award Finalist for First Novel (1981)'
        
        ],
        "likedPercent": 93.0,
        "price": 1.2454414692484055
    },
    {
        "id": 62291,
        "title": "A Storm of Swords",
        "series": "A Song of Ice and Fire #3",
        "author": "George R.R. Martin",
        "description": "An alternate cover for this isbn can be found here.Here is the third volume in George R.R. Martin's magnificent cycle of novels that includes A Game of Thrones and A Clash of Kings. Together, this series comprises a genuine masterpiece of modern fantasy, destined to stand as one of the great achievements of imaginative fiction.Of the five contenders for power, one is dead, another in disfavor, and still the wars rage as alliances are made and broken. Joffrey sits on the Iron Throne, the uneasy ruler of the Seven Kingdoms. His most bitter rival, Lord Stannis, stands defeated and disgraced, victim of the sorceress who holds him in her thrall. Young Robb still rules the North from the fortress of Riverrun. Meanwhile, making her way across a blood-drenched continent is the exiled queen, Daenerys, mistress of the only three dragons still left in the world. And as opposing forces manoeuver for the final showdown, an army of barbaric wildlings arrives from the outermost limits of civilization, accompanied by a horde of mythical Others\u2014a supernatural army of the living dead whose animated corpses are unstoppable. As the future of the land hangs in the balance, no one will rest until the Seven Kingdoms have exploded in a veritable storm of swords...",
        "language": "English",
        "isbn": "9780553573428",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Epic Fantasy',
            'Science Fiction Fantasy',
            'High Fantasy',
            'Adult',
            'Adventure',
            'Dragons',
            'Audiobook',
            'Epic'
        
        ],
        "pages": 1177,
        "awards": 
            ['Hugo Award Nominee for Best Novel (2001)',
            'Nebula Award Nominee for Best Novel (2001)',
            'Locus Award for Best Fantasy Novel (2001)',
            'Geffen Award for Best Translated Fantasy Book (2002)',
            'Premio Ignotus (2006)'
        
        ],
        "likedPercent": 99.0,
        "price": 3.57
    },
    {
        "id": 2696,
        "title": "The Canterbury Tales",
        "series": "",
        "author": "Geoffrey Chaucer, Nevill Coghill (Translator)",
        "description": "The procession that crosses Chaucer's pages is as full of life and as richly textured as a medieval tapestry. The Knight, the Miller, the Friar, the Squire, the Prioress, the Wife of Bath, and others who make up the cast of characters -- including Chaucer himself -- are real people, with human emotions and weaknesses. When it is remembered that Chaucer wrote in English at a time when Latin was the standard literary language across western Europe, the magnitude of his achievement is even more remarkable. But Chaucer's genius needs no historical introduction; it bursts forth from every page of The Canterbury Tales.If we trust the General Prologue, Chaucer intended that each pilgrim should tell two tales on the way to Canterbury and two tales on the way back. He never finished his enormous project and even the completed tales were not finally revised. Scholars are uncertain about the order of the tales. As the printing press had yet to be invented when Chaucer wrote his works, The Canterbury Tales has been passed down in several handwritten manuscripts.",
        "language": "English",
        "isbn": "9780140424386",
        "genres": 
            ['Classics',
            'Fiction',
            'Poetry',
            'Literature',
            'School',
            'Medieval',
            'Short Stories',
            'Historical Fiction',
            'Classic Literature',
            'Read For School'
        
        ],
        "pages": 521,
        "awards": 
            [''
        
        ],
        "likedPercent": 84.0,
        "price": 3.9
    },
    {
        "id": 7069,
        "title": "The World According to Garp",
        "series": "",
        "author": "John Irving (Goodreads Author)",
        "description": "This is the life and times of T. S. Garp, the bastard son of Jenny Fields\u2014a feminist leader ahead of her times. This is the life and death of a famous mother and her almost-famous son; theirs is a world of sexual extremes\u2014even of sexual assassinations. It is a novel rich with \"lunacy and sorrow\"; yet the dark, violent events of the story do not undermine a comedy both ribald and robust. In more than thirty languages, in more than forty countries\u2014with more than ten million copies in print\u2014this novel provides almost cheerful, even hilarious evidence of its famous last line: \"In the world according to Garp, we are all terminal cases.\"",
        "language": "English",
        "isbn": "9780345915597",
        "genres": 
            ['Fiction',
            'Classics',
            'Contemporary',
            'Literature',
            'Novels',
            'Literary Fiction',
            'Humor',
            'American',
            'Adult Fiction',
            'Drama'
        
        ],
        "pages": 610,
        "awards": 
            ['National Book Award for Fiction (Paperback) (1980)',
            'National Book Critics Circle Award Nominee for Fiction (1978)',
            'National Book Award Finalist for Fiction (1979)'
        
        ],
        "likedPercent": 94.0,
        "price": 8.64086345924121
    },
    {
        "id": 10799,
        "title": "A Farewell to Arms",
        "series": "",
        "author": "Ernest Hemingway",
        "description": "A Farewell to Arms is the unforgettable story of an American ambulance driver on the Italian front and his passion for a beautiful English nurse. Set against the looming horrors of the battlefield - the weary, demoralized men marching in the rain during the German attack on Caporetto; the profound struggle between loyalty and desertion\u2014this gripping, semiautobiographical work captures the harsh realities of war and the pain of lovers caught in its inexorable sweep. Ernest Hemingway famously said that he rewrote his ending to A Farewell to Arms thirty-nine times to get the words right.",
        "language": "English",
        "isbn": "9780099910107",
        "genres": 
            ['Classics',
            'Fiction',
            'Historical Fiction',
            'War',
            'Literature',
            'Novels',
            'American',
            'Romance',
            'Classic Literature',
            'School'
        
        ],
        "pages": 293,
        "awards": 
            [''
        
        ],
        "likedPercent": 90.0,
        "price": 0.91
    },
    {
        "id": 58696,
        "title": "David Copperfield",
        "series": "",
        "author": "Charles Dickens, Jeremy Tambling (Introduction)",
        "description": "David Copperfield is the story of a young man's adventures on his journey from an unhappy and impoverished childhood to the discovery of his vocation as a successful novelist. Among the gloriously vivid cast of characters he encounters are his tyrannical stepfather, Mr Murdstone; his brilliant, but ultimately unworthy school-friend James Steerforth; his formidable aunt, Betsey Trotwood; the eternally humble, yet treacherous Uriah Heep; frivolous, enchanting Dora Spenlow; and the magnificently impecunious Wilkins Micawber, one of literature's great comic creations. In David Copperfield - the novel he described as his 'favourite child' - Dickens drew revealingly on his own experiences to create one of the most exuberant and enduringly popular works, filled with tragedy and comedy in equal measure. This edition uses the text of the first volume publication of 1850, and includes updated suggestions for further reading, original illustrations by 'Phiz', a revised chronology and expanded notes. In his new introduction, Jeremy Tambling discusses the novel's autobiographical elements, and its central themes of memory and identity.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Historical Fiction',
            'Novels',
            '19th Century',
            'British Literature',
            'Classic Literature',
            'Victorian',
            'Audiobook'
        
        ],
        "pages": 882,
        "awards": 
            ['Audie Award Nominee for Fiction of Nonfiction Licenses or Distributed for Martin Jarvis (2003)'
        
        ],
        "likedPercent": 93.0,
        "price": 11.717413394085844
    },
    {
        "id": 6350972,
        "title": "Tote M\u00e4dchen l\u00fcgen nicht",
        "series": "",
        "author": "Jay Asher (Goodreads Author), Knut Kr\u00fcger (\u00dcbersetzer)",
        "description": "You can\u2019t stop the future. You can\u2019t rewind the past.The only way to learn the secret . . . is to press play.Clay Jensen returns home from school to find a strange package with his name on it lying on his porch. Inside he discovers several cassette tapes recorded by Hannah Baker\u2013his classmate and crush\u2013who committed suicide two weeks earlier. Hannah\u2019s voice tells him that there are thirteen reasons why she decided to end her life. Clay is one of them. If he listens, he\u2019ll find out why. Clay spends the night crisscrossing his town with Hannah as his guide. He becomes a firsthand witness to Hannah\u2019s pain, and as he follows Hannah\u2019s recorded words throughout his town, what he discovers changes his life forever.",
        "language": "German",
        "isbn": "9783570160206",
        "genres": 
            ['Young Adult',
            'Contemporary',
            'Fiction',
            'Realistic Fiction',
            'Mystery',
            'Mental Health',
            'Teen',
            'Audiobook',
            'Romance',
            'High School'
        
        ],
        "pages": 288,
        "awards": 
            ['Georgia Peach Book Award Nominee for Honor book (2009)',
            'California Book Award for Young Adult (Silver) (2007)',
            'South Carolina Book Award for Young Adult Book (2010)',
            'Deutscher Jugendliteraturpreis Nominee for Preis der Jugendjury (2010)',
            'Lincoln Award (2013)',
            'Missouri Gateway Readers Award (2010)',
            'Oklahoma Sequoyah Award for High School (2010)',
            'Premi Protagonista Jove for Categoria 13-14 anys (2011)'
        
        ],
        "likedPercent": 89.0,
        "price": 3.86
    },
    {
        "id": 37442,
        "title": "Wicked: The Life and Times of the Wicked Witch of the West",
        "series": "The Wicked Years #1",
        "author": "Gregory Maguire, Douglas Smith (Illustrator)",
        "description": "When Dorothy triumphed over the Wicked Witch of the West in L. Frank Baum's classic tale we heard only her side of the story. But what about her arch-nemesis, the mysterious Witch? Where did she come from? How did she become so wicked? And what is the true nature of evil?Gregory Maguire creates a fantasy world so rich and vivid that we will never look at Oz the same way again. Wicked is about a land where animals talk and strive to be treated like first-class citizens, Munchkinlanders seek the comfort of middle-class stability, and the Tin Man becomes a victim of domestic violence. And then there is the little green-skinned girl named Elphaba, who will grow up to become the infamous Wicked Witch of the West, a smart, prickly, and misunderstood creature who challenges all our preconceived notions about the nature of good and evil.An astonishingly rich re-creation of the land of Oz, this book retells the story of Elphaba, the Wicked Witch of the West, who wasn't so wicked after all. Taking readers past the yellow brick road and into a phantasmagoric world rich with imagination and allegory, Gregory Maguire just might change the reputation of one of the most sinister characters in literature.",
        "language": "English",
        "isbn": "9780060987107",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Adult',
            'Science Fiction Fantasy',
            'Retellings',
            'Adult Fiction',
            'Magic',
            'Witches',
            'Fairy Tales',
            'Classics'
        
        ],
        "pages": 406,
        "awards": 
            ['T\u00e4htifantasia Award Nominee (2009)'
        
        ],
        "likedPercent": 80.0,
        "price": 2.76
    },
    {
        "id": 402093,
        "title": "Sh\u014dgun",
        "series": "Asian Saga: Chronological Order #1",
        "author": "James Clavell",
        "description": "Alternate Cover for ISBN: 0440178002A bold English adventurer. An invincible Japanese warlord. A beautiful woman torn between two ways of life. All brought together in an extraordinary saga aflame with passion, conflict, ambition, and the struggle for power.Here is the world-famous novel of Japan that is the earliest book in James Clavell\u2019s masterly Asian saga. Set in the year 1600, it tells the story of a bold English pilot whose ship was blown ashore in Japan, where he encountered two people who were to change his life: a warlord with his own quest for power, and a beautiful interpreter torn between two ways of life and two ways of love. The principal figures are John Blackthorne, whose dream it is to be the first Englishman to circumnavigate the globe, to wrest control of the trade between Japan and China from Portuguese, and to return home a man of wealth and position; Toranaga, the most powerful feudal lord in Japan, who strives and schemes to seize ultimate power by becoming Shogun\u2014the Supreme Military Dictator\u2014and to unite the warring samurai fiefdoms under his own masterly and farsighted leadership; and the Lady Mariko, a Catholic convert whose conflicting loyalties to the Church and her country are compounded when she falls in love with Blackthorne, the barbarian intruder. In dramatizing how a Westerner, the representative man of his time, comes to be altered by his exposure to an alien culture, Mr. Clavell provides a spellbinding depiction of a nation seething with violence and intrigue as it moves from the medieval world to the modern.",
        "language": "English",
        "isbn": "9780440178002",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Japan',
            'Historical',
            'Classics',
            'Adventure',
            'Asia',
            'Literature',
            'Novels',
            'Japanese Literature'
        
        ],
        "pages": 1152,
        "awards": 
            [''
        
        ],
        "likedPercent": 97.0,
        "price": 7.04
    },
    {
        "id": 4588,
        "title": "Extremely Loud & Incredibly Close",
        "series": "",
        "author": "Jonathan Safran Foer (Goodreads Author)",
        "description": "Nine-year-old Oskar Schell is an inventor, amateur entomologist, Francophile, letter writer, pacifist, natural historian, percussionist, romantic, Great Explorer, jeweller, detective, vegan, and collector of butterflies. When his father is killed in the September 11th attacks on the World Trade Centre, Oskar sets out to solve the mystery of a key he discovers in his father's closet. It is a search which leads him into the lives of strangers, through the five boroughs of New York, into history, to the bombings of Dresden and Hiroshima, and on an inward journey which brings him ever closer to some kind of peace.",
        "language": "English",
        "isbn": "9780618711659",
        "genres": 
            ['Fiction',
            'Contemporary',
            'Historical Fiction',
            'Novels',
            'Adult Fiction',
            'Adult',
            'Literary Fiction',
            'Literature',
            'New York',
            'Young Adult'
        
        ],
        "pages": 326,
        "awards": 
            ['Prix des libraires du Qu\u00e9bec for Laur\u00e9ats hors Qu\u00e9bec (2007)',
            'Luisterboek Award (2009)',
            'LovelyBooks Leserpreis Nominee for Allgemeine Literatur (2009)'
        
        ],
        "likedPercent": 91.0,
        "price": 2.41
    },
    {
        "id": 853510,
        "title": "Murder on the Orient Express",
        "series": "Hercule Poirot #10",
        "author": "Agatha Christie",
        "description": "Just after midnight, a snowdrift stops the Orient Express in its tracks. The luxurious train is surprisingly full for the time of the year, but by the morning it is one passenger fewer. An American tycoon lies dead in his compartment, stabbed a dozen times, his door locked from the inside.Isolated and with a killer in their midst, detective Hercule Poirot must identify the murderer\u2014in case he or she decides to strike again.",
        "language": "English",
        "isbn": "9780007119318",
        "genres": 
            ['Mystery',
            'Classics',
            'Fiction',
            'Crime',
            'Mystery Thriller',
            'Audiobook',
            'Thriller',
            'Detective',
            'Adult',
            'British Literature'
        
        ],
        "pages": 347,
        "awards": 
            [''
        
        ],
        "likedPercent": 97.0,
        "price": 2.56
    },
    {
        "id": 18116,
        "title": "His Dark Materials",
        "series": "His Dark Materials #1-3",
        "author": "Philip Pullman",
        "description": "The Golden Compass, The Subtle Knife, and The Amber Spyglass are available together in one volume perfect for any fan or newcomer to this modern fantasy classic series.These thrilling adventures tell the story of Lyra and Will\u2014two ordinary children on a perilous journey through shimmering haunted otherworlds. They will meet witches and armored bears, fallen angels and soul-eating specters. And in the end, the fate of both the living\u2014and the dead\u2014will rely on them.Phillip Pullman\u2019s spellbinding His Dark Materials trilogy has captivated readers for over twenty years and won acclaim at every turn. It will have you questioning everything you know about your world and wondering what really lies just out of reach.",
        "language": "English",
        "isbn": "9780440238607",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Childrens',
            'Science Fiction Fantasy',
            'Science Fiction',
            'Adventure',
            'Classics',
            'Steampunk',
            'Magic'
        
        ],
        "pages": 1088,
        "awards": 
            ['Literaturpreis der Jury der jungen Leser for Kinderbuch (2002)'
        
        ],
        "likedPercent": 94.0,
        "price": 3.57
    },
    {
        "id": 3008,
        "title": "A Little Princess",
        "series": "",
        "author": "Frances Hodgson Burnett, Nancy Bond (Foreword)",
        "description": "Sara Crewe, an exceptionally intelligent and imaginative student at Miss Minchin's Select Seminary for Young Ladies, is devastated when her adored, indulgent father dies. Now penniless and banished to a room in the attic, Sara is demeaned, abused, and forced to work as a servant. How this resourceful girl's fortunes change again is at the center of A Little Princess, one of the best-loved stories in all of children's literature. This unique and fully annotated edition appends excerpts from Frances Hodgson Burnett's original 1888 novella Sara Crewe and the stage play that preceded the novel, as well as an early story, \"Behind the White Brick,\" allowing readers to see how A Little Princess evolved. In his delightful introduction, U. C. Knoepflmacher considers the fairy-tale allusions and literary touchstones that place the book among the major works of Victorian literature, and shows it to be an exceptionally rich and resonant novel.",
        "language": "English",
        "isbn": "9780142437018",
        "genres": 
            ['Classics',
            'Fiction',
            'Childrens',
            'Young Adult',
            'Historical Fiction',
            'Middle Grade',
            'Historical',
            'Literature',
            'Juvenile',
            'Novels'
        
        ],
        "pages": 242,
        "awards": 
            [''
        
        ],
        "likedPercent": 95.0,
        "price": 2.87
    },
    {
        "id": 37470,
        "title": "The Other Boleyn Girl",
        "series": "The Plantagenet and Tudor Novels #9",
        "author": "Philippa Gregory (Goodreads Author)",
        "description": "This is an alternate cover edition of ISBN 9780743227445Two sisters competing for the greatest prize: The love of a kingWhen Mary Boleyn comes to court as an innocent girl of fourteen, she catches the eye of Henry VIII. Dazzled, Mary falls in love with both her golden prince and her growing role as unofficial queen. However, she soon realises just how much she is a pawn in her family's ambitious plots as the king's interest begins to wane and she is forced to step aside for her best friend and rival: her sister, Anne. Then Mary knows that she must defy her family and her king and take fate into her own hands.A rich and compelling novel of love, sex, ambition, and intrigue, The Other Boleyn Girl introduces a woman of extraordinary determination and desire who lived at the heart of the most exciting and glamourous court in Europe and survived by following her heart.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Historical',
            'Romance',
            'Adult',
            'British Literature',
            'Historical Romance',
            'Tudor Period',
            'Chick Lit',
            'Adult Fiction'
        
        ],
        "pages": 661,
        "awards": 
            ['\Romantic Novel of the Year (RoNas) Award (2002)\',
            'Goodreads Choice Award Nominee for Fiction (2009)'
        
        ],
        "likedPercent": 95.0,
        "price": 18.559970081257482
    },
    {
        "id": 375013,
        "title": "Schindler's List",
        "series": "",
        "author": "Thomas Keneally",
        "description": "In the shadow of Auschwitz, a flamboyant German industrialist grew into a living legend to the Jews of Cracow. He was a womaniser, a heavy drinker and a bon viveur, but to them he became a saviour. This is the extraordinary story of Oskar Schindler, who risked his life to protect Jews in Nazi-occupied Poland and who was transformed by the war into a man with a mission, a compassionate angel of mercy.",
        "language": "English",
        "isbn": "9780340606513",
        "genres": 
            ['History',
            'Nonfiction',
            'Classics',
            'Holocaust',
            'War',
            'Historical',
            'World War II',
            'Biography',
            'Literature',
            'Media Tie In'
        
        ],
        "pages": 429,
        "awards": 
            ['Booker Prize (1982)',
            'Los Angeles Times Book Prize for Fiction (1983)'
        
        ],
        "likedPercent": 96.0,
        "price": 0.85
    },
    {
        "id": 39999,
        "title": "The Boy in the Striped Pajamas",
        "series": "",
        "author": "John Boyne",
        "description": "If you start to read this book, you will go on a journey with a nine-year-old boy named Bruno. (Though this isn't a book for nine-year-olds.) And sooner or later you will arrive with Bruno at a fence.\r\n\r\nFences like this exist all over the world. We hope you never have to encounter one.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Young Adult',
            'Historical',
            'Holocaust',
            'War',
            'Classics',
            'World War II',
            'School',
            'Childrens'
        
        ],
        "pages": 240,
        "awards": 
            ['\Pacific Northwest Library Association Young Readers Choice Award for Intermediate (2009)\',
            'Deutscher Jugendliteraturpreis Nominee for Preis der Jugendjury (2008)',
            '\Bord G\u00e1is Energy Irish Book Award for John Murray Show Listeners Choice Award (2007)\',
            'LovelyBooks Leserpreis Nominee for Allgemeine Literatur (2009)',
            'Premi Protagonista Jove for Categoria 15-16 anys (2008)'
        
        ],
        "likedPercent": 95.0,
        "price": 11.718741378809415
    },
    {
        "id": 40604658,
        "title": "Jurassic Park",
        "series": "Jurassic Park #1",
        "author": "Michael Crichton",
        "description": "An astonishing technique for recovering and cloning dinosaur DNA has been discovered. Now humankind\u2019s most thrilling fantasies have come true. Creatures extinct for eons roam Jurassic Park with their awesome presence and profound mystery, and all the world can visit them\u2014for a price. Until something goes wrong. . . . In Jurassic Park, Michael Crichton taps all his mesmerizing talent and scientific brilliance to create his most electrifying technothriller.",
        "language": "English",
        "isbn": "B007UH4D3G",
        "genres": 
            ['Science Fiction',
            'Fiction',
            'Thriller',
            'Adventure',
            'Fantasy',
            'Horror',
            'Classics',
            'Science Fiction Fantasy',
            'Dinosaurs',
            'Suspense'
        
        ],
        "pages": 466,
        "awards": 
            ['Audie Award for Science Fiction (2016)',
            'Books I Loved Best Yearly (BILBY) Awards for Secondary (1996)',
            'South Carolina Book Award for Young Adult Book (1994)',
            'Colorado Blue Spruce Young Adult Book Award (1993)',
            '\Nevada Young Readers Award for Young Adult Category  (1993)\',
            'Evergreen Teen Book Award Nominee (1993)',
            'Soaring Eagle Book Award (1995)',
            'Iowa Teen Award (1995)'
        
        ],
        "likedPercent": 93.0,
        "price": 5.820767701407918
    },
    {
        "id": 6527740,
        "title": "Last Sacrifice",
        "series": "Vampire Academy #6",
        "author": "Richelle Mead (Goodreads Author)",
        "description": "They come first.My vision was growing dimmer, the blackness and ghosts closing in. I swore it was like I could hear Robert whispering in my ear: The world of the dead won't give you up a second time. Just before the light completely vanished, I saw Dimitri's face join Lissa's. I wanted to smile. I decided then that if the two people I loved most were safe, I could leave this world.The dead could finally have me.Rose Hathaway has always played by her own rules. She broke the law when she ran away from St. Vladimir's Academy with her best friend and last surviving Dragomir princess, Lissa. She broke the law when she fell in love with her gorgeous, off-limits instructor, Dimitri. And she dared to defy Queen Tatiana, leader of the Moroi world, risking her life and reputation to protect generations of dhampir guardians to come.Now the law has finally caught up with Rose - for a crime she didn't even commit. She's in prison for the highest offense imaginable: the assassination of a monarch. She'll need help from both Dimitri and Adrian to find the one living person who can stall her execution and force the Moroi elite to acknowledge a shocking new candidate for the royal throne: Vasilisa Dragomir.But the clock on Rose's life is running out. Rose knows in her heart the world of the dead wants her back...and this time she is truly out of second chances. The big question is, when your whole life is about saving others, who will save you?Join Rose, Dimitri, Adrian, and Lissa in Last Sacrifice, the epic, unforgettable finale to Richelle Mead's international #1 bestselling Vampire Academy series.",
        "language": "English",
        "isbn": "9781595143068",
        "genres": 
            ['Young Adult',
            'Vampires',
            'Fantasy',
            'Paranormal',
            'Romance',
            'Urban Fantasy',
            'Paranormal Romance',
            'Supernatural',
            'Fiction',
            'Magic'
        
        ],
        "pages": 594,
        "awards": 
            ['Goodreads Choice Award Nominee for Young Adult Fantasy (2010)'
        
        ],
        "likedPercent": 96.0,
        "price": 3.8
    },
    {
        "id": 9361589,
        "title": "The Night Circus",
        "series": "",
        "author": "Erin Morgenstern (Goodreads Author)",
        "description": "The circus arrives without warning. No announcements precede it. It is simply there, when yesterday it was not. Within the black-and-white striped canvas tents is an utterly unique experience full of breathtaking amazements. It is called Le Cirque des R\u00eaves, and it is only open at night. But behind the scenes, a fierce competition is underway\u2014a duel between two young magicians, Celia and Marco, who have been trained since childhood expressly for this purpose by their mercurial instructors. Unbeknownst to them, this is a game in which only one can be left standing, and the circus is but the stage for a remarkable battle of imagination and will. Despite themselves, however, Celia and Marco tumble headfirst into love\u2014a deep, magical love that makes the lights flicker and the room grow warm whenever they so much as brush hands. True love or not, the game must play out, and the fates of everyone involved, from the cast of extraordinary circus performers to the patrons, hang in the balance, suspended as precariously as the daring acrobats overhead. Written in rich, seductive prose, this spell-casting novel is a feast for the senses and the heart.",
        "language": "English",
        "isbn": "9780385534635",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Romance',
            'Historical Fiction',
            'Magic',
            'Young Adult',
            'Magical Realism',
            'Adult',
            'Audiobook',
            'Historical'
        
        ],
        "pages": 391,
        "awards": 
            ['Locus Award for Best First Novel (2012)',
            'Orange Prize Nominee for Fiction Longlist (2012)',
            'Guardian First Book Award Nominee for Longlist (2011)',
            'Mythopoeic Fantasy Award Nominee for Adult Literature (2012)',
            'ALA Alex Award (2012)',
            'Lincoln Award Nominee (2014)',
            'The Kitschies Nominee for Golden Tentacle (Debut) (2011)',
            'Goodreads Choice Award Nominee for Best Fantasy and for Favorite Book (2011)',
            'International Dublin Literary Award Nominee (2013)'
        
        ],
        "likedPercent": 91.0,
        "price": 7.02
    },
    {
        "id": 6487308,
        "title": "Fallen",
        "series": "Fallen #1",
        "author": "Lauren Kate (Goodreads Author)",
        "description": "There\u2019s something achingly familiar about Daniel Grigori.Mysterious and aloof, he captures Luce Price\u2019s attention from the moment she sees him on her first day at the Sword & Cross boarding school in sultry Savannah, Georgia. He\u2019s the one bright spot in a place where cell phones are forbidden, the other students are all screw-ups, and security cameras watch every move.Even though Daniel wants nothing to do with Luce\u2014and goes out of his way to make that very clear\u2014she can\u2019t let it go. Drawn to him like a moth to a flame, she has to find out what Daniel is so desperate to keep secret\u2026 even if it kills her.",
        "language": "English",
        "isbn": "9780385738934",
        "genres": 
            ['Young Adult',
            'Fantasy',
            'Romance',
            'Paranormal',
            'Angels',
            'Paranormal Romance',
            'Fiction',
            'Supernatural',
            'Urban Fantasy',
            'Teen'
        
        ],
        "pages": 452,
        "awards": 
            [''
        
        ],
        "likedPercent": 84.0,
        "price": 4.64
    },
    {
        "id": 7332,
        "title": "The Silmarillion",
        "series": "Middle-earth Universe",
        "author": "J.R.R. Tolkien, Christopher Tolkien (Editor), Ted Nasmith (Illustrator)",
        "description": "A number-one New York Times bestseller when it was originally published, THE SILMARILLION is the core of J.R.R. Tolkien's imaginative writing, a work whose origins stretch back to a time long before THE HOBBIT.Tolkien considered THE SILMARILLION his most important work, and, though it was published last and posthumously, this great collection of tales and legends clearly sets the stage for all his other writing. The story of the creation of the world and of the the First Age, this is the ancient drama to which the characters in THE LORD OF THE RINGS look back and in whose events some of them, such as Elrond and Galadriel, took part. The three Silmarils were jewels created by Feanor, most gifted of the Elves. Within them was imprisoned the Light of the Two Trees of Valinor before the Trees themselves were destroyed by Morgoth, the first Dark Lord. Thereafter, the unsullied Light of Valinor lived on only in the Silmarils, but they were seized by Morgoth and set in his crown, which was guarded in the impenetrable fortress of Angband in the north of Middle-earth. THE SILMARILLION is the history of the rebellion of Feanor and his kindred against the gods, their exile from Valinor and return to Middle-earth, and their war, hopeless despite all their heroism, against the great Enemy.This second edition features a letter written by J.R.R. Tolkien describing his intentions for the book, which serves as a brilliant exposition of his conception of the earlier Ages of Middle-earth.",
        "language": "English",
        "isbn": "9780618391110",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Classics',
            'High Fantasy',
            'Science Fiction Fantasy',
            'Epic Fantasy',
            'Mythology',
            'Literature',
            'Novels',
            'Adventure'
        
        ],
        "pages": 386,
        "awards": 
            ['Locus Award for Best Fantasy Novel (1978)',
            'Ditmar Award for Best International Long Fiction (1978)',
            'Gandalf Award (1978)'
        
        ],
        "likedPercent": 89.0,
        "price": 17.07
    },
    {
        "id": 514811,
        "title": "The Secret Magdalene",
        "series": "",
        "author": "Ki Longfellow (Goodreads Author)",
        "description": "Raised like sisters, Mariamne and Salome are indulged with riches, position, and learning\u2014a rare thing for females in Jerusalem. But Mariamne has a further gift: an illness has left her with visions; she has the power of prophecy. It is her prophesying that drives the two girls to flee to Egypt, where they study philosophy, mathematics, and astronomy in the Great Library of Alexandria.After seven years they return to a Judaea where many now believe John the Baptizer is the messiah. Salome too begins to believe, but Mariamne, now called Magdalene, is drawn to his cousin, Yeshu'a, a man touched by the divine in the same way she was during her days of illness. Together they speak of sharing their direct experience of God; but Yeshu'a unexpectedly gains a reputation as a healer, and as the ill and the troubled flock to him, he and Magdalene are forced to make a terrible decision.This radical retelling of the greatest story ever told brings Mary Magdalene to life\u2014not as a prostitute or demon-possessed\u2014but as an educated woman who was truly the \"apostle to the apostles.\"From the Hardcover edition.",
        "language": "English",
        "isbn": "9780307346667",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Religion',
            'Historical',
            'Spirituality',
            'Novels',
            'Contemporary',
            'Biblical Fiction',
            'Literature',
            'Biblical'
        
        ],
        "pages": 448,
        "awards": 
            [''
        
        ],
        "likedPercent": 87.0,
        "price": 5.6
    },
    {
        "id": 6149,
        "title": "Beloved",
        "series": "",
        "author": "Toni Morrison",
        "description": "Winner of the Pulitzer Prize, Toni Morrison\u2019s Beloved is a spellbinding and dazzlingly innovative portrait of a woman haunted by the past.Sethe was born a slave and escaped to Ohio, but eighteen years later she is still not free. She has borne the unthinkable and not gone mad, yet she is still held captive by memories of Sweet Home, the beautiful farm where so many hideous things happened. Meanwhile Sethe\u2019s house has long been troubled by the angry, destructive ghost of her baby, who died nameless and whose tombstone is engraved with a single word: Beloved.Sethe works at beating back the past, but it makes itself heard and felt incessantly in her memory and in the lives of those around her. When a mysterious teenage girl arrives, calling herself Beloved, Sethe\u2019s terrible secret explodes into the present.Combining the visionary power of legend with the unassailable truth of history, Morrison\u2019s unforgettable novel is one of the great and enduring works of American literature.",
        "language": "English",
        "isbn": "9781400033416",
        "genres": 
            ['Fiction',
            'Classics',
            'Historical Fiction',
            'Magical Realism',
            'Literature',
            'African American',
            'Historical',
            'Novels',
            'School',
            'Literary Fiction'
        
        ],
        "pages": 324,
        "awards": 
            ['Pulitzer Prize for Fiction (1988)',
            'American Book Award (1988)',
            'Anisfield-Wolf Book Award (1988)',
            'National Book Critics Circle Award Nominee for Fiction (1987)',
            'Frederic G. Melcher Book Award (1988)',
            'National Book Award Finalist for Fiction (1987)'
        
        ],
        "likedPercent": 88.0,
        "price": 3.8
    },
    {
        "id": 17690,
        "title": "The Trial",
        "series": "",
        "author": "Franz Kafka, Max Brod (Afterword), Willa Muir (Translator), Edwin Muir (Translator)",
        "description": "Written in 1914 but not published until 1925, a year after Kafka\u2019s death, The Trial is the terrifying tale of Josef K., a respectable bank officer who is suddenly and inexplicably arrested and must defend himself against a charge about which he can get no information. Whether read as an existential tale, a parable, or a prophecy of the excesses of modern bureaucracy wedded to the madness of totalitarianism, The Trial has resonated with chilling truth for generations of readers.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Philosophy',
            'German Literature',
            'Novels',
            'Dystopia',
            '20th Century',
            'Czech Literature',
            'Literary Fiction'
        
        ],
        "pages": 255,
        "awards": 
            ['\Helen and Kurt Wolff Translators Prize Nominee for Breon Mitchell (1999)\'
        
        ],
        "likedPercent": 91.0,
        "price": 18.766459486664385
    },
    {
        "id": 310612,
        "title": "A Confederacy of Dunces",
        "series": "",
        "author": "John Kennedy Toole, Walker Percy (Foreword)",
        "description": "Alternate cover for this ISBN can be found here\"A green hunting cap squeezed the top of the fleshy balloon of a head. The green earflaps, full of large ears and uncut hair and the fine bristles that grew in the ears themselves, stuck out on either side like turn signals indicating two directions at once. Full, pursed lips protruded beneath the bushy black moustache and, at their corners, sank into little folds filled with disapproval and potato chip crumbs.\"Meet Ignatius J. Reilly, the hero of John Kennedy Toole's tragicomic tale, A Confederacy of Dunces. This 30-year-old medievalist lives at home with his mother in New Orleans, pens his magnum opus on Big Chief writing pads he keeps hidden under his bed, and relays to anyone who will listen the traumatic experience he once had on a Greyhound Scenicruiser bound for Baton Rouge. (\"Speeding along in that bus was like hurtling into the abyss.\") But Ignatius's quiet life of tyrannizing his mother and writing his endless comparative history screeches to a halt when he is almost arrested by the overeager Patrolman Mancuso--who mistakes him for a vagrant--and then involved in a car accident with his tipsy mother behind the wheel. One thing leads to another, and before he knows it, Ignatius is out pounding the pavement in search of a job.Over the next several hundred pages, our hero stumbles from one adventure to the next. His stint as a hotdog vendor is less than successful, and he soon turns his employers at the Levy Pants Company on their heads. Ignatius's path through the working world is populated by marvelous secondary characters: the stripper Darlene and her talented cockatoo; the septuagenarian secretary Miss Trixie, whose desperate attempts to retire are constantly, comically thwarted; gay blade Dorian Greene; sinister Miss Lee, proprietor of the Night of Joy nightclub; and Myrna Minkoff, the girl Ignatius loves to hate. The many subplots that weave through A Confederacy of Dunces are as complicated as anything you'll find in a Dickens novel, and just as beautifully tied together in the end. But it is Ignatius--selfish, domineering, and deluded, tragic and comic and larger than life--who carries the story. He is a modern-day Quixote beset by giants of the modern age. His fragility cracks the shell of comic bluster, revealing a deep streak of melancholy beneath the antic humor. John Kennedy Toole committed suicide in 1969 and never saw the publication of his novel. Ignatius Reilly is what he left behind, a fitting memorial to a talented and tormented life.",
        "language": "English",
        "isbn": "9780802130204",
        "genres": 
            ['Fiction',
            'Classics',
            'Humor',
            'Literature',
            'Comedy',
            'Novels',
            'American',
            'Literary Fiction',
            'Audiobook',
            'Contemporary'
        
        ],
        "pages": 394,
        "awards": 
            ['Pulitzer Prize for Fiction (1981)',
            'PEN/Faulkner Award for Fiction Nominee (1981)',
            'Los Angeles Times Book Prize Nominee for Fiction (1980)'
        
        ],
        "likedPercent": 86.0,
        "price": 5.91
    },
    {
        "id": 3876,
        "title": "The Sun Also Rises",
        "series": "",
        "author": "Ernest Hemingway",
        "description": "The quintessential novel of the Lost Generation, The Sun Also Rises is one of Ernest Hemingway's masterpieces, and a classic example of his spare but powerful writing style. A poignant look at the disillusionment and angst of the post-World War I generation, the novel introduces two of Hemingway's most unforgettable characters: Jake Barnes and Lady Brett Ashley. The story follows the flamboyant Brett and the hapless Jake as they journey from the wild nightlife of 1920s Paris to the brutal bullfighting rings of Spain with a motley group of expatriates. It is an age of moral bankruptcy, spiritual dissolution, unrealized love, and vanishing illusions. First published in 1926, The Sun Also Rises helped to establish Hemingway as one of the greatest writers of the twentieth century.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Novels',
            'American',
            'Historical Fiction',
            'Spain',
            'School',
            'Classic Literature',
            '20th Century'
        
        ],
        "pages": 189,
        "awards": 
            [''
        
        ],
        "likedPercent": 89.0,
        "price": 17.933935462535505
    },
    {
        "id": 10507293,
        "title": "The Selection",
        "series": "The Selection #1",
        "author": "Kiera Cass (Goodreads Author)",
        "description": "For thirty-five girls, the Selection is the chance of a lifetime. The opportunity to escape the life laid out for them since birth. To be swept up in a world of glittering gowns and priceless jewels. To live in a palace and compete for the heart of gorgeous Prince Maxon.But for America Singer, being Selected is a nightmare. It means turning her back on her secret love with Aspen, who is a caste below her. Leaving her home to enter a fierce competition for a crown she doesn't want. Living in a palace that is constantly threatened by violent rebel attacks.Then America meets Prince Maxon. Gradually, she starts to question all the plans she's made for herself\u2014and realizes that the life she's always dreamed of may not compare to a future she never imagined.",
        "language": "English",
        "isbn": "9780062059932",
        "genres": 
            ['Young Adult',
            'Romance',
            'Dystopia',
            'Fantasy',
            'Fiction',
            'Science Fiction',
            'Audiobook',
            'Teen',
            'Chick Lit',
            'Young Adult Fantasy'
        
        ],
        "pages": 336,
        "awards": 
            ['Lincoln Award Nominee (2015)',
            'Goodreads Choice Award Nominee for Young Adult Fantasy & Science Fiction (2012)'
        
        ],
        "likedPercent": 92.0,
        "price": 5.01
    },
    {
        "id": 144974,
        "title": "The Velveteen Rabbit",
        "series": "",
        "author": "Margery Williams Bianco, William Nicholson (Illustrator)",
        "description": "Nursery magic is very strange and wonderful, and only those playthings that are old and wise and experienced like the Skin Horse understand all about it.Like the Skin Horse, Margery Williams understood how toys\u2014and people\u2014become real through the wisdom and experience of love. This reissue of a favorite classic, with the original story and illustrations as they first appeared in 1922, will work its magic for all who read it.",
        "language": "English",
        "isbn": "9780380002559",
        "genres": 
            ['Childrens',
            'Classics',
            'Fiction',
            'Picture Books',
            'Fantasy',
            'Animals',
            'Young Adult',
            'Juvenile',
            'Kids',
            'Short Stories'
        
        ],
        "pages": 40,
        "awards": 
            ['Lewis Carroll Shelf Award (1971)'
        
        ],
        "likedPercent": 95.0,
        "price": 5.9
    },
    {
        "id": 6148028,
        "title": "Catching Fire",
        "series": "The Hunger Games #2",
        "author": "Suzanne Collins",
        "description": "SPARKS ARE IGNITING.FLAMES ARE SPREADING.AND THE CAPITAL WANTS REVENGE.Against all odds, Katniss Everdeen has survived the Hunger Games. She and fellow District 12 tribute Peeta Mellark are miraculously still alive. Katniss should be relieved, happy even. Yet nothing is the way Katniss wishes it to be. Gale holds her at an icy distance. Peeta has turned his back on her completely. And there are whispers of a rebellion against the Capitol - a rebellion that Katniss and Peeta may have helped create.Much to her shock, Katniss has fueled an unrest that she's afraid she cannot stop. And what scares her even more is that she's not entirely convinced she should try. As time draws near for Katniss and Peeta to visit the districts on the Capitol's cruel Victory Tour, the stakes are higher than ever. If they can't prove, without a shadow of a doubt, that they are lost in their love for each other, the consequences will be horrifying. Katniss is about to be tested as never before.",
        "language": "English",
        "isbn": "9780439023498",
        "genres": 
            ['Young Adult',
            'Dystopia',
            'Fiction',
            'Fantasy',
            'Science Fiction',
            'Romance',
            'Adventure',
            'Teen',
            'Post Apocalyptic',
            'Action'
        
        ],
        "pages": 391,
        "awards": 
            ['Locus Award Nominee for Best Young Adult Book (2010)',
            'Golden Duck Award for Young Adult (Hal Clement Award) (2010)',
            'Soaring Eagle Book Award (2011)',
            '\Childrens Choice Book Award for Teen Choice Book of the Year (2010)\',
            'Indies Choice Book Award for Young Adult (2010)',
            'Teen Read Award Nominee for Best Read (2010)',
            'DABWAHA Romance Tournament for Best Young Adult (2010)',
            'Goodreads Choice Award for Favorite Book and Young Adult Series (2009) and Nominee for Best of the Best  (2018)',
            'Premio El Templo de las Mil Puertas Nominee for Mejor novela extranjera perteneciente a saga (2010)'
        
        ],
        "likedPercent": 97.0,
        "price": 3.66
    },
    {
        "id": 7736182,
        "title": "The Lost Hero",
        "series": "The Heroes of Olympus #1",
        "author": "Rick Riordan (Goodreads Author)",
        "description": "JASON HAS A PROBLEM. He doesn\u2019t remember anything before waking up in a bus full of kids on a field trip. Apparently he has a girlfriend named Piper, and his best friend is a guy named Leo. They\u2019re all students at the Wilderness School, a boarding school for \u201cbad kids,\" as Leo puts it. What did Jason do to end up here? And where is here, exactly? Jason doesn't know anything\u2014except that everything seems very wrong.PIPER HAS A SECRET. Her father has been missing for three days, ever since she had that terrifying nightmare about his being in trouble. Piper doesn\u2019t understand her dream, or why her boyfriend suddenly doesn\u2019t recognize her. When a freak storm hits during the school trip, unleashing strange creatures and whisking her, Jason, and Leo away to someplace called Camp Half-Blood, she has a feeling she\u2019s going to find out, whether she wants to or not.LEO HAS A WAY WITH TOOLS. When he sees his cabin at Camp Half-Blood, filled with power tools and machine parts, he feels right at home. But there\u2019s weird stuff, too\u2014like the curse everyone keeps talking about, and some camper who's gone missing. Weirdest of all, his bunkmates insist that each of them\u2014including Leo\u2014is related to a god. Does this have anything to do with Jason's amnesia, or the fact that Leo keeps seeing ghosts?Join new and old friends from Camp Half-Blood in this thrilling first book in The Heroes of Olympus series. Best-selling author Rick Riordan has pumped up the action, humor, suspense, and mystery in an epic adventure that will leave readers panting for the next installment.",
        "language": "English",
        "isbn": "9781423113393",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Mythology',
            'Fiction',
            'Middle Grade',
            'Adventure',
            'Childrens',
            'Greek Mythology',
            'Urban Fantasy',
            'Young Adult Fantasy'
        
        ],
        "pages": 553,
        "awards": 
            ['\West Australian Young Readers Book Award (WAYRBA) for Older Readers (2011)\',
            'Evergreen Teen Book Award (2013)',
            'Goodreads Choice Award Nominee for Young Adult Fantasy and for Favorite Book (2010)'
        
        ],
        "likedPercent": 96.0,
        "price": 10.25
    },
    {
        "id": 7896527,
        "title": "Throne of Glass",
        "series": "Throne of Glass #1",
        "author": "Sarah J. Maas (Goodreads Author)",
        "description": "This is a previously published edition of  ISBN13: 9781599906959.After serving out a year of hard labor in the salt mines of Endovier for her crimes, 18-year-old assassin Celaena Sardothien is dragged before the Crown Prince. Prince Dorian offers her her freedom on one condition: she must act as his champion in a competition to find a new royal assassin.Her opponents are men-thieves and assassins and warriors from across the empire, each sponsored by a member of the king's council. If she beats her opponents in a series of eliminations, she'll serve the kingdom for four years and then be granted her freedom. Celaena finds her training sessions with the captain of the guard, Westfall, challenging and exhilarating. But she's bored stiff by court life. Things get a little more interesting when the prince starts to show interest in her ... but it's the gruff Captain Westfall who seems to understand her best.Then one of the other contestants turns up dead ... quickly followed by another. Can Celaena figure out who the killer is before she becomes a victim? As the young assassin investigates, her search leads her to discover a greater destiny than she could possibly have imagined.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Romance',
            'Fiction',
            'Magic',
            'Young Adult Fantasy',
            'High Fantasy',
            'New Adult',
            'Adventure',
            'Paranormal'
        
        ],
        "pages": 406,
        "awards": 
            ['Lincoln Award Nominee (2015)',
            'North Carolina Young Adult Book Award for High School (2015)',
            'Goodreads Choice Award Nominee for Young Adult Fantasy & Science Fiction (2012)'
        
        ],
        "likedPercent": 93.0,
        "price": 5.362245189038656
    },
    {
        "id": 6479259,
        "title": "Spirit Bound",
        "series": "Vampire Academy #5",
        "author": "Richelle Mead (Goodreads Author)",
        "description": "Salvation has its price . . .The words stunned Adrian for a moment, but he kept going. \"You're lying. What you're describing is impossible. There's no way to save a Strigoi. When they're gone, they're gone. They're dead. Undead. Forever.\"Robert's next words weren't directed at Adrian. They were spoken to me. \"That which is dead doesn't always stay dead....\"After a long and heartbreaking journey to Siberia, Dimitri\u2019s birthplace, Rose Hathaway has finally returned to St. Vladimir\u2019s\u2014and to her best friend, Lissa Dragomir. It's graduation, and the girls can\u2019t wait for their real lives outside the academy\u2019s cold iron gates to finally begin. But even with the intrigue and excitement of court life looming, Rose\u2019s heart still aches for Dimitri. He\u2019s out there, somewhere.She failed to kill him when she had the chance, and now her worst fears are about to come true. Dimitri has tasted her blood, and she knows in her heart that he is hunting her. And if Rose won't join him, he won't rest until he has silenced her . . . forever.But Rose can't forget what she learned on her journey\u2014whispers of a magic too impossible and terrifying to comprehend. A magic inextricably tied to Lissa that could hold the answer to all of Rose's prayers, but not without devastating consequences. Now Rose will have to decide what\u2014and who\u2014matters most to her. And in the end, is true love really worth the price?Fall in love with Rose and Dimitri all over again in Spirit Bound, the eagerly awaited fifth novel in Richelle Mead's enthralling Vampire Academy series.",
        "language": "English",
        "isbn": "9781595142504",
        "genres": 
            ['Young Adult',
            'Vampires',
            'Fantasy',
            'Paranormal',
            'Romance',
            'Urban Fantasy',
            'Paranormal Romance',
            'Supernatural',
            'Fiction',
            'Magic'
        
        ],
        "pages": 489,
        "awards": 
            ['\Childrens Choice Book Award Nominee for Teen Choice Book of the Year (2011)\',
            'Teen Read Award Nominee for Best Series (2010)',
            'Goodreads Choice Award for Goodreads Author and Nominee for Favorite Book (2010)'
        
        ],
        "likedPercent": 96.0,
        "price": 4.59
    },
    {
        "id": 10025305,
        "title": "Clockwork Prince",
        "series": "The Infernal Devices #2",
        "author": "Cassandra Clare (Goodreads Author)",
        "description": "In the magical underworld of Victorian London, Tessa Gray has at last found safety with the Shadowhunters. But that safety proves fleeting when rogue forces in the Clave plot to see her protector, Charlotte, replaced as head of the Institute. If Charlotte loses her position, Tessa will be out on the street\u2014and easy prey for the mysterious Magister, who wants to use Tessa\u2019s powers for his own dark ends.With the help of the handsome, self-destructive Will and the fiercely devoted Jem, Tessa discovers that the Magister\u2019s war on the Shadowhunters is deeply personal. He blames them for a long-ago tragedy that shattered his life. To unravel the secrets of the past, the trio journeys from mist-shrouded Yorkshire to a manor house that holds untold horrors, from the slums of London to an enchanted ballroom where Tessa discovers that the truth of her parentage is more sinister than she had imagined. When they encounter a clockwork demon bearing a warning for Will, they realize that the Magister himself knows their every move\u2014and that one of their own has betrayed them.Tessa finds her heart drawn more and more to Jem, but her longing for Will, despite his dark moods, continues to unsettle her. But something is changing in Will\u2014the wall he has built around himself is crumbling. Could finding the Magister free Will from his secrets and give Tessa the answers about who she is and what she was born to do?As their dangerous search for the Magister and the truth leads the friends into peril, Tessa learns that when love and lies are mixed, they can corrupt even the purest heart.",
        "language": "English",
        "isbn": "9781416975885",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Romance',
            'Paranormal',
            'Steampunk',
            'Historical Fiction',
            'Urban Fantasy',
            'Fiction',
            'Angels',
            'Vampires'
        
        ],
        "pages": 498,
        "awards": 
            ['Teen Buckeye Book Award Nominee (2012)',
            '\Childrens Choice Book Award Nominee for Teen Choice Book of the Year (2012)\'
        
        ],
        "likedPercent": 97.0,
        "price": 5.69
    },
    {
        "id": 1375,
        "title": "The Iliad/The Odyssey",
        "series": "",
        "author": "Homer, Robert Fagles (Translator), Bernard Knox (Introduction)",
        "description": "Gripping listeners and readers for more than 2,700 years, 'The Iliad' is the story of the Trojan War and the rage of Achilles. Combining the skills of a poet and scholar, Robert Fagles brings the energy of contemporary language to this enduring heroic epic. If 'The Iliad' is the world's greatest war story, then 'The Odyssey' is literature's greatest evocation of every man's journey through life. Here again, Fagles has performed the translator's task magnificently, giving us an Odyssey to read aloud, to savor, and to treasure for its sheer lyrical mastery. Each volume contains a superb introduction with textual and critical commentary by renowned classicist Bernard Knox.",
        "language": "English",
        "isbn": "9780147712554",
        "genres": 
            ['Classics',
            'Fiction',
            'Poetry',
            'Mythology',
            'Literature',
            'Fantasy',
            'Historical Fiction',
            'School',
            'Adventure',
            'Historical'
        
        ],
        "pages": 1556,
        "awards": 
            [''
        
        ],
        "likedPercent": 93.0,
        "price": 6.15
    },
    {
        "id": 17250,
        "title": "The Crucible",
        "series": "",
        "author": "Arthur Miller, Christopher Bigs(Introduction)",
        "description": "\"I believe that the reader will discover here the essential nature of one of the strangest and most awful chapters in human history,\" Arthur Miller wrote of his classic play about the witch-hunts and trials in seventeenth-century Salem, Massachusetts. Based on historical people and real events, Miller's drama is a searing portrait of a community engulfed by hysteria. In the rigid theocracy of Salem, rumors that women are practicing witchcraft galvanize the town's most basic fears and suspicions; and when a young girl accuses Elizabeth Proctor of being a witch, self-righteous church leaders and townspeople insist that Elizabeth be brought to trial. The ruthlessness of the prosecutors and the eagerness of neighbor to testify against neighbor brilliantly illuminates the destructive power of socially sanctioned violence.Written in 1953, The Crucible is a mirror Miller uses to reflect the anti-communist hysteria inspired by Senator Joseph McCarthy's \"witch-hunts\" in the United States. Within the text itself, Miller contemplates the parallels, writing, \"Political opposition... is given an inhumane overlay, which then justifies the abrogation of all normally applied customs of civilized behavior. A political policy is equated with moral right, and opposition to it with diabolical malevolence.\"WIth an introduction by Christopher Bigsby.(back cover)",
        "language": "English",
        "isbn": "9780142437339",
        "genres": 
            ['Classics',
            'Plays',
            'Fiction',
            'Historical Fiction',
            'Drama',
            'School',
            'Read For School',
            'Historical',
            'High School',
            'Literature'
        
        ],
        "pages": 143,
        "awards": 
            ['\New York Drama Critics Circle Award Nominee for Best American Play (1953)\'
        
        ],
        "likedPercent": 86.0,
        "price": 3.98
    },
    {
        "id": 135479,
        "title": "Cat's Cradle",
        "series": "",
        "author": "Kurt Vonnegut Jr.",
        "description": "Told with deadpan humour and bitter irony, Kurt Vonnegut's cult tale of global destruction preys on our deepest fears of witnessing Armageddon and, worse still, surviving it ...Dr Felix Hoenikker, one of the founding 'fathers' of the atomic bomb, has left a deadly legacy to the world. For he's the inventor of 'ice-nine', a lethal chemical capable of freezing the entire planet. The search for its whereabouts leads to Hoenikker's three ecentric children, to a crazed dictator in the Caribbean, to madness. Felix Hoenikker's Death Wish comes true when his last, fatal gift to humankind brings about the end, that for all of us, is nigh...",
        "language": "English",
        "isbn": "9780140285604",
        "genres": 
            ['Fiction',
            'Classics',
            'Science Fiction',
            'Humor',
            'Literature',
            'Novels',
            'Dystopia',
            'American',
            'Fantasy',
            '20th Century'
        
        ],
        "pages": 179,
        "awards": 
            ['Hugo Award Nominee for Best Novel (1964)'
        
        ],
        "likedPercent": 96.0,
        "price": 5.69
    },
    {
        "id": 9777,
        "title": "The God of Small Things",
        "series": "",
        "author": "Arundhati Roy (Goodreads Author), Claude Demanuelli (Translator), Barbara Auer (Narrator), Diana Quick (Reading), Luana Stoica (trad.), Donada Peters (Narrator), Josep Juli\u00e0 Ballb\u00e9 (Translator)",
        "description": "The year is 1969. In the state of Kerala, on the southernmost tip of India, a skyblue Plymouth with chrome tailfins is stranded on the highway amid a Marxist workers' demonstration. Inside the car sit two-egg twins Rahel and Esthappen, and so begins their tale. . . .Armed only with the invincible innocence of children, they fashion a childhood for themselves in the shade of the wreck that is their family--their lonely, lovely mother, Ammu (who loves by night the man her children love by day), their blind grandmother, Mammachi (who plays Handel on her violin), their beloved uncle Chacko (Rhodes scholar, pickle baron, radical Marxist, bottom-pincher), their enemy, Baby Kochamma (ex-nun and incumbent grandaunt), and the ghost of an imperial entomologist's moth (with unusually dense dorsal tufts).When their English cousin, Sophie Mol, and her mother, Margaret Kochamma, arrive on a Christmas visit, Esthappen and Rahel learn that Things Can Change in a Day. That lives can twist into new, ugly shapes, even cease forever, beside their river \"graygreen.\" With fish in it. With the sky and trees in it. And at night, the broken yellow moon in it.The brilliantly plotted story uncoils with an agonizing sense of foreboding and inevitability. Yet nothing prepares you for what lies at the heart of it.The God of Small Things takes on the Big Themes--Love. Madness. Hope. Infinite Joy. Here is a writer who dares to break the rules. To dislocate received rhythms and create the language she requires, a language that is at once classical and unprecedented. Arundhati Roy has given us a book that is anchored to anguish, but fueled by wit and magic. --front flap",
        "language": "English",
        "isbn": "9780679457312",
        "genres": 
            ['Fiction',
            'India',
            'Historical Fiction',
            'Contemporary',
            'Novels',
            'Indian Literature',
            'Literary Fiction',
            'Literature',
            'Classics',
            'Asia'
        
        ],
        "pages": 340,
        "awards": 
            ['Booker Prize (1997)',
            'International Dublin Literary Award Nominee (1999)'
        
        ],
        "likedPercent": 90.0,
        "price": 3.17
    },
    {
        "id": 5659,
        "title": "The Wind in the Willows",
        "series": "",
        "author": "Kenneth Grahame, Gillian Avery (Introduction)",
        "description": "\"There is nothing half so much worth doing as simply messing around in boats.\"\r\n\r\nWhen Mole flees his little underground home he discovers new friends and adventures with Raj, Toad and Badger.\r\n\r\nThis much-loved story has been carefully retold for young children to enjoy. With beautiful illustrations throughout, it provides the perfect introduction to a classic tale.",
        "language": "English",
        "isbn": "9780143039099",
        "genres": 
            ['Classics',
            'Fiction',
            'Childrens',
            'Fantasy',
            'Animals',
            'Young Adult',
            'Adventure',
            'Literature',
            'Middle Grade',
            'Audiobook'
        
        ],
        "pages": 197,
        "awards": 
            ['Lewis Carroll Shelf Award (1958)',
            'Australian Book Industry Award (ABIA) Nominee for Older Children (ages 8-14) (2008)'
        
        ],
        "likedPercent": 92.0,
        "price": 4.18
    },
    {
        "id": 8130077,
        "title": "The Screwtape Letters",
        "series": "",
        "author": "C.S. Lewis",
        "description": "The Screwtape Letters by C.S.\u00a0 Lewis is a classic masterpiece of religious satire that entertains readers with its sly and ironic portrayal of human life and foibles from the vantage point of Screwtape, a highly placed assistant to \"Our Father Below.\" At once wildly comic, deadly serious, and strikingly original, C.S. Lewis's The Screwtape Letters is the most engaging account of temptation\u2014and triumph over it\u2014ever written.\u00a0",
        "language": "English",
        "isbn": "B002BD2V2Y",
        "genres": 
            ['Fiction',
            'Classics',
            'Christian',
            'Religion',
            'Christianity',
            'Fantasy',
            'Theology',
            'Christian Fiction',
            'Faith',
            'Philosophy'
        
        ],
        "pages": 228,
        "awards": 
            ['Nautilus Book Award for Audio Books & Spoken Word (2010)',
            'Audie Award for Classic (2000)'
        
        ],
        "likedPercent": 94.0,
        "price": 17.103635984612218
    },
    {
        "id": 2865,
        "title": "Girl with a Pearl Earring",
        "series": "",
        "author": "Tracy Chevalier (Goodreads Author)",
        "description": "With precisely 35 canvases to his credit, the Dutch painter Johannes Vermeer represents one of the great enigmas of 17th-century art. The meager facts of his biography have been gleaned from a handful of legal documents. Yet Vermeer's extraordinary paintings of domestic life, with their subtle play of light and texture, have come to define the Dutch golden age. His portrait of the anonymous Girl with a Pearl Earring has exerted a particular fascination for centuries\u2014and it is this magnetic painting that lies at the heart of Tracy Chevalier's second novel of the same title.Girl with a Pearl Earring centers on Vermeer's prosperous Delft household during the 1660s. When Griet, the novel's quietly perceptive heroine, is hired as a servant, turmoil follows. First, the 16-year-old narrator becomes increasingly intimate with her master. Then Vermeer employs her as his assistant\u2014and ultimately has Griet sit for him as a model.",
        "language": "English",
        "isbn": "9780452287020",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Historical',
            'Classics',
            'Art',
            'Romance',
            'Adult Fiction',
            'Adult',
            'Novels',
            'Literature'
        
        ],
        "pages": 233,
        "awards": 
            ['Orange Prize Nominee for Fiction Longlist (2000)',
            'ALA Alex Award (2001)',
            'Lincoln Award Nominee (2006)',
            'Premi Llibreter de narrativa Nominee (2001)'
        
        ],
        "likedPercent": 92.0,
        "price": 2.86
    },
    {
        "id": 561909,
        "title": "The Hiding Place: The Triumphant True Story of Corrie Ten Boom",
        "series": "",
        "author": "Corrie ten Boom, John Sherrill, Elizabeth Sherrill (Goodreads Author)",
        "description": "At one time Corrie ten Boom would have laughed at the idea that there would ever be a story to tell. For the first fifty years of her life nothing at all out of the ordinary had ever happened to her. She was an old-maid watchmaker living contentedly with her spinster sister and their elderly father in the tiny Dutch house over their shop. Their uneventful days, as regulated as their own watches, revolved around their abiding love for one another. However, with the Nazi invasion and occupation of Holland, a story did ensue. Corrie ten Boom and her family became leaders in the Dutch Underground, hiding Jewish people in their home in a specially built room and aiding their escape from the Nazis. For their help, all but Corrie found death in a concentration camp. The Hiding Place is their story.",
        "language": "English",
        "isbn": "9780553256697",
        "genres": 
            ['Nonfiction',
            'Biography',
            'History',
            'Christian',
            'Classics',
            'Memoir',
            'Holocaust',
            'World War II',
            'Historical',
            'Autobiography'
        
        ],
        "pages": 242,
        "awards": 
            [''
        
        ],
        "likedPercent": 95.0,
        "price": 4.17
    },
    {
        "id": 30118,
        "title": "A Light in the Attic",
        "series": "",
        "author": "Shel Silverstein",
        "description": "Last night while I lay thinking here Some Whatifs crawled inside my ear And pranced and partied all night long And sang their same old Whatif song: Whatif I flunk that test?Whatif green hair grows on my chest?Whatif nobody likes me?Whatif a bolt of lightning strikes me?...This 20th anniversary of Shel Silverstein's A Light in the Attic includes a CD of highlights from his Grammy Award-winning album.Here in the attic of Shel Silverstein you will find Backward Bill, Sour Face Ann, the Meehoo with an Exactlywatt, and the Polar Bear in the Frigidaire. You will talk with Broiled Face, and find out what happens when Somebody steals your knees, you get caught by the Quick-Digesting Gink, a Mountain snores, and They Put a Brassiere on the Camel.From the creator of the beloved poetry collections Where the Sidewalk Ends and Falling Up, here is another wondrous book of poems and drawings.",
        "language": "English",
        "isbn": "9780060513061",
        "genres": 
            ['Poetry',
            'Childrens',
            'Classics',
            'Fiction',
            'Humor',
            'Young Adult',
            'Picture Books',
            'Juvenile',
            'Middle Grade',
            'Banned Books'
        
        ],
        "pages": 176,
        "awards": 
            ['\George C. Stone Center for Childrens Books Recognition of Merit Award (1984)\',
            'Magnesia Litera for Translation (Litera za p\u0159ekladovou knihu) (2015)',
            'Garden State Book Award',
            'Vlag en Wimpel Griffeljury (1985)',
            '\William Allen White Childrens Book Award (1984)\'
        
        ],
        "likedPercent": 96.0,
        "price": 12.08
    },
    {
        "id": 23807,
        "title": "The Silence of the Lambs",
        "series": "Hannibal Lecter #2",
        "author": "Thomas Harris",
        "description": "Hannibal Lecter. The ultimate villain of modern fiction. Read the five-million-copy bestseller that scared the world silent. The Silence of the Lambs. A young FBI trainee. An evil genius locked away for unspeakable crimes. A plunge into the darkest chambers of a psychopath's mind--in the deadly search for a serial killer. - back cover",
        "language": "English",
        "isbn": "9780099446781",
        "genres": 
            ['Horror',
            'Fiction',
            'Thriller',
            'Mystery',
            'Crime',
            'Suspense',
            'Mystery Thriller',
            'Classics',
            'Novels',
            'Drama'
        
        ],
        "pages": 421,
        "awards": 
            ['Bram Stoker Award for Best Novel (1988)',
            'World Fantasy Award Nominee for Best Novel (1989)',
            'Anthony Award for Best Novel (1989)',
            'Grand Prix de Litt\u00e9rature Polici\u00e8re for Romans \u00e9trangers (1991)',
            '\u3053\u306e\u30df\u30b9\u30c6\u30ea\u30fc\u304c\u3059\u3054\u3044\uff01 for Best Translated Mystery Novel of the Year in Japan (1989)'
        
        ],
        "likedPercent": 94.0,
        "price": 3.11
    },
    {
        "id": 6068551,
        "title": "Shiver",
        "series": "The Wolves of Mercy Falls #1",
        "author": "Maggie Stiefvater (Goodreads Author)",
        "description": "For years, Grace has watched the wolves in the woods behind her house. One yellow-eyed wolf\u2014her wolf\u2014is a chilling presence she can't seem to live without.Meanwhile, Sam has lived two lives: In winter, the frozen woods, the protection of the pack, and the silent company of a fearless girl. In summer, a few precious months of being human\u2026 until the cold makes him shift back again.Now, Grace meets a yellow-eyed boy whose familiarity takes her breath away. It's her wolf. It has to be. But as winter nears, Sam must fight to stay human\u2014or risk losing himself, and Grace, forever.",
        "language": "English",
        "isbn": "9780545123266",
        "genres": 
            ['Young Adult',
            'Fantasy',
            'Romance',
            'Paranormal',
            'Werewolves',
            'Fiction',
            'Paranormal Romance',
            'Supernatural',
            'Urban Fantasy',
            'Teen'
        
        ],
        "pages": 392,
        "awards": 
            ['Georgia Peach Book Award (2010)',
            '\Pennsylvania Young Readers Choice Award Nominee (2011)\',
            '\Childrens Choice Book Award Nominee for Teen Choice Book of the Year (2010)\',
            'Florida Teens Read Nominee (2010)',
            'Teen Read Award Nominee for Best Read (2010)',
            'The Inky Awards for Silver Inky (2010)',
            'Lincoln Award Nominee (2012)',
            'The Inky Awards Shortlist for Silver Inky (2010)',
            'Missouri Gateway Readers Award Nominee (2012)',
            'Premi Protagonista Jove for Categoria 15-16 anys (2011)'
        
        ],
        "likedPercent": 86.0,
        "price": 7.05
    },
    {
        "id": 24770,
        "title": "Uglies",
        "series": "Uglies #1",
        "author": "Scott Westerfeld (Goodreads Author)",
        "description": "Tally is about to turn sixteen, and she can't wait. In just a few weeks she'll have the operation that will turn her from a repellent ugly into a stunning pretty. And as a pretty, she'll be catapulted into a high-tech paradise where her only job is to have fun.But Tally's new friend Shay isn't sure she wants to become a pretty. When Shay runs away, Tally learns about a whole new side of the pretty world\u2014and it isn't very pretty. The authorities offer Tally a choice: find her friend and turn her in, or never turn pretty at all. Tally's choice will change her world forever....",
        "language": "English",
        "isbn": "9780689865381",
        "genres": 
            ['Young Adult',
            'Dystopia',
            'Science Fiction',
            'Fiction',
            'Fantasy',
            'Romance',
            'Teen',
            'Adventure',
            'Post Apocalyptic',
            'Science Fiction Fantasy'
        
        ],
        "pages": 425,
        "awards": 
            ['Georgia Peach Book Award Nominee for Honor book (2008)',
            'Golden Duck Award for Young Adult (Hal Clement Award) (2006)',
            'Ditmar Award Nominee for Best Novel (2006)',
            'South Carolina Book Award Nominee for Young Adult Book Award (2008)',
            'Rhode Island Teen Book Award Nominee (2007)',
            'Eliot Rosewater Indiana High School Book Award (2007)',
            'Lincoln Award (2007)',
            'Prix Et-lisez-moi (2009)',
            'Missouri Gateway Readers Award Nominee (2008)'
        
        ],
        "likedPercent": 89.0,
        "price": 3.58
    },
    {
        "id": 6752378,
        "title": "City of Fallen Angels",
        "series": "The Mortal Instruments #4",
        "author": "Cassandra Clare (Goodreads Author)",
        "description": "The Mortal War is over, and sixteen-year-old Clary Fray is back home in New York, excited about all the possibilities before her. She\u2019s training to become a Shadowhunter and to use her unique power. Her mother is getting married to the love of her life. Downworlders and Shadowhunters are at peace at last. And\u2014most importantly of all\u2014she can finally call Jace her boyfriend.But nothing comes without a price.Someone is murdering Shadowhunters, provoking tensions between Downworlders and Shadowhunters that could lead to a second, bloody war. Clary\u2019s best friend, Simon, can\u2019t help her\u2014his mother just found out that he\u2019s a vampire, and now he\u2019s homeless. When Jace begins to pull away from her without explaining why, Clary is forced to delve into the heart of a mystery whose solution reveals her worst nightmare: she herself has set in motion a terrible chain of events that could lead to her losing everything she loves. Even Jace.",
        "language": "English",
        "isbn": "9781442403543",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Paranormal',
            'Romance',
            'Urban Fantasy',
            'Vampires',
            'Fiction',
            'Angels',
            'Supernatural',
            'Magic'
        
        ],
        "pages": 425,
        "awards": 
            ['Goodreads Choice Award for Goodreads Author and Nominee for Favorite Book and for Young Adult Fantasy & Science Fiction (2011)'
        
        ],
        "likedPercent": 94.0,
        "price": 4.75
    },
    {
        "id": 4069,
        "title": "Man's Search for Meaning",
        "series": "",
        "author": "Viktor E. Frankl, Harold S. Kushner (Foreword), William J. Winslade (Afterword), Isle Lasch (Translator)",
        "description": "Psychiatrist Viktor Frankl's memoir has riveted generations of readers with its descriptions of life in Nazi death camps and its lessons for spiritual survival. Based on his own experience and the stories of his patients, Frankl argues that we cannot avoid suffering but we can choose how to cope with it, find meaning in it, and move forward with renewed purpose. At the heart of his theory, known as logotherapy, is a conviction that the primary human drive is not pleasure but the pursuit of what we find meaningful. Man's Search for Meaning has become one of the most influential books in America; it continues to inspire us all to find significance in the very act of living.",
        "language": "English",
        "isbn": "9780807014295",
        "genres": 
            ['Nonfiction',
            'Psychology',
            'Philosophy',
            'History',
            'Memoir',
            'Self Help',
            'Biography',
            'Classics',
            'Holocaust',
            'Spirituality'
        
        ],
        "pages": 165,
        "awards": 
            [''
        
        ],
        "likedPercent": 96.0,
        "price": 7.37
    },
    {
        "id": 5203,
        "title": "She's Come Undone",
        "series": "",
        "author": "Wally Lamb (Goodreads Author)",
        "description": "In this extraordinary coming-of-age odyssey, Wally Lamb invites us to hitch a wild ride on a journey of love, pain, and renewal with the most heartbreakingly comical heroine to come along in years.Meet Dolores Price. She's 13, wise-mouthed but wounded, having bid her childhood goodbye. Stranded in front of her bedroom TV, she spends the next few years nourishing herself with the Mallomars, potato chips, and Pepsi her anxious mother supplies. When she finally orbits into young womanhood at 257 pounds, Dolores is no stronger and life is no kinder. But this time she's determined to rise to the occasion and give herself one more chance before she really goes under.",
        "language": "English",
        "isbn": "9780671021009",
        "genres": 
            ['Fiction',
            'Contemporary',
            'Chick Lit',
            'Adult Fiction',
            'Novels',
            'Coming Of Age',
            'Adult',
            'Literary Fiction',
            'Drama',
            'Mental Illness'
        
        ],
        "pages": 465,
        "awards": 
            ['Los Angeles Times Book Prize'
        
        ],
        "likedPercent": 89.0,
        "price": 1.91
    },
    {
        "id": 480204,
        "title": "The Phantom of the Opera",
        "series": "",
        "author": "Gaston Leroux, Alexander Teixeira de Mattos (Translator)",
        "description": "First published in French as a serial in 1909, The Phantom of the Opera is a riveting story that revolves around the young, Swedish Christine Daa\u00e9. Her father, a famous musician, dies, and she is raised in the Paris Opera House with his dying promise of a protective angel of music to guide her. After a time at the opera house, she begins hearing a voice, who eventually teaches her how to sing beautifully. All goes well until Christine's childhood friend Raoul comes to visit his parents, who are patrons of the opera, and he sees Christine when she begins successfully singing on the stage. The voice, who is the deformed, murderous 'ghost' of the opera house named Erik, however, grows violent in his terrible jealousy, until Christine suddenly disappears. The phantom is in love, but it can only spell disaster.Leroux's work, with characters ranging from the spoiled prima donna Carlotta to the mysterious Persian from Erik's past, has been immortalized by memorable adaptations. Despite this, it remains a remarkable piece of Gothic horror literature in and of itself, deeper and darker than any version that follows.",
        "language": "English",
        "isbn": "9780060809249",
        "genres": 
            ['Classics',
            'Fiction',
            'Horror',
            'Romance',
            'Gothic',
            'Mystery',
            'Historical Fiction',
            'France',
            'Literature',
            'Fantasy'
        
        ],
        "pages": 360,
        "awards": 
            [''
        
        ],
        "likedPercent": 92.0,
        "price": 2.86
    },
    {
        "id": 12691,
        "title": "Marley and Me: Life and Love With the World's Worst Dog",
        "series": "",
        "author": "John Grogan",
        "description": "John and Jenny were just beginning their life together. They were young and in love, with a perfect little house and not a care in the world. Then they brought home Marley, a wiggly yellow furball of a puppy. Life would never be the same.Marley quickly grew into a barreling, ninety-seven-pound streamroller of a Labrador retriever, a dog like no other. He crashed through screen doors, gouged through drywall, flung drool on guests, stole women's undergarments, and ate nearly everything he could get his mouth around, including couches and fine jewelry. Obedience school did no good\u2014Marley was expelled. Neither did the tranquilizers the veterinarian prescribed for him with the admonishment, \"Don't hesitate to use these.\"And yet Marley's heart was pure. Just as he joyfully refused any limits on his behavior, his love and loyalty were boundless, too. Marley shared the couple's joy at their first pregnancy, and their heartbreak over the miscarriage. He was there when babies finally arrived and when the screams of a seventeen-year-old stabbing victim pierced the night. Marley shut down a public beach and managed to land a role in a feature-length movie, always winning hearts as he made a mess of things. Through it all, he remained steadfast, a model of devotion, even when his family was at its wit's end. Unconditional love, they would learn, comes in many forms.",
        "language": "English",
        "isbn": "9780739461198",
        "genres": 
            ['Nonfiction',
            'Animals',
            'Memoir',
            'Dogs',
            'Biography',
            'Humor',
            'Biography Memoir',
            'Adult',
            'Contemporary',
            'Autobiography'
        
        ],
        "pages": 291,
        "awards": 
            ['Puddly Award for Nonfiction (2007)'
        
        ],
        "likedPercent": 95.0,
        "price": 5.29
    },
    {
        "id": 24337,
        "title": "Ella Enchanted",
        "series": "Ella Enchanted #1",
        "author": "Gail Carson Levine (Goodreads Author)",
        "description": "At birth, Ella is inadvertently cursed by an imprudent young fairy named Lucinda, who bestows on her the \"gift\" of obedience. Anything anyone tells her to do, Ella must obey. Another girl might have been cowed by this affliction, but not feisty Ella: \"Instead of making me docile, Lucinda's curse made a rebel of me. Or perhaps I was that way naturally.\" When her beloved mother dies, leaving her in the care of a mostly absent and avaricious father, and later, a loathsome stepmother and two treacherous stepsisters, Ella's life and well-being seem to be in grave peril. But her intelligence and saucy nature keep her in good stead as she sets out on a quest for freedom and self-discovery as she tries to track down Lucinda to undo the curse, fending off ogres, befriending elves, and falling in love with a prince along the way. Yes, there is a pumpkin coach, a glass slipper, and a happily ever after, but this is the most remarkable, delightful, and profound version of Cinderella you'll ever read.Gail Carson Levine's examination of traditional female roles in fairy tales takes some satisfying twists and deviations from the original. Ella is bound by obedience against her will, and takes matters in her own hands with ambition and verve. Her relationship with the prince is balanced and based on humor and mutual respect; in fact, it is she who ultimately rescues him. Ella Enchanted has won many well-deserved awards, including a Newbery Honor.",
        "language": "English",
        "isbn": "9780590920681",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Romance',
            'Fairy Tales',
            'Childrens',
            'Middle Grade',
            'Retellings',
            'Magic',
            'Adventure'
        
        ],
        "pages": 232,
        "awards": 
            ['Newbery Medal Nominee (1998)',
            '\Mythopoeic Fantasy Award Nominee for Childrens Literature (1999)\',
            'Grand Canyon Reader Award for Teen Book (1999)',
            'Maryland Black-Eyed Susan Book Award for Grade 6-9 (2000)',
            '\Dorothy Canfield Fisher Childrens Book Award (1999)\',
            'Iowa Teen Award (2000)',
            'California Young Readers Medal for Middle School/Junior High (2000)',
            '\Rebecca Caudill Young Readers Book Award (2000)\'
        
        ],
        "likedPercent": 92.0,
        "price": 1.91
    },
    {
        "id": 11275,
        "title": "The Wind-Up Bird Chronicle",
        "series": "\u306d\u3058\u307e\u304d\u9ce5\u30af\u30ed\u30cb\u30af\u30eb #1-3",
        "author": "Haruki Murakami, Jay Rubin (Translator)",
        "description": "Japan's most highly regarded novelist now vaults into the first ranks of international fiction writers with this heroically imaginative novel, which is at once a detective story, an account of a disintegrating marriage, and an excavation of the buried secrets of World War II.In a Tokyo suburb a young man named Toru Okada searches for his wife's missing cat. Soon he finds himself looking for his wife as well in a netherworld that lies beneath the placid surface of Tokyo. As these searches intersect, Okada encounters a bizarre group of allies and antagonists: a psychic prostitute; a malevolent yet mediagenic politician; a cheerfully morbid sixteen-year-old-girl; and an aging war veteran who has been permanently changed by the hideous things he witnessed during Japan's forgotten campaign in Manchuria.Gripping, prophetic, suffused with comedy and menace, The Wind-Up Bird Chronicle is a tour de force equal in scope to the masterpieces of Mishima and Pynchon.Three books in one volume: The Thieving Magpie, Bird as Prophet, The Birdcatcher. This translation by Jay Rubin is in collaboration with the author.",
        "language": "English",
        "isbn": "9780965341981",
        "genres": 
            ['Fiction',
            'Magical Realism',
            'Japan',
            'Japanese Literature',
            'Fantasy',
            'Contemporary',
            'Literature',
            'Novels',
            'Mystery',
            'Asia'
        
        ],
        "pages": 607,
        "awards": 
            ['Japan-U.S. Friendship Commission Prize for the Translation of Japanese Literature (1999)',
            'Yomiuri Prize \u8aad\u58f2\u6587\u5b66\u8cde for Fiction (1995)',
            'International Dublin Literary Award Nominee for Shortlist (1999)'
        
        ],
        "likedPercent": 95.0,
        "price": 22.25
    },
    {
        "id": 36381037,
        "title": "Cinder",
        "series": "The Lunar Chronicles #1",
        "author": "Marissa Meyer (Goodreads Author)",
        "description": "Humans and androids crowd the raucous streets of New Beijing. A deadly plague ravages the population. From space, a ruthless Lunar people watch, waiting to make their move. No one knows that Earth\u2019s fate hinges on one girl. . . . Cinder, a gifted mechanic, is a cyborg. She\u2019s a second-class citizen with a mysterious past, reviled by her stepmother and blamed for her stepsister\u2019s illness. But when her life becomes intertwined with the handsome Prince Kai\u2019s, she suddenly finds herself at the center of an intergalactic struggle, and a forbidden attraction. Caught between duty and freedom, loyalty and betrayal, she must uncover secrets about her past in order to protect her world\u2019s future.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Young Adult',
            'Fantasy',
            'Science Fiction',
            'Romance',
            'Dystopia',
            'Retellings',
            'Fiction',
            'Fairy Tales',
            'Audiobook',
            'Young Adult Fantasy'
        
        ],
        "pages": 400,
        "awards": 
            ['Golden Duck Award for Young Adult (Hal Clement Award) (2013)',
            'Kalbacher Klapperschlange for Altersgruppe 7. - 9. Klasse (2015)',
            '\Grand Prix de lImaginaire Nominee for Roman jeunesse \u00e9tranger (2014)\',
            '\Pennsylvania Young Readers Choice Award Nominee for Young Adults (2014)\',
            'Rhode Island Teen Book Award Nominee (2014)',
            'California Young Readers Medal for Young Adult (2016)',
            'Lincoln Award Nominee (2014)',
            'Goodreads Choice Award Nominee for Young Adult Fantasy & Science Fiction and for Goodreads Author (2012)',
            'Premio El Templo de las Mil Puertas Nominee for Mejor novela extranjera perteneciente a saga (2012)',
            '\Rebecca Caudill Young Readers Book Award Nominee (2016)\'
        
        ],
        "likedPercent": 93.0,
        "price": 18.948772815551667
    },
    {
        "id": 11566,
        "title": "The Green Mile",
        "series": "The Green Mile #1-6",
        "author": "Stephen King (Goodreads Author)",
        "description": "When it first appeared, one volume per month, Stephen King's THE GREEN MILE was an unprecedented publishing triumph: all six volumes ended up on the New York Times bestseller lists\u2014simultaneously\u2014and delighted millions of fans the world over.Welcome to Cold Mountain Penitentiary, home to the Depression-worn men of E Block. Convicted killers all, each awaits his turn to walk the Green Mile, keeping a date with \"Old Sparky,\" Cold Mountain's electric chair. Prison guard Paul Edgecombe has seen his share of oddities in his years working the Mile. But he's never seen anyone like John Coffey, a man with the body of a giant and the mind of a child, condemned for a crime terrifying in its violence and shocking in its depravity. In this place of ultimate retribution, Edgecombe is about to discover the terrible, wondrous truth about Coffey, a truth that will challenge his most cherished beliefes... and yours.",
        "language": "English",
        "isbn": "9780451933027",
        "genres": 
            ['Horror',
            'Fiction',
            'Fantasy',
            'Thriller',
            'Mystery',
            'Supernatural',
            'Paranormal',
            'Crime',
            'Drama',
            'Historical Fiction'
        
        ],
        "pages": 592,
        "awards": 
            ['Bram Stoker Award for Best Novel (1996)',
            'Audie Award for Fiction',
            'Unabridged (1997)'
        
        ],
        "likedPercent": 98.0,
        "price": 17.56
    },
    {
        "id": 40495148,
        "title": "Blindness",
        "series": "Blindness #1",
        "author": "Jos\u00e9 Saramago",
        "description": "From Nobel Prize\u2013winning author Jos\u00e9 Saramago, a magnificent, mesmerizing parable of lossA city is hit by an epidemic of \"white blindness\" that spares no one. Authorities confine the blind to an empty mental hospital, but there the criminal element holds everyone captive, stealing food rations, and assaulting women. There is one eyewitness to this nightmare who guides her charges\u2014among them a boy with no mother, a girl with dark glasses, a dog of tears\u2014through the barren streets, and their procession becomes as uncanny as the surroundings are harrowing. As Blindness reclaims the age-old story of a plague, it evokes the vivid and trembling horrors of the twentieth century, leaving readers with a powerful vision of the human spirit that's bound both by weakness and exhilarating strength.",
        "language": "English",
        "isbn": "B003T0GBOM",
        "genres": 
            ['Fiction',
            'Dystopia',
            'Science Fiction',
            'Classics',
            'Novels',
            'Literature',
            'Portugal',
            'Horror',
            'Portuguese Literature',
            'Contemporary'
        
        ],
        "pages": 349,
        "awards": 
            ['Premio San Clemente for Novela Estranxeira (1999)',
            'International Dublin Literary Award Nominee (1999)'
        
        ],
        "likedPercent": 94.0,
        "price": 15.412921211558881
    },
    {
        "id": 10572,
        "title": "A Clash of Kings",
        "series": "A Song of Ice and Fire #2",
        "author": "George R.R. Martin",
        "description": "A comet the color of blood and flame cuts across the sky. Two great leaders\u2014Lord Eddard Stark and Robert Baratheon\u2014who hold sway over an age of enforced peace are dead, victims of royal treachery. Now, from the ancient citadel of Dragonstone to the forbidding shores of Winterfell, chaos reigns. Six factions struggle for control of a divided land and the Iron Throne of the Seven Kingdoms, preparing to stake their claims through tempest, turmoil, and war. It is a tale in which brother plots against brother and the dead rise to walk in the night. Here a princess masquerades as an orphan boy; a knight of the mind prepares a poison for a treacherous sorceress; and wild men descend from the Mountains of the Moon to ravage the countryside. Against a backdrop of incest and fratricide, alchemy and murder, victory may go to the men and women possessed of the coldest steel...and the coldest hearts. For when kings clash, the whole land trembles.Here is the second volume in George R.R. Martin magnificent cycle of novels that includes A Game of Thrones and A Storm of Swords. As a whole, this series comprises a genuine masterpiece of modern fantasy, bringing together the best the genre has to offer. Magic, mystery, intrigue, romance, and adventure fill these pages and transport us to a world unlike any we have ever experienced. Already hailed as a classic, George R.R. Martin stunning series is destined to stand as one of the great achievements of imaginative fiction.",
        "language": "English",
        "isbn": "9780553381696",
        "genres": 
            ['Fantasy',
            'Fiction',
            'Epic Fantasy',
            'Science Fiction Fantasy',
            'High Fantasy',
            'Adult',
            'Adventure',
            'Dragons',
            'Audiobook',
            'Epic'
        
        ],
        "pages": 969,
        "awards": 
            ['Nebula Award Nominee for Best Novel (1999)',
            'Locus Award for Best Fantasy Novel (1999)',
            'Premio Ignotus for Novela extranjera (2004)'
        
        ],
        "likedPercent": 98.0,
        "price": 1.91
    },
    {
        "id": 10975,
        "title": "The Sound and the Fury",
        "series": "",
        "author": "William Faulkner",
        "description": "Alternate version of this book.The tragedy of the Compson family features some of the most memorable characters in literature: beautiful, rebellious Caddy; the manchild Benjy; haunted, neurotic Quentin; Jason, the brutal cynic; and Dilsey, their black servant. Their lives fragmented and harrowed by history and legacy, the character\u2019s voices and actions mesh to create what is arguably Faulkner\u2019s masterpiece and one of the greatest novels of the twentieth century.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Novels',
            'American',
            '20th Century',
            'Southern Gothic',
            'Southern',
            'Literary Fiction',
            'School'
        
        ],
        "pages": 366,
        "awards": 
            [''
        
        ],
        "likedPercent": 87.0,
        "price": 14.25133308900342
    },
    {
        "id": 40874325,
        "title": "The Shack",
        "series": "",
        "author": "William Paul Young",
        "description": "The Shack, the cherished novel that sold over 23 million copies worldwide, spent 147 weeks on the bestseller list, and went on to become a major motion picture, is now available in a beautiful keepsake edition to celebrate its tenth anniversary of touching lives all over the world. Mackenzie Allen Phillips's youngest daughter, Missy, has been abducted during a family vacation, and evidence that she may have been brutally murdered is found in an abandoned shack deep in the Oregon wilderness. Four years later, in the midst of his Great Sadness, Mack receives a suspicious note, apparently from God, inviting him back to that shack for a weekend. Against his better judgment he arrives at the shack on a wintry afternoon and walks back into his darkest nightmare. What he find there will change his life forever. In an age where religion seems to grow increasingly irrelevant, The Shack wrestles with the timeless question: Where is God in a world so filled with unspeakable pain? Discover the answers that astounded and transformed Mack in this special leather edition, and find out why The Shack has stolen the hearts of millions for ten years.",
        "language": "English",
        "isbn": "B001B8Z2S0",
        "genres": 
            ['Fiction',
            'Christian',
            'Christian Fiction',
            'Religion',
            'Spirituality',
            'Faith',
            'Inspirational',
            'Christianity',
            'Adult Fiction',
            'Adult'
        
        ],
        "pages": 294,
        "awards": 
            ['LovelyBooks Leserpreis Nominee for Allgemeine Literatur (2009)'
        
        ],
        "likedPercent": 83.0,
        "price": 3.554891800057446
    },
    {
        "id": 30183,
        "title": "Marked",
        "series": "House of Night #1",
        "author": "P.C. Cast (Goodreads Author), Kristin Cast (Goodreads Author)",
        "description": "Also see: Alternate Cover Editions for this ISBN [ACE]  \r\n  ACE #1\r\nAfter a Vampire Tracker Marks her with a crescent moon on her forehead, 16-year-old Zoey Redbird enters the House of Night and learns that she is no average fledgling. She has been Marked as special by the vampyre Goddess Nyx and has affinities for all five elements: Air, Fire Water, Earth and Spirit. But she is not the only fledgling at the House of Night with special powers. When she discovers that the leader of the Dark Daughters, the school\u2019s most elite club, is mis-using her Goddess-given gifts, Zoey must look deep within herself for the courage to embrace her destiny \u2013 with a little help from her new vampyre friends (or Nerd Herd, as Aphrodite calls them)",
        "language": "English",
        "isbn": "9780312360269",
        "genres": 
            ['Young Adult',
            'Vampires',
            'Fantasy',
            'Paranormal',
            'Romance',
            'Fiction',
            'Supernatural',
            'Urban Fantasy',
            'Paranormal Romance',
            'Teen'
        
        ],
        "pages": 306,
        "awards": 
            ['\Romantic Times Reviewers Choice Award (RT Award) for Young Adult (2007)\'
        
        ],
        "likedPercent": 85.0,
        "price": 1.79
    },
    {
        "id": 39832183,
        "title": "The Guernsey Literary and Potato Peel Pie Society",
        "series": "",
        "author": "Mary Ann Shaffer, Annie Barrows",
        "description": " #1 NEW YORK TIMES BESTSELLER - NOW A MAJOR MOTION PICTURE ON NETFLIX - A remarkable tale of the island of Guernsey during the German Occupation, and of a society as extraordinary as its name. \"I wonder how the book got to Guernsey? Perhaps there is some sort of secret homing instinct in books that brings them to their perfect readers.\" January 1946: London is emerging from the shadow of the Second World War, and writer Juliet Ashton is looking for her next book subject. Who could imagine that she would find it in a letter from a man she's never met, a native of the island of Guernsey, who has come across her name written inside a book by Charles Lamb...As Juliet and her new correspondent exchange letters, Juliet is drawn into the world of this man and his friends\u2014and what a wonderfully eccentric world it is. The Guernsey Literary and Potato Peel Pie Society\u2014born as a spur-of-the-moment alibi when its members were discovered breaking curfew by the Germans occupying their island\u2014boasts a charming, funny, deeply human cast of characters, from pig farmers to phrenologists, literature lovers all.Juliet begins a remarkable correspondence with the society's members, learning about their island, their taste in books, and the impact the recent German occupation has had on their lives. Captivated by their stories, she sets sail for Guernsey, and what she finds will change her forever.Written with warmth and humor as a series of letters, this novel is a celebration of the written word in all its guises and of finding connection in the most surprising ways.",
        "language": "English",
        "isbn": "9781984801814",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Historical',
            'Romance',
            'World War II',
            'Book Club',
            'War',
            'Adult',
            'Adult Fiction',
            'Books About Books'
        
        ],
        "pages": 291,
        "awards": 
            ['Indies Choice Book Award for Best Indie Buzz Book (Fiction) (2009)',
            'LovelyBooks Leserpreis Nominee for Allgemeine Literatur (2009)'
        
        ],
        "likedPercent": 95.0,
        "price": 3.65
    },
    {
        "id": 46170,
        "title": "For Whom the Bell Tolls",
        "series": "",
        "author": "Ernest Hemingway",
        "description": "In 1937 Ernest Hemingway traveled to Spain to cover the civil war there for the North American Newspaper Alliance. Three years later he completed the greatest novel to emerge from \"the good fight,\" For Whom the Bell Tolls. The story of Robert Jordan, a young American in the International Brigades attached to an antifascist guerilla unit in the mountains of Spain, it tells of loyalty and courage, love and defeat, and the tragic death of an ideal. In his portrayal of Jordan's love for the beautiful Maria and his superb account of El Sordo's last stand, in his brilliant travesty of La Pasionaria and his unwillingness to believe in blind faith, Hemingway surpasses his achievement in The Sun Also Rises and A Farewell to Arms to create a work at once rare and beautiful, strong and brutal, compassionate, moving and wise. \"If the function of a writer is to reveal reality,\" Maxwell Perkins wrote to Hemingway after reading the manuscript, \"no one ever so completely performed it.\" Greater in power, broader in scope, and more intensely emotional than any of the author's previous works, it stands as one of the best war novels of all time.",
        "language": "English",
        "isbn": "9999999999999",
        "genres": 
            ['Classics',
            'Fiction',
            'Literature',
            'Historical Fiction',
            'War',
            'Novels',
            'American',
            'Spain',
            'Classic Literature',
            'Literary Fiction'
        
        ],
        "pages": 471,
        "awards": 
            [''
        
        ],
        "likedPercent": 92.0,
        "price": 8.161452480943446
    },
    {
        "id": 7745,
        "title": "Fear and Loathing in Las Vegas",
        "series": "",
        "author": "Hunter S. Thompson, Ralph Steadman (Illustrator)",
        "description": "Fear and Loathing in Las Vegas is the best chronicle of drug-soaked, addle-brained, rollicking good times ever committed to the printed page. It is also the tale of a long weekend road trip that has gone down in the annals of American pop culture as one of the strangest journeys ever undertaken.",
        "language": "English",
        "isbn": "9780679785897",
        "genres": 
            ['Fiction',
            'Classics',
            'Humor',
            'Journalism',
            'Novels',
            'American',
            'Literature',
            'Contemporary',
            'Travel',
            'Comedy'
        
        ],
        "pages": 204,
        "awards": 
            [''
        
        ],
        "likedPercent": 93.0,
        "price": 5.69
    },
    {
        "id": 9328,
        "title": "The House of the Spirits",
        "series": "Del Valle Family #3",
        "author": "Isabel Allende (Goodreads Author), Magda Bogin (Translator)",
        "description": "In one of the most important and beloved Latin American works of the twentieth century, Isabel Allende weaves a luminous tapestry of three generations of the Trueba family, revealing both triumphs and tragedies. Here is patriarch Esteban, whose wild desires and political machinations are tempered only by his love for his ethereal wife, Clara, a woman touched by an otherworldly hand. Their daughter, Blanca, whose forbidden love for a man Esteban has deemed unworthy infuriates her father, yet will produce his greatest joy: his granddaughter Alba, a beautiful, ambitious girl who will lead the family and their country into a revolutionary future.The House of the Spirits is an enthralling saga that spans decades and lives, twining the personal and the political into an epic novel of love, magic, and fate.",
        "language": "English",
        "isbn": "9780553383805",
        "genres": 
            ['Fiction',
            'Magical Realism',
            'Historical Fiction',
            'Classics',
            'Fantasy',
            'Spanish Literature',
            'Literature',
            'Historical',
            'Novels',
            'Latin American'
        
        ],
        "pages": 448,
        "awards": 
            ['Deutscher H\u00f6rbuchpreis for Beste Fiktion (2011)',
            '\Prix du Grand Roman d\u00e9vasion (1984)\'
        
        ],
        "likedPercent": 96.0,
        "price": 3.32
    },
    {
        "id": 24812,
        "title": "The Complete Calvin and Hobbes",
        "series": "Calvin and Hobbes",
        "author": "Bill Watterson",
        "description": "[ \r\n  Box Set\r\n | Book One | Book Two | Book Three ]Calvin and Hobbes is unquestionably one of the most popular comic strips of all time. The imaginative world of a boy and his real-only-to-him tiger was first syndicated in 1985 and appeared in more than 2,400 newspapers when Bill Watterson retired on January 1, 1996. The entire body of Calvin and Hobbes cartoons published in a truly noteworthy tribute to this singular cartoon in The Complete Calvin and Hobbes. Composed of three hardcover, four-color volumes in a sturdy slipcase, this New York Times best-selling edition includes all Calvin and Hobbes cartoons that ever appeared in syndication. This is the treasure that all Calvin and Hobbes fans seek.",
        "language": "English",
        "isbn": "9780740748479",
        "genres": 
            ['Comics',
            'Humor',
            'Graphic Novels',
            'Fiction',
            'Comedy',
            'Classics',
            'Graphic Novels Comics',
            'Comic Strips',
            'Childrens',
            'Comic Book'
        
        ],
        "pages": 1456,
        "awards": 
            [''
        
        ],
        "likedPercent": 99.0,
        "price": 110.67
    },
    {
        "id": 546018,
        "title": "Roots: The Saga of an American Family",
        "series": "",
        "author": "Alex Haley",
        "description": "When he was a boy in Henning, Tennessee, Alex Haley's grandmother used to tell him stories about their family\u2014stories that went back to her grandparents, and their grandparents, down through the generations all the way to a man she called \"the African.\" She said he had lived across the ocean near what he called the \"Kamby Bolongo\" and had been out in the forest one day chopping wood to make a drum when he was set upon by four men, beaten, chained and dragged aboard a slave ship bound for Colonial America.Still vividly remembering the stories after he grew up and became a writer, Haley began to search for documentation that might authenticate the narrative. It took ten years and a half a million miles of travel across three continents to find it, but finally, in an astonishing feat of genealogical detective work, he discovered not only the name of \"the African\"\u2014Kunta Kinte\u2014but the precise location of Juffure, the very village in The Gambia, West Africa, from which he was abducted in 1767 at the age of sixteen and taken on the Lord Ligonier to Maryland and sold to a Virginia planter.Haley has talked in Juffure with his own African sixth cousins. On September 29, 1967, he stood on the dock in Annapolis where his great-great-great-great-grandfather was taken ashore on September 29, 1767. Now he has written the monumental two-century drama of Kunta Kinte and the six generations who came after him\u2014slaves and freedmen, farmers and blacksmiths, lumber mill workers and Pullman porters, lawyers and architects\u2014and one author.But Haley has done more than recapture the history of his own family. As the first black American writer to trace his origins back to their roots, he has told the story of 25,000,000 Americans of African descent. He has rediscovered for an entire people a rich cultural heritage that slavery took away from them, along with their names and their identities. But Roots speaks, finally, not just to blacks, or to whites, but to all people and all races everywhere, for the story it tells is one of the most eloquent testimonials ever written to the indomitability of the human spirit.",
        "language": "English",
        "isbn": "9780440174646",
        "genres": 
            ['Historical Fiction',
            'Fiction',
            'Classics',
            'Historical',
            'African American',
            'Africa',
            'Race',
            'Literature',
            'Audiobook',
            'Novels'
        
        ],
        "pages": 729,
        "awards": 
            ['ASJA Outstanding Book Award (1978)',
            'Audie Award for Nonfiction (2008)',
            'Premio Bancarella (1978)',
            'National Book Critics Circle Award Nominee for General Nonfiction (1976)',
            'Lillian Smith Book Award (1977)'
        
        ],
        "likedPercent": 98.0,
        "price": 3.1
    },
    {
        "id": 10614,
        "title": "Misery",
        "series": "",
        "author": "Stephen King (Goodreads Author)",
        "description": "Alternate cover editions here and here.Paul Sheldon. He's a bestselling novelist who has finally met his biggest fan. Her name is Annie Wilkes and she is more than a rabid reader - she is Paul's nurse, tending his shattered body after an automobile accident. But she is also his captor, keeping him prisoner in her isolated house.",
        "language": "English",
        "isbn": "9780450417399",
        "genres": 
            ['Horror',
            'Fiction',
            'Thriller',
            'Suspense',
            'Mystery',
            'Novels',
            'Adult',
            'Mystery Thriller',
            'Crime',
            'Drama'
        
        ],
        "pages": 370,
        "awards": 
            ['Bram Stoker Award for Best Novel (1987)',
            'World Fantasy Award Nominee for Best Novel (1988)'
        
        ],
        "likedPercent": 95.0,
        "price": 1.12
    },
    {
        "id": 6294,
        "title": "Howl's Moving Castle",
        "series": "Howl's Moving Castle #1",
        "author": "Diana Wynne Jones",
        "description": "An alternative cover for this ISBN can be found hereSophie has the great misfortune of being the eldest of three daughters, destined to fail miserably should she ever leave home to seek her fate. But when she unwittingly attracts the ire of the Witch of the Waste, Sophie finds herself under a horrid spell that transforms her into an old lady. Her only chance at breaking it lies in the ever-moving castle in the hills: the Wizard Howl's castle. To untangle the enchantment, Sophie must handle the heartless Howl, strike a bargain with a fire demon, and meet the Witch of the Waste head-on. Along the way, she discovers that there's far more to Howl\u2014and herself\u2014than first meets the eye.",
        "language": "English",
        "isbn": "9780064410342",
        "genres": 
            ['Fantasy',
            'Young Adult',
            'Fiction',
            'Romance',
            'Magic',
            'Middle Grade',
            'Childrens',
            'Adventure',
            'Classics',
            'Young Adult Fantasy'
        
        ],
        "pages": 329,
        "awards": 
            ['\Phoenix Award (Childrens Literature Association) (2006)\',
            'Boston Globe-Horn Book Award (1987)'
        
        ],
        "likedPercent": 95.0,
        "price": 5.95
    },
    {
        "id": 350,
        "title": "Stranger in a Strange Land",
        "series": "",
        "author": "Robert A. Heinlein",
        "description": "NAME: Valentine Michael Smith\r\nANCESTRY: Human\r\nORIGIN: Mars\r\n\r\nValentine Michael Smith is a human being raised on Mars, newly returned to Earth. Among his people for the first time, he struggles to understand the social mores and prejudices of human nature that are so alien to him, while teaching them his own fundamental beliefs in grokking, watersharing, and love.",
        "language": "English",
        "isbn": "9780441788385",
        "genres": 
            ['Science Fiction',
            'Fiction',
            'Classics',
            'Science Fiction Fantasy',
            'Fantasy',
            'Novels',
            'Speculative Fiction',
            'Philosophy',
            'Religion',
            'Audiobook'
        
        ],
        "pages": 525,
        "awards": 
            ['Hugo Award for Best Novel (1962)',
            'Prometheus Hall of Fame Award (1987)'
        
        ],
        "likedPercent": 89.0,
        "price": 6.4
    }
]

# POST /api/getOrder - Handles the sorting based on the ratedBooks and sortCriteria
@app.route('/api/getOrder', methods=['POST', 'OPTIONS'])
def get_order():
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    
    data = request.json
    current_user = data.get('currentUser')
    rated_books = data.get('ratedBooks')
    sort_criteria = data.get('sortCriteria')
    
    print(f"Received request from user: {current_user}")
    print(f"Rated books: {rated_books}")
    print(f"Sort Criteria: {sort_criteria}")

    # Example: Sort books by rating if sortCriteria is "Similar Content"
    if sort_criteria == "Similar Content":
        sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Sort by rating
        return jsonify({"sortedBooks": sorted_books})

    elif sort_criteria == "Similar Authors":
        sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
        return jsonify({"sortedBooks": sorted_books})

    elif sort_criteria == "Similar Categories":
        sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
        return jsonify({"sortedBooks": sorted_books})

    elif sort_criteria == "Similar Page-length":
        sorted_books = sorted(books, key=lambda x: x['rating'], reverse=True)  # Example sorting logic
        return jsonify({"sortedBooks": sorted_books})

    return jsonify({"message": "No valid sorting criteria provided"}), 400

def _build_cors_prelight_response():
    response = jsonify()
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:4200")
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

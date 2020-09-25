import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

# query = cursor.execute("SELECT * FROM Dictionary Where Expression = 'line' ")
# results = cursor.fetchall()

# # for result in results:
#     print(result)  # ('line', 'Term used in GIS technologies in the vector type of internal data organization: spatial data are divided into point, line and polygon types.')
#                 # ('line', 'The descendants of one individual.')
#                 # ('line', 'A succession of notes forming a distinctive sequence.')
#                 # ('line', 'A measure of length equal to one twelfth of an inch.')
#                 # ('line', 'An infinitely long, infinitely thin, not bent line in geometry.')
#                 # ('line', 'A mark that is long relative to its width.')




# query = cursor.execute("SELECT * FROM Dictionary Where Expression = 'asfasfd' ")
# results = cursor.fetchall()

# for result in results:
#     print(result[1])
# else:
#     print("No word found!")  # No word found!




word = input("Enter a word: ")  # rain

query = cursor.execute("SELECT * FROM Dictionary Where Expression = '%s' " % word)  # This will process user input.
results = cursor.fetchall()

for result in results:
    print(result[1])  # Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.
                        # To fall from the clouds in drops of water.
else:
    print("No word found!")  

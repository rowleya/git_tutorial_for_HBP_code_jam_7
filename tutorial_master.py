
likes = list()
dislikes = list()

# update my likes list
likes.append("Bacon")
likes.append("Cheese")
likes.append("Halo")

# update my dislikes list
dislikes.append("Smelly feet")
dislikes.append("american chocolate")

# print out my likes list.
print "I like: "
for element in likes:
    print "{},".format(element)

# make some space between my likes and dislikes
print "\n\n"

# print out my dislikes list.
print "I dislike: "
for element in dislikes:
    print "{}".format(element)
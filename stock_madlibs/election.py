def madlib():
    person = input("Person in the room: ")
    number = input("Number: ")
    adj = input("Adjective: ")
    color = input("Color: ")
    noun = input("Noun: ")
    food = input("Type of Food(plural): ")
    noun2 = input("Noun: ")
    verb = input("Verb ending in 'ing': ")
    clothing = input("Piece of clothing:")
    adj2 = input("Adjective: ")
    celeb = input("Celebrity: ")
    number2 = input("Number: ")
    person2 = input("Person in the room: ")
    noun3 = input("Noun: ")
    person3 = input("Person in the room: ")
    job = input("Occupation: ")     

    madlib = f"My name is {person} and I am {number} years old.  If I were president, I'd do a whole bunch of {adj} things: \
    1. I would drive the biggest {color} car in the country.  And that car would go faster than any other {noun} in the world! \
    2. Everyone would eat pepperoni {food} for dinner. \
    3. I would live in the Statue of {noun2} and build a {verb} pool at her feet. \
    4. I would wear a/an {clothing} on my head, and everyone would say I look {adj2} like {celeb}. \
    5. School would be open only {number2} days a year. \
    6. I would give my friends the best jobs.  I would nominate {person2} to be secreatry of (the) {noun3}, and {person3} could be vice {job}!!"

    print(madlib)
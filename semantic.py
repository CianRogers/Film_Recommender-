import os
import spacy

# task 1 code extract
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print('\n')

# task 1 code extract
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))
            
print('\n')

# task 1 code extract            
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(f'{sentence} + "_" + {similarity}')

#===============================
# Task 1 - similarities noticed:
#===============================
# When comparing the similarities between "cat", "monkey", and "banana" using the medium-sized language model ('en_core_web_md'), I observed the following:

# Similarity between 'cat' and 'monkey': The similarity score between "cat" and "monkey" was moderately high. Therefore there is a certain degree of semantic similarity, 
# likely due to their shared association as animals.

# Similarity between 'cat' and 'banana': The similarity score between "cat" and "banana" was relatively low. 
# This indicates that the model perceives less semantic overlap between these two words, as they belong to different semantic categories (animal vs. fruit).

# Similarity between 'monkey' and 'banana': The similarity score between "monkey" and "banana" was also relatively low. Similarly to the comparison between "cat" and "banana", 
# the model identifies limited semantic association between these two words due to their distinct semantic categories.

#===============================
# Task 1 - Example similarities:
#===============================
# An example of my own could be comparing the similarities between modes of transport with wheels such as "car", "bicycle", and "airplane":

# For 'car' and 'bicycle': Given their shared association as modes of transportation with wheels, 
# the model might assign a moderately high similarity score between "car" and "bicycle".

# For'car' and 'airplane': Despite both being modes of transportation, 
# the semantic distance between "car" and "airplane" is likely greater compared to "car" and "bicycle". Therefore model may assign a lower similarity score to reflect this distinction.

# For 'bicycle' and 'airplane': Similar to the comparison between "car" and "airplane", 
# the semantic distance between "bicycle" and "airplane" is expected to be significant due to their different modes of operation and usage. As a result, 
# the model might assign a relatively low similarity score between these two words.

print('\n')
text_list = [
    "===============================",
    " Task 1 - similarities noticed:",
    "===============================",
    "When comparing the similarities between 'cat', 'monkey', and 'banana' using the medium-sized language model ('en_core_web_md'), I observed the following:",
    "",
    "Similarity between 'cat' and 'monkey': The similarity score between 'cat' and 'monkey' was moderately high. Therefore there is a certain degree of semantic similarity, likely due to their shared association as animals.",
    "",
    "Similarity between 'cat' and 'banana': The similarity score between 'cat' and 'banana' was relatively low. This indicates that the model perceives less semantic overlap between these two words, as they belong to different semantic categories (animal vs. fruit).",
    "",
    "Similarity between 'monkey' and 'banana': The similarity score between 'monkey' and 'banana' was also relatively low. Similarly to the comparison between 'cat' and 'banana', the model identifies limited semantic association between these two words due to their distinct semantic categories.",
    "",
    "===============================",
    " Task 1 - Example similarities:",
    "===============================",
    "An example of my own could be comparing the similarities between modes of transport with wheels such as 'car', 'bicycle', and 'airplane':",
    "",
    "For 'car' and 'bicycle': Given their shared association as modes of transportation with wheels, the model might assign a moderately high similarity score between 'car' and 'bicycle'.",
    "",
    "For 'car' and 'airplane': Despite both being modes of transportation, the semantic distance between 'car' and 'airplane' is likely greater compared to 'car' and 'bicycle'. Therefore model may assign a lower similarity score to reflect this distinction.",
    "",
    "For 'bicycle' and 'airplane': Similar to the comparison between 'car' and 'airplane', the semantic distance between 'bicycle' and 'airplane' is expected to be significant due to their different modes of operation and usage. As a result, the model might assign a relatively low similarity score between these two words."
]

# ======================================================================================================================================================================
# Task 1 - Run the example file on with the simpler language model ‘en_core_web_sm’ 
# write a note on what you notice may be different from the model 'en_core_web_md'
# ======================================================================================================================================================================

# Using the 'en_core_web_sm' model instead of 'en_core_web_md' seemed to result in lower similarity scores between tokens within the pieces of text within the example file. 
# This difference is potentially due to the smaller model's reduced capacity to capture linguistic nuances. 
# Although the smaller model's has a reduced capacity to capture linguistic nuances, the models accuracy can be increased by utilising more relevant data. 
# Accuracy can also be increased by utilising techniques like domain adaptation. 

# Print the similarities noticed answer list
for line in text_list:
    print(line)



print('\n' + 'Task 1 - Example similarities:' + 
      '\n' + '===============================')

tokens = nlp('car bicycle airplane')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

# Function to return movie suggestion to user
def suggest_movie(movie_description):
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    movies_file = os.path.join(current_dir, 'movies.txt')

    # Load large spacy language model
    nlp = spacy.load('en_core_web_lg')

    # Tokenize input description
    nlp_hulk_movie = nlp(movie_description)

    # Load movies.txt file and strip \n using line.strip 
    with open(movies_file, 'r', encoding='utf-8') as f:
        descriptions = [line.strip() for line in f.readlines()]

    # Tokenize stripped document text
    movies_doc = [nlp(description) for description in descriptions]

    # Calculate similarity between input description and each movie
    similarities = [nlp_hulk_movie.similarity(movie) for movie in movies_doc]

    # Dictionary to associate each movie's index value with its letter title
    dictionary = {idx: chr(ord('A') + idx) for idx in range(len(descriptions))}

    # Find the index of the most similar movie
    most_similar = similarities.index(max(similarities))

    # Print the most similar movie
    print(f'\nBased upon your previous viewing I recommend movie {dictionary[most_similar]}. \nEnjoy your film :)')

# Test the function with the Hulk movie description
hulk_description = ("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

print(f'\n==========================\nTask 2 - Movie suggestion:\n==========================')

suggest_movie(hulk_description)



                      



               

       

       


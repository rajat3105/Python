import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

#keep the text file in the same directory
file = open("python.txt", "r", encoding="utf-8")
file_contents=file.read()

def calculate_frequencies(file_contents):
    file_contents=file_contents.split()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "for", "it", "of", "and", "or", 
    "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", 
    "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", 
    "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", 
    "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", 
    "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", 
    "too", "very", "can", "will", "just", "in"]
    frequency={}
    for word in file_contents:
        word=word.lower()
        if word.isalpha():
            if word not in punctuations and word not in uninteresting_words:
                if word not in frequency:
                    frequency[word]=0
                frequency[word]+=1
    cloud = wordcloud.WordCloud(background_color='white',width=800,height=800)
    cloud.generate_from_frequencies(frequency)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
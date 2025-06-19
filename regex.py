import re

pattern=r"[A-Za-z]+yclone"
text= '''

Cyclone Dumazile was a strong tropical cyclone that formed in the South-West Indian Ocean in early March 2018. 
It originated from a low-pressure area near Agaléga on February 27, intensifying into a tropical disturbance on March 2 and receiving its name the following day after becoming a tropical storm. 
Cyclone Dumazile reached cycline Dyclone its strongest point on March 5, 
with sustained winds of 165 km/h (105 mph) over 10 minutes. It impacted Madagascar and Réunion, causing heavy rain. 
The cyclone weakened as it moved southeast, becoming post-tropical on March 7. 
'''

pattern_searched= re.finditer(pattern,text)  # Returns a callable object or iterator that gives you match objects one-by-one.
print(pattern_searched)           # callable iterator is not equal to callable object
# print(pattern_searched.span())

for each_match in pattern_searched:
    print(each_match.span())   # gives out the span in form of tuple
    print(text[each_match.span()[0]:each_match.span()[1]])   
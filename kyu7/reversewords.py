"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

"""


def reverse_words(text):
      #go for it
    rew=[]
    saperated=text.split(" ")
    for i in saperated:
            rew.append(i[::-1]) 

    return ' '.join(rew)

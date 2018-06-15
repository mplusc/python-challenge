import re
import os

#CHANGE FILES WHEN ANALZYING DIFFERENT EXCEL FILES
txtpath_1 = os.path.join('raw_data','paragraph_1.txt')
output_file = os.path.join("paragraph_analysis.txt")

paragraph=""

with open(txtpath_1)as txtfile:  
    
    paragraph = txtfile.read().replace("\n","n")

words_split = paragraph.split(" ")
words_count = len(words_split)

letter_counts=[]
    
    
for word in words_split:
        letter_counts.append(len(word))

average_letters = sum(letter_counts) / float(len(letter_counts))

sentence_split = re.split("(?<=[.!?]) +", paragraph)

        
print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

for sentence in sentence_split:
    words_per_sentence.append(len(sentence.split(" ")))

average_sentence_length = sum(words_per_sentence) / float(len(words_per_sentence))

output = (
print("------------------------------------------------"),
print("Paragraph Analysis"),
print("Approximate word count: " + str(words_count)),
print("Approximate sentence count: " + str(sentence_count)),
print("Average letter count: " +str(average_letters)),
print("Average sentence length: "+ str(average_sentence_length)))


with open(output_file,"w") as txtfile:
    txtfile.write("------------------------------------------------"+ '\n')
    txtfile.write("Paragraph Analysis"+ '\n')
    txtfile.write("Approximate word count: " + str(words_count)+ '\n')
    txtfile.write("Approximate sentence count: " + str(sentence_count)+'\n')
    txtfile.write("Average letter count: " +str(average_letters)+ '\n')
    txtfile.write("Average sentence length: "+ str(average_sentence_length)+ '\n')


###Data set 2    
import re
import os

#CHANGE FILES WHEN ANALZYING DIFFERENT EXCEL FILES
txtpath_2 = os.path.join('raw_data','paragraph_2.txt')
output_file = os.path.join("paragraph_analysis.txt")

paragraph=""

with open(txtpath_2)as txtfile:  
    
    paragraph = txtfile.read().replace("\n","n")

words_split = paragraph.split(" ")
words_count = len(words_split)

letter_counts=[]
    
    
for word in words_split:
        letter_counts.append(len(word))

average_letters = sum(letter_counts) / float(len(letter_counts))

sentence_split = re.split("(?<=[.!?]) +", paragraph)

        
print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

for sentence in sentence_split:
    words_per_sentence.append(len(sentence.split(" ")))

average_sentence_length = sum(words_per_sentence) / float(len(words_per_sentence))

output = (
print("------------------------------------------------"),
print("Paragraph Analysis"),
print("Approximate word count: " + str(words_count)),
print("Approximate sentence count: " + str(sentence_count)),
print("Average letter count: " +str(average_letters)),
print("Average sentence length: "+ str(average_sentence_length)))


with open(output_file,"a") as txtfile:
    txtfile.write("------------------------------------------------"+ '\n')
    txtfile.write("Paragraph Analysis"+ '\n')
    txtfile.write("Approximate word count: " + str(words_count)+ '\n')
    txtfile.write("Approximate sentence count: " + str(sentence_count)+'\n')
    txtfile.write("Average letter count: " +str(average_letters)+ '\n')
    txtfile.write("Average sentence length: "+ str(average_sentence_length)+ '\n')

import re
import numpy as np
import time
import config
from collections import Counter

def get_conversations():
	'''
		
		Function made ONLY for Cornell dataset to extract conversations from the raw file.

	'''
	conversations = []
	with open('raw_cornell_data/movie_conversations.txt', 'r') as f:
		for line in f.readlines():
			
			conversation = line.split(' +++$+++ ')[-1]
			conversation = conversation.replace("'", "")
			conversation = conversation[1:-2]
			conversation = conversation.split(", ")
			conversations.append(conversation)

	return conversations



def get_movie_lines():

	'''
		The helper function used to extract movie_lines from the Cornell dataset

	'''
	sentences = {}
	with open('raw_cornell_data/movie_lines.txt', 'r') as f:
		for line in f.readlines():
			sentences[line.split(' +++$+++ ')[0]] = line.split(' +++$+++ ')[-1].replace('\n', "")

	return sentences


def questions_vs_answers(convs, lines):
	'''

		Save to the file questions and answers extracted from the raw files. VERSION 1

	'''

	for i in range(len(convs)):
		conversation = convs[i]
		if len(conversation) % 2 == 0:
			for line in range(len(conversation)):
				if line % 2 == 0:
					with open('movie_questions.txt', 'a') as f:
						f.write(lines[conversation[line]] + "\n")
				else:
					with open('movie_answers.txt', 'a') as f:
						f.write(lines[conversation[line]] + "\n")

def questions_vs_answers_v2(convs, lines):
	'''

		Save to the file questions and answers extracted from the raw files. VERSION 2

	'''
	for i in range(len(convs)):
		conversation = convs[i]
		for line in range(len(conversation) - 1):

			with open('movie_questions_2.txt', 'a') as f:
				f.write(lines[conversation[line]] + "\n")
			with open('movie_answers_2.txt', 'a') as f:
				f.write(lines[conversation[line + 1]] + "\n")


def cornell_tokenizer(text):
	'''
	
		Basic, starting tokenizer used for sentence preprocessing.

	'''
	text = re.sub(r"\'m", " am", text)
	text = re.sub(r"\'s", " is", text)
	text = re.sub(r"\'re", " are", text)
	text = re.sub(r"\'ll", " will", text)
	text = re.sub(r"\'d", " would", text)
	text = re.sub(r"won't", "will not", text)
	text = re.sub(r"can't", "cannot", text)
	text = re.sub(r"\.", " . ", text)
	text = re.sub(r"\?", " ? ", text)
	text = re.sub(r"!", " ! ", text)
	text = re.sub(r"/", " / ", text)
	text = re.sub(r",", " , ", text)
	text = re.sub(r'"', ' " ', text)
	text = re.sub(r"-", " - ", text)

	text = re.sub(r"[-<>{}+=|?'()\:@]", "", text)
	return text.replace('\n', '')


def clean_data():
	'''
		Raw data clearner.
	'''
	cleaned_questions = []
	cleaned_answers = []

	with open('movie_questions_2.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			cleaned_questions.append(cornell_tokenizer(line))

	with open('movie_answers_2.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			cleaned_answers.append(cornell_tokenizer(line))

	return cleaned_questions, cleaned_answers

def create_vocab(questions, answers):

	'''
		
		This function is used to create vocabulary, word_to_id and id_to_word dicts from cleaned data (got from the last question).

	'''

	assert len(questions) == len(answers)
	vocab = []
	for i in range(len(questions)):
		words = questions[i].split()
		for word in words:
			vocab.append(word)

		words = answers[i].split()
		for word in words:
			vocab.append(word)


	vocab = Counter(vocab)
	new_vocab = []
	for key in vocab.keys():
		if vocab[key] >= config.VOCAB_THRESHOLD:
			new_vocab.append(key)

	new_vocab = ['<PAD>', '<GO>', '<UNK>', '<EOS>'] + new_vocab

	word_to_id = {word:i for i, word in enumerate(new_vocab)}
	id_to_word = {i:word for i, word in enumerate(new_vocab)}

	return new_vocab, word_to_id, id_to_word


def encoder(data, word_to_id, targets=False):

	'''
	
		Using word_to_id dictionery to map each word in the sample to it's own int representation

	'''
	encoded_data = []

	for i in range(len(data)):

		encoded_line = []
		words = data[i].split()
		for word in words:

			if word not in word_to_id.keys():
				encoded_line.append(word_to_id['<UNK>'])
			else:
				encoded_line.append(word_to_id[word])

		if targets:
			encoded_line.append(word_to_id['<EOS>'])

		encoded_data.append(encoded_line)


	return np.array(encoded_data)


def pad_data(data, word_to_id, max_len, target=False):
	'''
		
		If the sentence is shorter then wanted length, pad it to that length

	'''
	if target:
		return data + [word_to_id['<PAD>']] * (max_len - len(data))
	else:
		return [word_to_id['<PAD>']] * (max_len - len(data)) + data


def bucket_data(questions, answers, word_to_id):

	'''
	
		If you prefere bucketing version of the padding, use this function to create buckets of your data.

	'''
	assert len(questions) == len(answers)

	bucketed_data = []
	already_added = []
	for bucket in config.BUCKETS:
		data_for_bucket = []
		encoder_max = bucket[0]
		decoder_max = bucket[1]
		for i in range(len(questions)):
			if len(questions[i]) <= encoder_max and len(answers[i]) <= decoder_max:
				if i not in already_added:
					data_for_bucket.append((pad_data(questions[i], word_to_id, encoder_max), pad_data(answers[i], word_to_id, decoder_max, True)))
					already_added.append(i)

		bucketed_data.append(data_for_bucket)

	return bucketed_data









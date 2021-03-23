import os

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from rake_nltk import Rake
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd 
from telnetlib import SE
from ctypes.wintypes import WORD


FILTERED_COURSES = None
SELECTED_COURSE = None


def clean_col_names(df, columns):
	"""
	Cleans column names
	-----
	columns:
		List of column names
	"""

	new = []
	for c in columns:
		new.append(c.lower().replace(' ', '_'))
	return new


def prepare_data(df):
	"""
	Prepares the final dataset
	-----
	df:
		dataframe
	"""

	# clean column names
	df.columns = clean_col_names(df, df.columns)

	# impute missing values that creeped in
	df['skills'] = df['skills'].fillna('Missing')
	df['instructors'] = df['instructors'].fillna('Missing')

	# making certain features numeric
	def make_numeric(x):
		if(x == 'Missing'):
			return np.nan
		return float(x)

	df['course_rating'] = df['course_rating'].apply(make_numeric)
	df['course_rated_by'] = df['course_rated_by'].apply(make_numeric)
	df['percentage_of_new_career_starts'] = df['percentage_of_new_career_starts'].apply(make_numeric)
	df['percentage_of_pay_increase_or_promotion'] = df['percentage_of_pay_increase_or_promotion'].apply(make_numeric)

	def make_count_numeric(x):
	    if('k' in x):
	        return (float(x.replace('k', '')) * 1000)
	    elif('m' in x):
	        return (float(x.replace('m', '')) * 1000000)
	    elif('Missing' in x):
	        return (np.nan)

	df['enrolled_student_count'] = df['enrolled_student_count'].apply(make_count_numeric)

    # extract time to complete
	def find_time(x):
	    l = x.split(' ')
	    idx = 0
	    for i in range(len(l)):
	        if(l[i].isdigit()):
	            idx = i 
	    try:
	        return (l[idx] + ' ' + l[idx + 1])
	    except:
	        return l[idx]

	df['estimated_time_to_complete'] = df['estimated_time_to_complete'].apply(find_time)

	# split by skills
	def split_it(x):
		return (x.split(','))

	df['skills'] = df['skills'].apply(split_it)

	return df


def filter(dataframe, chosen_options, feature, id):
	selected_records = []
	for i in range(922):
		for op in chosen_options:
			if op in dataframe[feature][i]:
				selected_records.append(dataframe[id][i])
	return selected_records


def extract_keywords(df, feature):

    r = Rake()
    keyword_lists = []
    for i in range(df[feature].shape[0]):
        descr = df[feature][i]
        r.extract_keywords_from_text(descr)
        key_words_dict_scores = r.get_word_degrees()
        keywords_string = " ".join(list(key_words_dict_scores.keys()))
        keyword_lists.append(keywords_string)
        
    return keyword_lists


def recommendations(df, input_course, course_category, cosine_sim,  find_similar=True, how_many=3):
    
    # initialise recommended courses list
    recommended = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_course)
    filtered_course = [word.lower() for word in word_tokens if not (word in stop_words)]  
    selected_course = df[df['skills'].str.lower().str.contains('|'.join(filtered_course)).any(level=0)]
    print("selected:",selected_course["course_name"])
    
    # index of the course fed as input
    if not selected_course.empty:
    	idx = selected_course.index[0]
    	

    	
    	if(find_similar):
    		score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
    	else:
    		score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=True)
    		

    # getting the indexes of the top 'how_many' courses
    	if(len(score_series) < how_many):
    		how_many = len(score_series)
    	top_sugg = list(score_series.iloc[1:how_many + 1].index)
    	
    
    # populating the list with the titles of the best 10 matching movies
    	for i in top_sugg:
    		qualified = df['course_name'].iloc[i]
    		recommended.append(qualified)

    return recommended


def content_based_recommendations(df, input_course, course_category, courses):

	# filter out the courses
	df = df[df['course_name'].isin(courses)].reset_index()
	# create description keywords
	df['descr_keywords'] = extract_keywords(df, 'skills')
	# instantiating and generating the count matrix
	count = CountVectorizer()
	count_matrix = count.fit_transform(df['descr_keywords'])
	# generating the cosine similarity matrix
	cosine_sim = cosine_similarity(count_matrix, count_matrix)

	# make the recommendation
	rec_courses_similar = recommendations(df, input_course,course_category, cosine_sim, True)
	if len(rec_courses_similar) != 0:
		temp_sim = df[df['course_name'].isin(rec_courses_similar)]
		#print("Top 5 most similar courses")
		#print(temp_sim[['course_name', 'course_url']])
		return temp_sim
	else:
		print("Sorry, No course Available!")
		return rec_courses_similar


def prep_for_cbr(df, input_course, course_category):

	skills_avail = []
	for i in range(922):
		
		skills_avail = skills_avail + list(df['skills'][i].split(","))
	skills_avail = list(set(skills_avail))
	
	skills_select = ["Programming", " Communication", " Analytical"]
	# use button to make the update of filtering
	skill_filtered = None
	courses = None
	
	# if st.sidebar.button("Filter Courses"):
	temp = filter(df, skills_select, 'skills', 'course_url')
	skill_filtered = df[df['course_url'].isin(temp)].reset_index()
	# update filtered courses
	courses = skill_filtered['course_name']
	#print("### Filtered courses based on skill preferences")
	# some more info
	#print("**Number of programmes filtered:**", skill_filtered.shape[0])
	#print("**Number of courses:**",
	#	skill_filtered[skill_filtered['learning_product_type'] == 'COURSE'].shape[0])
	#print("**Number of professional degrees:**",
	#	skill_filtered[skill_filtered['learning_product_type'] == 'PROFESSIONAL CERTIFICATE'].shape[0])
	#print("**Number of specializations:**",
	#	skill_filtered[skill_filtered['learning_product_type'] == 'SPECIALIZATION'].shape[0])
	# basic plots
	
	# there should be more than atleast 2 courses
	if(len(courses) <= 2):
		print("*There should be atleast 3 courses. Do add more.*")
	
	return content_based_recommendations(df, input_course,course_category, courses)


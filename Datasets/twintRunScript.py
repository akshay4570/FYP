import os
import sys
import time

depresssive_words = ["\"Double depression\"",
					"depression",
					"\"Major depressive disorder\"",
					"stress",
					"trauma",
					"panic",
					"anxiety",
					"\"Bipolar Disorder\"",
					"PTSD",
					"\"Suicidal behavior\"",
					"Sucide",
					"Depersonalization",
					"\"Psychotic depression\"",
					"\"scale for depression\"",
					"\"Post-traumatic stress disorder\""]


for tweet in depresssive_words:
	arguments = f"twint -s {tweet} --since 2020-01-01 -o {tweet}.csv --csv --limit 25000"
	os.system(arguments)

	
	
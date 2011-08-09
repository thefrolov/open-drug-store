# -*- coding: utf-8 -*-

from datetime import datetime 
from time import strptime


import shlex

def _date_from_str(date_str):
	return datetime(*strptime(date_str,"%d.%m.%Y")[0:3])
	
	
def parseStr(str_for_parse,whitespace):
	my_splitter = shlex.shlex(str_for_parse, posix=True)
	my_splitter.whitespace = whitespace
	my_splitter.whitespace_split = True
	return list(my_splitter)

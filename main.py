#!/usr/local/bin/python3
import time
import sys
import re

WHITE = "\033[4;37m"
RED = "\033[1;31m"
GREEN = "\033[0;32m"
YELL = "\033[0;33m"
UNDER = "\033[4m"
BLUE = "\033[0;34m"
CLEAR = "\033[0m"

class MySyntaxError(Exception):
	pass

class FileNotFoundError(Exception):
	pass		

def ft_final_step(my_bool, x, one_line, List_tmp, s, arg):
	if not List_tmp[1]:
		return
	tmp = "\t"
	if (my_bool):
		if arg == "-stepTrue":
			print (str(s)+" •\t" + one_line)
		tmp += GREEN + x + CLEAR
		if len(List_tmp[1]) > 1:
			tp = ""
			for elem in List_tmp[1]:
				tp += elem + ", "
			tmp += GREEN+"=>True" + CLEAR + " \t"
			tmp += UNDER+"So " + tp + "are True"+CLEAR
		else :
			tmp += GREEN+"=>True" + CLEAR + " \t"
			tmp += UNDER+"So " + List_tmp[1][0] + " is True"+CLEAR
		print (tmp)
	else:
		if (arg != "-stepTrue"):
			tmp += RED + x + CLEAR
			tmp += "=>"
			tmp += "\033[1;31mFalse " + CLEAR
			print (tmp)

def ft_steps(my_bool, ListDel, one_line, List_tmp, TrueList, s,arg):
	tmp = "\t"	
	if List_tmp[0][0] in TrueList:
		tmp += GREEN + List_tmp[0][0]
	else:
		tmp += RED + List_tmp[0][0]
	tmp += CLEAR + one_line[ListDel[0]]
	if List_tmp[0][1] in TrueList:
		tmp += GREEN + List_tmp[0][1]
	else:
		tmp += RED + List_tmp[0][1]
	if (my_bool):
		if arg == "-stepTrue":
			print (str(s)+" •\t" + one_line)
		tp = ""
		if len(List_tmp[1]) > 1:
			for elem in List_tmp[1]:
				tp += elem + ", "
			tmp += GREEN+"=>True" + CLEAR  + " \t"
			if len(List_tmp[0]) == 2:
				tmp += UNDER+"So " + tp + "are True"+CLEAR
		else :
			tmp += GREEN+"=>True" + CLEAR + " \t" 
			if len(List_tmp[0]) == 2:
				tmp += UNDER+"So " + List_tmp[1][0] + " is True"+CLEAR
		print (tmp)
	else:
		if (arg != "-stepTrue"):
			print (tmp + "\033[1;31m=>False" + CLEAR)

def ft_is_all_or(one_line, ListDel):
	for elem in ListDel:
		if (one_line[elem] != '|'):
			return (False)
	return (True)

def ft_check_is_better(elem, ListWeight):
	bkp1 = []
	bkp2 = []

	for e in ListWeight:
		# print ("e =")
		# print (e[0][0])
		if (elem == e[0][0]):
			bkp1 = e
		elif (("!" + elem) == e[0][0]):
			bkp2 = e
	# print ("hey this is bkp1")
	# print (bkp1)
	# print ("hey this is bkp2")
	# print (bkp2)
	if (bkp1 and bkp2):
		if (len(bkp1[1]) > len(bkp2[1])):
			return (True)
		else :
			return (False)
	return (True)


def ft_check_line(one_line, one_List, TrueList, AllElem, arg, s, ListWeight):
	List_tmp = [[],[]] * 1
	for el in one_List[0]:
		List_tmp[0].append(el)
	for el in one_List[1]:
		List_tmp[1].append(el)
	tmp_string = ""
	elem = ""
	ret = False
	stop = False
	OrList = []
	ListDel = [m.start() for m in re.finditer('(\||\+|\^)', one_line)]
	flag = False
	if arg == "-step":
		print (str(s)+" •\t" + one_line)
	# print ("line = "+ one_line)
	# print (ListDel);
	# print ("TrueList =")
	# print (TrueList)
	# if (ft_is_all_or(one_line, ListDel)):
	# 	print ("TRUUUUUUUE")
	while (len(List_tmp[0]) > 1):
		flag = True
		if (one_line[ListDel[0]] == '|'):
			if (List_tmp[0][0] not in TrueList and List_tmp[0][1] not in TrueList):
				if arg[:5] == "-step":
					ft_steps(False, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(0)
			elif (List_tmp[0][0] in TrueList):
				if arg[:5] == "-step":
					ft_steps(True, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(1)
			else:
				if arg[:5] == "-step":
					ft_steps(True, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(0)
		elif (one_line[ListDel[0]] == '+'):
			if (List_tmp[0][1] in TrueList and List_tmp[0][0] in TrueList):
				if arg[:5] == "-step":
					ft_steps(True, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(0)
			elif (List_tmp[0][0] in TrueList):
				if arg[:5] == "-step":
					ft_steps(False, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(0)
			else: 
				if arg[:5] == "-step":
					ft_steps(False, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(1)
		elif (one_line[ListDel[0]] == '^'):
			if (List_tmp[0][1] not in TrueList and List_tmp[0][0] in TrueList):
				if arg[:5] == "-step":
					ft_steps(True, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(1)
			elif (List_tmp[0][1] in TrueList and List_tmp[0][0] not in TrueList):
				if arg[:5] == "-step":
					ft_steps(True, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(0)
			else :
				if arg[:5] == "-step":
					ft_steps(False, ListDel, one_line, List_tmp, TrueList, s, arg)
				List_tmp[0].pop(1)
				List_tmp[0].pop(0)
		ListDel.pop(0)
	if (len(List_tmp[0]) == 1):
		line_right = one_line[one_line.find("=>")+2:]
		x = List_tmp[0][0]
		if x in TrueList:
			freshList = [[],[]]
			if not flag and arg[:5] == "-step" and not '^'  and not '|' in line_right:
				ft_final_step(True, x, one_line,List_tmp, s, arg)
			if len(ListDel) > 0:
				# print ("ListDel")
				# print (ListDel)
				# print (len(ListDel))
				while (len(ListDel) > 0):
					# print ("List_tmp[1]")
					# print (List_tmp[1])
					pos = one_line[ListDel[0]]
					# if pos == '^':
					# 	if List_tmp[1][0] in TrueList and List_tmp[1][1] not in TrueList:
					# 		print ("if")
					# 		freshList[1].append(List_tmp[1][0])
					# 	elif List_tmp[1][1] in TrueList and List_tmp[1][0] not in TrueList:
					# 		print ("else")
					# 		freshList[1].append(List_tmp[1][1])
					# 	if not flag and arg[:5] == "-step":
					# 		ft_final_step(True, x, one_line, freshList, s, arg)
					# 	print ("aaaaaahhhhhhh")
					# 	ListDel.pop(0)
					# 	List_tmp[1].pop(1)
					# 	List_tmp[1].pop(0)
					# 	continue 
					# print ("arg = ")
					# print (arg)
					if arg == '-interactif' and (pos == '|' or pos == '^'):
						# print ("interactif mode")
						exit = True
						while (exit):
							stop = False;
							if (len(ListDel) > 0):
								# print ("ATTFEFTG")
								pos = one_line[ListDel[0]]

							# print ("ListDel = ")
							# print (ListDel)
							# print ("List_tmp[1]")
							# print (List_tmp[1])
							# print ("freshList")
							# print (freshList)
							# print ("TrueList")
							# print (TrueList)

							if len(ListDel) == 0 and len(List_tmp[1]) == 0:
								exit = False
							else:
								while(True):
									if (List_tmp[1][0] in TrueList):
										stop = True;
										# print ("break")
										break
									key = input(BLUE + "Interactif mode: if you want " + List_tmp[1][0] + " True Type 'y' ortherwise 'n'" + CLEAR + "\n")
									if key == "y" or key == "Y":
										key = True
										break
									if key == "n" or key == "N":
										key = False
										break
								# print ("AFTER while")
								if not stop and key:
									# print ("if key")
									if List_tmp[1][0] not in TrueList:
										# print ("List_tmp[1][0] not in TrueList:")
										# print (List_tmp[1][0])
										freshList[1].extend([List_tmp[1][0]])
										TrueList.extend([List_tmp[1][0]])
										ft_nop(TrueList, elem)
								elif not stop and key == False and pos != '|':# and len(List_tmp[1]) == 2 and len(freshList[1]) == 0:
									# print ("if not key")
									# print ("List_tmp[1]")
									# print (List_tmp[1])
										# len(List_tmp[0]) == 0 and								
									if  List_tmp[1][1] not in TrueList:
										# print ("List_tmp[1][1] not in TrueList:")
										# print (List_tmp[1][1])
										freshList[1].extend([List_tmp[1][1]])
										TrueList.extend([List_tmp[1][1]])
										ft_nop(TrueList, elem)
										if (pos == '^'):
											TrueList.extend([List_tmp[1][1]])
								# print ("END")
								# print ("pos")
								# print (pos)

							if len(ListDel) == 0:
								break
							if len(ListDel) >= 1:
								ListDel.pop(0)
								if (pos == '^'):
									List_tmp[1].pop(1)
								List_tmp[1].pop(0)
								# print ("pllll")

								if not List_tmp[1]:
									break
						ret = True
						if ListDel:
							ListDel.pop(0)
						if List_tmp[1]:
							List_tmp[1].pop(0)
					else:
						# print ("else List_tmp[1]")
						# print (List_tmp[1])
						bkp = ""
						for elem in List_tmp[1]:
							if elem not in TrueList:# and ("!" + elem) not in TrueList:
								if (ft_check_is_better(elem, ListWeight) == False):
									continue
								if (len(ListDel) and one_line[ListDel[0]] == '^'):
									if (bkp in TrueList):
										bkp = elem
										continue
								elif (len(ListDel) and one_line[ListDel[0]] == '|'):
									OrList.extend([elem])
									if (len(OrList) % 2 == 1):
										ListDel.pop(0)

								freshList[1].extend([elem])
								TrueList.extend([elem])
								# if (one_line[ListDel[0]] == '^'):
								# 	List_tmp[1].pop(1)

								ft_nop(TrueList, elem)
								bkp = elem
							# elif len(ListDel) >= 1:
							# 	print ("List_tmpfwfwrfwfwefwefwef")
							# 	print (List_tmp)
							# 	print ("ListDelfr3fr")
							# 	print (ListDel)
							# 	if (len(ListDel) >= 1 and one_line[ListDel[0]] == '^' and len(List_tmp[1]) >= 1):
							# 		print ("pop1")
							# 		List_tmp[1].pop(1)
							# 	print ("pop0")
							# 	List_tmp[1].pop(0)
							# 	ListDel.pop(0)

						if not flag and arg[:5] == "-step":
							ft_final_step(True, x, one_line, freshList, s, arg)
						# print ("RETURN True")
						return (True)
			else:
				if not flag and arg[:5] == "-step":
					ft_final_step(True, x, one_line,List_tmp, s, arg)
				for elem in List_tmp[1]:
					if elem not in TrueList:
						TrueList.extend([elem])
						ft_nop(TrueList, elem)
						ret = True
				List_tmp[1].pop(0)
		else:
			if not flag and arg[:5] == "-step":
				ft_final_step(False, x, one_line,List_tmp, s, arg)
		if (ret):
			return (True)
	return (False)

def 	ft_nop(TrueList, elem):
	if "!" in elem:
		if elem[1:] in TrueList:
			TrueList.remove(elem[1:])
	else:
		if "!"+elem in TrueList:
			TrueList.remove("!"+elem)

def 	ft_getkey(key):
	if key == "Y" or key == "y":
			return True
	if key == "N" or key == "n":
			return True
	return False

def		ft_resolv(ListSystem, ListLine, TrueList, AllElem, QueryList, arg, ListWeight):
	# print ("ft_resolv")
	length = len(ListLine)
	i = 0
	s = 1
	while (i < length):
		if (ft_check_line(ListLine[i], ListSystem[i], TrueList, AllElem, arg, s, ListWeight) == True):
			ListLine.pop(i)
			ListSystem.pop(i)
			length = len(ListLine)
			i = 0
			ft_query(QueryList, TrueList, False)
			if len(QueryList) == 0:
				return
		else:
			i += 1
		s += 1
	ft_query(QueryList, TrueList, True)

def 	ft_parentheses(line):
	if "=>" in line:
		posD = line.find("=>")
		line_right = line[posD+2:]
		if '(' in line_right or ')' in line_right:
			raise MySyntaxError("parentheses in conclusion are forbidden '" + line_right + "'")
	else:
		return line
	OpenList = [m.start() for m in re.finditer(r'(\()', line)]
	while (len(OpenList) > 0):
		a = 0
		OpenList = [m.start() for m in re.finditer(r'(\()', line)]
		CloseList = [m.start() for m in re.finditer(r'(\))', line)]
		while (a < len(OpenList) - 1) :
			if OpenList[a] > CloseList[0]:
				break 
			a += 1
		if (OpenList[a] != 1 and len(OpenList) == 1):
			tmp = line[OpenList[a]+1:CloseList[0]]
			if not tmp:
				line = line[:OpenList[a]-1]+line[CloseList[0]+1:]
			else:
				if (OpenList[a] <= 0):
					line = tmp + line[:0]+line[CloseList[0]+1:]
				else:
					line = tmp + line[OpenList[a]-1] + line[:OpenList[a]-1]+line[CloseList[0]+1:]
		else:
			tmp = line[OpenList[a]:CloseList[0]+1]
			tmp = tmp[:-1]
			tmp = tmp[1:]
			i = OpenList[a]
			if (tmp):
				while (i > 0):
					if (line[i] in "+|^"):
						tmp += line[i]
						break
					i -= 1
			line = tmp + line[:OpenList[a]] + line[CloseList[0]+1:]
		OpenList.pop(a)
		CloseList.pop(0)
	return (line)

def 	ft_priority(line):
	if "=>" in line:
		posD = line.find("=>")
		my_str = line[:posD]
		if '|' in my_str and '+' in my_str:
			posa = my_str.find('|')
			posb = my_str.find('+')
			if posa < posb:
				tmp = my_str[posa] + my_str[:posa]
				my_str = my_str[posa+1:] + tmp + line[posD:]
				return (my_str)
	return(line)

def 	ft_double(line):
	ret = [m.start() for m in re.finditer('(\||\+|\^|=>|<=>)', line)]
	for x, elem in enumerate(ret):
		if x > 0:
			if elem - ret[x-1] == 1:
				return True
	return False

def 	ft_syntax(line):
	stri = ""
	ret = re.findall("(!\+|!=|!^|!\||!!|\?\?)", line)
	if (len(ret) > 0):
		for elem in ret[:-1]:
			stri += elem + ", "
		stri += ret[-1]
	if (stri):
		print (YELL +YELL + "SyntaxError Error" + CLEAR + " : Unexpected charactere in : '"+line+"'\n\tThe Following was unexpected : " + stri)
	stri = ""
	if (line[0] == '='):
		ret = re.findall("(\?|!|\+|^|\\|!!|\?\?)", line)
		if (len(ret) > 0):
			for elem in ret[:-1]:
				if not (elem):
					continue
				stri += elem + ", "
			stri += ret[-1]
		if (stri):
			print (YELL +YELL + "SyntaxError Error" + CLEAR + " : Unexpected charactere in : '"+line+"'\n\tThe Following was unexpected : " + stri)
	stri = ""
	if (len(line) > 1 and line[0] == '?'):
		strok = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
		line = line[1:]
		for c in line[:-1]:
			if (c not in strok):
				stri += c + ", "
		if (len(line) and line[-1] not in strok):
			stri += line[-1]
		if (stri):
			print (YELL +YELL + "SyntaxError Error" + CLEAR + " : Unexpected charactere in : '"+line+"'\n\tThe Following was unexpected : " + stri)

def 	ft_filtre(line):
	stri = ""
	if "()" in line:
		while ("()" in line):
			line = line.replace("()","")
	ret = re.findall("[^A-Z^+<=>?!()|]",line)
	if len(ret) > 0:
		if (len(ret) > 1):
			for e in ret[:-1] :
				stri += e + ", "
			stri += ret [-1]
		else:
			stri += ret[0]
		raise MySyntaxError("Unexpected charactere in : '"+line+"'\n\tThe Following was unexpected : " + stri)
		# return True
	if ft_double(line):
		raise MySyntaxError("Unexpected charactere in : '"+line+"'\n\tDoublon detected")
	ft_syntax(line)

	return False

def 	ft_syntax_parse(ListLine, TrueList, line, QueryList):
	ft_filtre(line)
		# raise MySyntaxError("Unexpected charactere in '"+line+"'")
	if "(" in line or ")" in line:
		if (line.count('(') != line.count(')')):
			raise MySyntaxError("unbalanced parentheses in '"+ line + "'")
		line = ft_parentheses(line)
	elif '|' in line and '+' in line:
		line = ft_priority(line)
	if ft_double(line):
		raise MySyntaxError("Unexpected charactere in '"+line+"'")
	if line.count('=') > 1 and line.count('>') > 1:
			raise MySyntaxError("format error in : '" + line + "'\n\tUnexpected '=>'")
	if line.count('=') > 1:
			raise MySyntaxError("format error in : '" + line + "'\n\tUnexpected '='")
	if line.count('>') > 1:
			raise MySyntaxError("format error in : '" + line + "'\n\tUnexpected '>'")
	if "<=>" in line:
		pos = line.find("<=>")
		ListLine.append(line.replace("<", ""))
		sstr = line[pos+3:] + "=>"
		sstr += line[:pos]
		line = sstr
	if "=>" in line:
		stri = ""
		if ('?' in line):
			for x in range(0, line.count('?')):
				stri += "?"
				print (YELL +"SyntaxError Error" + CLEAR + " : Unexpected charactere '" + stri +"'' in  line '"+line+"'")
		ListLine.append(line)
	elif (line[0] == "="):
		if len(TrueList) > 0:
			TrueList[0] += line[1:]
		else :
			TrueList.append(line[1:])
	elif (line[0] == "?"):
		if len(QueryList) > 0:
			QueryList[0] += line[1:]
		else :
			QueryList.append(line[1:])
	else:
		raise MySyntaxError("bad syntax in '"+line+"'")

def 	ft_open_and_read(filename, ListLine, TrueList, QueryList):
	bkp = ""
	with open(filename) as file:
		for i, line in enumerate(file):
			line = line.replace(' ', '').replace('\t' , '').replace('\n','')
			if ("#" in line):
				line = line[:line.find("#")]
			if (line):
				try:
					bkp += line+"\n"
					ft_syntax_parse(ListLine, TrueList, line, QueryList)
					pass
				except MySyntaxError as e:
					print (RED + "SystemError : " + CLEAR + "line " + str(i+1) + ": " +str(e))
					raise SystemError()
	if not ListLine:
		raise RuntimeError(RED + "Parsing Error : Empty File" + CLEAR)
	if not TrueList:
		TrueList.append("")
	if not QueryList or ( not QueryList[0] ):
		raise RuntimeError(RED + "Parsing Error : No Query found" + CLEAR)
	else:
		print (WHITE+"YOUR INPUT :"+ CLEAR)
		print (bkp)

def 	ft_parse_line(ListLine, TrueString, AllElem):
	new_list = []
	tmp = []
	for line in ListLine:
		for elem in (re.split(r"[+^|]|=>|<=>", line)):
			# print ("elem =")
			# print (elem)
			if (elem and elem not in AllElem):
				if "!" in elem and elem not in AllElem:
					if (elem[1:] and elem[1:] not in AllElem):
						AllElem.append(elem[1:])
					AllElem.append(elem)
					tmp.append(elem[1:])
				else:
					AllElem.append(elem)
	for elem in AllElem:
		if elem in TrueString:
			new_list.append(elem)
	for elem in tmp:
		if (elem not in TrueString):
			new_list.append("!"+elem)
	return new_list

def     ft_get_right_part(line_right, AllElem):
	line_right += "=>"
	lDel = ['+','^','|','=']
	new_list = [[]]*1
	posa = 0
	for x, i in enumerate(line_right):
		for el in lDel:
			if el == i:
				posb = x
				if (line_right[posa:posb] not in new_list[0] and line_right[posa:posb] in AllElem):
					new_list[0].append(line_right[posa:posb])
					posa = posb+1
	return new_list

def 	ft_get_right_part2222(line_right, AllElem, TheFinalList):
	line_right += "=>"
	lDel = ['+','^','|','=']
	lDel2 = ['+','|', '=']
	new_list = [[]]*1
	ret_list = [[]]*1
	posa = 0

	string = ""
	for x, i in enumerate(line_right):		
		# print(line_right)
		for el in lDel2:
			if el == i:
				posb = x
				if (line_right[posa:posb] not in string):# and line_right[posa:posb] in AllElem):
					# print (line_right[posa:posb])
					string += line_right[posa:posb] + el
				posa = posb + 1

	if (len(string) > 2 and string[-1] != '='):
		# print ("DIFF")
		string = string[:-1] + '=>'
	# print ("string")
	# print (string)

	posa = 0
	for x, i in enumerate(string):
		# print(string)
		# print ("line_right")
		for el in lDel2:
			if el == i:
				posb = x
				# print (string[posa:posb])
				if (string[posa:posb] not in new_list[0] and string[posa:posb] in AllElem):
					new_list[0].append(string[posa:posb])
					posa = posb+1
	# print ("new_list ==")
	# print (new_list)
	for elem in new_list[0]:
		if (elem in TheFinalList):
			ret_list[0].append(elem)
	# print ("new_list222 ==")
	# print (ret_list)
	return ret_list

def 	ft_get_left_part(line_left, AllElem):
	new_list = []
	lDel = ['+','^','|','=']
	posa = 0
	for x, i in enumerate(line_left):
		if i in lDel:
			posb = x
			if (line_left[posa:posb] not in new_list and line_left[posa:posb] in AllElem):
				new_list.append(line_left[posa:posb])
				posa = posb+1
	return new_list

def 	ft_parse_system(ListLine, AllElem):
	final_list = []
	for line in ListLine:
		new_list = []
		pos = line.find("=>")
		new_list.append(ft_get_left_part(line[:pos+2], AllElem))
		new_list.extend(ft_get_right_part(line[pos+2:], AllElem))
		final_list.append(new_list)
	return final_list


def 	ft_parse_weight(ListLine, AllElem, TheFinalList):
	# print ("PART")
	final_list = []
	for line in ListLine:
		new_list = []
		pos = line.find("=>")
		new_list.append(ft_get_left_part(line[:pos+2], AllElem))

		new_list.extend(ft_get_right_part2222(line[pos+2:], AllElem, TheFinalList))
		# new_list.extend((str(line.count('|') + line.count('+') + 1)))
		final_list.append(new_list)
	return final_list

def 	ft_query(QueryList, TrueList, pre):
	my_len = len(QueryList)
	x = 0
	z = 0
	while (x < my_len):
		if QueryList[x] in TrueList:
			print (GREEN + QueryList[x] + " is True" + CLEAR)
			QueryList.pop(x)
			my_len = len(QueryList)
		else:
			if pre is True:
				print (RED + QueryList[x] + " is False" + CLEAR)
			x +=1
		z += 1

def 	ft_update(QueryList, AllElem):
	new_list  = []
	for elem in AllElem:
		if elem in QueryList[0] and elem not in new_list:
			new_list.extend(elem)
	print (BLUE + "The Following Querry are valid : ", end="")
	for x, elem in enumerate(new_list):
		print(elem, end="")
		if x+1 == len(new_list):
			print ("")
		else:
			print (", ", end="")
	print (CLEAR, end="")
	return new_list


def 	makemylist(ListSystem, QueryList):
	TheFinalList = []
	
	for elem in QueryList:
		TheFinalList.append(elem)
	
	for elem in ListSystem:
		TheFinalList.append(elem[0][0])
	return (TheFinalList)

def 	main(filename, arg):
	ListLine = []
	ListSystem = []
	AllElem = []
	TrueList = []
	QueryList = []
	TheFinalList = []
	try :
		ft_open_and_read(filename, ListLine, TrueList, QueryList)
		pass
	except OSError as e:
		raise FileNotFoundError(RED+"FileNotFoundError : " + CLEAR +  filename + ' not found')
		pass
	TrueList = ft_parse_line(ListLine, TrueList[0], AllElem)
	# print ("AllElem")
	# print (AllElem)
	# print ("TrueList")
	# print (TrueList)
	QueryList = ft_update(QueryList, AllElem)
	# print ("QueryList")
	# print (QueryList)
	if arg[:5] == '-step':
		print (GREEN + "Green Token are True " + CLEAR + "|" + RED + " Red Token are False" + CLEAR)
	ft_query(QueryList, TrueList, False)
	if len(QueryList):
		ListSystem = ft_parse_system(ListLine, AllElem)
		# print ("ListSystem")
		# print (ListSystem)
		TheFinalList = makemylist(ListSystem, QueryList)
		# print ("TheFinalList")
		# print (TheFinalList)
		ListWeight = ft_parse_weight(ListLine, AllElem, TheFinalList)
		# print ("ListWeight")
		# print (ListWeight)
		# return (0)
		ft_resolv(ListSystem, ListLine, TrueList, AllElem, QueryList, arg, ListWeight)
	return (0)

if __name__ == "__main__":
	my_arg = ["-step","-stepTrue","-interactif"]
	try:
		l = len(sys.argv)
		if l == 2 and sys.argv[1] not in my_arg:
			main (sys.argv[1], "")
		elif l == 3 and sys.argv[1] == my_arg[0]:
			main (sys.argv[2], my_arg[0])
		elif l == 3 and sys.argv[1] == my_arg[1]:
			main (sys.argv[2], my_arg[1])
		elif l == 3 and sys.argv[1] == my_arg[2]:
			main (sys.argv[2], my_arg[2])
		else:
			print ("USAGE = ./main -[ARG] [FILNAME]")
			print ("-step : for step by step explanation")
			print ("-stepTrue : To see only True step")
			print ("-interactif : To choose in case of underterminded conclusion")
		pass
	except RuntimeError as e:
		print ("RuntimeError")
		print (e)
		pass
	except FileNotFoundError as e:
		print ("FileNotFoundError")
		print (e)
		pass
	except SystemError as e:
		print ("SystemError")
		pass
	# except Exception as e:
	# 	print ("Exception")
	# 	print (RED+"Unexpected Error"+CLEAR)
	# 	pass
	except KeyboardInterrupt as e:
		print("KeyboardInterrupt")
		pass

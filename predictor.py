def predictor() :

	from IPython.display import clear_output
	from pickle import load
	from os import system
	def clean() :
		__clean__ = system('cls')
	file = open('classifier.pkl','rb')
	clf = load(file)
	s = True
	while s :
		review = input('\n Enter your review : ')
		prd = clf.predict([review])[0]
		if prd == 'pos' :
				print('\n\n\nIt\'s a POSITIVE review    :) \n\n\n')
		else :
				print('\n\n\nIt\'s a NEGATIVE review    :( \n\n\n')
		a = input('Do you wanna check another review ? (Y/N) ')
		if a.lower() == 'n':
				s = False
				clean()
		else :
				clean()
				continue

def test() :

	print('success')
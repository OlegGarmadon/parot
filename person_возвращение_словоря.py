def build_person(first_name, last_name):
	"""Возвращает словарь с информацией о человеке."""
	person = {'first': first_name, 'last': last_name}
	return person


musician = build_person('greg', 'filips')
print(musician)

def build_person(first_name, last_name, age=None):
	"""Возвращает словарь с информацией о человеке."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person


musician = build_person('greg', 'filips', age=34)
print(musician)
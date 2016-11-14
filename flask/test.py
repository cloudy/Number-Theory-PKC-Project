import os
import math
import itertools
from fractions import gcd
from random import randint
import binascii
import struct

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import Required



DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

def is_prime(num):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				return False;
				break
		else:
			return True;
	else:
		return False;

#Extended euclidean algorithm from:
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

def main():
	p = 2**31-1
	q = 2**61-1
	n = p * q
	phi = (p-1)*(q-1)
	
	e = randint(0,phi)
	while gcd(e, phi) != 1:
		e = randint(0,phi)
	
	bezout = xgcd(e, phi)
	
	d = bezout[1]%phi
	
	#words = 'sda'
	#print("ORIGINAL STRING: ", words)
	#m = toBinary(words)
	#print("WORDS TO BINARY: ", m)	
	#decword = toString(m)
	#print("DECWORD  DECODE: ",decword)
	#print("WORDS TO BINARY: ",m)
	m = 2**91
	print("ORIGINAL BEFR: ", m)
	#m = int(input("enter an int: "))

	c = pow(m,e,n)
	print("CIPHERTEXT ENC : ", c)


	decode = pow(c,d,n)
	print("ORIGINAL TEXT IN: ", decode)


if __name__ == "__main__":
	main()
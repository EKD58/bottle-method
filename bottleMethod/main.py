#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
bottle sample code.
Method test
main function
"""

import bottle



HOST = 'localhost'
PORT = 50000



# -----------------------------------------------------------------------------
@bottle.route('/argTest')
@bottle.route('/argTest/')
@bottle.route('/argTest/<arg>')
@bottle.route('/argTest/<arg>/')
def arg_test_func(arg='defaultArgument'):
	"""
	argument test

	http://HOST:PORT/argTest
		-> Hello defaultArg

	http://HOST:PORT/argTest/
		-> Hello defaultArg

	http://HOST:PORT/argTest/xxx
		-> Hello xxx

	http://HOST:PORT/argTest/xxx/
		-> Hello xxx

	http://HOST:PORT/argTest/xxx/yyy
		-> 404

	http://HOST:PORT/argTest/xxx/yyy/
		-> 404
	"""
	return 'Hello {arg}'.format(arg=arg)



# -----------------------------------------------------------------------------
@bottle.route('/dateTest')
@bottle.route('/dateTest/')
@bottle.route('/dateTest/<month:re:[a-z]+>/<day:int>/<path:path>')
def date_test_func(month='99', day=99, path='xxx'):
	"""
	argument test 2

	http://HOST:PORT/dateTest
		-> Hello month=99 day=99 path=xxx

	http://HOST:PORT/dateTest/
		-> Hello month=99 day=99 path=xxx

	http://HOST:PORT/dateTest/april
		-> 404

	http://HOST:PORT/dateTest/april/
		-> 404

	http://HOST:PORT/dateTest///
		-> 404

	http://HOST:PORT/dateTest////
		-> 404

	http://HOST:PORT/dateTest/april//xxx
		-> 404

	http://HOST:PORT/dateTest//77/xxx
		-> 404

	http://HOST:PORT/dateTest/yyy/77/xxx
		-> Hello month=yyy day=77 path=xxx

	http://HOST:PORT/dateTest/april/29//dev/null
		-> Hello month=april day=29 path=/dev/null

	http://HOST:PORT/dateTest/aprilll/88////dev/null////
		-> Hello month=aprilll day=88 path=///dev/null///
	"""
	return 'Hello month={month} day={day} path={path}'.format(month=month, day=day, path=path)



# -----------------------------------------------------------------------------
#@get('/postTest')
#@get('/postTest/')
@bottle.route('/postTest', method='GET')
@bottle.route('/postTest/', method='GET')
def get_post_test():
	"""
	return the page calling POST method /postTest (input of Param1 and param2)

	http://HOST:PORT/postTest
		-> Param1:None  Param2:None

	http://HOST:PORT/postTest/
		-> Param1:None  Param2:None

	http://HOST:PORT/postTest?
		-> Param1:None  Param2:None

	http://HOST:PORT/postTest?aaa=123
		-> Param1:None  Param2:None

	http://HOST:PORT/postTest?p1=123
		-> Param1:123  Param2:None

	http://HOST:PORT/postTest/?p1=123
		-> Param1:123  Param2:None

	http://HOST:PORT/postTest?p1=zzzzz&
		-> Param1:zzzzz  Param2:None

	http://HOST:PORT/postTest?p1=zzzzz&p2
		-> Param1:zzzzz  Param2:None

	http://HOST:PORT/postTest?p1=zzzzz&p2=
		-> Param1:zzzzz  Param2:None

	http://HOST:PORT/postTest?p1=zzzzz&p2=ppppp
		-> Param1:zzzzz  Param2:ppppp (* Display)

	http://HOST:PORT/postTest?p1=zzzzz&param2=ppp
		-> Param1:zzzzz  Param2:None
	"""
	param1 = bottle.request.query.get('p1')
	param2 = bottle.request.query.get('p2')

	#GETで何も渡されていない時はparam1,param2に何も入れない
	param1 = "" if param1 is None else param1
	param2 = "" if param2 is None else param2

	return '''
	<form action="/postTest" method="post">
		Param1: <input name="param1" type="text" value="{param1}"/></br>
		Param2: <input name="param2" type="param2" value="{param2}"/></br>
		<input value="postTest" type="submit" /></br>
	</form>
	'''.format(param1=param1, param2=param2)



# -----------------------------------------------------------------------------
#@post('/postTest')
@bottle.route('/postTest', method='POST')
def post_post_test():
	"""
	post test

	http://HOST:PORT/postTest
		param1=uuu
		param2=ppp
			-> uuu ppp

	http://HOST:PORT/postTest
		param1=uuuu
			-> uuuu None

	http://HOST:PORT/postTest?param1=zzzzz&param2=ppppp
		param1=uuu
		param2=ppp
			-> uuu ppp
	"""
	param1 = bottle.request.forms.get('param1')
	param2 = bottle.request.forms.get('param2')

	return "Hello POST {param1} {param2}".format(param1=param1, param2=param2)



# -----------------------------------------------------------------------------
@bottle.route('/putTest', method='PUT')
def put_test():
	"""
	put test

	http://HOST:PORT/putTest
	"""

	return "Hello PUT"



# -----------------------------------------------------------------------------
@bottle.route('/deleteTest', method='DELETE')
def delete_test():
	"""
	delete test

	http://HOST:PORT/deleteTest
	"""

	return "Hello DELETE"



# -----------------------------------------------------------------------------
@bottle.error(404)
def error404(error):
	"""
	404 Not found

	http://HOST:PORT/hoge
	"""
	return "404 page {err}".format(err=error)



# -----------------------------------------------------------------------------
def main():
	"""
	main function
	"""

	bottle.run(host=HOST, port=PORT, debug=True)
	return 0

from multiprocessing import Process
import sys
import taggers
import time

sentence = ("All truth passes through three stages. First, "
			"it is ridiculed. Second, it is violently opposed. "
			"Third, it is accepted as being self-evident. "
			"- Arthur Schopenhauer (1788-1860) ")


def func1():
	start = time.time()
	print 'NLTK Tagging: starting'
	t = taggers.nltk_tag(sentence)
	pass
	end = time.time()
	print '\nNLTK Tagging: finishing\ntags:%s' % t,'\ntime:',(end - start)

def func2():
	start = time.time()
	print 'Senna Tagging: starting'
	t = taggers.senna_tag(sentence) 
	pass
	end = time.time()
	print '\nSenna Tagging: finishing\ntags:%s' % t,'\ntime:',(end - start)

def func3():
	start = time.time()
	print 'Stanford Tagging: starting'
	t = taggers.stanford_tag(sentence) 
	pass
	end = time.time()
	print '\nStanford Tagging: finishing\ntags:%s' % t,'\ntime:',(end - start)

if __name__ == '__main__':
	p1 = Process(target=func1)
	p1.start()
	p2 = Process(target=func2)
	p2.start()
	p3 = Process(target=func3)
	p3.start()
	p1.join()
	p2.join()
	p3.join()


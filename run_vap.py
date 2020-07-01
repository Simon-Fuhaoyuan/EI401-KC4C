#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os, shutil

__metaclass__ = type

class vap:
	def __init__(self,):
		self.working = False
	
	def work(self, path):
		self.working = True
		os.system('bash /home/atlas/kc401-Group3/run_vap.sh')
		del_ls = os.listdir(path)
		for name in del_ls:
			file_path = os.path.join(path, name)
			try:
				os.remove(file_path)
			except:
				shutil.rmtree(file_path)
		shutil.move('/home/atlas/video_person/video', path)
		self.working = False
	
	def is_working(self):
		return self.working

if __name__ == '__main__':
	path = '/home/atlas/video_test'
	a = vap()
	a.work(path)
	

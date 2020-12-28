#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import argparse
import extractor
import helper
from os import walk
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.title("Imagic")

frame = Frame(root,height=600,width=600)
frame.pack()

def opendir():
	global inputdir
	root.directory=tkFileDialog.askdirectory()
	inputdir=root.directory
	print(root.directory)

def save():
	global outputdir
	root.savedirectory=tkFileDialog.askdirectory()
	outputdir=root.savedirectory
	print(root.savedirectory)

def start():
	global inputdir, outputdir
	helper.initialize_sqli()
	image_list = list(helper.list_files(inputdir, "image/jpeg"))

	for filename in image_list:
		print ("Processing %s" % (filename,))
		# Creation of the SQLite row for the file
		helper.image_row("evidences", filename)
		extractor.basic_info(filename)
		if gps.get():
			extractor.PIL_exif_data_GPS(filename)
		if md5.get():
			extractor.md5(filename)
		if sha256.get():
			extractor.sha256(filename)
		if sha512:
			extractor.sha512(filename)
		if exif.get():
			extractor.exif_info(filename)
		helper.create_csv(outputdir)

def var_state():
	print ("MD5 status: %d" % md5.get())
	print ("Sha265 status: %d" % sha256.get())
	print ("Sha512 status: %d" % sha512.get())
	print ("exif status: %d" % exif.get())
	print ("gps status: %d" % gps.get())
	print ("error status: %d" % error_analysis.get())

label_1 = Label(frame, text="Add Image Directory(more than one image and must be JPEG)")
label_2 = Label(frame, text="Save file destination")
# label_3 = Label(frame, text="Selected files")
label_4 = Label(frame, text="Extract exif metadata and image hashing")
label_5 = Label(frame, text="Calculate perceptual image hashing")

# button_1 = Button(frame, text="Browse")
button_1 = Button(frame, text="Browse", command=opendir)
button_2 = Button(frame, text="Browse", command=save)
button_3 = Button(frame, text="Start", command=start)
# button_5= Button(frame, text="Show", command=var_state)


exif=Tkinter.IntVar()
gps=Tkinter.IntVar()
error_analysis=Tkinter.IntVar()
md5=Tkinter.IntVar()
sha256=Tkinter.IntVar()
sha512=Tkinter.IntVar()

check_1 = Checkbutton(frame, text="Extract exif metadata", variable=exif)
check_2 = Checkbutton(frame, text="Extract, parse and convert to coordinates, GPS exif metadata from images*", variable=gps)
# check_3 = Checkbutton(frame, text="Extract, Error Level Analysis image*", variable=error_analysis)

check_5 = Checkbutton(frame, text="MD5", variable=md5)
check_6 = Checkbutton(frame, text="SHA256", variable=sha256)
check_7 = Checkbutton(frame, text="SHA512", variable=sha512)
# print(var.get())
label_1.grid(column=0, row=0)
button_1.grid(column=0, row=1, padx=20, pady=10)
label_2.grid(column=0, row=4)
button_2.grid(column=0, row=5, padx=20, pady=10)
button_3.grid(column=0, row=9)
# button_5.grid(column=0, row=10)
# label_3.grid(column=1, row=0)
label_4.grid(column=2, row=2)
check_1.grid(column=2, row=1, sticky=W)
check_2.grid(column=2, row=2, sticky=W)
# check_3.grid(column=2, row=3, sticky=W)
# check_4.grid(column=2, row=4, sticky=W)
label_5.grid(column=2, row=5)
check_5.grid(column=2, row=6, sticky=W)
check_6.grid(column=2, row=7, sticky=W)
check_7.grid(column=2, row=8, sticky=W)

root.mainloop()
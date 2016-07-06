#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
Author: Suresh Podeti
written on :

This program provides an API to manage todo list



"""
import sys,os
import argparse


def add_event(event_string):
 
 print "event added successfully!"
def delete_event(event_id=None):
 print "event deleted successfully!"
def search_event(event_id=None):
 print "search results are:"
def show_list():
 print "prints list of items" 

def main():
 parser=argparse.ArgumentParser(description='To do list command line arguments')
 parser.add_argument('a','--add',help='adds an event to the list',action='store',type=str)
 parser.add_argument('d','--delete',help='delete an event by id',action='store',type=int)
 parser.add_argument('s','--search',help='search an event by id',action='store',type=int)
 parser.add_argument('l','--completelist',help='show the list of all events',action='store')
 args=parser.parse_args()
 
 if args.add:
  add_event(args.add)
 if args.delete:
  delete_event(args.delete)
 if args.search:
  search_event(args.search)
 if args.completelist:
  show_list()

if __name__=='__main__':
 main()

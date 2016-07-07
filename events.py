#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
Author: Suresh Podeti
written on :07/07/16

This program provides an API to manage todo list



"""
import sys,os
import argparse
import json
import time

#function to add an event
def add_event(event_string):
 date=time.strftime('%x')
 a_dict={date:event_string}
 if os.path.isfile('suresh.json'):
  with open('suresh.json') as fh:
   data=json.load(fh)
  data.update(a_dict)
  with open('suresh.json','w') as fh:
   json.dump(data,fh)
  
 else:
  fh=open('suresh.json','w')
  json.dump(a_dict,fh)
 print "event added successfully!"

#function to delete an event by date(event id)
def delete_event(event_id=None):
 if os.path.isfile('suresh.json'):
  with open('suresh.json') as fh:
   data=json.load(fh)
   del data[event_id]
  with open('suresh.json','w') as fh:
   json.dump(data,fh)
 else:
  print "No event to delete." 
 print "event deleted successfully!"



#function to search event by date 
def search_event(event_id=None):
 if os.path.isfile('suresh.json'):
  with open('suresh.json') as fh:
   data=json.load(fh)
   return data[event_id]
 else:
   print "No event exist in the list"

#function to show list of events
def show_list():
 if os.path.isfile('suresh.json'):
  with open('suresh.json') as fh:
   data=json.load(fh)
  return data
 else:
  print "No events show in the list"
  

def main():
 parser=argparse.ArgumentParser(description='To do list command line arguments')
 parser.add_argument('-a','--add',help='adds an event to the list',action='store',type=str)
 parser.add_argument('-d','--delete',help='delete an event by date format dd/mm/yy',action='store',type=str)
 parser.add_argument('-s','--search',help='search an event by date format dd/mm/yy',action='store',type=str)
 parser.add_argument('-l','--completelist',help='show the list of all events')
 args=parser.parse_args()
 
 if args.add:
  add_event(args.add)
 if args.delete:
  delete_event(args.delete)
 if args.search:
  print  search_event(args.search)
 if args.completelist:
  print show_list()

if __name__=='__main__':
 main()

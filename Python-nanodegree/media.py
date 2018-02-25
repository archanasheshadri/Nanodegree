# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 12:43:09 2017

@author: archa
"""
import webbrowser

class Movie():
    """This is to test"""
    
    def __init__(self,movie_title,trailer_youtube):
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube
        
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:26:41 2017

@author: archa
"""

import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None,
                "insr": []
        }

        # YOUR CODE HERE
        fnm = author.find('fnm')
        if fnm is not None:
            data['fnm'] = fnm.text
        snm = author.find('snm')
        
        if snm is not None:
            data['snm'] = snm.text
            
        email = author.find('email')
        if email is not None:
            data['email'] = email.text
            
        
        for insr in author.iter('insr'):
            iid = insr.attrib['iid']
            #for iid in insr.attrib['iid'] :
            data['insr'].append(iid)
                
            
        

        authors.append(data)

    return authors


def test():
    
    root = get_root(article_file)
    data = get_authors(root)
    print data

test()

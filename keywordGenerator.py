#takes a keyword in and generates two files: a keyword and generated keywords; and a keyword definition file

import traceback
import sys
import re
import time
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from nltk.corpus import wordnet as wn

masterKeywordFile = open('decode_wordnet/masterKeywordFile.TXT','w') #keyword definition file
keywordTreeFile = open('decode_wordnet/keywordTreeFile.TXT','w') #keyword generation file

masterKeywordList = []
masterKeywordList = masterKeywordList + ['allocation']   #initial word, in this case 'allocation'

driver = webdriver.Firefox()  #use Firefox
driver.get("http://aione.tritera.com/gui/goto.main.php#")  #go to website
time.sleep(10) #wait 10 sec for browser to load

for masterKeywordListIndex in range(0,201):  #do this for 200 words in masterKeywordList
    
    wordnetDefs = []
    for i in range(0,20):  #print every definition possible for the word in master keyword file (expect less than 20 definitions)
        try: #replaces spaces with underscores
            keyword = masterKeywordList[masterKeywordListIndex]
            keyword = keyword.replace(' ','_')  #wordnet needs underscores not spaces
            wordnetDefs = wordnetDefs + [wn.synsets(keyword)[i].definition()] #wordnet lookup
            masterKeywordFile.write( keyword + '\t' + str(wordnetDefs[i]) +'\n')
        except:
            pass

    for k in range(0,len(wordnetDefs)):  #do this for each wordnet definition of the keyword
        
        if 'computer science' in wordnetDefs[k]: #takes (computer science) out of string
            wordnetDefs[k] = wordnetDefs[k][19:] #starts 19 characters after first paranthesis in (computer sci...
            
        elem = driver.find_element_by_link_text('Source')  #find Source tab and store to element elem
        elem.click()  #click Source tab
        time.sleep(1) #give some time after click
        elem2 = driver.find_element_by_id('sourceText')  #find text element
        elem2.clear()  #clear the contents of the textbox
        elem2.send_keys(wordnetDefs[k]) #input definition
        driver.find_element_by_id("btn_find_all").click()  #click
        time.sleep(10) #wait 10 sec for page to load results
        
        for i in range(0,20):  #get up to 20 keywords (expect less)
            try:
                value1 = driver.find_element_by_id('.word'+str(i)+'. ').get_attribute("value")
                time.sleep(5)
                if str(value1) in masterKeywordList:
                    pass
                else:  #store keyword if returned keyword not in master keyword list
                    masterKeywordList = masterKeywordList + [str(value1)]
                    keywordTreeFile.write(keyword + '\t' + str(value1) + '\n')
            except Exception, err:
                #print traceback.format_exc()
                break #it was hanging here, so break was necessary        

masterKeywordFile.close()
keywordTreeFile.close()
driver.close()
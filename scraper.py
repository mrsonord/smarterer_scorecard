import scraperwiki
import lxml.html
# 
# # Read in a page
html = scraperwiki.scrape("http://smarterer.com/Mrsonord")
root = lxml.html.fromstring(html)
for el in root.cssselect("div.unit img", "div.unit a", "div.unit h4"):           
    print el.attrib['src']
    print el.text
# 
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
# 
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
# 
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")
# PLEASE READ THIS BEFORE EDITING
#
# This script generates your email alerts, to tell you when your scrapers
# are broken or someone has edited them.
#
# It works by emailing you the output of this script. If you read the code and
# know what you're doing, you can customise it, and make it send other emails
# for other purposes.

#from html5lib import parse
#root = parse(content, treebuilder='lxml', namespaceHTMLElements=False)




#print html



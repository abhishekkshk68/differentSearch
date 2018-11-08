from flask import Flask,render_template,request
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from whoosh.fields import *
from whoosh.qparser import QueryParser, SequencePlugin, PhrasePlugin
import whoosh.qparser as qparser

index_path = r"C:\Users\Abhi\Google Drive\wiki_pedia_index\Index"
ix = open_dir(index_path)
mparser = MultifieldParser(["title" ,"content"], schema=ix.schema)
mparser.remove_plugin_class(qparser.PhrasePlugin)
mparser.add_plugin(qparser.SequencePlugin())
#q = mparser.parse( query +'~5')
distance = 1
string_query="North India"
proximty_query = "\"" + string_query + "\"" + '~' + str((distance+1)*2)
query = mparser.parse(proximty_query)

with ix.searcher() as searcher:
    result = searcher.search(query ,limit=10)
    print(len(result))
    for hit in result:
        print (hit['title'])
"""
.. module:: CountWords

CountWords
*************

:Description: CountWords

    Generates a list with the counts and the words in the 'text' field of the documents in an index

:Authors: bejar
    

:Version: 

:Created on: 04/07/2017 11:58 

"""

from __future__ import print_function
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from elasticsearch.exceptions import NotFoundError, TransportError

import argparse

output_path= "./result_token"
output_file = output_path+ "/letter.txt"

__author__ = 'bejar'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', default=None, required=True, help='Index to search')
    parser.add_argument('--alpha', action='store_true', default=False, help='Sort words alphabetically')
    args = parser.parse_args()

    index = args.index

    try:
        client = Elasticsearch(timeout=1000)
        voc = {}
        sc = scan(client, index=index, query={"query" : {"match_all": {}}})
        for s in sc:
            try:
                tv = client.termvectors(index=index, id=s['_id'], fields=['text'])
                if 'text' in tv['term_vectors']:
                    for t in tv['term_vectors']['text']['terms']:
                        if t in voc:
                            voc[t] += tv['term_vectors']['text']['terms'][t]['term_freq']
                        else:
                            voc[t] = tv['term_vectors']['text']['terms'][t]['term_freq']
            except TransportError:
                pass
        lpal = []

        for v in voc:
            lpal.append((v.encode("utf-8", "ignore"), voc[v]))

        fo = open(output_file, "w")
        for pal, cnt in sorted(lpal, key=lambda x: x[0 if args.alpha else 1]):
            #print(f'{cnt}, {pal.decode("utf-8")}')
            fo.write(f'{cnt}, {pal.decode("utf-8")}')
            fo.write('\n')
        #print('--------------------')
        fo.write('--------------------')
        #print(f'{len(lpal)} Words')
        fo.write(f'{len(lpal)} Words')
        fo.close()
    except NotFoundError:
        print(f'Index {index} does not exists')
        
from __future__ import unicode_literals
import utilities
from stanford_corenlp_pywrapper import sockwrap
from flask.ext.restful import Resource, reqparse
from flask.ext.restful.representations.json import output_json

output_json.func_globals['settings'] = {'ensure_ascii': False,
                                        'encoding': 'utf8'}
p = utilities.start_stanford()

class StanfordAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('text', type=unicode,
                                    location='json')
        super(StanfordAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        text = args['text']
        output = p.parse_doc(text)
        return output

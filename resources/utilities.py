import glob
import json 
from ConfigParser import ConfigParser
from stanford_corenlp_pywrapper import sockwrap

config_file = glob.glob('resources/config.ini')
parser = ConfigParser()
parser.read(config_file)

def parse_config():
    try:
        jars = json.loads(parser.get('Stanford', 'jars'))
        return jars
    except Exception as e:
        print 'There was an error parsing the config file. {}'.format(e)

def start_stanford():
    jars = parse_config()
    p = sockwrap.SockWrap(configfile='resources/stanford_config.ini',
                          corenlp_jars=jars)
    return p

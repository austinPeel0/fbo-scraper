# -*- coding: utf-8 -*-

import os, json
import fbo_weekly_scraper

elem_json = fbo_weekly_scraper.get_json_from_xml_file(file_path=os.getcwd()+"/tests/test_data.xml",save=False)
a = json.loads(elem_json)




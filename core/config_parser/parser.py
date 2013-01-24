#coding: utf-8

import ConfigParser
import os

class ProjectConfig:
    '''
    Configuration parser
    '''
    def __init__(self, filenames=[]):
        self.parser = ConfigParser.ConfigParser()
        self.check_files_exist(filenames)
        if filenames:
            self.parser.read(filenames)

    def check_files_exist(self, filenames):
        for filename in filenames:
            if not os.path.exists(filename):
                raise Exception('File "%s"does not exist' % filename)

    def read(self, filenames):
        '''
        read configuration from filenames
        '''
        self.parser = ConfigParser()
        self.parser.read(filenames)

    def items(self, section):
        return self.parser.items(section) if self.parser.has_section(section) else []

    def get(self, section, option):
        return self.parser.get(section, option).strip()

    def get_bool(self, section, option):
        try:
            value = self.parser.getboolean(section, option)
        except:
            value = False
        return value

    def get_int(self, section, option):
        try:
            value = self.parser.getint(section, option)
        except:
            value = 0
        return value

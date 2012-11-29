import re
import os
import string
import sublime, sublime_plugin


class ExtractLocaleCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        currentWord = self.view.substr(region)
        fileName = self.view.file_name()
        replacer = Replacer(fileName, currentWord)
        print os.popen(replacer.cmd()).read()
        self.view.replace(edit, region, replacer.erbTag())

class Replacer:

  def __init__(self, file_name, text):
    self.folder_name, self.file_name = os.path.split(file_name)
    self.absolute_path = file_name
    self.text = text

  def keyName(self):
    regex = re.compile('[^a-zA\s]')
    no_punc = regex.sub('', self.text.lower())
    return '_'.join(no_punc.split())

  def key(self):
    app = 'app' + os.sep + 'views' + os.sep
    path = self.absolute_path.split(app)[-1].replace('.html.erb', '')
    return 'en.' + path.replace(os.sep, '.') + '.' + self.keyName()

  def erbTag(self):
    return "<%%= t('.%s') %%>" % self.keyName()

  def localeFile(self):
    app = os.sep + 'app' + os.sep
    locales = os.sep + 'config' + os.sep + 'locales' + os.sep
    return self.folder_name.replace(app, locales) + os.sep + 'en.yml'

  def cmd(self):
    cp = os.path.split(os.path.realpath(__file__))[0]
    ruby_script  = os.path.join(cp, 'lib', 'add_to_yaml.rb')
    ruby_interpreter = "/usr/bin/env ruby"
    args = "' '".join([ruby_script, self.localeFile(), self.key(), self.text])
    return "/usr/bin/env ruby '%s'" % args

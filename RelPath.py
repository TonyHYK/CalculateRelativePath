import sublime, sublime_plugin
from os.path import relpath

class relpathselectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		srcPath = view.file_name()

		paths = [v.file_name() for v in self.view.window().views()]

		regions = view.split_by_newlines(view.sel()[0])
		for region in reversed(regions):
			string = view.substr(region)

			path = [p for p in paths if string in p]
			if path:
				view.replace(edit, region, relpath(path[0], srcPath))


class relpathwindowCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		srcPath = view.file_name()

		paths = [v.file_name() for v in self.view.window().views()]
		paths.remove(srcPath)
		
		for path in paths:
			self.view.insert(edit, self.view.sel()[0].begin(), relpath(path, srcPath) + '\n')

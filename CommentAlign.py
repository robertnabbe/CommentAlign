import sublime, sublime_plugin

class CommentAlignCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		syntax = self.view.settings().get("syntax");
		supported = [
			'ActionScript.sublime-syntax', 
			'C.sublime-syntax', 
			'C++.sublime-syntax', 
			'C#.sublime-syntax',
			'CSS.sublime-syntax',  
			'D.sublime-syntax', 
			'Go.sublime-syntax', 
			'Java.sublime-syntax', 
			'JavaScript.sublime-syntax',
			'LESS.tmLanguage',  
			'Objective-C.sublime-syntax', 
			'PHP.sublime-syntax', 
			'Rust.sublime-syntax', 
			'Scala.sublime-syntax', 
			'SASS.sublime-syntax', 
			'Swift.sublime-syntax', 
			'Xojo.sublime-syntax'
			];

		if any(x in syntax for x in supported):
			for region in self.view.sel():
				longest_line = 0;
				content_updated = [];

				if region.empty(): #no selection was made, default to selection the whole document
					selection = self.view.substr(sublime.Region(0, self.view.size()));
					sel_start = 0;
					sel_end = self.view.size();
				else: #selection exists
					selection = self.view.substr(region);
					sel_start = region.begin();
					sel_end = region.end();
					
				for i, line in enumerate(selection.split("\n")):
					code = line.rsplit("//");
					if len(code[0]) > longest_line:
						longest_line = len(code[0]);

				for line in selection.split("\n"):
					if "//" in line:
						line = line.rsplit("//",1);
						line = "".join((line[0].ljust(longest_line," ") + " //" + line[1]));
					content_updated.append(line);

				self.view.erase(edit, sublime.Region(sel_start, sel_end)); #clear region
				self.view.insert(edit, sel_start, "\n".join(content_updated))

		else:
			syntax = (syntax.rsplit("/",1)[1]).split(".")[0]
			errormsg = "Current syntax (" + syntax + ") is not supported."
			sublime.status_message(errormsg);
			sublime.error_message(errormsg);
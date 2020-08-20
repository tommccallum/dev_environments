"""
Provide statistics about our code files such as:
- functions per file
- classes per file
- lines per file
- blank lines per file
- enums
"""
import os
import glob
import re

path = "src"
verbose=0

class StatCounter:
    def __init__(self, filename):
        self.filename=filename
        self.classes =0 
        self.structs=0
        self.functions=0
        self.enums=0
        self.total_lines = 0
        self.blank_lines=0
        self.code_lines=0
        self.cout=0
        self.defines=0
        self.single_comments = 0
        self.multiline_comments=0

    def accumulate(self, totals):
        totals.classes += self.classes
        totals.structs += self.structs
        totals.functions += self.functions
        totals.enums += self.enums
        totals.total_lines += self.total_lines
        totals.blank_lines += self.blank_lines
        totals.code_lines += self.code_lines
        totals.cout += self.cout
        totals.defines += self.defines
        totals.single_comments += self.single_comments
        totals.multiline_comments += self.multiline_comments


    def __repr__(self):
        return "{:<50} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(
                self.filename,
                self.total_lines,
                self.code_lines, 
                self.structs,
                self.classes,
                self.functions, 
                self.enums,
                self.defines,
                self.cout,
                self.single_comments,
                self.multiline_comments
                )

def stats(this_path: str):
    stats_collection = [];
    files = glob.glob(os.path.join(this_path,"*.cpp"));
    files = files + glob.glob(os.path.join(this_path,"*.hpp"));
    for file in files:
        if verbose:
            print("Processing {}".format(file))
        stat_counter = StatCounter(os.path.basename(file))
        with open(file,"r") as fh:
            state = 0
            line = ""
            for line in fh:
                stat_counter.total_lines += 1
                if state == 0:
                    if re.search("^\s*$", line):
                        stat_counter.blank_lines += 1
                    if re.search("\/\/", line):
                        stat_counter.single_comments += 1
                    if re.search("\/\*", line):
                        stat_counter.multiline_comments += 1
                        state = 1
                    if not re.search("^\s*\/\/", line) and not re.search("^\s*\/\*", line) and not re.search("^\s*$", line):
                        stat_counter.code_lines += 1
                    if re.search("^\s*\w+\s+\w+\(", line):
                        stat_counter.functions += 1
                    if re.search("^\s*class\s\w+[:{]{0,1}", line):
                        stat_counter.classes += 1
                    if re.search("^\s*struct\s\w+[:{\n]{0,1}", line):
                        stat_counter.structs += 1
                    if re.search("^\s*enum\s+", line):
                        stat_counter.enums += 1
                    if re.search("[:\s]cout\s", line):
                        stat_counter.cout += 1
                    if re.search("^\s*#\s*define\s+", line):
                        stat_counter.defines += 1
                if state == 1 and re.search("\*\/", line):
                    state = 0
            stats_collection.append( stat_counter )
    return stats_collection

def print_stats(stat_collection):
    stat_collection.sort(key=lambda x : x.filename)
    #col_width = max(len(stat.filename) for stat in stat_collection) + 2 
    width = 110
    draw_line = "{0:-^"+str(width)+"}"
    print(draw_line.format(""))
    print("{:<50} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format("Filename",
        "Ln", "Code", "Strct",
        "Class", 
        "Func", "Enum", "Defn", 
        "cout", "//", "/**/"))
    print(draw_line.format(""))    
    totals = StatCounter("Totals")
    for st in stat_collection:
        st.accumulate(totals)
        print(st)
    print(draw_line.format(""))
    print(totals)

if __name__ == "__main__":
    print_stats(stats(path))


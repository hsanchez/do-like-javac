from . import jprint
from . import randoop
from . import bixie
from . import graphtools
from . import chicory
from . import dyntrace
from . import dyntracecounts

# import soot
from . import check
from . import infer

TOOLS = {
  # 'soot'      : soot,
  'checker'   : check,
  'inference' : infer,
  'print'     : jprint,
  'randoop'   : randoop,
  'bixie'     : bixie,
  'graphtool' : graphtools,
  'chicory'   : chicory,
  'dyntrace'  : dyntrace,
  'dyntracecounts' : dyntracecounts,
}

def parsers():
  return [mod.argparser for name, mod in TOOLS.items() if mod.argparser]

def check_tool(tool):
  if tool in TOOLS:
    return tool
  else:
    print(f"ERROR: Could not find tool {tool}")
    return None

def parse_tools(tools):
  return [tool for tool in tools.split(',') if check_tool(tool)]

def run(args, javac_commands, jars):
  if args.tool:
    for tool in parse_tools(args.tool):
      TOOLS[tool].run(args, javac_commands, jars)

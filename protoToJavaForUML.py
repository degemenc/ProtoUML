import re
import sys

p = open(sys.argv[1], "r")

result = ""
convertDataTypes = False
emptyKeywords = []

for s in p:
  if s[0:6] == "syntax" or s[0:6] == "option" or s[0:7] == "package":
    continue;

  # Conform to proto3
  s = s.replace("optional ", "")
  s = s.replace("required ", "")

  if s[0:7] == "message":
    s = s.replace("message", "class")

  if s[0:7] == "service":
    s = s.replace("service", "class")

  if convertDataTypes:
    s = s.replace("int32", "int")
    s = s.replace("int64", "long")
    s = s.replace("bool ", "boolean ")
    s = s.replace("string", "String")

  if '=' in s:
    s = s[0:s.find(' =')] + ";"

  if 'repeated' in s:
    m = re.search('repeated (.+?) ', s).group(1)
    s = s.replace('repeated ', '')
    s = s.replace(m, m + "[]")

  if 'rpc' in s:
    m = re.search('returns \((.+?)\)', s).group(1)
    s = s.replace("rpc", m)
    s = s.replace(" returns (" + m + ")", " { return null; }")
    
    m = re.search('\((.+?)\)', s).group(1)
    if m in emptyKeywords:
      s = s.replace(m, "")
    else:
      s = s.replace(")", " request)")

  if '{}' in s:
    m = re.search('class (.+?) {', s).group(1)
    if m not in emptyKeywords:
      emptyKeywords.append(m)
    continue

  result += s + "\n"

p.close()
f = open(sys.argv[2], "w")
f.write(result)
f.close()

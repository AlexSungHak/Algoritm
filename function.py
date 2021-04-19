def snippet1(self, importPath, filename):
      for i in importPath:
    fullName = i + "/" + filename
   if os.path.exists(fullName):
      return True
  return False
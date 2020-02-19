import arcpy
arcpy.management.CalculateField("parcelas_SpatialJoin",
                                "verif", "isSame(!index!, !ID_TALHAO!)",
                                "PYTHON3", "def isSame(x, y):\n    fieldA = str(x)\n    fieldB = str(y)\n    if fieldA == fieldB" +
    ":\n        return 1\n    else:\n        return 0")

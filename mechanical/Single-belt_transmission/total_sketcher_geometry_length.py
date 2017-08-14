# backref: [[id:63e03519-d595-4444-8e2b-f03469cdbb42][Develop macro to sum up the lengths of sketcher geometries]]
total_length = sum([item.length() for item in App.ActiveDocument.Sketch.Geometry if not item.Construction])

# Reference: https://www.freecadweb.org/wiki/index.php?title=Quantity

# Convert internal units into my current display units:
tu = FreeCAD.Units.parseQuantity

# How do I not hardcode "mm" here?:
(preferred, value, unit) = tu("{} mm".format(total_length)).getUserPreferred()

# This emits '3 "' for 3 inches. How do I print it as "3 in"?
print "Total length of all non-construction objects in sketcher: {}".format(preferred)

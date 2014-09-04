import vigra
import numpy
import cmaps


f = "figure_1.png"
# cmaps.print_possible_cmaps()
img = numpy.squeeze(vigra.readImage(f))
img_heat = cmaps.apply_cmap(img, "gist_heat")
# vigra.impex.writeImage(img_heat, "figure_1_heat.png")
vigra.imshow(numpy.swapaxes(img_heat, 1, 0))
vigra.show()

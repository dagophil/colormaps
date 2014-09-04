import pylab
import numpy


def print_possible_cmaps():
    """Print the available colormaps."""
    maps = [m for m in pylab.cm.datad if not m.endswith("_r")]
    maps.sort()
    for m in maps:
        print m


def apply_cmap(img, cmap, min_value=None, max_value=None):
    """Applies the colormap to the image and returns the result.

    If min_value is None or max_value is None, the min and max values from img are used.
    :param img: image
    :param cmap: string that specifies the colormap
    :param min_value: min value of the colormap
    :param max_value: max value of the colormap
    :return: the image with the applied colormap
    """
    img = numpy.squeeze(img).astype(numpy.float32)
    if len(img.shape) != 2:
        raise Exception("The given image must be 2-dimensional.")

    # Check min and max values.
    if min_value is None:
        min_value = numpy.min(img)
    if max_value is None:
        max_value = numpy.max(img)

    # Convert img to fit into the values 0 to 255.
    img = ((img - min_value) * 255 / max_value).astype(numpy.uint8)

    # Apply the colormap.
    cmap = pylab.get_cmap(cmap)
    return cmap(img)

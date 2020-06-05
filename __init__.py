# -*- coding: utf-8 -*-
"""
/***************************************************************************
 cocotrainer
                                 A QGIS plugin
 This plugin creates an image dataset in the coco format based on objects in a vector layer and extends from a raster layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-06-03
        copyright            : (C) 2020 by Jonathan Gerbscheid
        email                : jonathan@youngmavericks.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load cocotrainer class from file cocotrainer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cocotrainer import cocotrainer
    return cocotrainer(iface)

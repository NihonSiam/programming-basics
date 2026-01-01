from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    """
    Add a square to the drawing.
    Parameters:
        PDwg: Drawing object to add the square to.
        left: X-coordinate of the left edge.
        top: Y-coordinate of the top edge.
        sideLength: Length of the square's sides.
        color: Fill color of the square.
        strokeColor: Stroke color of the square.
    """
    # TODO: Implement drawing a square using svgwrite.Rect
    pass

def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    """
    Add a circle to the drawing.
    Parameters:
        PDwg: Drawing object to add the circle to.
        centerX: X-coordinate of the circle center.
        centerY: Y-coordinate of the circle center.
        radius: Radius of the circle.
        color: Fill color of the circle.
        stroke: Stroke color of the circle.
    """
    # TODO: Implement drawing a circle using svgwrite.Circle
    pass

def saveSvg(PDwg: Drawing, file) -> None:
    """
    Save the drawing to an SVG file.
    Parameters:
        PDwg: Drawing object to save.
        file: Filename to save the SVG as.
    """
    # TODO: Save the drawing using Drawing.saveas
    pass


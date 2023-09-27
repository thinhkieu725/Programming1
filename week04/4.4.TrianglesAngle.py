"""
COMP.CS.100 Programming 1
4.4.TrianglesAngle.py
Creator: Thinh Kieu
Student number: 152167613
"""

def calculate_angle (angle1, angle2 = 90):
    """
    Calculate the third angle of a triangle, given the two others.
    variables:
        angle1 _ int _ magnitude of angle 1
        angle2 _ int _ magnitude of angle 2 _ set at default = 90
    return: angle3 _ int _ magnitude of angle 3
    """
    angle3 = 180 - angle1 - angle2
    return angle3

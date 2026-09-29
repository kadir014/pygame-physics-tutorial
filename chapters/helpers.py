import pygame
from pygame import Vector2


def draw_arrow(
        surface: pygame.Surface,
        color: pygame.typing.ColorLike,
        start: pygame.typing.Point,
        end: pygame.typing.Point,
        head_length: int = 10,
        head_angle: float = 60.0,
        width: int = 1
    ) -> None:
    """
    Helper function to draw an arrow segment.
    
    Parameters
    ----------
    surface
        Destination surface to draw on.
    color
        Color of the arrow
    start
        Starting point in surface space.
    end
        Ending point (arrow head) in surface space.
    head_length
        Length of arrow head in pixels.
    head_angle
        Angle of the arrow head in degrees.
    width
        Line width of arrow.
    """

    start, end = Vector2(start), Vector2(end)

    delta = end - start
    if delta.length() == 0.0:
        return
    dir = delta.normalize()

    head0 = dir.rotate(90 + head_angle) * head_length
    head1 = dir.rotate(-(90 + head_angle)) * head_length

    pygame.draw.aaline(surface, color, start, end, width)
    pygame.draw.aaline(surface, color, end, end + head0, width)
    pygame.draw.aaline(surface, color, end, end + head1, width)
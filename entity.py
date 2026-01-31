"""
Facilitates a shared entity class for now.
"""
import pygame


class Entity:
    """
    Parent class holder for other entities.
    """
    def update(self, dt: float):
        """
        Update entity parameters

        :param dt: The delta time
        :type dt: float
        """
        pass

    def draw(self, screen: pygame.Surface):
        """
        Draw entity
        
        :param screen: The main game surface
        :type screen: pygame.Surface
        """
        pass

    def kill(self):
        """
        Entity kill method.  Results in auto cleanup.
        """
        pass

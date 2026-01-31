import pygame


class Entity:
    def update(self, dt: float):
        """
        Update entity parameters

        :param dt: Delta time
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

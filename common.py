import pygame as pg


class Button(object):

    def __init__(self, rect, color, function, **kwargs):
        self.rect = pg.Rect(rect)
        self.color = color
        self.function = function
        self.clicked = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.text = kwargs.get("text")
        self.font = kwargs.get("font", pg.font.Font(None, 16))
        self.call_on_release = kwargs.get("call_on_release", True)
        self.hover_color = kwargs.get("hover_color")
        self.clicked_color = kwargs.get("clicked_color")
        self.font_color = kwargs.get("font_color", pg.Color("white"))
        self.hover_font_color = kwargs.get("hover_font_color")
        self.clicked_font_color = kwargs.get("clicked_font_color")
        self.click_sound = kwargs.get("click_sound")
        self.hover_sound = kwargs.get("hover_sound")
        self.render_text()

    def render_text(self):
        """
            Renders the text of the button
            * sets the color for when on hover over
            * set color for when clicked
        """
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text, True, color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text, True, color)
            self.text = self.font.render(self.text, True, self.font_color)

    def check_event(self, event):
        result = None
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            result = self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            result = self.on_release()
        if result:
            return result

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                result = self.function()
                if result:
                    return result

    def on_release(self):
        result = None
        if self.clicked and self.call_on_release:
            result = self.function()
        self.clicked = False
        if result:
            return result

    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:  # TODO maybe remove
                    self.hover_sound.play()
        else:
            self.hovered = False

    def update(self, surface):
        color = self.color
        text = self.text
        self.check_hover()
        if self.clicked and self.clicked_color:
            color = self.clicked_color
            if self.clicked_font_color:
                text = self.clicked_text
        elif self.hovered and self.hover_color:
            color = self.hover_color
            if self.hover_font_color:
                text = self.hover_text
        surface.fill(pg.Color("black"), self.rect)
        surface.fill(color, self.rect.inflate(-4, -4))  # Creates a black border around the button
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)

rounded_box = "font-weight: normal; color: #FFF; border-radius: 7px; font-size: 14px; padding: 2 2 2 2px;"
smaller_rounded_box = "font-weight: normal; color: #FFF; border-radius: 7px; font-size: 14px; padding: 3 5 3 5px;"

calendar_widget_style = """
                border-radius: 2px;
                background-color: {};
                """

calendar_tooltip_style = """
                color: #fff;
                border-radius: 5px;
                background-color: #4b4b4b;
                padding: 5 5 5 5px;
                """

check_bar = """
                border: 2px solid {};
                border-radius: 6px;
                background-color: {};
                """

check_bar_unclicked = """
                    border: 2px solid #dde6f6;
                    border-radius: 6px;
                    background-color: white;
                    """

check_bar_first_click = """
                    border: 2px solid #5C94A8;
                    border-radius: 6px;
                    background-color: #78C3DE;
                    """

check_bar_second_click = """
                    border: 2px solid #126E87;
                    border-radius: 6px;
                    background-color: #0890C1;
                    """

check_bar_unclickable = """
                    border: 2px solid #b8c2d4;
                    border-radius: 6px;
                    background-color: #dde6f6;
                    """

check_bar_today_unclicked = """
                    border: 2px solid #858585;
                    border-radius: 6px;
                    background-color: white;
                    """


check_bar_first_click_blue = """
                    border: 2px solid #5C94A8;
                    border-radius: 6px;
                    background-color: #78C3DE;
                    """

check_bar_second_click_blue = """
                    border: 2px solid #126E87;
                    border-radius: 6px;
                    background-color: #0890C1;
                    """

scrollArea_style = """
                    QScrollArea {
						background: #ffffff;
						border: 0px solid;
                    }

                    QScrollBar::vertical {
                        width: 8px;
                        margin: 0px 0 0px 0;
						background: transparent;
                      }

                      QScrollBar::handle:vertical {
                        min-height: 10px;
						background: #dde6f6;
						border-radius: 4px;
                      }

                      QScrollBar::add-line:vertical {
                        background: transparent;
                        height: 0px; 
                        subcontrol-position: bottom;
                        subcontrol-origin: margin;
                      }

                      QScrollBar::sub-line:vertical {
                        background: transparent;
                        height: 0px; 
                        subcontrol-position: top;
                        subcontrol-origin: margin;
                      }

                      QScrollBar::up-arrow:vertical { 
						background: transparent;
						height: 0px; 
                      }

                      QScrollBar::down-arrow:vertical {
						background: transparent;                        
						height: 0px; 
                        width: 40px;
                      }
                      """

colors = {"red": "#E26457", "yellow": "#E2B757", "blue": "#465999", "green": "#42AB59"}

blue_color_scheme = {"main": "#465999", "highlight": "#6f80b8", "shadow": "#2f4385", "dark-shadow": "#1c2a57"}
red_color_scheme = {"main": "#e26457", "highlight": "#ff988d", "shadow": "#c44234", "dark-shadow": "#80281e"}
green_color_scheme = {"main": "#42ab59", "highlight": "#70c983", "shadow": "#27943f", "dark-shadow": "#176127"}
yellow_color_scheme = {"main": "#e2b757", "highlight": "#ffdc8d", "shadow": "#c49834", "dark-shadow": "#80621e"}

color_schemes = {"blue": blue_color_scheme, "red": red_color_scheme, "green": green_color_scheme, "yellow": yellow_color_scheme}

def check_bar_second(color):
    color = color or "red"
    scheme = color_schemes[color]
    style = check_bar.format(scheme["shadow"], scheme["main"])
    return style

def check_bar_first(color):
    color = color or "red"
    scheme = color_schemes[color]
    style = check_bar.format(scheme["main"], scheme["highlight"])
    return style

def check_bar_today(color):
    color = color or "red"
    scheme = color_schemes[color]
    style = check_bar.format(scheme["main"], "white")
    return style

def add_bgcolor_to_style(color, style):
    color = color or "red"
    return "{}background: {}; ".format(style, colors[color])

def add_to_style(add, style):
    return style + add
    
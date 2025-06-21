
from controllers.main_controller import MainController
from views.home_view import render_home

if __name__ == "__main__":
    controller = MainController()
    render_home()
    print(controller.home())

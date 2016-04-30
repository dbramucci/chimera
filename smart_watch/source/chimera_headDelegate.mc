using Toybox.WatchUi as Ui;

class chimera_headDelegate extends Ui.BehaviorDelegate {

    function initialize() {
        BehaviorDelegate.initialize();
    }

    function onMenu() {
        Ui.pushView(new Rez.Menus.MainMenu(), new chimera_headMenuDelegate(), Ui.SLIDE_UP);
        return true;
    }

}
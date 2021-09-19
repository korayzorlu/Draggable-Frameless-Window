def moveWindow(e):
    global clickPosition
    if mainWindow.isMaximized() == False:
        if e.buttons() == Qt.LeftButton:
            mainWindow.move(mainWindow.pos() + e.globalPos() - clickPosition)
            clickPosition = e.globalPos()
            e.accept()

label1.mouseMoveEvent = moveWindow

def mousePressEvent(event):
    global clickPosition
    clickPosition = event.globalPos()

label1.mousePressEvent = mousePressEvent
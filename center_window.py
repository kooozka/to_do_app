def center(window):
        qr = window.frameGeometry()
        cp = window.screen().availableGeometry().center()
        qr.moveCenter(cp)
        window.move(qr.topLeft())
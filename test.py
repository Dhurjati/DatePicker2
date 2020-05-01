from PyQt5 import QtCore, QtGui, QtWidgets

QSS = '''
QCalendarWidget QAbstractItemView
{ 
    selection-background-color: #042944; 
    selection-color: white;
}
QCalendarWidget QWidget 
{
  color:grey;
}
QCalendarWidget QTableView
{
    border-width:0px;
    background-color:lightgrey;
}
'''

class MainWindow(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent,
            verticalHeaderFormat=QtWidgets.QCalendarWidget.NoVerticalHeader,
            gridVisible=False)

        for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday,):
            fmt = self.weekdayTextFormat(d)
            fmt.setForeground(QtGui.QBrush(QtGui.QColor("#33B5E5")))
            # (0,QtGui.QBrush(QtGui.QColor("#123456")))
            self.setWeekdayTextFormat(d, fmt)

    def paintCell(self, painter, rect, date):
        if date == self.selectedDate():
            painter.save()
            painter.fillRect(rect, QtGui.QColor("#D3D3D3"))
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtGui.QColor("#33B5E5"))
            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
            r.moveCenter(rect.center())
            painter.drawEllipse(r)
            painter.setPen(QtGui.QPen(QtGui.QColor("white")))
            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            super(MainWindow, self).paintCell(painter, rect, date)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(QSS)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
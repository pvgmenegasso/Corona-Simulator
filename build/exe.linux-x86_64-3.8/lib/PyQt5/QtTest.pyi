# The PEP 484 type hints stub file for the QtTest module.
#
# Generated by SIP 4.19.21
#
# Copyright (c) 2020 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtWidgets
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QAbstractItemModelTester(QtCore.QObject):

    class FailureReportingMode(int): ...
    QtTest = ... # type: 'QAbstractItemModelTester.FailureReportingMode'
    Warning = ... # type: 'QAbstractItemModelTester.FailureReportingMode'
    Fatal = ... # type: 'QAbstractItemModelTester.FailureReportingMode'

    @typing.overload
    def __init__(self, model: QtCore.QAbstractItemModel, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, model: QtCore.QAbstractItemModel, mode: 'QAbstractItemModelTester.FailureReportingMode', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def failureReportingMode(self) -> 'QAbstractItemModelTester.FailureReportingMode': ...
    def model(self) -> QtCore.QAbstractItemModel: ...


class QSignalSpy(QtCore.QObject):

    def __init__(self, signal: pyqtBoundSignal) -> None: ...

    def __delitem__(self, i: int) -> None: ...
    def __setitem__(self, i: int, value: typing.Iterable[typing.Any]) -> None: ...
    def __getitem__(self, i: int) -> typing.List[typing.Any]: ...
    def __len__(self) -> int: ...
    def wait(self, timeout: int = ...) -> bool: ...
    def signal(self) -> QtCore.QByteArray: ...
    def isValid(self) -> bool: ...


class QTest(sip.simplewrapper):

    class KeyAction(int): ...
    Press = ... # type: 'QTest.KeyAction'
    Release = ... # type: 'QTest.KeyAction'
    Click = ... # type: 'QTest.KeyAction'
    Shortcut = ... # type: 'QTest.KeyAction'

    class QTouchEventSequence(sip.simplewrapper):

        def __init__(self, a0: 'QTest.QTouchEventSequence') -> None: ...

        def commit(self, processEvents: bool = ...) -> None: ...
        def stationary(self, touchId: int) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def release(self, touchId: int, pt: QtCore.QPoint, window: typing.Optional[QtGui.QWindow] = ...) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def release(self, touchId: int, pt: QtCore.QPoint, widget: QtWidgets.QWidget) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def move(self, touchId: int, pt: QtCore.QPoint, window: typing.Optional[QtGui.QWindow] = ...) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def move(self, touchId: int, pt: QtCore.QPoint, widget: QtWidgets.QWidget) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def press(self, touchId: int, pt: QtCore.QPoint, window: typing.Optional[QtGui.QWindow] = ...) -> 'QTest.QTouchEventSequence': ...
        @typing.overload
        def press(self, touchId: int, pt: QtCore.QPoint, widget: QtWidgets.QWidget) -> 'QTest.QTouchEventSequence': ...

    @typing.overload
    def touchEvent(self, widget: QtWidgets.QWidget, device: QtGui.QTouchDevice) -> 'QTest.QTouchEventSequence': ...
    @typing.overload
    def touchEvent(self, window: QtGui.QWindow, device: QtGui.QTouchDevice) -> 'QTest.QTouchEventSequence': ...
    @typing.overload
    def qWaitForWindowExposed(self, window: QtGui.QWindow, timeout: int = ...) -> bool: ...
    @typing.overload
    def qWaitForWindowExposed(self, widget: QtWidgets.QWidget, timeout: int = ...) -> bool: ...
    @typing.overload
    def qWaitForWindowActive(self, window: QtGui.QWindow, timeout: int = ...) -> bool: ...
    @typing.overload
    def qWaitForWindowActive(self, widget: QtWidgets.QWidget, timeout: int = ...) -> bool: ...
    def qWait(self, ms: int) -> None: ...
    @typing.overload
    def mouseRelease(self, widget: QtWidgets.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mouseRelease(self, window: QtGui.QWindow, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mousePress(self, widget: QtWidgets.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mousePress(self, window: QtGui.QWindow, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mouseMove(self, widget: QtWidgets.QWidget, pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mouseMove(self, window: QtGui.QWindow, pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mouseDClick(self, widget: QtWidgets.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mouseDClick(self, window: QtGui.QWindow, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mouseClick(self, widget: QtWidgets.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def mouseClick(self, window: QtGui.QWindow, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keySequence(self, widget: QtWidgets.QWidget, keySequence: typing.Union[QtGui.QKeySequence, QtGui.QKeySequence.StandardKey, str, int]) -> None: ...
    @typing.overload
    def keySequence(self, window: QtGui.QWindow, keySequence: typing.Union[QtGui.QKeySequence, QtGui.QKeySequence.StandardKey, str, int]) -> None: ...
    @typing.overload
    def keyRelease(self, widget: QtWidgets.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyRelease(self, widget: QtWidgets.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyRelease(self, window: QtGui.QWindow, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyRelease(self, window: QtGui.QWindow, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyPress(self, widget: QtWidgets.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyPress(self, widget: QtWidgets.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyPress(self, window: QtGui.QWindow, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyPress(self, window: QtGui.QWindow, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyEvent(self, action: 'QTest.KeyAction', widget: QtWidgets.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyEvent(self, action: 'QTest.KeyAction', widget: QtWidgets.QWidget, ascii: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyEvent(self, action: 'QTest.KeyAction', window: QtGui.QWindow, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyEvent(self, action: 'QTest.KeyAction', window: QtGui.QWindow, ascii: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    def keyClicks(self, widget: QtWidgets.QWidget, sequence: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyClick(self, widget: QtWidgets.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyClick(self, widget: QtWidgets.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyClick(self, window: QtGui.QWindow, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyClick(self, window: QtGui.QWindow, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    def qSleep(self, ms: int) -> None: ...

[Variables]

; ---------------------------------------- Launcher

scale=1
spacing=10

;           Item 1
e1X=1.5
; horizontal position on grid

e1Y=1
; vertical position on grid

e1Image=#@#images\one.png
; image/icon path

e1Action=["C:\Path\To\File\Or\Folder"]
; program/folder path or website URL

;           Item 2
e2X=2.5
e2Y=1
e2Image=#@#images\two.png
e2Action=["C:\Path\To\File\Or\Folder"]
;           Item 3
e3X=3
e3Y=2
e3Image=#@#images\three.png
e3Action=["C:\Path\To\File\Or\Folder"]
;           Item 4
e4X=2.5
e4Y=3
e4Image=#@#Images\four.png
e4Action=["C:\Path\To\File\Or\Folder"]
;           Item 5
e5X=1.5
e5Y=3
e5Image=#@#images\five.png
e5Action=["C:\Path\To\File\Or\Folder"]
;           Item 6
e6X=1
e6Y=2
e6Image=#@#images\six.png
e6Action=["C:\Path\To\File\Or\Folder"]
;           Item 7
e7X=2
e7Y=2
e7Image=#@#images\seven.png
e7Action=["C:\Path\To\File\Or\Folder"]


; ---------------------------------------- Panel

pLX=#e3X#
; the item farthest right

pLY=#e4Y#
; the item farthest down

pImageTint=60,60,60,200
; color of the back panels

nText="Numbers"
; folder text

sideOpen=1
sidePanel=0
; pick a side for the opening panel and the main panel (0 -> on the left, 1 -> on the right)
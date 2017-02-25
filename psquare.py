caret = editor.getCurrentPos()
anchor = editor.getAnchor()

if anchor > caret:
    caret, anchor = anchor, caret

editor.replaceSel('[' + editor.getSelText() + ']')
editor.setSelection(caret + 2, anchor)

# Suggested shortcut: Ctrl+Alt+9

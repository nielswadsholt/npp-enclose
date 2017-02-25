selection = editor.getSelText()
open_chars = '"\'{(['
close_chars = '"\'})]'

if selection[0] in open_chars and close_chars[open_chars.find(selection[0])] == selection[-1]:
    caret = editor.getCurrentPos()
    anchor = editor.getAnchor()
    
    if anchor > caret:
        caret, anchor = anchor, caret
    
    editor.replaceSel(selection[1:-1])
    editor.setSelection(caret - 2, anchor)

# Suggested shortcut: Ctrl+Alt+0

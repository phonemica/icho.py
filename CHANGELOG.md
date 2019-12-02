# Ichō.py Changelog

Ichō has been in development since late 2016, with the first python implementation first used in November 2018. This changelog was created in April 2019 to track QOL improvements and changes from earlier versions. This is not an exhaustive list, but is meant to be a rough record of what has been addressed and what is still needed.

## Version 0.2

### 2019.0514
- Consolidation of files to prepare for language switching
- Moved CouchDB login credentials to `auth.py`
- Swapped out `couchdb` for `cloudant` and changed corresponding code. There might be a few holdovers which still need attention. Cloning from and saving to remote are working.
- Re-established remote database, updated against SQLite with `upload.py`.
- Moved scripts to their own ignorable folder to prevent confusion by users later on.
- Added gloss filtering to TreeWidget

### 2019.0430

- TreeView filtering is now case-sensitive for Stephen's font.
- Re-coded `ui/main.py` to clean things up
- Fixed IndexError causing crashes when pasting long strings into search box
- Minor UX/UI improvements
- Last-modified date now included in database for each entry
- Added secondary sorting by gloss in the TreeView

### 2019.0428

- Headword count re-added below TreeView
- Began label/entry name cleanup, moving away from QtDesigner default names
- Adding global font size to fix small text on macOS retina screens
- TreeView SQLite3 filters for `{}` `%{}` `{}%` and `%{}%` with dropdown box

### 2019.0427

- Filtering the TreeView is now possible
- When a gloss is not present, TreeView shows definition in that column
- Examples are now editable in the form panel
- Unicode (Myanmar block) now working for lexemes
- Automatically change forms like <ū₁sɛ₆ho₆haü₃thüŋ₆hāŋ₆> to <ū₁ sɛ₆ ho₆ haü₃ thüŋ₆ hāŋ₆> where needed

This is the last version Ailot has as of 28 April 2019.

## High priority future changes:

- Need to not run through everything in TreeView with every edit

## Low priority changes:

- Photos should have thumbnail view in-app
- Audio should have preview in-app

## to-do
- maybe automatically filter the list when an entry is clicked? will that mess up what's selected? what happens when saving? maybe have a checkbox to enable/disable that as a mode
- re-add vform and stem alternation boxes
- set up language selection better